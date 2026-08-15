# Artifact #9 — Performance Tuning Checklist for Workflows & FHIR Stores

**Platform:** Onyx Interoperability Platform
**Version:** 1.0
**Last Updated:** 2026-07-07
**Owner:** Platform Engineering / Interoperability Team
**Classification:** Internal — Engineering Reference

---

## Table of Contents

1. [Databricks Cluster Sizing](#1-databricks-cluster-sizing)
2. [Bundle Sizing & Batch Optimization](#2-bundle-sizing--batch-optimization)
3. [Retry & Shred Logic](#3-retry--shred-logic)
4. [Workload Profiling](#4-workload-profiling)
5. [HealthLake Performance](#5-healthlake-performance)
6. [Firely Performance](#6-firely-performance)
7. [Network & I/O](#7-network--io)
8. [Pre-Change Performance Review Checklist](#8-pre-change-performance-review-checklist)
9. [Performance Testing Procedures](#9-performance-testing-procedures)

---

## 1. Databricks Cluster Sizing

### 1.1 Cluster Type Selection

| Workflow Family | Recommended Cluster Type | Rationale |
|---|---|---|
| ADT / Scheduling (low-volume, latency-sensitive) | Single-node or small Standard | Minimal shuffle; prioritize startup time |
| Clinical Document Ingestion (CDA/C-CDA → FHIR) | Memory-optimized (e.g., `r5.xlarge`+) | Large XML parsing, DOM trees in memory |
| Bulk FHIR Export Processing | Compute-optimized (e.g., `c5.2xlarge`+) | CPU-bound JSON transformation |
| Large Batch Reconciliation | Storage-optimized with autoscale | Heavy shuffle, large intermediate datasets |
| Real-time Streaming (Kafka → FHIR) | Delta Live Tables (DLT) with Enhanced Autoscaling | Continuous processing, auto-managed |

### 1.2 Worker Node Sizing by Workflow Family

| Workflow Family | Min Workers | Max Workers | Instance Type | Memory/CPU Ratio |
|---|---|---|---|---|
| ADT / Scheduling | 1 | 2 | `m5.large` | 4:1 (8 GB / 2 vCPU) |
| Clinical Document Transform | 2 | 8 | `r5.xlarge` | 8:1 (32 GB / 4 vCPU) |
| Bulk Export / Import | 2 | 16 | `c5.2xlarge` | 4:1 (16 GB / 8 vCPU) |
| Batch Reconciliation | 4 | 24 | `r5.2xlarge` | 8:1 (64 GB / 8 vCPU) |
| Streaming Pipelines | 2 | 12 | `m5.xlarge` | 4:1 (16 GB / 4 vCPU) |

### 1.3 Autoscaling Configuration

```json
{
  "autoscale": {
    "min_workers": 2,
    "max_workers": 12,
    "scale_up_threshold": 0.7,
    "scale_down_threshold": 0.3,
    "scale_down_grace_period_minutes": 10
  }
}
```

**Guidelines:**
- **Scale-up trigger:** CPU utilization > 70% sustained for 2 minutes OR pending task queue > 2× active slots
- **Scale-down trigger:** CPU utilization < 30% sustained for 10 minutes
- **Grace period:** Minimum 10 minutes before scale-down to avoid thrashing
- **Step size:** Scale up aggressively (2× current), scale down conservatively (−1 node)

### 1.4 Spot vs. On-Demand Strategy

| Scenario | Strategy | Spot % | Fallback |
|---|---|---|---|
| Batch workflows (non-time-critical) | Spot-first | 80–100% | On-demand fallback pool |
| Time-critical transforms (< 15 min SLA) | Mixed | 50% spot | On-demand driver + spot workers |
| Streaming / DLT | On-demand only | 0% | N/A — interruption unacceptable |
| Dev / Test | Spot-only | 100% | Retry on interruption |

**Spot best practices:**
- Use diversified instance pools (3+ instance types)
- Set `spot_bid_max_price` to on-demand price (don't cap)
- Enable `availability_zone_flexibility`
- Configure graceful decommissioning timeout: 120s

### 1.5 Memory/CPU Ratio Guidelines

| Workload Characteristic | Recommended Ratio | Indicator |
|---|---|---|
| JSON/XML parsing, large payloads | 8:1 (memory-heavy) | GC pressure, OOM errors |
| Pure transformation logic | 4:1 (balanced) | High CPU, low memory pressure |
| Large joins / reconciliation | 8:1+ (memory-heavy) | Shuffle spill to disk |
| Network-bound (API calls) | 4:1 (balanced) | Low CPU, high I/O wait |

**Driver node:** Always 1 tier larger than workers (e.g., if workers = `r5.xlarge`, driver = `r5.2xlarge`)

---

## 2. Bundle Sizing & Batch Optimization

### 2.1 Optimal FHIR Bundle Sizes

| FHIR Server | Bundle Type | Optimal Size | Max Size | Notes |
|---|---|---|---|---|
| **AWS HealthLake** | Transaction | 25–50 resources | 160 resources | Hard limit at 160; throttling above 100 |
| **AWS HealthLake** | Batch | 50–100 resources | 160 resources | Less strict ordering; higher throughput |
| **Firely Server** | Transaction | 50–200 resources | 500 resources | MongoDB write concern affects limit |
| **Firely Server** | Batch | 100–500 resources | 1000 resources | Configurable via `BundleOptions` |

### 2.2 Batch vs. Transaction Selection

```
┌─────────────────────────────────────────────────────┐
│          DECISION: Batch vs. Transaction             │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Need all-or-nothing atomicity?                     │
│    YES → Transaction                                │
│    NO  ↓                                            │
│                                                     │
│  Resources have inter-dependencies (references)?    │
│    YES → Transaction (server resolves order)        │
│    NO  ↓                                            │
│                                                     │
│  Throughput is primary concern?                     │
│    YES → Batch (parallel server-side processing)    │
│    NO  → Transaction (safer default)               │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 2.3 Chunking Strategies

**Strategy 1: Fixed-Size Chunking**
```python
def chunk_resources(resources, chunk_size=50):
    """Simple fixed-size chunking for homogeneous resources."""
    for i in range(0, len(resources), chunk_size):
        yield resources[i:i + chunk_size]
```

**Strategy 2: Dependency-Aware Chunking**
```python
def chunk_with_dependencies(resources):
    """
    Group resources by dependency graph.
    Patients first, then dependent resources (Encounters, Observations).
    Each chunk is self-contained for reference resolution.
    """
    # Phase 1: Identify root resources (no outbound references)
    roots = [r for r in resources if not r.get('references')]
    dependents = [r for r in resources if r.get('references')]
    
    # Phase 2: Group dependents with their roots
    chunks = []
    current_chunk = []
    current_size = 0
    
    for root in roots:
        deps = find_dependents(root, dependents)
        group = [root] + deps
        
        if current_size + len(group) > MAX_BUNDLE_SIZE:
            chunks.append(current_chunk)
            current_chunk = group
            current_size = len(group)
        else:
            current_chunk.extend(group)
            current_size += len(group)
    
    if current_chunk:
        chunks.append(current_chunk)
    
    return chunks
```

**Strategy 3: Weighted Chunking (by payload size)**
```python
MAX_BUNDLE_BYTES = 5 * 1024 * 1024  # 5 MB

def chunk_by_size(resources, max_bytes=MAX_BUNDLE_BYTES):
    """Chunk based on serialized payload size, not count."""
    current_chunk = []
    current_bytes = 0
    
    for resource in resources:
        resource_bytes = len(json.dumps(resource).encode('utf-8'))
        if current_bytes + resource_bytes > max_bytes and current_chunk:
            yield current_chunk
            current_chunk = [resource]
            current_bytes = resource_bytes
        else:
            current_chunk.append(resource)
            current_bytes += resource_bytes
    
    if current_chunk:
        yield current_chunk
```

### 2.4 Parallelism Settings

| Target | Recommended Parallelism | Rationale |
|---|---|---|
| HealthLake (single data store) | 4–8 concurrent bundles | Throttling at ~10 TPS per data store |
| Firely Server (single instance) | 8–16 concurrent bundles | MongoDB write capacity dependent |
| Firely Server (clustered) | 16–32 concurrent bundles | Per-node capacity × node count |
| Cross-region replication | 2–4 concurrent bundles | Network latency dominates |

**Spark parallelism mapping:**
```python
# Match partition count to target parallelism
df = df.repartition(8)  # For HealthLake target

# Use mapPartitions for connection pooling
def send_bundles_partition(partition):
    session = create_http_session()  # One session per partition
    for bundle in partition:
        response = session.post(fhir_endpoint, json=bundle)
        yield response.status_code

results = df.rdd.mapPartitions(send_bundles_partition)
```

---

## 3. Retry & Shred Logic

### 3.1 Exponential Backoff Configuration

```python
RETRY_CONFIG = {
    "max_retries": 5,
    "base_delay_seconds": 1.0,
    "max_delay_seconds": 60.0,
    "exponential_base": 2,
    "jitter": "full",  # full | equal | none
    "retryable_status_codes": [429, 500, 502, 503, 504],
    "retryable_exceptions": [
        "ConnectionTimeout",
        "ConnectionReset", 
        "TooManyRequests"
    ]
}
```

**Backoff formula:**
```
delay = min(max_delay, base_delay × (exponential_base ^ attempt)) + random(0, jitter_range)
```

**Example progression (full jitter):**
| Attempt | Base Delay | Actual Delay (with jitter) |
|---|---|---|
| 1 | 1s | 0–1s |
| 2 | 2s | 0–2s |
| 3 | 4s | 0–4s |
| 4 | 8s | 0–8s |
| 5 | 16s | 0–16s |

### 3.2 Circuit Breaker Pattern

```python
class CircuitBreaker:
    """
    States: CLOSED (normal) → OPEN (failing) → HALF_OPEN (testing)
    """
    FAILURE_THRESHOLD = 5        # Consecutive failures to trip
    RECOVERY_TIMEOUT = 30        # Seconds before trying HALF_OPEN
    SUCCESS_THRESHOLD = 3        # Successes in HALF_OPEN to close
    MONITORING_WINDOW = 60       # Seconds to track failure rate
    FAILURE_RATE_THRESHOLD = 0.5 # 50% failure rate trips breaker

    def should_allow_request(self):
        if self.state == "CLOSED":
            return True
        elif self.state == "OPEN":
            if time_since_tripped > self.RECOVERY_TIMEOUT:
                self.state = "HALF_OPEN"
                return True
            return False
        elif self.state == "HALF_OPEN":
            return True  # Allow limited requests to test recovery
```

**Circuit breaker settings by target:**

| Target | Failure Threshold | Recovery Timeout | Monitoring Window |
|---|---|---|---|
| HealthLake | 5 consecutive | 30s | 60s |
| Firely Server | 10 consecutive | 15s | 30s |
| External EHR endpoints | 3 consecutive | 60s | 120s |
| Kafka (producer) | 5 consecutive | 10s | 30s |

### 3.3 Shred (Split Failed Bundles) Logic

When a transaction bundle fails, the "shred" strategy splits it into smaller units to isolate the failing resource(s):

```
┌────────────────────────────────────────────────────────────────┐
│                    SHRED DECISION TREE                          │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Bundle submission failed?                                     │
│    │                                                           │
│    ├─ HTTP 400 (Bad Request) → Shred immediately              │
│    │   Split into individual resources                         │
│    │   Resubmit each; capture per-resource errors              │
│    │                                                           │
│    ├─ HTTP 413 (Payload Too Large) → Binary split              │
│    │   Split bundle in half, resubmit halves                   │
│    │   Recurse until success or single-resource bundles        │
│    │                                                           │
│    ├─ HTTP 422 (Unprocessable) → Dependency-aware shred        │
│    │   Parse OperationOutcome for offending resource           │
│    │   Remove offending resource + dependents                  │
│    │   Resubmit remainder; route failures to DLQ              │
│    │                                                           │
│    └─ HTTP 5xx (Server Error) → Retry first, then shred       │
│        After max retries, apply binary split strategy          │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

**Shred implementation:**
```python
async def shred_and_retry(bundle, error_response):
    """Split failed bundle and retry sub-bundles."""
    
    if error_response.status == 413:
        # Binary split
        mid = len(bundle.entry) // 2
        left = bundle.entry[:mid]
        right = bundle.entry[mid:]
        return await asyncio.gather(
            submit_bundle(create_bundle(left)),
            submit_bundle(create_bundle(right))
        )
    
    elif error_response.status == 400:
        # Individual resource submission
        results = []
        for entry in bundle.entry:
            result = await submit_single_resource(entry)
            if not result.success:
                await route_to_dead_letter(entry, result.error)
            results.append(result)
        return results
    
    elif error_response.status == 422:
        # Parse and remove offending resources
        offenders = parse_operation_outcome(error_response)
        clean_entries = [e for e in bundle.entry 
                        if e.resource.id not in offenders]
        await submit_bundle(create_bundle(clean_entries))
        for entry in bundle.entry:
            if entry.resource.id in offenders:
                await route_to_dead_letter(entry, "Unprocessable")
```

### 3.4 Dead Letter Queue (DLQ) Handling

**DLQ Structure:**
```json
{
  "dead_letter_record": {
    "id": "dlq-uuid-001",
    "timestamp": "2026-07-07T14:30:00Z",
    "source_workflow": "clinical_document_ingestion",
    "source_job_id": "job-12345",
    "original_bundle_id": "bundle-67890",
    "failed_resource": {
      "resourceType": "Observation",
      "id": "obs-abc-123"
    },
    "error": {
      "http_status": 422,
      "operation_outcome": { ... },
      "message": "Reference Patient/unknown-patient not found"
    },
    "retry_count": 5,
    "last_retry": "2026-07-07T14:29:45Z",
    "state": "exhausted",
    "resolution": null
  }
}
```

**DLQ Processing Rules:**
1. **Auto-retry:** Resources with transient errors (5xx) retry every 15 minutes for 24 hours
2. **Manual review:** Resources with validation errors (400/422) queue for analyst review
3. **Expiration:** Unresolved items older than 7 days escalate to on-call
4. **Replay:** Resolved items can be replayed via `POST /admin/dlq/{id}/replay`

### 3.5 Idempotency

| Method | Idempotency Strategy | Implementation |
|---|---|---|
| `PUT` (update) | Naturally idempotent | Use conditional update: `If-Match: W/"version"` |
| `POST` (create) | Client-assigned ID | Include `resource.id` + `If-None-Exist` header |
| `Bundle (transaction)` | Request ID header | `X-Request-Id: {uuid}` — server deduplicates |
| `Bundle (batch)` | Per-entry fullUrl | Use `urn:uuid:{deterministic-hash}` as fullUrl |

**Idempotency key generation:**
```python
import hashlib

def generate_idempotency_key(resource):
    """Deterministic key from resource content."""
    canonical = json.dumps(resource, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(canonical.encode()).hexdigest()[:32]
```

---

## 4. Workload Profiling

### 4.1 Spark UI Navigation Guide

| Tab | What to Look For | Action Threshold |
|---|---|---|
| **Jobs** | Failed jobs, long-running stages | Any job > 2× median duration |
| **Stages** | Shuffle read/write, task skew | Shuffle spill > 0 bytes |
| **Storage** | Cached RDD memory usage | Cache utilization < 50% → unpersist |
| **Executors** | GC time %, memory usage | GC time > 10% of task time |
| **SQL** | Physical plan, exchange nodes | Broadcast join on large table |
| **Streaming** | Processing time vs batch interval | Processing > 80% of interval |

### 4.2 Identifying Bottlenecks

#### Shuffle Bottleneck
**Symptoms:**
- High "Shuffle Read" / "Shuffle Write" in Stages tab
- Tasks waiting on shuffle fetch
- Network saturation between executors

**Fixes:**
```python
# Increase shuffle partitions for large datasets
spark.conf.set("spark.sql.shuffle.partitions", 200)  # Default: 200

# Use broadcast join for small lookup tables (< 100 MB)
from pyspark.sql.functions import broadcast
result = large_df.join(broadcast(small_lookup), "key")

# Avoid unnecessary shuffles
df = df.repartition("patient_id")  # Co-locate related data
```

#### Spill Bottleneck
**Symptoms:**
- "Spill (Memory)" and "Spill (Disk)" > 0 in task metrics
- Slow disk I/O on worker nodes
- OOM errors on individual tasks

**Fixes:**
```python
# Increase executor memory
spark.conf.set("spark.executor.memory", "8g")
spark.conf.set("spark.executor.memoryOverhead", "2g")

# Increase memory fraction for execution
spark.conf.set("spark.memory.fraction", 0.8)       # Default: 0.6
spark.conf.set("spark.memory.storageFraction", 0.3) # Default: 0.5

# Reduce partition skew
df = df.repartition(400, "hash_key")  # More, smaller partitions
```

#### GC Pressure
**Symptoms:**
- GC time > 10% of task time (visible in Executors tab)
- Long GC pauses (> 500ms)
- "java.lang.OutOfMemoryError: GC overhead limit exceeded"

**Fixes:**
```python
# Switch to G1GC for large heaps
spark.conf.set("spark.executor.extraJavaOptions", 
    "-XX:+UseG1GC -XX:G1HeapRegionSize=16m "
    "-XX:InitiatingHeapOccupancyPercent=35 "
    "-XX:ConcGCThreads=4")

# Reduce object creation (use DataFrame API, not UDFs)
# Avoid: df.rdd.map(lambda row: transform(row))
# Prefer: df.withColumn("result", expr("transform_sql"))

# Increase off-heap memory for Tungsten
spark.conf.set("spark.memory.offHeap.enabled", "true")
spark.conf.set("spark.memory.offHeap.size", "4g")
```

#### I/O Bottleneck
**Symptoms:**
- Tasks spending > 50% time on read/write
- Low CPU utilization despite available tasks
- High "Input Size" with low "Records" (large individual records)

**Fixes:**
```python
# Enable compression for shuffle
spark.conf.set("spark.shuffle.compress", "true")
spark.conf.set("spark.shuffle.spill.compress", "true")

# Use columnar formats for intermediate storage
df.write.parquet("s3://bucket/intermediate/", compression="zstd")

# Parallel I/O to FHIR servers (see Section 2.4)
spark.conf.set("spark.sql.files.maxPartitionBytes", "128m")
```

### 4.3 Memory Tuning Reference

```
┌──────────────────────────────────────────────────────────┐
│              Executor Memory Layout                        │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  Total Executor Memory (spark.executor.memory = 8g)      │
│  ┌────────────────────────────────────────────────────┐  │
│  │  Reserved (300 MB)                                  │  │
│  ├────────────────────────────────────────────────────┤  │
│  │  User Memory (1 - fraction) × (Total - 300 MB)     │  │
│  │  = 0.4 × 7.7 GB = 3.08 GB                         │  │
│  │  [Python UDFs, internal metadata]                  │  │
│  ├────────────────────────────────────────────────────┤  │
│  │  Unified Memory (fraction × (Total - 300 MB))      │  │
│  │  = 0.6 × 7.7 GB = 4.62 GB                         │  │
│  │  ┌──────────────────────────────────────────────┐  │  │
│  │  │  Storage (storageFraction = 50%) = 2.31 GB   │  │  │
│  │  │  [Cached DataFrames, broadcast variables]    │  │  │
│  │  ├──────────────────────────────────────────────┤  │  │
│  │  │  Execution (remaining 50%) = 2.31 GB         │  │  │
│  │  │  [Shuffles, joins, sorts, aggregations]      │  │  │
│  │  └──────────────────────────────────────────────┘  │  │
│  └────────────────────────────────────────────────────┘  │
│                                                          │
│  + Memory Overhead (spark.executor.memoryOverhead = 2g)  │
│    [Container overhead, PySpark, off-heap]               │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### 4.4 Partition Optimization

| Scenario | Target Partition Size | Partition Count Formula |
|---|---|---|
| Reading from S3/ADLS | 128 MB per partition | `total_data_size / 128 MB` |
| Post-shuffle processing | 100–200 MB per partition | `spark.sql.shuffle.partitions` |
| Writing to FHIR server | 1 bundle per partition (for parallelism control) | `total_bundles / desired_concurrency` |
| Streaming micro-batch | 1–5 seconds of data | Kafka partition count |

---

## 5. HealthLake Performance

### 5.1 Throughput Limits

| Operation | Limit | Scope | Notes |
|---|---|---|---|
| `CreateResource` | 50 TPS | Per data store | Soft limit; requestable increase |
| `ReadResource` | 100 TPS | Per data store | Includes `vread` |
| `SearchResource` | 10 TPS | Per data store | Complex queries count as 2–5x |
| `Bundle (transaction)` | 10 TPS | Per data store | Each bundle = 1 request |
| `Bundle (batch)` | 10 TPS | Per data store | Resources inside count toward write TPS |
| `$export` | 1 concurrent | Per data store | Long-running async operation |
| `$import` | 1 concurrent | Per data store | Bulk ingestion path |

### 5.2 Request Pattern Optimization

**DO:**
- Batch writes into bundles of 50–100 resources
- Use `If-None-Exist` for conditional creates (avoids duplicates)
- Distribute requests evenly over time (no burst patterns)
- Use `_count` parameter to limit search result pages
- Prefer `_id` searches over complex chained queries

**DON'T:**
- Send > 10 bundle requests per second
- Use `_include` with `*` (wildcard includes)
- Chain more than 2 levels of `_revinclude`
- Run full-table scans without date range filters
- Submit overlapping `$export` jobs

### 5.3 Bulk Import Optimization

```json
{
  "importConfig": {
    "inputS3Uri": "s3://onyx-fhir-import/batch-2026-07-07/",
    "dataAccessRoleArn": "arn:aws:iam::123456789:role/HealthLakeImportRole",
    "jobName": "daily-clinical-import",
    "fileFormat": "NDJSON"
  }
}
```

**Import performance tips:**
- **File sizing:** 50–200 MB NDJSON files (too small = overhead; too large = no parallelism)
- **File count:** 10–100 files per import job (HealthLake parallelizes across files)
- **Pre-validation:** Validate FHIR resources before import (invalid resources fail silently)
- **Ordering:** Place Patient resources in early files (reference targets available first)
- **Monitoring:** Poll `DescribeImportJob` every 60s; expect ~1,000 resources/second

### 5.4 Query Optimization

| Query Pattern | Performance | Optimization |
|---|---|---|
| `GET /Patient?_id=abc` | ⚡ Fast | Direct key lookup |
| `GET /Patient?identifier=MRN\|123` | ⚡ Fast | Indexed field |
| `GET /Observation?patient=Patient/abc&date=gt2026-01-01` | ✅ Good | Indexed + date filter |
| `GET /Observation?code=http://loinc.org\|12345` | ✅ Good | Token search indexed |
| `GET /Observation?value-quantity=gt100` | ⚠️ Slow | Quantity comparisons expensive |
| `GET /Patient?_has:Observation:patient:code=12345` | ❌ Very slow | Reverse chain = table scan |

### 5.5 $export Tuning

```
GET /fhir/$export
  ?_outputFormat=application/fhir+ndjson
  &_type=Patient,Encounter,Observation
  &_since=2026-07-01T00:00:00Z
  &_typeFilter=Observation?code=http://loinc.org|12345
```

**Export optimization:**
- Always specify `_type` (avoid exporting all resource types)
- Use `_since` for incremental exports (requires previous export timestamp)
- Apply `_typeFilter` for resource-level filtering (reduces output volume)
- Expected throughput: 10,000–50,000 resources/minute depending on complexity
- Output lands in S3; use multipart download for large exports

---

## 6. Firely Performance

### 6.1 MongoDB Index Optimization

**Essential indexes for Firely Server:**
```javascript
// Patient lookup (most common)
db.Patient.createIndex({ "identifier.value": 1, "identifier.system": 1 })
db.Patient.createIndex({ "name.family": 1, "name.given": 1 })
db.Patient.createIndex({ "meta.lastUpdated": -1 })

// Observation queries
db.Observation.createIndex({ "subject.reference": 1, "effectiveDateTime": -1 })
db.Observation.createIndex({ "code.coding.system": 1, "code.coding.code": 1 })
db.Observation.createIndex({ 
    "subject.reference": 1, 
    "code.coding.code": 1, 
    "effectiveDateTime": -1 
})

// Encounter queries
db.Encounter.createIndex({ "subject.reference": 1, "period.start": -1 })
db.Encounter.createIndex({ "status": 1, "class.code": 1 })

// Bundle tracking / history
db.searchindex.createIndex({ "key": 1, "value": 1, "resourceType": 1 })

// Compound index for search engine
db.searchindex.createIndex({ 
    "resourceType": 1, 
    "key": 1, 
    "value": 1, 
    "resourceId": 1 
}, { background: true })
```

**Index health checks:**
```javascript
// Check index usage stats
db.Patient.aggregate([{ $indexStats: {} }])

// Identify slow queries (> 100ms)
db.setProfilingLevel(1, { slowms: 100 })
db.system.profile.find().sort({ ts: -1 }).limit(20)

// Check index sizes
db.stats().indexSizes
```

### 6.2 Connection Pool Configuration

**Firely Server `appsettings.json`:**
```json
{
  "MongoDB": {
    "ConnectionString": "mongodb://firely-mongo:27017",
    "DatabaseName": "firely_fhir",
    "MaxConnectionPoolSize": 200,
    "MinConnectionPoolSize": 25,
    "WaitQueueTimeout": "00:00:30",
    "ConnectTimeout": "00:00:10",
    "SocketTimeout": "00:00:30",
    "ServerSelectionTimeout": "00:00:15",
    "WriteConcern": "majority",
    "ReadPreference": "secondaryPreferred"
  }
}
```

**Connection pool sizing formula:**
```
max_pool_size = (expected_concurrent_requests × avg_query_time_ms) / 1000 × 1.5
```

Example: 100 concurrent requests × 50ms avg = 5 connections needed × 1.5 safety = 8 minimum
- Rule of thumb: `max_pool_size = 2 × expected_peak_concurrent_requests`

### 6.3 Query Plan Analysis

```javascript
// Analyze query execution plan
db.Observation.find({
    "subject.reference": "Patient/abc",
    "code.coding.code": "12345",
    "effectiveDateTime": { $gte: ISODate("2026-01-01") }
}).explain("executionStats")

// Key metrics to check:
// - totalDocsExamined vs. nReturned (ratio should be < 10:1)
// - executionTimeMillis (should be < 100ms for indexed queries)
// - stage: should show IXSCAN, not COLLSCAN
// - indexBounds: verify the expected index is used
```

**Query plan red flags:**

| Indicator | Threshold | Action |
|---|---|---|
| COLLSCAN in winningPlan | Any occurrence | Add missing index |
| docsExamined/nReturned > 100 | > 100:1 ratio | Improve index selectivity |
| executionTimeMillis > 500ms | > 500ms | Compound index or query redesign |
| Sort in memory | Any large sort | Add sort key to index |

### 6.4 Cache Configuration

**Firely Server cache settings:**
```json
{
  "Cache": {
    "MaxCacheEntries": 10000,
    "ExpirationMinutes": 30,
    "SlidingExpirationMinutes": 10,
    "ConformanceCacheMinutes": 60,
    "SearchCacheEnabled": true,
    "SearchCacheMaxSize": 5000,
    "SearchCacheTTLMinutes": 5,
    "CapabilityStatementCacheMinutes": 1440
  }
}
```

**Cache tuning guidelines:**
- **ConformanceCache:** Long TTL (60+ min) — rarely changes
- **SearchCache:** Short TTL (5 min) — balances freshness vs. performance
- **ResourceCache:** Medium TTL (30 min) — frequently accessed patients/practitioners
- **Monitor hit rate:** Target > 80% for conformance, > 50% for search

### 6.5 Firely Search Index (FSI) Tuning

**FSI rebuild triggers:**
- After bulk import > 10,000 resources
- After schema/SearchParameter changes
- When query performance degrades (> 2× baseline)

**FSI configuration:**
```json
{
  "FhirSearchIndex": {
    "Enabled": true,
    "BatchSize": 500,
    "ParallelIndexingThreads": 4,
    "RebuildOnStartup": false,
    "IncrementalIndexing": true,
    "IndexRefreshIntervalSeconds": 5
  }
}
```

**FSI performance tips:**
- Keep `BatchSize` between 200–1000 (balance memory vs. throughput)
- Set `ParallelIndexingThreads` = CPU cores / 2
- Enable `IncrementalIndexing` for production (avoid full rebuilds)
- Monitor index lag: `GET /admin/fsi/status`

---

## 7. Network & I/O

### 7.1 VPC Endpoint Configuration

| Service | Endpoint Type | Rationale |
|---|---|---|
| AWS HealthLake | Interface endpoint | Private connectivity, no internet transit |
| S3 (for export/import) | Gateway endpoint | Free, no NAT gateway charges |
| Secrets Manager | Interface endpoint | Credential retrieval without internet |
| CloudWatch | Interface endpoint | Metrics/logs stay in VPC |
| STS | Interface endpoint | Token refresh without internet |

**VPC endpoint performance benefits:**
- Eliminates NAT gateway bandwidth bottleneck (max 45 Gbps per NAT)
- Reduces latency by 1–5ms (no internet routing)
- Eliminates NAT gateway data processing charges ($0.045/GB)
- Enables private DNS resolution within VPC

### 7.2 Connection Pooling

**HTTP connection pool configuration (Python/requests):**
```python
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def create_fhir_session():
    session = requests.Session()
    
    adapter = HTTPAdapter(
        pool_connections=20,      # Number of connection pools
        pool_maxsize=50,          # Connections per pool
        max_retries=Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504]
        ),
        pool_block=False          # Don't block when pool exhausted
    )
    
    session.mount("https://", adapter)
    session.headers.update({
        "Content-Type": "application/fhir+json",
        "Accept": "application/fhir+json",
        "Connection": "keep-alive"
    })
    
    return session
```

**Pool sizing by target:**

| Target | pool_connections | pool_maxsize | Keep-alive timeout |
|---|---|---|---|
| HealthLake | 5 | 20 | 60s |
| Firely Server | 10 | 50 | 120s |
| External EHR | 3 | 10 | 30s |

### 7.3 Compression

**Enable gzip for FHIR payloads:**
```python
session.headers.update({
    "Accept-Encoding": "gzip, deflate",
    "Content-Encoding": "gzip"  # For request bodies > 1 KB
})

# Compress outgoing bundles
import gzip
import json

def compress_bundle(bundle):
    json_bytes = json.dumps(bundle).encode('utf-8')
    if len(json_bytes) > 1024:  # Only compress if > 1 KB
        return gzip.compress(json_bytes)
    return json_bytes
```

**Compression impact estimates:**
| FHIR Resource Type | Avg Uncompressed | Avg Compressed | Ratio |
|---|---|---|---|
| Patient | 2.5 KB | 0.8 KB | 3:1 |
| Observation | 1.2 KB | 0.4 KB | 3:1 |
| Bundle (50 resources) | 150 KB | 25 KB | 6:1 |
| Bundle (200 resources) | 600 KB | 80 KB | 7.5:1 |
| DocumentReference (with attachment) | 500 KB | 350 KB | 1.4:1 |

### 7.4 DNS Caching

**JVM DNS cache (for Spark/Databricks):**
```python
# Set in spark configuration
spark.conf.set("spark.executor.extraJavaOptions",
    "-Dsun.net.inetaddr.ttl=60 "     # Cache DNS for 60s (default: forever)
    "-Dsun.net.inetaddr.negative.ttl=10"  # Cache negative for 10s
)
```

**Application-level DNS caching:**
```python
import dns.resolver
from cachetools import TTLCache

dns_cache = TTLCache(maxsize=1000, ttl=60)

def cached_resolve(hostname):
    if hostname not in dns_cache:
        answers = dns.resolver.resolve(hostname, 'A')
        dns_cache[hostname] = [r.address for r in answers]
    return dns_cache[hostname]
```

**DNS optimization checklist:**
- [ ] JVM TTL set to 60s (not infinite/0)
- [ ] VPC DNS resolver configured (AmazonProvidedDNS)
- [ ] Private hosted zones for internal services
- [ ] DNS query logging enabled for troubleshooting
- [ ] Route 53 health checks for failover endpoints

---

## 8. Pre-Change Performance Review Checklist

Complete this 30-item checklist before any major interoperability change (new workflow, FHIR store migration, cluster resize, bundle configuration change, etc.).

### Baseline Verification (Items 1–8)

| # | Item | Status | Notes |
|---|---|---|---|
| 1 | Current P50/P95/P99 latency documented for affected workflows | ☐ | |
| 2 | Current throughput (resources/minute) baselined | ☐ | |
| 3 | Current error rate (%) captured for 7-day window | ☐ | |
| 4 | Current cluster utilization (CPU/memory/network) profiled | ☐ | |
| 5 | Current FHIR store response times (read/write/search) captured | ☐ | |
| 6 | Current bundle success rate and average bundle size documented | ☐ | |
| 7 | DLQ depth and age distribution recorded | ☐ | |
| 8 | Peak hour traffic patterns identified and documented | ☐ | |

### Capacity Planning (Items 9–15)

| # | Item | Status | Notes |
|---|---|---|---|
| 9 | Expected volume change calculated (% increase/decrease) | ☐ | |
| 10 | FHIR store TPS headroom verified (current usage vs. limits) | ☐ | |
| 11 | Cluster max-workers sufficient for projected load | ☐ | |
| 12 | Network bandwidth adequate (VPC endpoint limits, NAT capacity) | ☐ | |
| 13 | Storage capacity checked (S3 lifecycle, MongoDB disk, temp space) | ☐ | |
| 14 | Connection pool sizes validated against new concurrency levels | ☐ | |
| 15 | Memory allocation sufficient for new payload sizes | ☐ | |

### Risk Assessment (Items 16–22)

| # | Item | Status | Notes |
|---|---|---|---|
| 16 | Rollback plan documented with estimated rollback time | ☐ | |
| 17 | Impact on downstream consumers assessed | ☐ | |
| 18 | Impact on upstream producers assessed | ☐ | |
| 19 | Retry/circuit breaker thresholds appropriate for new patterns | ☐ | |
| 20 | Idempotency maintained through the change | ☐ | |
| 21 | Data consistency guarantees preserved | ☐ | |
| 22 | Concurrent change conflicts checked (no overlapping deployments) | ☐ | |

### Monitoring & Alerting (Items 23–27)

| # | Item | Status | Notes |
|---|---|---|---|
| 23 | Alerts updated for new expected thresholds | ☐ | |
| 24 | Dashboard shows relevant metrics for the change | ☐ | |
| 25 | Log level increased to DEBUG for affected components (temporary) | ☐ | |
| 26 | Performance regression detection configured (automated comparison) | ☐ | |
| 27 | On-call engineer briefed on change and expected behavior | ☐ | |

### Validation & Sign-off (Items 28–30)

| # | Item | Status | Notes |
|---|---|---|---|
| 28 | Load test completed in staging with production-scale data | ☐ | |
| 29 | Performance comparison report reviewed (staging vs. production baseline) | ☐ | |
| 30 | Sign-off obtained from: Platform Lead ☐ / Data Eng ☐ / SRE ☐ | ☐ | |

---

## 9. Performance Testing Procedures

### 9.1 Load Testing Framework

**Tool selection:**
| Scenario | Tool | Rationale |
|---|---|---|
| FHIR API load testing | Locust (Python) | Custom FHIR payload generation |
| Bundle throughput testing | k6 (JavaScript) | High-concurrency HTTP testing |
| End-to-end workflow testing | Spark load generator | Tests full pipeline including transforms |
| HealthLake limits probing | AWS SDK + custom script | Precise TPS measurement |

**Locust FHIR load test example:**
```python
from locust import HttpUser, task, between
import json

class FHIRLoadTest(HttpUser):
    wait_time = between(0.1, 0.5)
    
    @task(3)
    def create_patient_bundle(self):
        bundle = generate_patient_bundle(size=50)
        self.client.post(
            "/fhir",
            json=bundle,
            headers={"Content-Type": "application/fhir+json"},
            name="POST /fhir (Patient Bundle x50)"
        )
    
    @task(5)
    def search_patient(self):
        mrn = random_mrn()
        self.client.get(
            f"/fhir/Patient?identifier=MRN|{mrn}",
            name="GET /Patient by MRN"
        )
    
    @task(2)
    def read_observation(self):
        patient_id = random_patient_id()
        self.client.get(
            f"/fhir/Observation?patient={patient_id}&_count=50",
            name="GET /Observation by Patient"
        )
```

### 9.2 Baseline Establishment

**Baseline metrics to capture:**
```yaml
performance_baseline:
  capture_period: "7 consecutive business days"
  metrics:
    latency:
      - p50_ms
      - p95_ms
      - p99_ms
      - max_ms
    throughput:
      - resources_per_minute_avg
      - resources_per_minute_peak
      - bundles_per_minute
    errors:
      - error_rate_percent
      - timeout_rate_percent
      - throttle_rate_percent (429s)
    resources:
      - cluster_cpu_avg_percent
      - cluster_memory_avg_percent
      - executor_gc_time_percent
      - shuffle_bytes_per_job
    fhir_store:
      - read_latency_p95_ms
      - write_latency_p95_ms
      - search_latency_p95_ms
      - concurrent_connections_avg
```

**Baseline capture script:**
```python
def capture_baseline(workflow_name, days=7):
    """Capture 7-day performance baseline for a workflow."""
    metrics = {
        "workflow": workflow_name,
        "period_start": (datetime.now() - timedelta(days=days)).isoformat(),
        "period_end": datetime.now().isoformat(),
        "latency": {
            "p50_ms": query_cloudwatch_percentile(workflow_name, 50),
            "p95_ms": query_cloudwatch_percentile(workflow_name, 95),
            "p99_ms": query_cloudwatch_percentile(workflow_name, 99),
        },
        "throughput": {
            "avg_resources_per_min": query_avg_throughput(workflow_name),
            "peak_resources_per_min": query_peak_throughput(workflow_name),
        },
        "error_rate": query_error_rate(workflow_name),
        "resource_utilization": query_cluster_metrics(workflow_name),
    }
    
    save_baseline(workflow_name, metrics)
    return metrics
```

### 9.3 Regression Detection

**Automated regression detection rules:**

| Metric | Warning Threshold | Critical Threshold | Window |
|---|---|---|---|
| P95 latency | > 1.5× baseline | > 2× baseline | 30 min rolling |
| P99 latency | > 2× baseline | > 3× baseline | 30 min rolling |
| Throughput | < 0.8× baseline | < 0.5× baseline | 15 min rolling |
| Error rate | > 2× baseline OR > 1% | > 5× baseline OR > 5% | 10 min rolling |
| Bundle success rate | < 95% | < 90% | 15 min rolling |
| GC time | > 15% of task time | > 25% of task time | Per job |

**Statistical regression detection:**
```python
import numpy as np
from scipy import stats

def detect_regression(baseline_samples, current_samples, alpha=0.05):
    """
    Two-sample t-test for performance regression.
    Returns True if current performance is statistically worse.
    """
    # One-tailed test: is current mean significantly HIGHER than baseline?
    t_stat, p_value = stats.ttest_ind(
        current_samples, 
        baseline_samples, 
        alternative='greater'
    )
    
    regression_detected = p_value < alpha
    
    # Also check practical significance (> 20% degradation)
    baseline_mean = np.mean(baseline_samples)
    current_mean = np.mean(current_samples)
    practical_regression = (current_mean - baseline_mean) / baseline_mean > 0.2
    
    return {
        "statistical_regression": regression_detected,
        "practical_regression": practical_regression,
        "p_value": p_value,
        "baseline_mean": baseline_mean,
        "current_mean": current_mean,
        "percent_change": ((current_mean - baseline_mean) / baseline_mean) * 100
    }
```

### 9.4 Capacity Planning Formulas

**Formula 1: Required cluster size**
```
required_workers = ceil(
    (peak_resources_per_hour × avg_processing_time_ms) / 
    (3600 × 1000 × cores_per_worker × utilization_target)
)

Example:
  peak = 500,000 resources/hour
  avg_processing = 50ms per resource
  cores_per_worker = 4
  utilization_target = 0.7

  required_workers = ceil((500000 × 50) / (3600000 × 4 × 0.7))
                   = ceil(25000000 / 10080000)
                   = ceil(2.48)
                   = 3 workers (minimum)
```

**Formula 2: FHIR store capacity**
```
required_tps = ceil(
    (peak_resources_per_hour / 3600) × 
    (1 + retry_overhead_percent / 100) × 
    (1 + headroom_percent / 100)
)

Example:
  peak = 500,000 resources/hour → 139 resources/second
  bundle_size = 50 → 2.78 bundles/second
  retry_overhead = 10%
  headroom = 30%

  required_tps = ceil(2.78 × 1.10 × 1.30) = ceil(3.97) = 4 TPS (bundle submissions)
```

**Formula 3: Memory per executor**
```
required_memory_gb = max(
    (avg_partition_size_mb × partitions_per_executor / 1024) × 2.5,
    (largest_single_record_mb × parallelism_per_executor / 1024) × 3
)

Example:
  avg_partition = 128 MB
  partitions_per_executor = 4 (= cores)
  
  required_memory = (128 × 4 / 1024) × 2.5 = 1.25 GB minimum
  → With overhead: 4 GB executor memory recommended
```

**Formula 4: Bundle parallelism**
```
optimal_parallelism = min(
    target_tps × avg_latency_seconds,     # Little's Law
    fhir_store_tps_limit × 0.8,            # Stay under throttle threshold
    available_executor_cores × 0.5          # Leave cores for transforms
)

Example:
  target_tps = 8 bundles/sec
  avg_latency = 0.5s
  fhir_store_limit = 10 TPS

  Little's Law: 8 × 0.5 = 4 concurrent
  Throttle safety: 10 × 0.8 = 8 concurrent
  
  optimal_parallelism = min(4, 8, available_cores) = 4 concurrent bundles
```

**Formula 5: Autoscale headroom**
```
max_workers = ceil(
    required_workers_at_peak × 
    (1 + burst_headroom_percent / 100) × 
    (1 / (1 - spot_interruption_rate))
)

Example:
  required_at_peak = 8 workers
  burst_headroom = 25% (for unexpected spikes)
  spot_interruption_rate = 0.05 (5%)

  max_workers = ceil(8 × 1.25 × 1.053) = ceil(10.53) = 11 workers
```

### 9.5 Performance Test Schedule

| Test Type | Frequency | Duration | Scope |
|---|---|---|---|
| Smoke test | Every deployment | 5 minutes | Basic functionality at low load |
| Load test | Weekly (automated) | 30 minutes | Sustained load at expected peak |
| Stress test | Monthly | 60 minutes | 2× expected peak, find breaking point |
| Soak test | Quarterly | 8 hours | Detect memory leaks, connection exhaustion |
| Chaos test | Quarterly | 2 hours | Simulate failures (node death, network partition) |
| Capacity test | Before major changes | 2 hours | Validate formulas against reality |

### 9.6 Performance Test Report Template

```markdown
## Performance Test Report

**Test Date:** YYYY-MM-DD
**Test Type:** [Load / Stress / Soak / Chaos]
**Workflow Under Test:** [workflow name]
**Environment:** [staging / pre-prod]

### Test Parameters
- Duration: X minutes
- Concurrent users/threads: N
- Target throughput: X resources/minute
- Bundle size: N resources
- Parallelism: N concurrent bundles

### Results Summary
| Metric | Baseline | Measured | Change | Status |
|--------|----------|----------|--------|--------|
| P50 latency | Xms | Xms | +X% | ✅/⚠️/❌ |
| P95 latency | Xms | Xms | +X% | ✅/⚠️/❌ |
| Throughput | X/min | X/min | +X% | ✅/⚠️/❌ |
| Error rate | X% | X% | +X% | ✅/⚠️/❌ |
| CPU utilization | X% | X% | +X% | ✅/⚠️/❌ |
| Memory utilization | X% | X% | +X% | ✅/⚠️/❌ |

### Observations
- [ observation 1 ]
- [ observation 2 ]

### Recommendations
- [ recommendation 1 ]
- [ recommendation 2 ]

### Sign-off
- Tested by: [name]
- Reviewed by: [name]
- Approved for production: ☐ Yes / ☐ No / ☐ Conditional
```

---

## Appendix A: Quick Reference Card

### Critical Thresholds at a Glance

| System | Metric | Yellow | Red |
|---|---|---|---|
| Databricks | Executor GC time | > 10% | > 20% |
| Databricks | Shuffle spill to disk | > 0 | > 1 GB |
| Databricks | Task skew (max/median) | > 3× | > 10× |
| HealthLake | Bundle TPS | > 8 TPS | > 10 TPS (limit) |
| HealthLake | Search latency P95 | > 500ms | > 2000ms |
| Firely | MongoDB connections | > 70% pool | > 90% pool |
| Firely | Query without IXSCAN | Any occurrence | — |
| Firely | FSI index lag | > 30s | > 120s |
| Network | Connection pool exhaustion | > 80% | > 95% |
| Pipeline | DLQ depth | > 100 items | > 1000 items |
| Pipeline | Error rate | > 1% | > 5% |

### Emergency Performance Playbook

1. **Throttling detected (429s spiking):**
   - Immediately reduce parallelism by 50%
   - Enable circuit breaker if not active
   - Check if concurrent jobs are competing

2. **OOM errors on executors:**
   - Increase `spark.executor.memory` by 50%
   - Reduce partition size (increase partition count)
   - Check for data skew in affected stage

3. **Latency spike (> 3× baseline):**
   - Check FHIR store health dashboard
   - Verify no MongoDB lock contention (Firely)
   - Check for network saturation (VPC flow logs)

4. **DLQ growing rapidly:**
   - Pause affected workflow
   - Sample DLQ for error pattern
   - If validation errors: check upstream data quality
   - If transient errors: check target system health

---

## Appendix B: Configuration Templates

### Databricks Cluster JSON (Production Batch)
```json
{
  "cluster_name": "onyx-clinical-batch-prod",
  "spark_version": "14.3.x-scala2.12",
  "node_type_id": "r5.2xlarge",
  "driver_node_type_id": "r5.4xlarge",
  "autoscale": {
    "min_workers": 4,
    "max_workers": 16
  },
  "aws_attributes": {
    "first_on_demand": 1,
    "availability": "SPOT_WITH_FALLBACK",
    "zone_id": "auto",
    "spot_bid_price_percent": 100,
    "ebs_volume_count": 1,
    "ebs_volume_size": 100,
    "ebs_volume_type": "GENERAL_PURPOSE_SSD"
  },
  "spark_conf": {
    "spark.sql.shuffle.partitions": "200",
    "spark.executor.memory": "12g",
    "spark.executor.memoryOverhead": "3g",
    "spark.memory.fraction": "0.7",
    "spark.shuffle.compress": "true",
    "spark.sql.adaptive.enabled": "true",
    "spark.sql.adaptive.coalescePartitions.enabled": "true"
  },
  "custom_tags": {
    "team": "interoperability",
    "environment": "production",
    "cost_center": "platform-eng"
  }
}
```

### Retry Configuration (Production)
```json
{
  "retry_policy": {
    "healthlake": {
      "max_retries": 5,
      "base_delay_ms": 1000,
      "max_delay_ms": 60000,
      "jitter": "full",
      "retryable_codes": [429, 500, 502, 503, 504],
      "circuit_breaker": {
        "failure_threshold": 5,
        "recovery_timeout_ms": 30000,
        "half_open_requests": 3
      }
    },
    "firely": {
      "max_retries": 3,
      "base_delay_ms": 500,
      "max_delay_ms": 30000,
      "jitter": "equal",
      "retryable_codes": [429, 500, 502, 503],
      "circuit_breaker": {
        "failure_threshold": 10,
        "recovery_timeout_ms": 15000,
        "half_open_requests": 5
      }
    }
  },
  "shred_policy": {
    "enabled": true,
    "strategy": "binary_split_then_individual",
    "max_shred_depth": 3,
    "dead_letter_after_shred_failure": true
  },
  "dead_letter": {
    "auto_retry_interval_minutes": 15,
    "auto_retry_max_age_hours": 24,
    "escalation_age_days": 7,
    "max_queue_depth_alert": 1000
  }
}
```

---

*Document maintained by Platform Engineering. For questions or updates, contact the Interoperability team.*
