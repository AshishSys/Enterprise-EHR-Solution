# Firely vs HealthLake Support Matrix

## Decision Matrix for CMS Interoperability Engineers (Onyx/Abacus)

> **Purpose:** Help engineers quickly determine whether a problem is Firely-specific, HealthLake-specific, or integration-specific when working on CMS interoperability workflows.
>
> **Last Updated:** 2026-07-07 | **Audience:** Onyx/Abacus Engineering Teams

---

## Table of Contents

1. [Architecture Comparison](#1-architecture-comparison)
2. [Ingestion & Data Loading](#2-ingestion--data-loading)
3. [API Behavior Differences](#3-api-behavior-differences)
4. [Performance Characteristics](#4-performance-characteristics)
5. [Validation Behavior](#5-validation-behavior)
6. [Migration Patterns](#6-migration-patterns)
7. [Decision Matrix (Core Artifact)](#7-decision-matrix)
8. [Operational Differences](#8-operational-differences)
9. [Known Limitations & Workarounds](#9-known-limitations--workarounds)

---

## 1. Architecture Comparison

### Side-by-Side Overview

| Dimension | Firely Server | AWS HealthLake |
|-----------|--------------|----------------|
| **Runtime** | .NET 8+ application | AWS Managed Service (serverless) |
| **Data Store** | MongoDB (primary), SQL Server (optional) | Purpose-built AWS data store (columnar + index) |
| **Deployment** | Self-managed: on-prem, VM, K8s, Docker | Fully managed: single API call to provision |
| **FHIR Version** | R3, R4, R5 (configurable) | R4 only (as of 2026) |
| **Scaling** | Manual horizontal scaling (multiple instances + load balancer) | Auto-scales based on request volume |
| **Authentication** | Configurable (SMART on FHIR, OAuth2, custom) | AWS IAM + Signature V4 (SMART on FHIR via proxy) |
| **Extensibility** | Plugins, interceptors, custom operations | Limited to supported operations; Lambda integration for transforms |
| **Multi-tenancy** | Compartments or separate instances | Separate data stores per tenant |
| **Network** | Any network topology | VPC endpoints, PrivateLink, or public endpoint |

### Deployment Models

```
┌─────────────────────────────────────────────────────────────────┐
│                     FIRELY DEPLOYMENT                            │
│                                                                 │
│  ┌──────────┐    ┌──────────────┐    ┌──────────────────┐      │
│  │  Client  │───▶│ Load Balancer│───▶│ Firely Server(s) │      │
│  └──────────┘    └──────────────┘    │  (.NET process)  │      │
│                                      └────────┬─────────┘      │
│                                               │                 │
│                                      ┌────────▼─────────┐      │
│                                      │    MongoDB        │      │
│                                      │  (Replica Set)   │      │
│                                      └──────────────────┘      │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                   HEALTHLAKE DEPLOYMENT                          │
│                                                                 │
│  ┌──────────┐    ┌──────────────┐    ┌──────────────────┐      │
│  │  Client  │───▶│ AWS API GW / │───▶│   HealthLake     │      │
│  └──────────┘    │ Direct Call   │    │   Data Store     │      │
│                  └──────────────┘    └────────┬─────────┘      │
│                                               │                 │
│                                      ┌────────▼─────────┐      │
│                                      │  S3 (bulk I/O)   │      │
│                                      │  CloudWatch      │      │
│                                      │  Lake Formation  │      │
│                                      └──────────────────┘      │
└─────────────────────────────────────────────────────────────────┘
```

### Scaling Approaches

| Aspect | Firely | HealthLake |
|--------|--------|------------|
| **Horizontal scaling** | Add instances behind LB; share MongoDB | Automatic (transparent) |
| **Read replicas** | MongoDB replica sets | Managed internally |
| **Write throughput** | Limited by MongoDB write concern config | Managed; throttled at service limits |
| **Burst capacity** | Requires pre-provisioning | Auto-burst with soft/hard limits |
| **Max data store size** | Limited by MongoDB cluster capacity | Effectively unlimited (petabyte-scale) |

### Cost Models

| Component | Firely | HealthLake |
|-----------|--------|------------|
| **Base cost** | License fee + infrastructure (VMs, MongoDB) | Per-request + storage |
| **Storage** | MongoDB hosting costs | $3.60/GB/month (indexed FHIR data) |
| **Requests** | Infrastructure cost (fixed) | ~$0.05 per 1,000 read requests |
| **Data import** | Compute costs for FSI | $0.19 per GB imported |
| **Data export** | Compute costs for $export | $0.19 per GB exported |
| **Scaling costs** | Linear with instance count | Pay-per-use, auto-scales |

---

## 2. Ingestion & Data Loading

### Firely Server Ingest (FSI)

| Feature | Details |
|---------|---------|
| **Tool** | Firely Server Ingest (FSI) CLI / SDK |
| **Input formats** | FHIR Bundles (JSON/XML), individual resources |
| **Bulk load** | FSI direct MongoDB insert (bypasses REST API for speed) |
| **Incremental** | REST API (PUT/POST), Transaction bundles |
| **Transaction bundles** | Full ACID support, max ~500-1000 entries per bundle (practical) |
| **Batch bundles** | Supported, no transactional guarantees |
| **Validation on ingest** | Configurable: off, structural, profile-based |
| **Throughput (FSI bulk)** | 5,000–50,000 resources/sec (depends on hardware) |
| **Throughput (REST)** | 100–500 resources/sec per instance |
| **Conditional creates** | Supported via If-None-Exist header |
| **Upsert** | Supported via PUT with client-assigned IDs |

### HealthLake Import

| Feature | Details |
|---------|---------|
| **Primary bulk method** | `$import` operation (S3-based) |
| **Input format** | NDJSON files in S3 bucket |
| **API ingestion** | CreateResource, UpdateResource, batch bundles |
| **Transaction bundles** | **NOT supported** — only batch bundles |
| **Batch bundle limit** | Max 160 entries per batch bundle (hard limit) |
| **Validation on import** | Always validates structure; profiles configurable |
| **$import throughput** | 10,000+ resources/sec (varies by resource complexity) |
| **API throughput** | Subject to TPS limits (default: 100 TPS, requestable increase) |
| **Conditional creates** | Supported |
| **Upsert** | Supported via PUT with client-assigned IDs |
| **$import idempotency** | Re-importing same data creates duplicates unless IDs match |

### Critical Differences for Onyx/Abacus Workflows

| Scenario | Firely Approach | HealthLake Approach | Integration Concern |
|----------|----------------|--------------------|--------------------|
| **Initial data load (millions of resources)** | FSI bulk → MongoDB | Upload NDJSON to S3 → `$import` | Different formats require dual pipeline |
| **Real-time member updates** | POST/PUT via REST | CreateResource/UpdateResource API | Unified client can abstract; watch for ID generation differences |
| **CMS submission bundles** | Transaction bundle (full ACID) | Convert to batch bundle (no transactions!) | **Must redesign transaction logic for HealthLake** |
| **Bulk claims load** | FSI with pre-validation | NDJSON → S3 → $import | Validation timing differs: pre-load vs during-load |
| **Reference resolution** | Resolved at bundle processing time | Resolved at individual entry level (batch) | Broken references may silently succeed in HealthLake batch |

### Unified Workflow Pattern

```
┌──────────────────┐     ┌────────────────────────────┐
│  Source System   │     │    Ingestion Orchestrator   │
│  (Claims, ADT,  │────▶│    (Onyx/Abacus Service)    │
│   Eligibility)  │     └──────────┬─────────────────┘
└──────────────────┘               │
                                   ├──────────────────────────┐
                          ┌────────▼─────────┐    ┌──────────▼──────────┐
                          │  Firely Pipeline  │    │ HealthLake Pipeline  │
                          │                  │    │                     │
                          │ 1. Validate      │    │ 1. Validate         │
                          │ 2. Bundle (txn)  │    │ 2. Convert → NDJSON │
                          │ 3. POST bundle   │    │ 3. Upload to S3     │
                          │ 4. Verify        │    │ 4. Trigger $import  │
                          └──────────────────┘    │ 5. Poll status      │
                                                  └─────────────────────┘
```

---

## 3. API Behavior Differences

### Search Parameter Support

| Search Feature | Firely | HealthLake | Notes |
|---------------|--------|------------|-------|
| **Standard search params** | All R4 defined params | Most R4 params (some gaps) | Check HealthLake docs for unsupported params |
| **Custom search params** | Fully supported (define & index) | **Not supported** | Must work around with $search or different query patterns |
| **Chained search** | Full support (`Patient.generalPractitioner.name`) | Limited depth (1-2 levels) | Deep chains may fail on HealthLake |
| **Reverse chaining (_has)** | Supported | Supported (limited) | Performance varies significantly |
| **Composite search params** | Supported | Limited support | Test each composite specifically |
| **_filter** | Supported (with extensions) | **Not supported** | Use equivalent _search parameters |
| **_text / _content** | Full-text search (configurable) | **Not supported** | No text search in HealthLake |
| **Token :text modifier** | Supported | **Not supported** | Must use exact token matching |
| **:above / :below (hierarchy)** | Supported | Limited | Code hierarchy searches differ |
| **_type parameter** | Supported | Supported | Behavior consistent |
| **Date precision** | Handles partial dates well | Strict ISO 8601 required | Normalize dates before querying HealthLake |

### Pagination Behavior

| Aspect | Firely | HealthLake |
|--------|--------|------------|
| **Default page size** | 10 (configurable server-wide) | 10 |
| **Max page size (_count)** | Configurable (default: 100, can be increased) | 1,000 (hard limit) |
| **Pagination mechanism** | Offset-based (link.next with _skip) | Opaque continuation token |
| **Consistency during pagination** | Snapshot at query time (configurable) | Eventually consistent (may see new data mid-pagination) |
| **Token expiry** | N/A (offset-based) | Tokens expire after ~5 minutes |
| **Total count (_total)** | Accurate (with performance cost) | Estimated (not exact for large result sets) |
| **Sort stability** | Stable across pages | Not guaranteed stable |

### Resource Versioning

| Aspect | Firely | HealthLake |
|--------|--------|------------|
| **Version ID format** | Sequential integer (1, 2, 3…) | UUID-like string |
| **_history endpoint** | Full support (resource + type + system level) | Resource-level only |
| **Version retention** | Configurable (keep all, last N, time-based) | All versions retained indefinitely |
| **vread** | Supported | Supported |
| **ETag / If-Match** | Supported for optimistic locking | Supported |
| **If-None-Match** | Supported | Supported |

### _include / _revinclude

| Aspect | Firely | HealthLake |
|--------|--------|------------|
| **_include** | Full support, multi-level with :iterate | Single level only (no :iterate) |
| **_revinclude** | Full support | Supported (limited to direct references) |
| **Max included resources** | Configurable | Hard limit ~1,000 included resources |
| **Circular reference handling** | Detected and stopped | N/A (single level only) |
| **:iterate** | Supported | **Not supported** |
| **Wildcard _include (*)** | Supported | **Not supported** |

### Custom Operations

| Operation | Firely | HealthLake |
|-----------|--------|------------|
| **$validate** | Full profile validation | Basic structural validation |
| **$everything** | Patient, Encounter | Patient only (limited params) |
| **$export** | Supported (Bulk Data Access IG) | Supported (S3 output) |
| **$import** | Via FSI (not standard $import) | Native support |
| **$member-match** | Plugin available | **Not supported** |
| **$submit** | Custom (CMS-specific) | Custom (CMS-specific) |
| **$convert** | Supported | **Not supported** |
| **$meta** | Supported | Limited |
| **Custom operations** | Fully extensible via plugins | Not extensible |

### Error Response Formats

**Firely OperationOutcome:**
```json
{
  "resourceType": "OperationOutcome",
  "issue": [{
    "severity": "error",
    "code": "processing",
    "details": {
      "coding": [{
        "system": "http://fire.ly/fhir/error-codes",
        "code": "VALIDATION_FAILED"
      }],
      "text": "Element 'Patient.birthDate': value '2024-13-45' is not a valid date"
    },
    "diagnostics": "Validation failed for profile http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient",
    "expression": ["Patient.birthDate"]
  }]
}
```

**HealthLake OperationOutcome:**
```json
{
  "resourceType": "OperationOutcome",
  "issue": [{
    "severity": "error",
    "code": "invalid",
    "diagnostics": "Invalid value for element birthDate: 2024-13-45"
  }]
}
```

**Key Differences:**
- Firely provides `expression` paths pinpointing the error location
- Firely includes structured `details.coding` for programmatic handling
- HealthLake errors are more terse; less context for debugging
- Firely supports multiple issues per OperationOutcome more consistently
- HealthLake may wrap AWS-level errors in OperationOutcome format

---

## 4. Performance Characteristics

### Query Latency Patterns

| Query Type | Firely (typical) | HealthLake (typical) | Notes |
|-----------|-------------------|---------------------|-------|
| **Read by ID** | 5–15ms | 20–50ms | HealthLake has higher base latency (network + service overhead) |
| **Simple search (indexed)** | 10–50ms | 50–200ms | Firely faster for warm queries on local infra |
| **Complex search (chained)** | 50–500ms | 200–2000ms | HealthLake degrades faster with complexity |
| **_include searches** | 20–100ms | 100–500ms | Both scale with included resource count |
| **_revinclude (large sets)** | 100–1000ms | 500–5000ms | HealthLake can timeout on very large reverse includes |
| **Count queries (_summary=count)** | 50–200ms | 200–1000ms | HealthLake estimates; Firely counts exactly |
| **$everything (Patient)** | 200–2000ms | 500–5000ms | Depends on patient data volume |
| **First query (cold)** | 50–200ms (JIT warmup) | 500–2000ms (cold start) | HealthLake cold starts are significant |

### Concurrent Request Handling

| Aspect | Firely | HealthLake |
|--------|--------|------------|
| **Max concurrent connections** | Limited by instance resources (typically 100–500/instance) | Service-level TPS limits |
| **Default TPS limit** | No hard limit (resource-bound) | 100 TPS (default), 500 TPS (increased) |
| **Throttling behavior** | 503 under resource exhaustion | 429 (ThrottlingException) with retry-after |
| **Connection pooling** | Application-level | Managed (SDK handles retries) |
| **Request timeout** | Configurable (default 30s) | 60s hard limit |
| **Retry strategy** | Client-side implementation | AWS SDK exponential backoff |
| **Bulk operation concurrency** | Can run multiple exports simultaneously | One active $import or $export per data store |

### Bulk Export ($export) Behavior

| Aspect | Firely | HealthLake |
|--------|--------|------------|
| **Output format** | NDJSON files (served via REST) | NDJSON files in S3 |
| **Trigger** | `GET [base]/$export` (async) | `StartFHIRExportJob` API |
| **Status polling** | Standard Bulk Data IG polling | AWS Job status API |
| **Parallelism** | Multiple exports can run concurrently | One export at a time per data store |
| **Filtering** | _type, _since, _typeFilter | _type, _since |
| **Output size limit** | Configurable file splitting | Auto-splits at ~500MB per file |
| **Completion time (1M resources)** | 5–30 minutes (depends on hardware) | 15–60 minutes |
| **Export authentication** | Same as server auth | S3 IAM permissions required |

### Optimization Approaches

| Strategy | Firely | HealthLake |
|----------|--------|------------|
| **Custom indexes** | Define custom search params → auto-index in MongoDB | Not available (fixed index strategy) |
| **Query optimization** | Analyze MongoDB explain plans | Limited visibility (CloudWatch metrics only) |
| **Caching** | Application-level caching, CDN for reads | No built-in caching; use API Gateway cache |
| **Connection management** | Tune MongoDB connection pool | Use AWS SDK connection reuse |
| **Batch reads** | Bundle GETs in batch | Batch bundle or parallel API calls |
| **Denormalization** | Not needed (flexible queries) | Consider flattening for search performance |

---

## 5. Validation Behavior

### Profile Validation

| Aspect | Firely | HealthLake |
|--------|--------|------------|
| **Validation engine** | .NET FHIR Validator (Firely SDK) | Internal AWS validator |
| **Profile support** | Full StructureDefinition support | Base profiles + US Core |
| **Custom profiles** | Upload StructureDefinitions; enforce on create/update | Upload StructureDefinitions; limited enforcement |
| **Validation modes** | Off, warnings-only, strict reject | On/off per data store |
| **Validation timing** | Configurable: on create, update, or on-demand via $validate | Always on create/update (if enabled) |
| **Error granularity** | Detailed element-level errors with FHIRPath expressions | Resource-level errors, less specific |
| **Slicing validation** | Full support | Partial (may miss slice violations) |
| **Extension validation** | Validates against extension definitions | Structural only (won't validate extension content deeply) |
| **Validation performance impact** | 10–30% slower writes when enabled | Negligible (built into pipeline) |

### Must-Support Enforcement

| Aspect | Firely | HealthLake |
|--------|--------|------------|
| **Must-support checking** | Configurable per profile | **No enforcement** — must-support is informational only |
| **Missing must-support elements** | Can reject or warn | Always accepts (validation passes) |
| **CMS interop impact** | Can enforce Da Vinci/US Core must-support | Must implement must-support checking externally |
| **Recommendation** | Enable for submission validation | Add pre-submission validation layer |

### Reference Integrity

| Aspect | Firely | HealthLake |
|--------|--------|------------|
| **Reference checking on write** | Configurable (enforce, warn, skip) | **No enforcement** — dangling references allowed |
| **Broken reference behavior** | Can reject resource with invalid references | Stores resource regardless |
| **Circular reference detection** | Supported | N/A (not checked) |
| **Reference resolution at read time** | Resolves if target exists; 404 if not | Returns reference as-is; client discovers 404 |
| **Impact on Onyx/Abacus** | Firely can guarantee integrity | Must validate references in application layer |

### Code System Validation

| Aspect | Firely | HealthLake |
|--------|--------|------------|
| **Terminology service** | Built-in or external $validate-code | Limited (validates known code systems) |
| **Custom ValueSets** | Full support (upload and enforce) | Upload supported; enforcement varies |
| **Required binding enforcement** | Rejects invalid codes | May allow invalid codes in some contexts |
| **CodeSystem supplements** | Supported | Not supported |
| **$lookup** | Supported | Not supported |
| **$expand** | Supported | Limited support |

---

## 6. Migration Patterns

### Firely → HealthLake Migration

```
Phase 1: Assessment
├── Catalog all custom search parameters (won't migrate)
├── Identify transaction bundle usage (must convert to batch)
├── Audit custom operations (need alternatives)
├── Measure data volume and resource type distribution
└── Document _include/:iterate usage (need simplification)

Phase 2: Data Migration
├── $export from Firely → NDJSON files
├── Transform IDs if needed (Firely sequential → HealthLake format)
├── Upload NDJSON to S3
├── Run HealthLake $import
├── Validate counts match (resource type by type)
└── Spot-check critical resources

Phase 3: Application Migration
├── Update client libraries (FHIR client → AWS SDK + FHIR)
├── Replace transaction bundles with batch + application-level rollback
├── Simplify _include queries (remove :iterate)
├── Replace custom search params with alternative query patterns
├── Update auth flow (SMART on FHIR → IAM SigV4)
└── Update error handling for HealthLake OperationOutcome format

Phase 4: Validation
├── Run integration test suite against HealthLake
├── Compare query results for sample patients
├── Verify submission workflows end-to-end
├── Performance benchmark critical paths
└── Verify bulk export works for downstream consumers
```

### Coexistence Pattern (Running Both)

```
┌──────────────────────────────────────────────────────────────────┐
│                     Onyx/Abacus Application                       │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │              FHIR Abstraction Layer                         │  │
│  │  ┌─────────────┐  ┌──────────────┐  ┌─────────────────┐   │  │
│  │  │  Router /   │  │  Query       │  │  Write           │   │  │
│  │  │  Selector   │  │  Translator  │  │  Coordinator     │   │  │
│  │  └─────────────┘  └──────────────┘  └─────────────────┘   │  │
│  └─────────────────────────┬──────────────────────────────────┘  │
│                            │                                     │
│              ┌─────────────┴─────────────┐                       │
│              ▼                           ▼                        │
│     ┌────────────────┐         ┌─────────────────┐              │
│     │  Firely Server │         │  HealthLake     │              │
│     │  (Source of    │         │  (Migration     │              │
│     │   Truth)       │         │   Target)       │              │
│     └────────────────┘         └─────────────────┘              │
└──────────────────────────────────────────────────────────────────┘
```

**Coexistence Constraints:**
- Writes go to Firely (source of truth) + async replication to HealthLake
- Reads can be routed by use case (Firely for complex queries, HealthLake for simple reads)
- ID mapping layer required if not using client-assigned IDs
- Event-driven sync (Firely interceptor → queue → HealthLake writer)
- Must handle eventual consistency between stores

### Data Sync Approaches

| Approach | Pros | Cons |
|----------|------|------|
| **Change event streaming** (Firely interceptor → Kafka → HealthLake) | Real-time, reliable | Complex infrastructure; requires Firely plugin |
| **Periodic $export → $import** | Simple, uses standard APIs | Lag between syncs; large data volumes |
| **Dual-write from application** | Simplest conceptually | Consistency risk; doubles write latency |
| **CDC from MongoDB** | Low-latency, reliable | Tied to Firely internals; breaks on upgrades |

### Feature Parity Gaps

| Feature | Available in Firely | Available in HealthLake | Workaround for HealthLake |
|---------|--------------------|-----------------------|--------------------------|
| Transaction bundles | ✅ | ❌ | Application-level saga pattern |
| Custom search params | ✅ | ❌ | Use _filter or restructure queries |
| _include:iterate | ✅ | ❌ | Multiple sequential queries |
| Full-text search | ✅ | ❌ | External search service (OpenSearch) |
| $member-match | ✅ (plugin) | ❌ | Custom Lambda implementation |
| Terminology $expand | ✅ | ⚠️ Limited | External terminology service |
| Resource-level history | ✅ | ✅ | — |
| System-level history | ✅ | ❌ | Aggregate from resource-level |
| Subscriptions (R4) | ✅ | ❌ | EventBridge + CloudWatch |
| Custom operations | ✅ | ❌ | API Gateway + Lambda |

---

## 7. Decision Matrix

### Quick Triage Guide

> **How to use this matrix:** Find the symptom/scenario in the left column. Check the three middle columns to identify the most likely source. Follow the diagnostic steps and resolution approach.

#### Legend
- 🔴 = High likelihood this is the source
- 🟡 = Possible source
- ⚪ = Unlikely source

---

### 7.1 Ingestion Failures

| # | Symptom/Error | Firely? | HealthLake? | Integration? | Diagnostic Steps | Resolution |
|---|--------------|---------|-------------|-------------|-----------------|------------|
| 1 | **Bundle rejected: "Transaction bundles not supported"** | ⚪ | 🔴 | 🟡 | Check bundle.type field; verify target system | Convert to batch bundle for HealthLake; implement app-level rollback |
| 2 | **Bundle fails: "Too many entries" (>160)** | ⚪ | 🔴 | 🟡 | Count entries; check which target received it | Split into multiple batch bundles of ≤160 for HealthLake; Firely can handle larger |
| 3 | **FSI bulk load fails mid-import** | 🔴 | ⚪ | ⚪ | Check FSI logs; verify MongoDB connectivity and disk space | Resume FSI from last checkpoint; check MongoDB replica set health |
| 4 | **$import job stuck in "IN_PROGRESS"** | ⚪ | 🔴 | ⚪ | Check job status via DescribeFHIRImportJob; check S3 permissions | Verify IAM role; check NDJSON format validity; contact AWS support if >24h |
| 5 | **Duplicate resources after re-import** | ⚪ | 🔴 | 🟡 | Check if resources have client-assigned IDs; check $import behavior | Always use PUT with client-assigned IDs for idempotent imports |
| 6 | **NDJSON parse errors in $import** | ⚪ | 🔴 | 🟡 | Check $import error manifest in S3 output; validate NDJSON format | Ensure one resource per line, valid JSON, no trailing commas |
| 7 | **Conditional create returns 412 (Precondition Failed)** | 🔴 | 🟡 | 🟡 | Check If-None-Exist header format; verify search criteria | Firely: check search param indexing; HealthLake: verify supported params in condition |
| 8 | **PUT with client ID returns 400** | 🟡 | 🟡 | 🔴 | Check ID format; verify resource type in URL matches body | Ensure ID format valid for target (Firely: alphanumeric; HealthLake: specific format rules) |
| 9 | **Timeout during large bundle submission** | 🟡 | 🟡 | 🔴 | Check bundle size; check network timeout settings | Reduce bundle size; increase client timeout; use async patterns for HealthLake |
| 10 | **Resources missing after successful bulk load** | 🟡 | 🟡 | 🔴 | Verify load counts; check for validation rejects in logs | Check error outputs (FSI log or $import manifest); resources may have been rejected silently |

### 7.2 Validation Errors

| # | Symptom/Error | Firely? | HealthLake? | Integration? | Diagnostic Steps | Resolution |
|---|--------------|---------|-------------|-------------|-----------------|------------|
| 11 | **Profile validation passes in one system but fails in other** | 🟡 | 🟡 | 🔴 | Run $validate on both systems; compare OperationOutcomes | Align validation profiles; Firely is stricter — test against Firely first |
| 12 | **"Unknown extension" error** | 🔴 | ⚪ | ⚪ | Check if extension StructureDefinition is loaded in Firely | Upload extension definition to Firely; HealthLake is more lenient on unknown extensions |
| 13 | **Reference validation failure** | 🔴 | ⚪ | 🟡 | Check if referenced resource exists; check Firely referenceValidation setting | Firely enforces reference integrity; HealthLake does not. Load referenced resources first |
| 14 | **Invalid code in required binding** | 🔴 | 🟡 | 🟡 | Check ValueSet binding strength; validate code against ValueSet | Firely rejects invalid required bindings; HealthLake may accept. Fix source data |
| 15 | **Slicing validation error** | 🔴 | ⚪ | 🟡 | Check discriminator paths; verify slice definitions loaded | Firely validates slicing strictly; HealthLake may not validate slices at all |

### 7.3 Search & Query Issues

| # | Symptom/Error | Firely? | HealthLake? | Integration? | Diagnostic Steps | Resolution |
|---|--------------|---------|-------------|-------------|-----------------|------------|
| 16 | **Search returns 0 results but resource exists** | 🟡 | 🟡 | 🔴 | Try read by ID; verify search parameter name/value; check indexing status | Firely: reindex; HealthLake: check if param is supported; Integration: check param encoding |
| 17 | **Chained search returns 400/error** | ⚪ | 🔴 | 🟡 | Test chain depth; check if intermediate params supported | Simplify chain for HealthLake (max 1-2 levels); break into multiple queries |
| 18 | **_include:iterate not returning nested resources** | ⚪ | 🔴 | 🟡 | Check if using :iterate; test with simple _include | HealthLake doesn't support :iterate — implement client-side iterative fetching |
| 19 | **Pagination returns duplicate/missing resources** | ⚪ | 🔴 | 🟡 | Check if data changed during pagination; verify token handling | HealthLake is eventually consistent — implement dedup logic; use shorter page windows |
| 20 | **_total=accurate returns wrong count** | 🟡 | 🔴 | ⚪ | Compare with manual count; check HealthLake behavior | HealthLake _total is estimated for large sets; Firely is accurate but slow |
| 21 | **Custom search parameter not found** | 🔴 | 🔴 | 🟡 | Verify param definition loaded (Firely); verify param supported (HealthLake) | Firely: POST SearchParameter + reindex; HealthLake: use only built-in params |
| 22 | **Date search returns unexpected results** | 🟡 | 🟡 | 🔴 | Check date precision in query; check timezone handling | Normalize to full ISO 8601; check UTC vs local time interpretation differences |

### 7.4 Performance Issues

| # | Symptom/Error | Firely? | HealthLake? | Integration? | Diagnostic Steps | Resolution |
|---|--------------|---------|-------------|-------------|-----------------|------------|
| 23 | **Sudden latency increase (10x normal)** | 🔴 | 🟡 | 🟡 | Firely: check MongoDB, CPU, memory; HealthLake: check CloudWatch; Both: check network | Firely: scale instances or optimize indexes; HealthLake: check for service issues |
| 24 | **429 Too Many Requests** | ⚪ | 🔴 | 🟡 | Check request rate; review HealthLake TPS limits | Implement exponential backoff; request limit increase from AWS |
| 25 | **$export takes hours for moderate dataset** | 🟡 | 🔴 | ⚪ | Check data store size; check if concurrent export running | HealthLake: only one export at a time; Firely: check disk I/O and tune thread count |
| 26 | **Query timeout (30s/60s exceeded)** | 🟡 | 🟡 | 🔴 | Simplify query; check _include depth; test sub-queries | Break into smaller queries; remove heavy _includes; add targeted search params |
| 27 | **Memory exhaustion during bulk operations** | 🔴 | ⚪ | 🟡 | Check Firely instance heap; check batch sizes in client | Increase Firely memory allocation; reduce batch size; use streaming patterns |

### 7.5 Authentication & Access

| # | Symptom/Error | Firely? | HealthLake? | Integration? | Diagnostic Steps | Resolution |
|---|--------------|---------|-------------|-------------|-----------------|------------|
| 28 | **401 Unauthorized** | 🟡 | 🟡 | 🔴 | Check token expiry; verify correct auth mechanism for target | Firely: refresh OAuth token; HealthLake: check IAM credentials/STS session |
| 29 | **403 Forbidden on specific resource type** | 🟡 | 🟡 | 🔴 | Check SMART scopes (Firely) or IAM policy (HealthLake) | Firely: verify scope includes resource type; HealthLake: check IAM Action permissions |
| 30 | **SignatureDoesNotMatch (HealthLake)** | ⚪ | 🔴 | 🟡 | Check clock sync; verify SigV4 signing logic; check region | Ensure system clock is synced; verify AWS region in endpoint URL matches credentials |
| 31 | **Token refresh fails mid-operation** | 🟡 | ⚪ | 🔴 | Check token TTL vs operation duration; check refresh mechanism | Implement proactive token refresh; extend token TTL for long-running operations |

### 7.6 Data Consistency

| # | Symptom/Error | Firely? | HealthLake? | Integration? | Diagnostic Steps | Resolution |
|---|--------------|---------|-------------|-------------|-----------------|------------|
| 32 | **Resource shows stale data after update** | ⚪ | 🔴 | 🟡 | Read immediately after write; check for caching layers | HealthLake has eventual consistency window (~1-2s); add read-after-write delay or use vread |
| 33 | **Version conflict (409) on update** | 🟡 | 🟡 | 🔴 | Check If-Match header; verify version ID format | Implement retry with fresh read → update cycle; check for concurrent writers |
| 34 | **Reference points to non-existent resource** | 🟡 | 🔴 | 🟡 | Check reference integrity; verify load order | HealthLake allows dangling refs; implement reference verification in pipeline |
| 35 | **Batch partially succeeded but no clear error** | ⚪ | 🔴 | 🟡 | Check individual entry responses in batch-response Bundle | Parse each entry in batch response; HealthLake batch entries are independent |

### 7.7 Integration-Specific Issues

| # | Symptom/Error | Firely? | HealthLake? | Integration? | Diagnostic Steps | Resolution |
|---|--------------|---------|-------------|-------------|-----------------|------------|
| 36 | **Same query returns different results from each store** | ⚪ | ⚪ | 🔴 | Compare data in each store; check sync lag; verify query translation | Check sync pipeline; verify query parameter mapping between stores |
| 37 | **ID mismatch between stores** | ⚪ | ⚪ | 🔴 | Check ID assignment strategy; verify sync maps IDs correctly | Use client-assigned IDs consistently; maintain ID mapping table if needed |
| 38 | **CMS submission fails after successful store** | ⚪ | ⚪ | 🔴 | Check CMS-specific validation; verify all required resources present | Run CMS pre-submission validation; check for CMS-specific extensions/profiles |
| 39 | **Webhook/notification not triggered after resource update** | 🟡 | 🔴 | 🟡 | Check subscription/notification config; check event delivery | Firely: check Subscription resources; HealthLake: use CloudTrail/EventBridge |
| 40 | **Bulk pipeline succeeds but downstream reports missing data** | ⚪ | ⚪ | 🔴 | Verify export completeness; check ETL transform; validate downstream queries | Check export _type filters; verify NDJSON parsing downstream; check for transform bugs |

---

## 8. Operational Differences

### Monitoring & Alerting

| Aspect | Firely | HealthLake |
|--------|--------|------------|
| **Health check** | `/health` endpoint (configurable) | DescribeFHIRDatastore API |
| **Metrics** | Custom metrics (Prometheus/StatsD exportable) | CloudWatch Metrics (built-in) |
| **Key metrics to monitor** | Request count, latency p50/p95, error rate, MongoDB ops, memory | SuccessfulRequests, ThrottledRequests, Latency, ActiveImports/Exports |
| **Log aggregation** | Application logs (stdout/file) → ELK/Splunk | CloudWatch Logs (automatic) |
| **Audit trail** | Configurable audit logging | CloudTrail (all API calls) |
| **Alerting** | Custom (Grafana/PagerDuty integration) | CloudWatch Alarms → SNS |
| **Distributed tracing** | OpenTelemetry support | X-Ray (limited) |

**Recommended Alerts for Each:**

| Alert | Firely Threshold | HealthLake Threshold |
|-------|------------------|---------------------|
| Error rate | > 1% of requests | > 1% of requests |
| Latency p95 | > 500ms | > 2000ms |
| Throttling | N/A | > 10 throttled requests/min |
| Memory usage | > 80% of allocated | N/A (managed) |
| MongoDB replication lag | > 5 seconds | N/A |
| $export duration | > 2x expected | > 2x expected |
| Import failures | Any failure | Error manifest non-empty |
| Disk usage | > 75% | N/A (managed) |

### Backup & Restore

| Aspect | Firely | HealthLake |
|--------|--------|------------|
| **Backup mechanism** | MongoDB dump/snapshot + config backup | Automatic (continuous backups, 7-day retention) |
| **Point-in-time recovery** | MongoDB oplog-based (if configured) | Not supported (backup is periodic) |
| **Cross-region DR** | Manual: replicate MongoDB + deploy Firely in DR region | Cross-region $export → $import |
| **RTO** | Depends on infrastructure (minutes to hours) | Create new data store + $import (hours) |
| **RPO** | Depends on backup frequency (minutes) | ~24 hours (daily backup) |
| **Restore process** | MongoDB restore → start Firely | Create new data store → $import from backup |
| **Testing restores** | Restore to separate MongoDB → connect Firely | Create test data store → import |

### Version Upgrades

| Aspect | Firely | HealthLake |
|--------|--------|------------|
| **Upgrade responsibility** | Self-managed (download + deploy new version) | AWS-managed (transparent) |
| **Upgrade frequency** | Monthly releases (self-paced adoption) | Continuous (no user action needed) |
| **Breaking changes** | Possible; review release notes | Rare; backwards-compatible by design |
| **Rollback** | Deploy previous version (if data schema compatible) | Not user-controlled |
| **Testing upgrades** | Deploy new version to staging with data copy | No staging available (use separate data store) |
| **FHIR version upgrade** | R4→R5 requires data migration planning | N/A (R4 only currently) |
| **Downtime for upgrade** | Rolling deployment possible (blue/green) | Zero downtime (managed) |

### Configuration Management

| Aspect | Firely | HealthLake |
|--------|--------|------------|
| **Configuration location** | appsettings.json / environment variables | Data store settings (API / Console) |
| **IaC support** | Docker Compose, Helm, Terraform (custom) | CloudFormation, Terraform (AWS provider) |
| **Configuration drift** | Risk: manual changes across instances | Low: single managed config |
| **Secret management** | External (Vault, K8s secrets, env vars) | AWS Secrets Manager / Parameter Store |
| **Feature flags** | Configuration file + restart | Not applicable (fixed feature set) |
| **Per-environment config** | Full control (dev/staging/prod) | Separate data stores per environment |

---

## 9. Known Limitations & Workarounds

### Firely Known Issues

| Issue | Impact | Workaround | Severity |
|-------|--------|-----------|----------|
| **MongoDB connection pool exhaustion under high concurrency** | Requests queue or fail with timeouts | Increase `maxPoolSize`; add connection monitoring; consider read preference secondaryPreferred | High |
| **FSI memory spike on large files** | OOM kill during bulk ingest of very large bundles | Split input files; increase memory allocation; use streaming mode | Medium |
| **Custom SearchParameter reindex blocks reads** | Performance degradation during reindex | Schedule reindex during maintenance windows; use rolling reindex | Medium |
| **Transaction bundle timeout with many inter-references** | Bundle fails for complex dependency graphs | Pre-sort entries by dependency order; split into smaller transactions | Medium |
| **Subscription notification delivery not guaranteed** | Missed updates for downstream consumers | Implement reconciliation polling alongside subscriptions | Medium |
| **Profile validation memory usage scales with profile complexity** | Slow validation for deeply nested profiles | Simplify profiles where possible; validate in batches | Low |
| **.NET garbage collection pauses** | Occasional latency spikes (50–200ms) | Use Server GC mode; tune GC settings for low-latency workloads | Low |
| **CORS configuration requires restart** | Can't dynamically update allowed origins | Plan CORS changes with deployment; use wildcard for dev | Low |

### HealthLake Known Issues

| Issue | Impact | Workaround | Severity |
|-------|--------|-----------|----------|
| **No transaction bundle support** | Cannot guarantee atomic multi-resource operations | Implement application-level saga pattern with compensating actions | Critical |
| **160 entry batch bundle limit** | Must split large submissions | Chunk into multiple batches; implement orchestration | High |
| **Eventual consistency (1-2s window)** | Read-after-write may return stale data | Add delay before read; use vread with known version; implement retry | High |
| **Single concurrent $import/$export** | Blocks pipeline if multiple jobs needed | Queue jobs; implement job scheduler; split by resource type | High |
| **No custom search parameters** | Cannot optimize queries for domain-specific patterns | Restructure queries; use only built-in params; denormalize data | High |
| **No _include:iterate** | Cannot fetch deep reference graphs in one query | Implement iterative client-side fetching; cache intermediate results | Medium |
| **Limited $validate** | Cannot do deep profile validation server-side | Run validation externally before submission (use Firely SDK or HL7 validator) | Medium |
| **Cold start latency (500ms–2s)** | First request after idle period is slow | Implement warm-up pings; account for cold starts in SLAs | Medium |
| **No Subscriptions (FHIR R4)** | Cannot get push notifications on resource changes | Poll with _lastUpdated; use CloudTrail events; implement change detection | Medium |
| **_total count is estimated for large result sets** | Cannot get exact counts for pagination UI | Use _summary=count with small date ranges; implement client-side counting | Low |
| **No full-text search** | Cannot search narrative or free-text fields | Export to OpenSearch for text queries; use structured search params | Low |

### Integration-Layer Workarounds

| Challenge | Pattern | Implementation Notes |
|-----------|---------|---------------------|
| **Transaction semantics on HealthLake** | Saga pattern: execute steps sequentially, compensate on failure | Track each step; implement `undo` for each resource create/update; use DLQ for failed compensations |
| **Query portability between stores** | Query abstraction layer | Map high-level queries to store-specific implementations; hide _include:iterate vs multi-query |
| **Consistent IDs across stores** | Client-assigned UUIDs | Generate UUIDs in application layer; use PUT everywhere; never rely on server-assigned IDs |
| **Validation consistency** | Pre-validation service | Validate against profiles using external validator before sending to either store |
| **Real-time sync** | Event-driven architecture | Firely interceptor → EventBridge/Kafka → HealthLake writer; handle conflicts with last-write-wins or merge |
| **Bulk operation coordination** | Job orchestrator | Queue bulk operations; handle one-at-a-time constraint for HealthLake; parallel for Firely |
| **Error normalization** | Error abstraction layer | Parse OperationOutcomes from both systems; normalize into unified error model for Onyx/Abacus |
| **Auth token management** | Token service | Manage OAuth tokens (Firely) and STS sessions (HealthLake) centrally; proactive refresh |
| **Performance SLA management** | Circuit breaker + fallback | Implement circuit breaker per store; fall back to other store for reads if one degrades |
| **Data reconciliation** | Periodic comparison job | Export from both, compare resource counts and checksums by type; alert on drift |

---

## Appendix A: Diagnostic Decision Tree

```
START: Issue reported in Onyx/Abacus FHIR integration
│
├── Is the error from a specific FHIR server response?
│   ├── YES → Check HTTP status code
│   │   ├── 400 Bad Request
│   │   │   ├── Check OperationOutcome for details
│   │   │   ├── Firely: detailed expression paths → likely validation issue
│   │   │   └── HealthLake: terse message → likely structural/format issue
│   │   │
│   │   ├── 401/403 Auth error
│   │   │   ├── Firely → Check OAuth token / SMART scope
│   │   │   ├── HealthLake → Check IAM role / SigV4 / STS token
│   │   │   └── Both? → Integration auth layer issue
│   │   │
│   │   ├── 404 Not Found
│   │   │   ├── After recent write? → HealthLake eventual consistency
│   │   │   ├── Reference to another resource? → Check load order
│   │   │   └── Search returning empty? → Check search param support
│   │   │
│   │   ├── 409 Conflict
│   │   │   └── Version conflict → Implement optimistic locking retry
│   │   │
│   │   ├── 422 Unprocessable
│   │   │   ├── Firely → Profile validation failure
│   │   │   └── HealthLake → Structural issue or unsupported feature
│   │   │
│   │   ├── 429 Too Many Requests
│   │   │   └── HealthLake TPS limit → Implement backoff / request increase
│   │   │
│   │   └── 500/503 Server Error
│   │       ├── Firely → Check server logs, MongoDB, resources
│   │       └── HealthLake → Check AWS service health; retry
│   │
│   └── NO → Check application logs
│       ├── Timeout? → Check query complexity / bundle size
│       ├── Connection refused? → Check network / endpoint config
│       └── Parse error? → Check response format expectations
│
└── Is the issue data-related (wrong/missing data)?
    ├── Data missing after load → Check load logs / error manifests
    ├── Data inconsistent between stores → Check sync pipeline
    ├── Data doesn't match source → Check transform logic
    └── Downstream reports wrong data → Check export filters / query logic
```

---

## Appendix B: Quick Reference Card

### When to Suspect Firely

- Detailed validation errors with FHIRPath expressions
- MongoDB-related timeouts or connection issues
- Issues only occurring when custom search params are used
- Memory or resource exhaustion patterns
- Issues after a Firely version upgrade
- Subscription/notification delivery problems

### When to Suspect HealthLake

- "Transaction not supported" errors
- Throttling (429) responses
- Eventual consistency symptoms (stale reads after write)
- Batch size limit errors (>160 entries)
- Missing search parameters or operations
- Cold start latency spikes
- S3 permission issues during $import/$export

### When to Suspect Integration Layer

- Same operation works on one store but not the other
- ID format mismatches
- Auth token issues affecting both stores differently
- Data drift between stores
- CMS submission failures despite successful storage
- Query returning different results from each store
- Timeout only from the application (not direct API call)

---

## Appendix C: Environment-Specific Configurations

### Firely Configuration Essentials (appsettings.json)

```json
{
  "FhirServer": {
    "FHIR": {
      "Version": "R4"
    },
    "Repository": {
      "Type": "MongoDB",
      "MongoDb": {
        "ConnectionString": "mongodb://...",
        "DatabaseName": "firely_r4",
        "MaxConnectionPoolSize": 200
      }
    },
    "Validation": {
      "Level": "Full",
      "ReferenceValidation": "Enforce"
    },
    "Search": {
      "MaxPageSize": 200,
      "DefaultPageSize": 20
    },
    "BulkDataExport": {
      "MaxConcurrentJobs": 3,
      "OutputFormat": "ndjson"
    }
  }
}
```

### HealthLake Configuration (Terraform)

```hcl
resource "aws_healthlake_fhir_datastore" "main" {
  datastore_name         = "onyx-abacus-r4"
  datastore_type_version = "R4"
  
  preload_data_config {
    preload_data_type = "SYNTHEA"  # or "NONE" for production
  }
  
  sse_configuration {
    kms_encryption_config {
      cmk_type   = "CUSTOMER_MANAGED_KMS_KEY"
      kms_key_id = aws_kms_key.healthlake.arn
    }
  }

  tags = {
    Environment = "production"
    Team        = "onyx-abacus"
  }
}
```

### Integration Layer Health Check Script

```python
# health_check.py - Quick validation for both stores
import requests
import boto3
from datetime import datetime

def check_firely(base_url, token):
    """Check Firely Server health."""
    resp = requests.get(
        f"{base_url}/metadata",
        headers={"Authorization": f"Bearer {token}"},
        timeout=10
    )
    return {
        "status": "healthy" if resp.status_code == 200 else "unhealthy",
        "latency_ms": resp.elapsed.total_seconds() * 1000,
        "fhir_version": resp.json().get("fhirVersion", "unknown")
    }

def check_healthlake(datastore_id, region):
    """Check HealthLake data store health."""
    client = boto3.client('healthlake', region_name=region)
    resp = client.describe_fhir_datastore(DatastoreId=datastore_id)
    store = resp['DatastoreProperties']
    return {
        "status": store['DatastoreStatus'],
        "endpoint": store['DatastoreEndpoint'],
        "created": store['CreatedAt'].isoformat()
    }

def check_sync_health(firely_url, firely_token, hl_datastore_id, region):
    """Compare resource counts between stores."""
    # Check a sample resource type count
    firely_resp = requests.get(
        f"{firely_url}/Patient?_summary=count",
        headers={"Authorization": f"Bearer {firely_token}"}
    )
    firely_count = firely_resp.json().get("total", 0)
    
    # HealthLake equivalent
    client = boto3.client('healthlake', region_name=region)
    # ... (implementation depends on access pattern)
    
    return {
        "firely_patient_count": firely_count,
        "drift_detected": False,  # Compare counts
        "checked_at": datetime.utcnow().isoformat()
    }
```

---

## Appendix D: Onyx/Abacus-Specific Patterns

### CMS Interoperability Submission Flow

```
┌──────────────┐     ┌──────────────┐     ┌───────────────┐
│  Onyx/Abacus │     │  Validation  │     │  FHIR Store   │
│  Application │────▶│  Service     │────▶│  (Firely or   │
│              │     │              │     │   HealthLake) │
└──────────────┘     └──────────────┘     └───────┬───────┘
                                                  │
                                          ┌───────▼───────┐
                                          │  CMS $submit  │
                                          │  Operation    │
                                          └───────┬───────┘
                                                  │
                                          ┌───────▼───────┐
                                          │  CMS Response │
                                          │  Processing   │
                                          └───────────────┘
```

### Key Decision Points for Onyx/Abacus Engineers

1. **For CMS submissions requiring atomic operations** → Use Firely (transaction support)
2. **For high-volume read queries at scale** → Consider HealthLake (auto-scaling)
3. **For complex search patterns** → Prefer Firely (custom search params, full-text)
4. **For AWS-native deployments** → HealthLake reduces operational overhead
5. **For strict validation requirements** → Use Firely as validation layer, even if storing in HealthLake
6. **For cost optimization at scale** → HealthLake for storage, Firely for complex operations

---

*End of Support Matrix — maintained by Onyx/Abacus Platform Engineering*
