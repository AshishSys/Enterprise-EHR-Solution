# Databricks Workflow Troubleshooting Handbook
## Onyx Interoperability Platform — Artifact #5

**Version:** 1.0  
**Last Updated:** 2026-07-07  
**Audience:** Data Engineers, Platform Engineers, SREs supporting CMS interoperability pipelines  
**Platform:** Databricks (Unity Catalog enabled), Azure/AWS deployment

---

## Table of Contents

1. [Workflow Structure & Naming Conventions](#1-workflow-structure--naming-conventions)
2. [Pipeline Steps by Workflow Family](#2-pipeline-steps-by-workflow-family)
3. [Runtime Infrastructure](#3-runtime-infrastructure)
4. [Troubleshooting Guide by Workflow Family](#4-troubleshooting-guide-by-workflow-family)
5. [Known Failure Modes](#5-known-failure-modes-detailed)
6. [Diagnostic Procedures](#6-diagnostic-procedures)
7. [Recovery Procedures](#7-recovery-procedures)

---

## 1. Workflow Structure & Naming Conventions

### 1.1 Workflow Naming Patterns

All Onyx workflows follow a strict naming convention to enable programmatic discovery, monitoring, and alerting:

```
onyx-{family}-{operation}-{mode}-{environment}
```

| Component | Values | Description |
|-----------|--------|-------------|
| `family` | `claims`, `clinical`, `formulary`, `pvd`, `cms0057`, `cms9115` | Workflow family / CMS rule |
| `operation` | `transform`, `upload`, `upsert`, `preprocess`, `extract`, `terminate` | Pipeline step |
| `mode` | `incremental`, `historical`, `bulk`, `retry` | Processing mode |
| `environment` | `dev`, `stg`, `prod` | Target environment |

**Examples:**

```
onyx-claims-transform-incremental-prod
onyx-clinical-upsert-historical-stg
onyx-formulary-extract-bulk-prod
onyx-pvd-preprocess-incremental-dev
onyx-cms0057-upload-incremental-prod
onyx-cms9115-transform-historical-prod
```

**Multi-task workflow naming (parent orchestrator):**

```
onyx-{family}-pipeline-{mode}-{environment}
```

Example: `onyx-claims-pipeline-incremental-prod` orchestrates all steps for claims incremental processing.

### 1.2 Extract Config Files Structure & Location

Extract configuration files define what data to pull from source systems, transformation mappings, and output schemas.

**Directory Structure:**

```
/Workspace/onyx/configs/
├── claims/
│   ├── extract_config.yaml
│   ├── field_mappings.yaml
│   ├── validation_rules.yaml
│   └── fhir_profiles/
│       ├── claim.profile.json
│       └── eob.profile.json
├── clinical/
│   ├── extract_config.yaml
│   ├── field_mappings.yaml
│   ├── validation_rules.yaml
│   └── fhir_profiles/
│       ├── encounter.profile.json
│       ├── condition.profile.json
│       └── procedure.profile.json
├── formulary/
│   ├── extract_config.yaml
│   ├── field_mappings.yaml
│   └── fhir_profiles/
│       └── medication_knowledge.profile.json
├── pvd/
│   ├── extract_config.yaml
│   ├── field_mappings.yaml
│   └── fhir_profiles/
│       ├── practitioner.profile.json
│       └── organization.profile.json
├── cms0057/
│   ├── extract_config.yaml
│   ├── payer_to_payer_mappings.yaml
│   └── fhir_profiles/
│       └── coverage.profile.json
└── cms9115/
    ├── extract_config.yaml
    ├── prior_auth_mappings.yaml
    └── fhir_profiles/
        └── claim_response.profile.json
```

**Extract Config YAML Structure:**

```yaml
# extract_config.yaml
version: "2.1"
family: claims
source:
  catalog: onyx_source
  schema: claims_raw
  tables:
    - name: medical_claims
      filter: "service_date >= '{watermark_date}'"
      partition_column: service_date
    - name: pharmacy_claims
      filter: "fill_date >= '{watermark_date}'"
      partition_column: fill_date

watermark:
  strategy: high_watermark  # or: full_refresh, cdc_timestamp
  column: last_modified_ts
  state_table: onyx_control.job_state.claims_watermark

output:
  catalog: onyx_staging
  schema: claims_sam
  format: delta
  mode: merge  # or: overwrite, append

quality:
  null_threshold: 0.05
  duplicate_strategy: latest_wins
  required_fields:
    - member_id
    - claim_id
    - service_date
```

### 1.3 Job State Table Design & Usage

The job state table is the central coordination mechanism for Onyx workflows.

**Table:** `onyx_control.pipeline_state.job_runs`

```sql
CREATE TABLE onyx_control.pipeline_state.job_runs (
  run_id              STRING        NOT NULL,
  workflow_name       STRING        NOT NULL,
  family              STRING        NOT NULL,
  operation           STRING        NOT NULL,
  mode                STRING        NOT NULL,
  environment         STRING        NOT NULL,
  status              STRING        NOT NULL,  -- PENDING, RUNNING, SUCCESS, FAILED, CANCELLED, RETRYING
  started_at          TIMESTAMP     NOT NULL,
  completed_at        TIMESTAMP,
  watermark_value     STRING,
  records_processed   BIGINT        DEFAULT 0,
  records_failed      BIGINT        DEFAULT 0,
  error_message       STRING,
  error_category      STRING,
  retry_count         INT           DEFAULT 0,
  max_retries         INT           DEFAULT 3,
  parent_run_id       STRING,       -- for multi-task workflows
  config_hash         STRING,       -- SHA256 of config at runtime
  wheel_version       STRING,
  image_tag           STRING,
  cluster_id          STRING,
  databricks_run_id   BIGINT,
  created_at          TIMESTAMP     DEFAULT current_timestamp(),
  updated_at          TIMESTAMP     DEFAULT current_timestamp()
)
USING DELTA
PARTITIONED BY (family, environment)
TBLPROPERTIES (
  'delta.enableChangeDataFeed' = 'true',
  'delta.autoOptimize.optimizeWrite' = 'true'
);
```

**Watermark Table:** `onyx_control.pipeline_state.watermarks`

```sql
CREATE TABLE onyx_control.pipeline_state.watermarks (
  family              STRING        NOT NULL,
  source_table        STRING        NOT NULL,
  environment         STRING        NOT NULL,
  last_successful_watermark   STRING,
  current_watermark           STRING,
  watermark_type      STRING,       -- timestamp, id, composite
  updated_at          TIMESTAMP     DEFAULT current_timestamp(),
  updated_by          STRING
)
USING DELTA;
```

**State Transitions:**

```
PENDING → RUNNING → SUCCESS
                  → FAILED → RETRYING → RUNNING → ...
                  → CANCELLED
```

### 1.4 Task Sequencing & Dependencies

**Standard Pipeline Task Graph:**

```
preprocess → transform → upload → upsert → terminate
     ↓            ↓          ↓        ↓         ↓
  validate     FM→SAM    SAM→CSV   CSV→FHIR   cleanup
```

**Dependency Configuration (Databricks JSON):**

```json
{
  "tasks": [
    {
      "task_key": "preprocess",
      "depends_on": [],
      "timeout_seconds": 3600
    },
    {
      "task_key": "transform",
      "depends_on": [{"task_key": "preprocess"}],
      "timeout_seconds": 7200
    },
    {
      "task_key": "upload",
      "depends_on": [{"task_key": "transform"}],
      "timeout_seconds": 5400
    },
    {
      "task_key": "upsert",
      "depends_on": [{"task_key": "upload"}],
      "timeout_seconds": 10800
    },
    {
      "task_key": "terminate",
      "depends_on": [{"task_key": "upsert"}],
      "run_if": "ALL_DONE",
      "timeout_seconds": 1800
    }
  ]
}
```

> **Important:** The `terminate` task uses `run_if: ALL_DONE` (not `ALL_SUCCESS`) to ensure cleanup runs even on failure.

---

## 2. Pipeline Steps by Workflow Family

### 2.1 Transform Step: FM → SAM

The Transform step converts data from the **Foundational Model (FM)** — normalized source data — into the **Standard Analytical Model (SAM)** — the Onyx-canonical representation optimized for FHIR mapping.

**Key Operations:**

| Operation | Description |
|-----------|-------------|
| Schema alignment | Map FM columns to SAM target schema |
| Code translation | Translate proprietary codes to standard terminologies (ICD-10, CPT, NDC, SNOMED) |
| Reference resolution | Resolve foreign keys to FHIR resource references |
| Temporal alignment | Normalize date/time formats, apply timezone rules |
| Aggregation | Roll up line-level data to claim/encounter level where needed |
| Enrichment | Add computed fields (age at service, LOS, etc.) |

**Family-Specific Transform Logic:**

| Family | FM Source | SAM Target | Key Transformations |
|--------|-----------|------------|---------------------|
| Claims | `claims_fm.medical_claims`, `claims_fm.pharmacy_claims` | `claims_sam.eob_records` | Adjudication mapping, DRG grouping, member ID crosswalk |
| Clinical | `clinical_fm.encounters`, `clinical_fm.diagnoses`, `clinical_fm.procedures` | `clinical_sam.clinical_events` | Encounter assembly, diagnosis ranking, procedure linkage |
| Formulary | `formulary_fm.drug_list`, `formulary_fm.tier_config` | `formulary_sam.formulary_items` | Tier assignment, PA requirements, quantity limits |
| PVD | `pvd_fm.providers`, `pvd_fm.organizations`, `pvd_fm.locations` | `pvd_sam.provider_directory` | NPI validation, taxonomy mapping, network status |
| CMS-0057 | `cms0057_fm.coverage`, `cms0057_fm.p2p_claims` | `cms0057_sam.payer_exchange` | Coverage period alignment, P2P consent tracking |
| CMS-9115 | `cms9115_fm.prior_auth`, `cms9115_fm.auth_decisions` | `cms9115_sam.prior_auth_records` | Decision tree mapping, timeline construction |

**Transform Code Pattern:**

```python
# Standard transform entry point
from onyx.transforms import BaseTransformer
from onyx.config import load_extract_config

class ClaimsTransformer(BaseTransformer):
    def __init__(self, config_path: str, run_id: str):
        super().__init__(config_path, run_id)
        self.family = "claims"
    
    def execute(self, spark):
        # Read FM source with watermark filter
        fm_df = self.read_source(spark)
        
        # Apply transformations
        sam_df = (
            fm_df
            .transform(self.apply_code_translations)
            .transform(self.resolve_references)
            .transform(self.apply_business_rules)
            .transform(self.validate_output_schema)
        )
        
        # Write to SAM with merge
        self.write_sam(sam_df)
        
        # Update state
        self.update_state(records_processed=sam_df.count())
```

### 2.2 Upload Step: SAM → CSV Export

The Upload step exports SAM data to CSV format for downstream FHIR bundle creation.

**Process:**

1. Read SAM Delta table (filtered by run watermark)
2. Apply final output transformations (string formatting, null handling)
3. Write partitioned CSV files to staging location
4. Generate manifest file listing all output files
5. Validate row counts match SAM source

**Output Location:**

```
abfss://onyx-staging@{storage_account}.dfs.core.windows.net/
  {family}/{environment}/csv_export/
    run_id={run_id}/
      part-00000.csv
      part-00001.csv
      ...
      _manifest.json
```

**Manifest Structure:**

```json
{
  "run_id": "run-20260707-001",
  "family": "claims",
  "timestamp": "2026-07-07T14:30:00Z",
  "total_records": 145230,
  "file_count": 12,
  "files": [
    {"name": "part-00000.csv", "records": 12500, "size_bytes": 4521003, "checksum": "sha256:abc123..."},
    ...
  ]
}
```

### 2.3 Upsert Step: FHIR Bundle Creation & Load

The Upsert step converts CSV records into FHIR R4 resources and loads them into the target FHIR store.

**Process Flow:**

```
CSV Records → FHIR Resource Mapper → Bundle Assembly → Validation → FHIR Store POST
```

**Bundle Configuration:**

| Family | FHIR Resources | Bundle Type | Max Bundle Size |
|--------|---------------|-------------|-----------------|
| Claims | ExplanationOfBenefit, Claim, Coverage | transaction | 50 resources |
| Clinical | Encounter, Condition, Procedure, Observation | transaction | 100 resources |
| Formulary | MedicationKnowledge, InsurancePlan | transaction | 200 resources |
| PVD | Practitioner, PractitionerRole, Organization, Location | transaction | 150 resources |
| CMS-0057 | Coverage, ExplanationOfBenefit | transaction | 50 resources |
| CMS-9115 | ClaimResponse, Claim | transaction | 75 resources |

**Upsert Strategy:**

```python
# FHIR conditional upsert logic
def upsert_bundle(bundle, fhir_client):
    for entry in bundle.entry:
        entry.request = {
            "method": "PUT",
            "url": f"{entry.resource.resourceType}?identifier={entry.resource.identifier[0].value}"
        }
    
    response = fhir_client.post_bundle(bundle)
    return parse_bundle_response(response)
```

### 2.4 Preprocessing: Data Validation & Dedup

**Validation Checks:**

| Check | Action on Failure | Threshold |
|-------|-------------------|-----------|
| Null required fields | Quarantine record | 0% tolerance |
| Schema type mismatch | Quarantine record | 0% tolerance |
| Referential integrity | Quarantine record | 5% tolerance |
| Business rule violation | Flag for review | 10% tolerance |
| Duplicate detection | Apply dedup strategy | N/A |
| Date range validity | Quarantine record | 0% tolerance |
| Code set membership | Flag + default code | 2% tolerance |

**Deduplication Strategy:**

```python
from onyx.preprocessing import DedupStrategy

# Configuration per family
DEDUP_CONFIGS = {
    "claims": DedupStrategy(
        keys=["claim_id", "line_number", "member_id"],
        tiebreaker="last_modified_ts",
        strategy="latest_wins"
    ),
    "clinical": DedupStrategy(
        keys=["encounter_id", "member_id", "service_date"],
        tiebreaker="source_load_ts",
        strategy="latest_wins"
    ),
    "pvd": DedupStrategy(
        keys=["npi", "effective_date"],
        tiebreaker="updated_at",
        strategy="latest_wins"
    )
}
```

### 2.5 Extraction: Extract Task Configuration

**SAM → CSV Extract Task:**

```yaml
# extract_task_config.yaml
extract:
  source:
    catalog: onyx_staging
    schema: claims_sam
    table: eob_records
    
  filter:
    watermark_column: processed_at
    state_lookup: true
    additional_filters:
      - "status = 'VALIDATED'"
      - "dq_score >= 0.95"
  
  output:
    format: csv
    delimiter: ","
    quote_char: '"'
    null_representation: ""
    header: true
    encoding: utf-8
    max_file_size_mb: 256
    compression: none  # FHIR loader expects uncompressed
    
  partitioning:
    strategy: round_robin  # or: hash, range
    target_partitions: 12
    
  columns:
    include: all  # or explicit list
    exclude:
      - _internal_id
      - _load_timestamp
      - _source_file
```

### 2.6 Termination: Cleanup, State Updates, Notifications

The Terminate step runs regardless of upstream success/failure (`run_if: ALL_DONE`).

**Terminate Operations:**

```python
class PipelineTerminator:
    def execute(self, context):
        run_id = context.run_id
        
        # 1. Determine final status
        final_status = self.compute_final_status(context)
        
        # 2. Update job state table
        self.update_job_state(run_id, final_status)
        
        # 3. Update watermark (only on success)
        if final_status == "SUCCESS":
            self.advance_watermark(context)
        
        # 4. Archive staging files
        self.archive_csv_exports(run_id)
        
        # 5. Clean up temp tables
        self.drop_temp_tables(run_id)
        
        # 6. Emit metrics
        self.emit_metrics(context, final_status)
        
        # 7. Send notifications
        if final_status == "FAILED":
            self.send_failure_alert(context)
        elif final_status == "SUCCESS":
            self.send_success_notification(context)
        
        # 8. Release cluster resources
        self.cleanup_cluster_state()
```

---

## 3. Runtime Infrastructure

### 3.1 Runtime Image Management

Onyx workflows use custom Docker images with pre-installed dependencies.

**Image Registry:**

```
{ecr_registry}/onyx/runtime:{tag}
```

**Image Tags Convention:**

```
onyx/runtime:v2.4.1-claims        # Family-specific image
onyx/runtime:v2.4.1-base          # Shared base image
onyx/runtime:v2.4.1-base-gpu      # GPU-enabled (for ML validation)
onyx/runtime:latest-dev           # Dev latest (mutable)
onyx/runtime:v2.4.1-prod          # Prod pinned (immutable)
```

**Dockerfile Structure:**

```dockerfile
FROM databricksruntime/standard:14.3-LTS

# System dependencies
RUN apt-get update && apt-get install -y \
    libxml2-dev \
    libxslt1-dev \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Onyx wheel packages
COPY dist/onyx_core-*.whl /tmp/
COPY dist/onyx_fhir-*.whl /tmp/
COPY dist/onyx_transforms-*.whl /tmp/
RUN pip install /tmp/onyx_*.whl

# Config files
COPY configs/ /opt/onyx/configs/
```

**Image Verification:**

```bash
# Check running image in Databricks cluster
%sh
cat /databricks/image_info.json | python -m json.tool

# Expected output
{
  "image_name": "onyx/runtime",
  "image_tag": "v2.4.1-claims",
  "build_date": "2026-07-01T10:00:00Z",
  "git_sha": "abc123def456",
  "onyx_core_version": "2.4.1",
  "onyx_fhir_version": "2.4.1"
}
```

### 3.2 Wheel Files (.whl) — Python Package Management

**Package Hierarchy:**

| Package | Purpose | Dependencies |
|---------|---------|-------------|
| `onyx-core` | Base utilities, config loading, state management | pydantic, pyyaml |
| `onyx-transforms` | FM→SAM transformation logic | onyx-core, pyspark |
| `onyx-fhir` | FHIR resource generation, validation, API client | onyx-core, fhir.resources |
| `onyx-extract` | CSV extraction and manifest generation | onyx-core, pyspark |
| `onyx-quality` | DQ rules, validation, quarantine | onyx-core, great-expectations |
| `onyx-monitoring` | Metrics, alerting, notifications | onyx-core, boto3 |

**Wheel Storage:**

```
dbfs:/onyx/wheels/{environment}/
├── onyx_core-2.4.1-py3-none-any.whl
├── onyx_transforms-2.4.1-py3-none-any.whl
├── onyx_fhir-2.4.1-py3-none-any.whl
├── onyx_extract-2.4.1-py3-none-any.whl
├── onyx_quality-2.4.1-py3-none-any.whl
└── onyx_monitoring-2.4.1-py3-none-any.whl
```

**Version Pinning in Workflows:**

```json
{
  "libraries": [
    {"whl": "dbfs:/onyx/wheels/prod/onyx_core-2.4.1-py3-none-any.whl"},
    {"whl": "dbfs:/onyx/wheels/prod/onyx_transforms-2.4.1-py3-none-any.whl"},
    {"whl": "dbfs:/onyx/wheels/prod/onyx_fhir-2.4.1-py3-none-any.whl"}
  ]
}
```

**Version Verification at Runtime:**

```python
import onyx.core
import onyx.transforms
import onyx.fhir

print(f"Core: {onyx.core.__version__}")
print(f"Transforms: {onyx.transforms.__version__}")
print(f"FHIR: {onyx.fhir.__version__}")

# Validate version alignment
assert onyx.core.__version__ == onyx.transforms.__version__ == onyx.fhir.__version__, \
    "CRITICAL: Wheel version mismatch detected!"
```

### 3.3 Config INI Files

**Structure:**

```ini
; onyx_config.ini
[DEFAULT]
environment = prod
region = us-east-1
log_level = INFO

[database]
catalog = onyx_prod
fm_schema = foundational_model
sam_schema = standard_analytical_model
control_schema = pipeline_state
control_catalog = onyx_control

[fhir]
base_url = https://fhir.onyx-prod.internal/R4
auth_method = oauth2_client_credentials
token_url = https://auth.onyx-prod.internal/oauth/token
client_id_secret = onyx/prod/fhir-client-id
client_secret_secret = onyx/prod/fhir-client-secret
timeout_seconds = 30
max_retries = 3
bundle_size = 50
concurrent_requests = 10

[storage]
staging_container = onyx-staging
archive_container = onyx-archive
storage_account = onyxprodsa
csv_export_path = csv_export
archive_retention_days = 90

[monitoring]
metrics_namespace = Onyx/Pipelines
alert_sns_topic = arn:aws:sns:us-east-1:123456789:onyx-pipeline-alerts
success_notification = true
failure_notification = true
sla_threshold_minutes = 120

[cluster]
node_type = Standard_DS4_v2
min_workers = 2
max_workers = 16
autoscale = true
spark_conf = spark.sql.adaptive.enabled=true,spark.sql.shuffle.partitions=200
```

**Environment-Specific Overrides:**

| Setting | Dev | Staging | Prod |
|---------|-----|---------|------|
| `fhir.base_url` | `https://fhir.onyx-dev.internal/R4` | `https://fhir.onyx-stg.internal/R4` | `https://fhir.onyx-prod.internal/R4` |
| `fhir.concurrent_requests` | 2 | 5 | 10 |
| `fhir.bundle_size` | 10 | 25 | 50 |
| `cluster.max_workers` | 4 | 8 | 16 |
| `monitoring.alert_sns_topic` | dev-alerts | stg-alerts | prod-alerts |
| `storage.archive_retention_days` | 7 | 30 | 90 |

### 3.4 Terraform Workflow Definitions

**Module Structure:**

```
terraform/
├── modules/
│   └── onyx_workflow/
│       ├── main.tf
│       ├── variables.tf
│       ├── outputs.tf
│       └── templates/
│           ├── claims_pipeline.json.tpl
│           ├── clinical_pipeline.json.tpl
│           └── ...
├── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── terraform.tfvars
│   │   └── backend.tf
│   ├── staging/
│   │   └── ...
│   └── prod/
│       └── ...
└── shared/
    ├── iam.tf
    ├── networking.tf
    └── secrets.tf
```

**Workflow Terraform Definition:**

```hcl
# modules/onyx_workflow/main.tf

resource "databricks_job" "onyx_pipeline" {
  name = "onyx-${var.family}-pipeline-${var.mode}-${var.environment}"
  
  schedule {
    quartz_cron_expression = var.schedule_cron
    timezone_id            = "America/New_York"
    pause_status           = var.schedule_enabled ? "UNPAUSED" : "PAUSED"
  }

  job_cluster {
    job_cluster_key = "main_cluster"
    new_cluster {
      spark_version = var.spark_version
      node_type_id  = var.node_type
      autoscale {
        min_workers = var.min_workers
        max_workers = var.max_workers
      }
      docker_image {
        url = "${var.ecr_registry}/onyx/runtime:${var.image_tag}"
        basic_auth {
          username = var.ecr_username
          password = var.ecr_password
        }
      }
      spark_conf = var.spark_conf
      custom_tags = {
        Family      = var.family
        Environment = var.environment
        Team        = "onyx-platform"
        CostCenter  = "interoperability"
      }
    }
  }

  task {
    task_key = "preprocess"
    job_cluster_key = "main_cluster"
    python_wheel_task {
      package_name = "onyx_quality"
      entry_point  = "preprocess"
      parameters   = ["--config", var.config_path, "--run-id", "{{job.run_id}}"]
    }
    library {
      whl = "dbfs:/onyx/wheels/${var.environment}/onyx_quality-${var.wheel_version}-py3-none-any.whl"
    }
  }

  task {
    task_key = "transform"
    depends_on {
      task_key = "preprocess"
    }
    job_cluster_key = "main_cluster"
    python_wheel_task {
      package_name = "onyx_transforms"
      entry_point  = "transform"
      parameters   = ["--config", var.config_path, "--run-id", "{{job.run_id}}"]
    }
    library {
      whl = "dbfs:/onyx/wheels/${var.environment}/onyx_transforms-${var.wheel_version}-py3-none-any.whl"
    }
  }

  # ... additional tasks ...

  notification_settings {
    no_alert_for_skipped_runs = true
  }

  email_notifications {
    on_failure = var.alert_emails
  }

  tags = {
    Family      = var.family
    ManagedBy   = "terraform"
    Repository  = "onyx-platform/workflows"
  }
}
```

**Variables File (prod):**

```hcl
# environments/prod/terraform.tfvars

environment    = "prod"
image_tag      = "v2.4.1-prod"
wheel_version  = "2.4.1"
spark_version  = "14.3.x-scala2.12"
node_type      = "Standard_DS4_v2"
min_workers    = 2
max_workers    = 16
ecr_registry   = "123456789.dkr.ecr.us-east-1.amazonaws.com"

families = {
  claims = {
    schedule_cron    = "0 0 2 * * ?"  # 2 AM daily
    schedule_enabled = true
    mode             = "incremental"
    config_path      = "/Workspace/onyx/configs/claims/extract_config.yaml"
  }
  clinical = {
    schedule_cron    = "0 0 3 * * ?"  # 3 AM daily
    schedule_enabled = true
    mode             = "incremental"
    config_path      = "/Workspace/onyx/configs/clinical/extract_config.yaml"
  }
  formulary = {
    schedule_cron    = "0 0 4 * * ?"  # 4 AM daily
    schedule_enabled = true
    mode             = "incremental"
    config_path      = "/Workspace/onyx/configs/formulary/extract_config.yaml"
  }
}
```

### 3.5 Environment Promotion (Dev → Staging → Prod)

**Promotion Pipeline:**

```
┌─────────┐    ┌─────────────┐    ┌──────────┐    ┌──────────┐
│  Build   │───▶│  Dev Deploy │───▶│ Stg Deploy│───▶│Prod Deploy│
│ & Test   │    │  + Smoke    │    │ + Integ   │    │ + Canary  │
└─────────┘    └─────────────┘    └──────────┘    └──────────┘
```

**Promotion Checklist:**

| Step | Gate | Automated? |
|------|------|------------|
| Unit tests pass | 100% pass | ✅ |
| Integration tests pass | 95%+ pass | ✅ |
| Wheel builds successfully | No errors | ✅ |
| Image builds and scans | No critical CVEs | ✅ |
| Dev smoke test | Pipeline completes | ✅ |
| Staging integration test | End-to-end success | ✅ |
| FHIR validation pass | 100% profile compliance | ✅ |
| Config diff review | No unexpected changes | ❌ (manual) |
| Terraform plan review | Approved by 2 engineers | ❌ (manual) |
| Prod canary (10% traffic) | Error rate < 0.1% | ✅ |
| Full prod rollout | Monitoring green 30min | ✅ |

---

## 4. Troubleshooting Guide by Workflow Family

### 4.1 Claims Workflow

**Common Failure Scenarios:**

1. Adjudication code mapping failures (new codes not in translation table)
2. Member ID crosswalk misses (member not in eligibility system)
3. DRG grouper timeout on large historical batches
4. EOB bundle size exceeding FHIR store limits
5. Duplicate claim submissions from source system reloads

**Symptom → Root Cause → Fix Table:**

| # | Symptom | Root Cause | Fix |
|---|---------|------------|-----|
| 1 | Transform fails with `KeyError: 'ADJ_CODE_XYZ'` | New adjudication code not in translation table | Add code to `configs/claims/field_mappings.yaml` → `adjudication_codes` section. Redeploy config. |
| 2 | High quarantine rate (>5%) on member_id null | Source system data quality issue — claims loaded before eligibility | Check source load timing. Coordinate with upstream to ensure eligibility loads before claims. Temporarily increase null_threshold if expected. |
| 3 | Transform OOM error on historical run | Full historical load exceeds cluster memory | Increase `max_workers` to 32 for historical. Add `spark.sql.adaptive.coalescePartitions.enabled=true`. Partition by service_date ranges. |
| 4 | Upsert returns HTTP 413 (Payload Too Large) | Bundle size exceeds FHIR store limit | Reduce `fhir.bundle_size` in config from 50 to 25. EOB resources are large. |
| 5 | Duplicate EOBs in FHIR store | Claim reprocessed by source without new ID | Run dedup query on FHIR store: `GET /ExplanationOfBenefit?identifier={id}&_count=0`. Implement `If-Match` header with version. |
| 6 | Upload step produces 0 CSV files | SAM table empty — watermark advanced past available data | Check watermark table. Reset watermark: `UPDATE watermarks SET last_successful_watermark = '{correct_date}' WHERE family = 'claims'` |
| 7 | Transform slow (>4 hours) | Code translation join causing shuffle spill | Broadcast the translation table: `spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "100m")`. Or pre-filter codes. |
| 8 | FHIR validation error: "invalid reference" | Referenced Practitioner/Organization not yet loaded | Ensure PVD pipeline completes before Claims. Add cross-family dependency check in preprocess. |
| 9 | State table shows RUNNING but job finished hours ago | Terminate task failed before updating state | Manually update: `UPDATE job_runs SET status='FAILED', error_message='Orphaned run - manual cleanup' WHERE run_id='{id}'` |
| 10 | Pharmacy claims missing NDC codes | Source pharmacy_claims table has null NDC for mail-order | Add fallback lookup to GPI→NDC mapping in transform. Add DQ rule to flag >2% null NDC. |

**Log Locations:**

```
# Databricks driver logs
/databricks/driver/logs/onyx-claims-transform-{run_id}.log

# Spark executor logs (for OOM/shuffle issues)
Cluster → Spark UI → Executors → stderr

# Application-level logs
spark.sparkContext.setLogLevel("DEBUG")
# Then check: Cluster → Driver Logs → Log4j output
```

**Diagnostic Commands:**

```sql
-- Check recent claims runs
SELECT * FROM onyx_control.pipeline_state.job_runs
WHERE family = 'claims' 
ORDER BY started_at DESC LIMIT 10;

-- Check watermark status
SELECT * FROM onyx_control.pipeline_state.watermarks
WHERE family = 'claims';

-- Count records in SAM waiting for extract
SELECT COUNT(*) as pending_records
FROM onyx_staging.claims_sam.eob_records
WHERE processed_at > (
    SELECT last_successful_watermark 
    FROM onyx_control.pipeline_state.watermarks 
    WHERE family = 'claims' AND source_table = 'eob_records'
);

-- Check quarantine volume
SELECT error_category, COUNT(*) as cnt
FROM onyx_staging.claims_sam.quarantine
WHERE run_id = '{run_id}'
GROUP BY error_category;
```

### 4.2 Clinical Workflow

**Common Failure Scenarios:**

1. Encounter assembly fails — missing admit/discharge events
2. ICD-10 code validation failures (invalid or retired codes)
3. Condition-Encounter linkage ambiguity
4. Large procedure volumes causing timeout
5. SNOMED translation gaps

**Symptom → Root Cause → Fix Table:**

| # | Symptom | Root Cause | Fix |
|---|---------|------------|-----|
| 1 | `EncounterAssemblyError: No discharge event for encounter {id}` | Open encounters in source — no discharge recorded | Add filter: `WHERE discharge_date IS NOT NULL` or create "open encounter" handling logic. Configure `allow_open_encounters: true` in config. |
| 2 | Transform produces 0 records despite source having data | Date filter too restrictive — watermark ahead of source refresh | Reset watermark to last known good date. Check source system refresh schedule. |
| 3 | FHIR validation: `Condition.code must be from ValueSet condition-code` | ICD-10 code not in FHIR value set (e.g., retired code) | Update code translation to map retired codes to current equivalents. Add to `retired_code_mappings.yaml`. |
| 4 | Upsert timeout after 3 hours | Large encounter bundles with many linked resources (20+ per encounter) | Reduce encounter bundle complexity. Split into Encounter-only + Condition-only + Procedure-only passes. |
| 5 | `DuplicateKeyError` in SAM table merge | Multiple source records for same encounter_id from different feeds | Add source_system to dedup key: `keys=["encounter_id", "member_id", "source_system"]` |
| 6 | Clinical transform missing procedure codes | CPT→SNOMED mapping table not updated | Refresh mapping table from NLM distribution. Run: `python -m onyx.maintenance.refresh_mappings --type cpt_snomed` |
| 7 | Memory pressure on executor nodes | Clinical encounters have variable-length arrays (diagnoses, procedures) causing skew | Enable AQE: `spark.sql.adaptive.skewJoin.enabled=true`. Increase executor memory to 16g. |
| 8 | FHIR store rejects Observation resources | `meta.profile` URL incorrect for US Core profile | Update FHIR profile URL in `clinical/fhir_profiles/observation.profile.json` to `http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab` |
| 9 | Partial encounter data (conditions without encounters) | Cross-table join timing — encounters not yet loaded when conditions arrive | Implement two-phase load: Phase 1 = Encounters, Phase 2 = linked resources. Add dependency check. |
| 10 | Date parsing errors in transform | Mixed date formats in source (`MM/DD/YYYY` vs `YYYY-MM-DD`) | Add date normalization to preprocess: `to_date(coalesce(try_to_date(col, 'yyyy-MM-dd'), try_to_date(col, 'MM/dd/yyyy')))` |

### 4.3 Formulary Workflow

**Common Failure Scenarios:**

1. Tier configuration changes mid-cycle
2. Drug list updates conflicting with active period
3. Formulary effective date mismatches
4. NDC-to-RxNorm mapping gaps
5. Quantity limit formatting issues

**Symptom → Root Cause → Fix Table:**

| # | Symptom | Root Cause | Fix |
|---|---------|------------|-----|
| 1 | `FormularyTierConflict: Drug {ndc} assigned to multiple tiers` | Source system has overlapping tier effective dates | Add conflict resolution rule: latest effective date wins. Alert pharmacy team for manual review. |
| 2 | Transform produces duplicate formulary items | Historical reload included records already in SAM | Ensure dedup runs with `keys=["ndc", "plan_id", "effective_date"]`. Force dedup in preprocess. |
| 3 | FHIR MedicationKnowledge validation failure | Missing required `code.coding.system` — NDC system URI incorrect | Set system to `http://hl7.org/fhir/sid/ndc`. Check field_mappings.yaml `drug_code_system` field. |
| 4 | Zero formulary items after transform | Filter excludes all records — effective_date in future | Adjust filter: `effective_date <= current_date() + interval 30 days` to include upcoming formulary. |
| 5 | `RxNormMappingError: No RxNorm for NDC {code}` | New NDC not in RxNorm crosswalk (recently approved drug) | Add manual mapping to `formulary/overrides/ndc_rxnorm_manual.csv`. File ticket for NLM update. |
| 6 | InsurancePlan resource rejected by FHIR store | Plan ID format doesn't match expected identifier pattern | Ensure plan_id is formatted as `{payer_id}-{plan_type}-{year}`. Update mapping logic. |
| 7 | Prior Authorization requirements not mapping | PA flag column renamed in source | Update extract_config.yaml `source.tables[].columns` mapping. Add column alias. |
| 8 | Formulary CSV export has encoding issues | Special characters in drug names (®, ™) | Set `output.encoding: utf-8-sig` in extract config. Add character sanitization in upload step. |
| 9 | Step quantity limits showing as 0 | Integer overflow on large quantity values stored as SMALLINT | Cast to INT in transform: `CAST(quantity_limit AS INT)`. Update SAM schema. |
| 10 | FHIR bundle rejected: "duplicate resource" | Same drug appears with different plan years in single bundle | Add plan_year to bundle partitioning key. One bundle per plan/year combination. |

### 4.4 PVD (Provider/Vendor Directory) Workflow

**Common Failure Scenarios:**

1. NPI validation failures (invalid check digit)
2. Provider taxonomy code mapping issues
3. Network status conflicts (in-network vs out-of-network)
4. Location/address geocoding failures
5. Large provider organizations with many practitioners

**Symptom → Root Cause → Fix Table:**

| # | Symptom | Root Cause | Fix |
|---|---------|------------|-----|
| 1 | `NPIValidationError: Invalid NPI check digit for {npi}` | Source has transposed digits or test NPIs | Add NPI Luhn validation in preprocess. Quarantine invalid NPIs. Cross-reference NPPES. |
| 2 | Transform produces empty PractitionerRole resources | Taxonomy code not mapping to NUCC provider type | Update taxonomy mapping table. Download latest NUCC CSV from CMS. Run refresh job. |
| 3 | FHIR Organization resources rejected | Missing required `type` coding | Add default organization type based on taxonomy. Map to `http://terminology.hl7.org/CodeSystem/organization-type`. |
| 4 | Duplicate Practitioner records (same NPI, different records) | Provider has multiple practice locations creating duplicate entries | Use NPI as primary dedup key for Practitioner. Create separate PractitionerRole per location. |
| 5 | Location.address validation failure | State abbreviation not matching USPS codes | Normalize state to 2-letter USPS code in preprocess. Add lookup table for common misspellings. |
| 6 | Transform timeout on large health system | Single organization with 10,000+ practitioners | Partition by organization_id. Process large orgs in dedicated sub-task with increased resources. |
| 7 | Network participation dates missing | Credentialing system doesn't export participation effective dates | Default to contract start date. Flag for manual review. Add DQ metric. |
| 8 | Upsert creates orphan PractitionerRoles | Referenced Organization not yet created in FHIR store | Implement ordered upsert: Organization → Practitioner → PractitionerRole → Location. |
| 9 | Provider specialty code "OTHER" flooding | Unmapped specialty codes defaulting to OTHER | Review unmapped codes in quarantine. Add top-10 unmapped to mapping table monthly. |
| 10 | Phone/fax number format validation errors | Source has inconsistent phone formats (with/without dashes, country code) | Normalize all phone numbers to E.164 format in preprocess. Use `phonenumbers` library. |

### 4.5 CMS-0057 (Payer-to-Payer) Workflow

**Common Failure Scenarios:**

1. Coverage period overlap with existing records
2. Consent tracking/revocation timing issues
3. Cross-payer identifier resolution failures
4. Prior payer data format incompatibilities
5. Large P2P bulk transfers overwhelming resources

**Symptom → Root Cause → Fix Table:**

| # | Symptom | Root Cause | Fix |
|---|---------|------------|-----|
| 1 | `CoverageOverlapError: Member {id} has overlapping coverage periods` | Prior payer didn't close coverage before new payer opened | Implement coverage gap/overlap resolution: truncate prior coverage end date to day before new coverage start. |
| 2 | Transform fails: `ConsentNotFound for member {id}` | P2P consent not yet recorded in consent management system | Add retry logic with 24-hour lookback. Queue record for reprocessing. Check consent ingestion pipeline. |
| 3 | `IdentifierResolutionError: Cannot resolve cross-payer member ID` | Member ID crosswalk between payers is incomplete | Queue for manual matching. Use probabilistic matching fallback (name + DOB + SSN-last4). Alert identity team. |
| 4 | Inbound P2P data fails schema validation | Prior payer sending data in FHIR STU3 format instead of R4 | Activate STU3→R4 converter in preprocess. Log payer for standards compliance outreach. |
| 5 | Upsert creates duplicate Coverage resources | Same coverage reported by both old and new payer | Add cross-payer dedup: `identifier=[member_id + payer_id + coverage_period]`. Merge metadata from both sources. |
| 6 | Bulk P2P transfer causes OOM | Single payer sending 500K+ member records in one batch | Enable streaming mode for P2P: `mode: streaming_micro_batch`. Process in 10K-record chunks. |
| 7 | EOB resources from prior payer missing required fields | Prior payer's data doesn't include all US Core required elements | Add data enrichment step to fill required fields with data-absent-reason extensions. |
| 8 | `TokenExpiredError` during long P2P transfer | OAuth token expires during multi-hour bulk transfer | Implement token refresh middleware. Set `token_refresh_buffer_seconds: 300` in FHIR config. |
| 9 | Coverage.subscriber reference invalid | Subscriber Patient resource not yet created from P2P data | Two-phase P2P load: Phase 1 = Patient resources, Phase 2 = Coverage + EOB. |
| 10 | Transform hangs on consent verification | Consent service is rate-limiting P2P requests | Implement backoff: exponential retry with jitter. Batch consent lookups: 100 per request. Cache verified consents. |

### 4.6 CMS-9115 (Prior Authorization) Workflow

**Common Failure Scenarios:**

1. Prior auth decision tree mapping complexity
2. Timeline construction across multiple auth events
3. ClaimResponse resource validation issues
4. Appeal/denial chain linkage
5. Auth expiration handling

**Symptom → Root Cause → Fix Table:**

| # | Symptom | Root Cause | Fix |
|---|---------|------------|-----|
| 1 | `DecisionMappingError: Unknown auth status '{status}'` | Source system has custom auth statuses not in mapping table | Add custom status to `prior_auth_mappings.yaml`. Map to standard: APPROVED, DENIED, PENDING, PARTIAL. |
| 2 | Timeline gaps in auth history | Events from different source tables with unsynchronized loads | Join all auth event sources (submission, review, decision, appeal) before timeline construction. Add temporal sort. |
| 3 | ClaimResponse FHIR validation: `outcome required` | Pending auths don't have outcome — field left null | Map pending auths to `outcome: "queued"`. Use FHIR ClaimResponse.outcome value set correctly. |
| 4 | `CircularReferenceError: Auth {id} references itself` | Appeal references original auth which references appeal | Implement DAG validation in preprocess. Break circular refs: appeals reference only the immediate prior decision. |
| 5 | Auth expiration not reflected in FHIR | Expired auths not being updated — only new auths processed | Add expiration sweep job: query auths where `expiration_date < current_date()` and update status to EXPIRED. |
| 6 | Duplicate ClaimResponse resources | Same auth decision reported in multiple events | Dedup on `auth_id + decision_date + outcome`. Keep latest event per decision point. |
| 7 | Transform fails on null service codes | Prior auth submitted without specific service codes (blanket auth) | Allow null service code for blanket auths. Map to ServiceRequest without code (use category only). |
| 8 | Upsert partial failure: 50% of bundle entries rejected | Mixed valid/invalid resources in same bundle | Enable individual resource error handling. Successful resources commit, failed ones go to retry queue. |
| 9 | Auth→Claim linkage missing | ClaimResponse doesn't reference original Claim | Add claim_id resolution in transform. Query claims SAM table for matching service/member/date. |
| 10 | `TimeoutError` on large auth history backfill | Historical load with 2M+ auth records | Partition by decision_date ranges (monthly). Process as parallel sub-tasks. Increase cluster to 32 workers. |

---

## 5. Known Failure Modes (Detailed)

### 5.1 Config Mismatch (Between INI, Terraform, and Runtime)

**Description:** Configuration drift between what Terraform deploys, what the INI file specifies, and what the runtime actually uses.

**Common Scenarios:**

| Scenario | Detection | Impact | Resolution |
|----------|-----------|--------|------------|
| INI updated but Terraform not applied | Config hash mismatch in state table | Pipeline uses old cluster settings | Run `terraform apply` for affected environment |
| Terraform applied but image not rebuilt | Image tag matches but contents differ | Old code running in new config context | Rebuild and push image, update tag |
| Environment variable override shadowing INI | Unexpected behavior, correct config in file | Silent incorrect behavior | Audit env vars on cluster: `%sh env | grep ONYX` |
| Secrets rotated but config still references old secret path | Auth failures at runtime | Pipeline fails at FHIR upsert | Update secret ARN/path in INI + redeploy |

**Detection Script:**

```python
import hashlib
import yaml
import json

def verify_config_alignment(environment):
    """Compare config across all sources for drift detection."""
    
    # 1. Read INI config
    ini_config = parse_ini(f"/Workspace/onyx/configs/{environment}/onyx_config.ini")
    
    # 2. Read Terraform state
    tf_state = read_terraform_output(environment)
    
    # 3. Read runtime config (from last successful run)
    runtime_config = spark.sql(f"""
        SELECT config_hash, wheel_version, image_tag
        FROM onyx_control.pipeline_state.job_runs
        WHERE environment = '{environment}' AND status = 'SUCCESS'
        ORDER BY completed_at DESC LIMIT 1
    """).first()
    
    # 4. Compare
    ini_hash = hashlib.sha256(json.dumps(ini_config, sort_keys=True).encode()).hexdigest()
    
    mismatches = []
    if ini_hash != runtime_config.config_hash:
        mismatches.append("INI config changed since last successful run")
    if tf_state['image_tag'] != runtime_config.image_tag:
        mismatches.append(f"Terraform image_tag ({tf_state['image_tag']}) != runtime ({runtime_config.image_tag})")
    if tf_state['wheel_version'] != runtime_config.wheel_version:
        mismatches.append(f"Terraform wheel ({tf_state['wheel_version']}) != runtime ({runtime_config.wheel_version})")
    
    return mismatches
```

### 5.2 Validation Errors (Schema, FHIR Profile, DQ Rules)

**Error Categories:**

| Category | Error Pattern | Severity | Auto-Recovery |
|----------|--------------|----------|---------------|
| Schema violation | `AnalysisException: Column 'X' not found` | CRITICAL | No — schema change requires code update |
| FHIR profile violation | `ValidationError: Resource does not conform to profile` | HIGH | No — mapping correction needed |
| DQ rule breach | `DataQualityThresholdExceeded: null_rate 0.12 > threshold 0.05` | MEDIUM | Configurable — can adjust threshold |
| Type mismatch | `CastError: Cannot cast 'ABC' to IntegerType` | HIGH | No — source data issue |
| Value set violation | `InvalidCodeError: Code 'XYZ' not in ValueSet` | MEDIUM | Yes — add to mapping table |

**FHIR Validation Error Handling:**

```python
from onyx.fhir.validation import FHIRValidator

validator = FHIRValidator(profile_path="/opt/onyx/configs/fhir_profiles/")

def validate_and_quarantine(resources, family):
    valid = []
    quarantined = []
    
    for resource in resources:
        result = validator.validate(resource)
        if result.is_valid:
            valid.append(resource)
        else:
            quarantined.append({
                "resource": resource,
                "errors": result.errors,
                "severity": max(e.severity for e in result.errors),
                "timestamp": datetime.utcnow()
            })
    
    # Write quarantined to review table
    if quarantined:
        spark.createDataFrame(quarantined).write.mode("append").saveAsTable(
            f"onyx_staging.{family}_sam.quarantine"
        )
    
    return valid
```

### 5.3 Duplicate Records

**Causes:**

| Cause | Detection Method | Resolution |
|-------|-----------------|------------|
| Source system reload (full refresh over incremental) | Record count spike + same IDs reappearing | Apply dedup with latest_wins strategy |
| Pipeline re-run without state reset | Multiple run_ids for same watermark period | Deduplicate SAM table, advance watermark |
| Cross-source duplicates (same record from two feeds) | Different source_system but same business key | Add source_priority ranking |
| FHIR store eventual consistency | GET after PUT returns old + new version | Use `If-None-Exist` header on conditional create |
| Retry logic creating duplicates | Same bundle submitted multiple times | Use idempotency key in bundle request |

**Dedup Detection Query:**

```sql
-- Detect duplicates in Claims SAM
WITH duplicates AS (
  SELECT 
    claim_id, 
    member_id, 
    service_date,
    COUNT(*) as dup_count,
    COLLECT_SET(run_id) as run_ids,
    COLLECT_SET(source_system) as sources
  FROM onyx_staging.claims_sam.eob_records
  GROUP BY claim_id, member_id, service_date
  HAVING COUNT(*) > 1
)
SELECT * FROM duplicates ORDER BY dup_count DESC;

-- Detect duplicates in FHIR store (via search)
-- GET /ExplanationOfBenefit?identifier=claim-12345&_summary=count
```

**Dedup Resolution:**

```python
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, col

def deduplicate_sam(df, family):
    """Apply family-specific deduplication."""
    config = DEDUP_CONFIGS[family]
    
    window = Window.partitionBy(*config.keys).orderBy(col(config.tiebreaker).desc())
    
    deduped = (
        df
        .withColumn("_row_num", row_number().over(window))
        .filter(col("_row_num") == 1)
        .drop("_row_num")
    )
    
    dup_count = df.count() - deduped.count()
    if dup_count > 0:
        logger.warning(f"Removed {dup_count} duplicate records for {family}")
    
    return deduped
```

### 5.4 Runtime/Package Drift

**Wheel Version Mismatch:**

```
Symptom: ImportError or AttributeError at runtime
Root cause: Cluster has cached old wheel, or Terraform points to wrong version
Detection:
```

```python
# Run on cluster to detect version issues
import pkg_resources

expected_version = "2.4.1"
packages = ["onyx-core", "onyx-transforms", "onyx-fhir", "onyx-extract", "onyx-quality"]

for pkg in packages:
    try:
        installed = pkg_resources.get_distribution(pkg).version
        status = "✅" if installed == expected_version else f"❌ MISMATCH (got {installed})"
        print(f"{pkg}: {installed} {status}")
    except pkg_resources.DistributionNotFound:
        print(f"{pkg}: ❌ NOT INSTALLED")
```

**Image Staleness Detection:**

```bash
# Check image build date vs current
IMAGE_INFO=$(cat /databricks/image_info.json 2>/dev/null || echo '{}')
BUILD_DATE=$(echo $IMAGE_INFO | python3 -c "import sys,json; print(json.load(sys.stdin).get('build_date','UNKNOWN'))")
echo "Image build date: $BUILD_DATE"

# Check if image is older than 7 days
python3 -c "
from datetime import datetime, timedelta
build_date = datetime.fromisoformat('$BUILD_DATE'.replace('Z','+00:00'))
age = datetime.now(build_date.tzinfo) - build_date
if age > timedelta(days=7):
    print(f'⚠️ WARNING: Image is {age.days} days old')
else:
    print(f'✅ Image is {age.days} days old (within threshold)')
"
```

### 5.5 State Table Corruption/Deadlocks

**Corruption Scenarios:**

| Scenario | Symptom | Detection Query |
|----------|---------|-----------------|
| Orphaned RUNNING state | Job shows complete in Databricks but RUNNING in state table | `SELECT * FROM job_runs WHERE status='RUNNING' AND started_at < current_timestamp() - INTERVAL 6 HOURS` |
| Watermark regression | Data re-processed from earlier date | `SELECT * FROM watermarks WHERE current_watermark < last_successful_watermark` |
| Concurrent writes | State table shows conflicting statuses | Check Delta history: `DESCRIBE HISTORY onyx_control.pipeline_state.job_runs` |
| Missing state records | Pipeline ran but no state table entry | Compare Databricks job run history with state table entries |

**Deadlock Detection:**

```sql
-- Find potential deadlocks (multiple RUNNING for same family+env)
SELECT family, environment, COUNT(*) as running_count
FROM onyx_control.pipeline_state.job_runs
WHERE status = 'RUNNING'
GROUP BY family, environment
HAVING COUNT(*) > 1;

-- Check for blocked watermark advances
SELECT w.family, w.source_table, w.last_successful_watermark,
       j.run_id, j.status, j.started_at
FROM onyx_control.pipeline_state.watermarks w
JOIN onyx_control.pipeline_state.job_runs j
  ON w.family = j.family
WHERE j.status = 'RUNNING'
  AND j.started_at < current_timestamp() - INTERVAL 2 HOURS;
```

### 5.6 Incremental vs Historical Workflow Conflicts

**Problem:** Running both incremental and historical workflows for the same family simultaneously causes data inconsistencies.

**Conflict Matrix:**

| Running | Attempting | Conflict? | Resolution |
|---------|-----------|-----------|------------|
| Incremental | Historical | ⚠️ YES | Pause incremental, run historical, then resume incremental with watermark reset |
| Historical | Incremental | ⚠️ YES | Queue incremental, it will process delta after historical completes |
| Incremental | Incremental | ❌ BLOCKED | State table prevents concurrent same-family runs |
| Historical | Historical | ❌ BLOCKED | State table prevents concurrent same-family runs |

**Prevention Logic:**

```python
def acquire_pipeline_lock(family, mode, environment):
    """Check for conflicts before starting pipeline."""
    
    # Check for any running pipeline in same family+env
    running = spark.sql(f"""
        SELECT run_id, mode, started_at
        FROM onyx_control.pipeline_state.job_runs
        WHERE family = '{family}'
          AND environment = '{environment}'
          AND status IN ('RUNNING', 'RETRYING')
    """).collect()
    
    if running:
        for run in running:
            if mode == 'historical' and run.mode == 'incremental':
                # Historical takes priority — pause incremental
                pause_workflow(run.run_id)
                logger.info(f"Paused incremental run {run.run_id} for historical load")
            elif mode == 'incremental' and run.mode == 'historical':
                raise ConflictError(
                    f"Cannot start incremental — historical run {run.run_id} in progress. "
                    f"Started at {run.started_at}. Wait for completion."
                )
            else:
                raise ConflictError(
                    f"Cannot start {mode} — another {run.mode} run {run.run_id} already active."
                )
    
    # Acquire lock
    insert_state_record(family, mode, environment, status="RUNNING")
```

### 5.7 Memory/Cluster Sizing Issues

**Sizing Guidelines by Family:**

| Family | Incremental (daily) | Historical (full) | Recommended Node Type |
|--------|---------------------|-------------------|-----------------------|
| Claims | 4-8 workers, 32GB each | 16-32 workers, 64GB each | Standard_DS4_v2 / m5.2xlarge |
| Clinical | 4-8 workers, 32GB each | 16-32 workers, 64GB each | Standard_DS4_v2 / m5.2xlarge |
| Formulary | 2-4 workers, 16GB each | 4-8 workers, 32GB each | Standard_DS3_v2 / m5.xlarge |
| PVD | 2-4 workers, 16GB each | 8-16 workers, 32GB each | Standard_DS3_v2 / m5.xlarge |
| CMS-0057 | 4-8 workers, 32GB each | 16-32 workers, 64GB each | Standard_DS4_v2 / m5.2xlarge |
| CMS-9115 | 2-4 workers, 16GB each | 8-16 workers, 32GB each | Standard_DS3_v2 / m5.xlarge |

**OOM Detection:**

```python
# Check for OOM indicators in Spark UI metrics
def check_memory_pressure(cluster_id):
    """Detect memory pressure indicators."""
    
    metrics = get_cluster_metrics(cluster_id)
    
    issues = []
    if metrics.gc_time_ratio > 0.3:
        issues.append(f"High GC time: {metrics.gc_time_ratio:.0%} (threshold: 30%)")
    if metrics.spill_to_disk_bytes > 0:
        issues.append(f"Disk spill detected: {metrics.spill_to_disk_bytes / 1e9:.1f} GB")
    if metrics.executor_failures > 0:
        issues.append(f"Executor failures: {metrics.executor_failures}")
    if metrics.peak_memory_usage > 0.9:
        issues.append(f"Peak memory: {metrics.peak_memory_usage:.0%} (threshold: 90%)")
    
    return issues
```

**Spark Configuration for Large Workloads:**

```python
# Apply when processing >10M records
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")
spark.conf.set("spark.sql.shuffle.partitions", "400")
spark.conf.set("spark.executor.memory", "32g")
spark.conf.set("spark.executor.memoryOverhead", "8g")
spark.conf.set("spark.driver.memory", "16g")
spark.conf.set("spark.sql.files.maxPartitionBytes", "128m")
spark.conf.set("spark.sql.broadcastTimeout", "600")
```

### 5.8 Network/Timeout Failures to FHIR Stores

**Common Network Issues:**

| Issue | Error Pattern | Fix |
|-------|---------------|-----|
| FHIR store overloaded | HTTP 429 (Too Many Requests) | Implement exponential backoff. Reduce `concurrent_requests`. |
| Token expiration | HTTP 401 during long run | Add token refresh logic. Set refresh buffer. |
| Connection timeout | `ConnectionTimeoutError` after 30s | Increase `timeout_seconds`. Check network route. Verify security group rules. |
| DNS resolution failure | `gaierror: Name or service not known` | Check DNS configuration. Verify VPC peering. Use IP-based failover. |
| TLS certificate issues | `SSLCertVerificationError` | Update CA bundle. Check cert expiration. Verify intermediate certs. |
| Load balancer 504 | HTTP 504 Gateway Timeout | Reduce bundle size. Check FHIR store health. Contact platform team. |

**Retry Configuration:**

```python
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=4, max=60),
    retry=retry_if_exception_type((ConnectionError, TimeoutError, HTTPError429))
)
def post_fhir_bundle(bundle, fhir_client):
    """Post bundle with retry logic."""
    try:
        response = fhir_client.post(
            "/",
            json=bundle.dict(),
            timeout=30,
            headers={"Prefer": "return=OperationOutcome"}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 429:
            retry_after = int(e.response.headers.get("Retry-After", 30))
            time.sleep(retry_after)
            raise
        elif e.response.status_code >= 500:
            raise  # Retry on server errors
        else:
            raise NonRetryableError(f"FHIR error {e.response.status_code}: {e.response.text}")
```

---

## 6. Diagnostic Procedures

### 6.1 How to Read Databricks Job Run Logs

**Step 1: Navigate to the job run**

```
Databricks Workspace → Workflows → Find job by name → Click run ID
```

**Step 2: Identify the failed task**

```
Run page shows task DAG with colored status:
  🟢 Green = Success
  🔴 Red = Failed
  ⚪ Gray = Skipped/Not Run
  🟡 Yellow = Running
```

**Step 3: Read task-level logs**

```
Click failed task → "Logs" tab → Select:
  - Driver Logs (stdout/stderr) — application-level errors
  - Spark Driver Logs (log4j) — Spark framework errors
  - Cluster Event Log — infrastructure events (OOM kills, spot loss)
```

**Step 4: Key log patterns to search for**

```bash
# Application errors (most common)
grep -i "ERROR\|EXCEPTION\|FAILED\|CRITICAL" driver_logs.txt

# OOM indicators
grep -i "OutOfMemory\|heap space\|GC overhead" driver_logs.txt

# Onyx-specific errors
grep -i "onyx\.\|OnyxError\|PipelineError" driver_logs.txt

# FHIR errors
grep -i "fhir\|bundle\|OperationOutcome\|HTTP [45]" driver_logs.txt

# Config issues
grep -i "config\|setting\|not found\|missing" driver_logs.txt
```

**Step 5: Check Spark UI for performance issues**

```
Failed task → "Spark UI" link → Check:
  - Jobs tab: Which Spark job failed?
  - Stages tab: Which stage has the most shuffle/spill?
  - SQL tab: Which query is slow?
  - Executors tab: Any dead executors?
```

### 6.2 How to Check Job State Table

```sql
-- 1. Current state of all pipelines
SELECT 
    family,
    operation,
    mode,
    environment,
    status,
    started_at,
    completed_at,
    TIMESTAMPDIFF(MINUTE, started_at, COALESCE(completed_at, current_timestamp())) as duration_min,
    records_processed,
    records_failed,
    error_category,
    retry_count
FROM onyx_control.pipeline_state.job_runs
WHERE environment = 'prod'
ORDER BY started_at DESC
LIMIT 50;

-- 2. Failed runs in last 24 hours
SELECT *
FROM onyx_control.pipeline_state.job_runs
WHERE status = 'FAILED'
  AND started_at > current_timestamp() - INTERVAL 24 HOURS
  AND environment = 'prod'
ORDER BY started_at DESC;

-- 3. Orphaned runs (started but never completed)
SELECT *
FROM onyx_control.pipeline_state.job_runs
WHERE status = 'RUNNING'
  AND started_at < current_timestamp() - INTERVAL 6 HOURS;

-- 4. Watermark status per family
SELECT 
    w.family,
    w.source_table,
    w.last_successful_watermark,
    w.current_watermark,
    w.updated_at,
    DATEDIFF(current_date(), TO_DATE(w.last_successful_watermark)) as days_behind
FROM onyx_control.pipeline_state.watermarks w
WHERE w.environment = 'prod'
ORDER BY days_behind DESC;

-- 5. Success rate by family (last 30 days)
SELECT 
    family,
    COUNT(*) as total_runs,
    SUM(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END) as successes,
    SUM(CASE WHEN status = 'FAILED' THEN 1 ELSE 0 END) as failures,
    ROUND(SUM(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) as success_rate
FROM onyx_control.pipeline_state.job_runs
WHERE environment = 'prod'
  AND started_at > current_timestamp() - INTERVAL 30 DAYS
GROUP BY family
ORDER BY success_rate ASC;
```

### 6.3 How to Verify Config Alignment Across Environments

**Procedure:**

```python
def verify_config_alignment():
    """Full config alignment check across all environments."""
    
    environments = ['dev', 'stg', 'prod']
    families = ['claims', 'clinical', 'formulary', 'pvd', 'cms0057', 'cms9115']
    
    report = []
    
    for family in families:
        for env in environments:
            # 1. Check extract config exists and is valid YAML
            config_path = f"/Workspace/onyx/configs/{family}/extract_config.yaml"
            try:
                config = yaml.safe_load(open(config_path))
                report.append({"family": family, "env": env, "check": "config_exists", "status": "PASS"})
            except Exception as e:
                report.append({"family": family, "env": env, "check": "config_exists", "status": "FAIL", "detail": str(e)})
                continue
            
            # 2. Check INI file
            ini_path = f"/Workspace/onyx/configs/{env}/onyx_config.ini"
            ini = configparser.ConfigParser()
            ini.read(ini_path)
            
            # 3. Check Terraform state matches INI
            tf_vars = load_terraform_vars(env)
            
            checks = [
                ("wheel_version", tf_vars.get('wheel_version'), get_deployed_wheel_version(env, family)),
                ("image_tag", tf_vars.get('image_tag'), get_cluster_image_tag(env, family)),
                ("fhir_url", ini.get('fhir', 'base_url'), get_runtime_fhir_url(env, family)),
            ]
            
            for check_name, expected, actual in checks:
                status = "PASS" if expected == actual else "FAIL"
                report.append({
                    "family": family, "env": env, 
                    "check": check_name, "status": status,
                    "expected": expected, "actual": actual
                })
    
    return pd.DataFrame(report)
```

**Quick CLI Check:**

```bash
# Compare configs between environments
diff <(grep -v "^;" configs/dev/onyx_config.ini | sort) \
     <(grep -v "^;" configs/prod/onyx_config.ini | sort)

# Check wheel versions on DBFS
dbfs ls dbfs:/onyx/wheels/prod/ | grep onyx_core
dbfs ls dbfs:/onyx/wheels/stg/ | grep onyx_core

# Verify Terraform state
cd terraform/environments/prod
terraform show -json | jq '.values.root_module.resources[] | select(.type == "databricks_job") | {name: .values.name, image: .values.job_cluster[0].new_cluster.docker_image.url}'
```

### 6.4 How to Identify Which Step Failed and Why

**Decision Tree:**

```
1. Check Databricks job run status
   └── Which task is red?
       ├── preprocess → Data quality issue or source unavailable
       ├── transform → Mapping/code error or OOM
       ├── upload → Storage/permission issue or empty SAM
       ├── upsert → FHIR store issue or validation failure
       └── terminate → Cleanup error (usually non-critical)

2. Check error message in state table
   └── SELECT error_message, error_category FROM job_runs WHERE run_id = '{id}'

3. Check driver logs for stack trace
   └── Search for "Traceback" or "Exception"

4. Check Spark UI for infrastructure issues
   └── Dead executors? Shuffle spill? Stage timeouts?

5. Check external dependencies
   └── FHIR store health? Source system available? Secrets valid?
```

**Automated Diagnosis Script:**

```python
def diagnose_failed_run(run_id):
    """Automated diagnosis of a failed pipeline run."""
    
    # Get run details
    run = spark.sql(f"""
        SELECT * FROM onyx_control.pipeline_state.job_runs 
        WHERE run_id = '{run_id}'
    """).first()
    
    diagnosis = {
        "run_id": run_id,
        "family": run.family,
        "operation": run.operation,
        "error_message": run.error_message,
        "error_category": run.error_category,
        "duration_min": (run.completed_at - run.started_at).total_seconds() / 60 if run.completed_at else None,
        "checks": []
    }
    
    # Check 1: Config hash
    expected_hash = compute_current_config_hash(run.family, run.environment)
    if expected_hash != run.config_hash:
        diagnosis["checks"].append({
            "check": "config_hash",
            "status": "WARNING",
            "detail": "Config has changed since this run started"
        })
    
    # Check 2: Wheel version
    current_wheel = get_current_wheel_version(run.environment)
    if current_wheel != run.wheel_version:
        diagnosis["checks"].append({
            "check": "wheel_version", 
            "status": "WARNING",
            "detail": f"Wheel updated: run used {run.wheel_version}, current is {current_wheel}"
        })
    
    # Check 3: Records processed vs expected
    if run.records_processed == 0 and run.operation == "transform":
        diagnosis["checks"].append({
            "check": "zero_records",
            "status": "ERROR",
            "detail": "Transform produced 0 records — check watermark and source data"
        })
    
    # Check 4: Error categorization
    if run.error_message:
        if "OutOfMemory" in run.error_message:
            diagnosis["recommendation"] = "Increase cluster memory or reduce partition size"
        elif "timeout" in run.error_message.lower():
            diagnosis["recommendation"] = "Check FHIR store health and increase timeout"
        elif "validation" in run.error_message.lower():
            diagnosis["recommendation"] = "Check quarantine table for specific validation failures"
        elif "permission" in run.error_message.lower():
            diagnosis["recommendation"] = "Check IAM roles and secret access"
    
    return diagnosis
```

### 6.5 How to Safely Re-Run Failed Workflows

**Pre-Re-Run Checklist:**

| # | Check | Command | Required? |
|---|-------|---------|-----------|
| 1 | Confirm no concurrent run | `SELECT * FROM job_runs WHERE family='{f}' AND status='RUNNING'` | ✅ Yes |
| 2 | Check if root cause is fixed | Review error + apply fix | ✅ Yes |
| 3 | Verify watermark state | `SELECT * FROM watermarks WHERE family='{f}'` | ✅ Yes |
| 4 | Check for partial data in SAM | `SELECT COUNT(*) FROM {family}_sam WHERE run_id='{failed_id}'` | ✅ Yes |
| 5 | Clean up partial data if needed | See [Recovery Procedures](#7-recovery-procedures) | Conditional |
| 6 | Verify config alignment | Run alignment check | Recommended |
| 7 | Check cluster health | Verify cluster can start | ✅ Yes |

**Safe Re-Run Procedure:**

```python
def safe_rerun(run_id, force=False):
    """Safely re-run a failed pipeline."""
    
    # 1. Get original run details
    original = get_run_details(run_id)
    assert original.status == 'FAILED', f"Can only re-run FAILED runs, got {original.status}"
    
    # 2. Check for concurrent runs
    concurrent = check_concurrent_runs(original.family, original.environment)
    if concurrent and not force:
        raise SafetyError(f"Concurrent run detected: {concurrent.run_id}. Use force=True to override.")
    
    # 3. Determine re-run strategy
    if original.operation == 'preprocess':
        # Full re-run from beginning
        strategy = "full_rerun"
    elif original.operation == 'transform':
        # Can restart from transform (preprocess was successful)
        strategy = "restart_from_transform"
    elif original.operation in ('upload', 'upsert'):
        # Check for partial data
        partial_records = count_partial_records(original)
        if partial_records > 0:
            # Clean up partial data first
            cleanup_partial_data(original)
        strategy = f"restart_from_{original.operation}"
    elif original.operation == 'terminate':
        # Just re-run terminate
        strategy = "restart_terminate_only"
    
    # 4. Update state table
    spark.sql(f"""
        UPDATE onyx_control.pipeline_state.job_runs
        SET status = 'RETRYING', 
            retry_count = retry_count + 1,
            updated_at = current_timestamp()
        WHERE run_id = '{run_id}'
    """)
    
    # 5. Trigger re-run
    new_run_id = trigger_workflow(
        family=original.family,
        mode=original.mode,
        environment=original.environment,
        start_from=strategy,
        parent_run_id=run_id
    )
    
    return {"strategy": strategy, "new_run_id": new_run_id}
```

**Re-Run from Specific Task (Databricks API):**

```python
import requests

def rerun_from_task(databricks_run_id, task_key):
    """Re-run a workflow from a specific failed task."""
    
    response = requests.post(
        f"{DATABRICKS_HOST}/api/2.1/jobs/runs/repair",
        headers={"Authorization": f"Bearer {DATABRICKS_TOKEN}"},
        json={
            "run_id": databricks_run_id,
            "rerun_tasks": [task_key],
            "rerun_dependent_tasks": True  # Also re-run downstream tasks
        }
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        raise DatabricksAPIError(f"Repair failed: {response.text}")
```

### 6.6 How to Handle Partial Loads

**Scenario:** Some FHIR bundles succeeded, some failed during upsert.

**Detection:**

```sql
-- Check bundle tracking table
SELECT 
    bundle_id,
    status,  -- SUCCESS, FAILED, PENDING
    resource_count,
    error_message,
    submitted_at
FROM onyx_control.pipeline_state.bundle_tracking
WHERE run_id = '{run_id}'
  AND status = 'FAILED';

-- Summary of partial load
SELECT 
    status,
    COUNT(*) as bundle_count,
    SUM(resource_count) as total_resources
FROM onyx_control.pipeline_state.bundle_tracking
WHERE run_id = '{run_id}'
GROUP BY status;
```

**Resolution Options:**

| Option | When to Use | Procedure |
|--------|------------|-----------|
| Retry failed bundles only | Transient error (timeout, 429) | Re-submit only FAILED bundles with same content |
| Rollback and retry all | Data corruption suspected | Delete successful resources, reset state, full re-run |
| Accept partial and continue | Non-critical failures (< 1%) | Mark failed as quarantined, advance watermark, review later |
| Manual intervention | Complex failures | Export failed bundles for manual review and correction |

**Retry Failed Bundles:**

```python
def retry_failed_bundles(run_id, max_retries=3):
    """Retry only the failed bundles from a partial load."""
    
    failed_bundles = spark.sql(f"""
        SELECT bundle_id, bundle_content, retry_count
        FROM onyx_control.pipeline_state.bundle_tracking
        WHERE run_id = '{run_id}' 
          AND status = 'FAILED'
          AND retry_count < {max_retries}
    """).collect()
    
    results = {"success": 0, "failed": 0, "skipped": 0}
    
    for bundle_row in failed_bundles:
        try:
            bundle = json.loads(bundle_row.bundle_content)
            response = post_fhir_bundle(bundle, fhir_client)
            
            # Update tracking
            update_bundle_status(bundle_row.bundle_id, "SUCCESS")
            results["success"] += 1
            
        except NonRetryableError as e:
            update_bundle_status(bundle_row.bundle_id, "FAILED", str(e))
            results["failed"] += 1
            
        except Exception as e:
            update_bundle_status(
                bundle_row.bundle_id, "FAILED", str(e),
                retry_count=bundle_row.retry_count + 1
            )
            results["failed"] += 1
    
    return results
```

---

## 7. Recovery Procedures

### 7.1 Safe Re-Run Patterns

**Pattern 1: Idempotent Full Re-Run**

Use when: You're unsure what state the data is in and want a clean slate.

```python
def idempotent_full_rerun(family, environment, watermark_override=None):
    """
    Completely idempotent re-run:
    1. Cleans up any partial state from failed run
    2. Resets watermark to last known good position
    3. Triggers fresh pipeline execution
    """
    
    # Step 1: Cancel any running/pending runs
    cancel_active_runs(family, environment)
    
    # Step 2: Clean partial SAM data from failed run
    last_failed = get_last_failed_run(family, environment)
    if last_failed:
        spark.sql(f"""
            DELETE FROM onyx_staging.{family}_sam.{get_sam_table(family)}
            WHERE _run_id = '{last_failed.run_id}'
        """)
        logger.info(f"Cleaned partial data from run {last_failed.run_id}")
    
    # Step 3: Reset watermark
    if watermark_override:
        new_watermark = watermark_override
    else:
        # Reset to last successful watermark
        new_watermark = spark.sql(f"""
            SELECT last_successful_watermark 
            FROM onyx_control.pipeline_state.watermarks
            WHERE family = '{family}' AND environment = '{environment}'
        """).first()[0]
    
    spark.sql(f"""
        UPDATE onyx_control.pipeline_state.watermarks
        SET current_watermark = '{new_watermark}',
            updated_at = current_timestamp(),
            updated_by = 'recovery_procedure'
        WHERE family = '{family}' AND environment = '{environment}'
    """)
    
    # Step 4: Mark old failed run as CANCELLED
    spark.sql(f"""
        UPDATE onyx_control.pipeline_state.job_runs
        SET status = 'CANCELLED',
            error_message = 'Superseded by recovery re-run',
            updated_at = current_timestamp()
        WHERE run_id = '{last_failed.run_id}'
    """)
    
    # Step 5: Trigger new run
    new_run_id = trigger_fresh_pipeline(family, environment, "incremental")
    
    return {
        "action": "idempotent_full_rerun",
        "cleaned_run": last_failed.run_id if last_failed else None,
        "watermark_reset_to": new_watermark,
        "new_run_id": new_run_id
    }
```

**Pattern 2: Resume from Failed Step**

Use when: You know the exact failure point and prior steps are clean.

```python
def resume_from_step(run_id, start_step):
    """Resume pipeline from a specific step (prior steps assumed clean)."""
    
    VALID_STEPS = ['preprocess', 'transform', 'upload', 'upsert', 'terminate']
    assert start_step in VALID_STEPS, f"Invalid step: {start_step}"
    
    run = get_run_details(run_id)
    
    # Use Databricks repair API to re-run from specific task
    repair_response = rerun_from_task(
        databricks_run_id=run.databricks_run_id,
        task_key=start_step
    )
    
    # Update state
    spark.sql(f"""
        UPDATE onyx_control.pipeline_state.job_runs
        SET status = 'RETRYING',
            retry_count = retry_count + 1,
            error_message = NULL,
            updated_at = current_timestamp()
        WHERE run_id = '{run_id}'
    """)
    
    return repair_response
```

**Pattern 3: Skip and Continue**

Use when: A non-critical batch of records failed but the rest should proceed.

```python
def skip_failed_records_and_continue(run_id, quarantine_reason):
    """Move failed records to quarantine and advance the pipeline."""
    
    run = get_run_details(run_id)
    
    # Get failed records
    failed_records = spark.sql(f"""
        SELECT * FROM onyx_staging.{run.family}_sam.staging
        WHERE _run_id = '{run_id}' AND _status = 'FAILED'
    """)
    
    # Move to quarantine
    failed_records.withColumn("quarantine_reason", lit(quarantine_reason)) \
                  .withColumn("quarantined_at", current_timestamp()) \
                  .write.mode("append") \
                  .saveAsTable(f"onyx_staging.{run.family}_sam.quarantine")
    
    # Remove from staging
    spark.sql(f"""
        DELETE FROM onyx_staging.{run.family}_sam.staging
        WHERE _run_id = '{run_id}' AND _status = 'FAILED'
    """)
    
    # Continue pipeline with remaining records
    remaining = spark.sql(f"""
        SELECT COUNT(*) FROM onyx_staging.{run.family}_sam.staging
        WHERE _run_id = '{run_id}' AND _status = 'PENDING'
    """).first()[0]
    
    if remaining > 0:
        trigger_from_step(run_id, 'upload')  # Continue from upload step
    else:
        logger.warning("No remaining records after quarantine — skipping pipeline")
    
    return {"quarantined": failed_records.count(), "remaining": remaining}
```

### 7.2 State Table Reset Procedures

**⚠️ CAUTION: State table modifications can cause data loss or duplication. Always take a backup first.**

**Procedure 1: Reset Single Run State**

```sql
-- Step 1: Backup the record
CREATE TABLE onyx_control.pipeline_state.job_runs_backup_20260707 AS
SELECT * FROM onyx_control.pipeline_state.job_runs
WHERE run_id = '{run_id}';

-- Step 2: Update state
UPDATE onyx_control.pipeline_state.job_runs
SET status = 'CANCELLED',
    error_message = 'Manual state reset by {engineer_name} - ticket {JIRA_ID}',
    completed_at = current_timestamp(),
    updated_at = current_timestamp()
WHERE run_id = '{run_id}';
```

**Procedure 2: Reset Watermark**

```sql
-- Step 1: Check current state
SELECT * FROM onyx_control.pipeline_state.watermarks
WHERE family = '{family}' AND environment = '{env}';

-- Step 2: Determine correct watermark
-- Option A: Reset to last successful run's watermark
SELECT watermark_value FROM onyx_control.pipeline_state.job_runs
WHERE family = '{family}' AND environment = '{env}' AND status = 'SUCCESS'
ORDER BY completed_at DESC LIMIT 1;

-- Option B: Reset to specific date
-- Use when you know the exact correct position

-- Step 3: Update watermark
UPDATE onyx_control.pipeline_state.watermarks
SET last_successful_watermark = '{correct_value}',
    current_watermark = '{correct_value}',
    updated_at = current_timestamp(),
    updated_by = '{engineer_name} - {JIRA_ID}'
WHERE family = '{family}' AND environment = '{env}';
```

**Procedure 3: Clear All Orphaned Runs**

```sql
-- Find orphaned runs (RUNNING for >6 hours)
SELECT run_id, family, operation, started_at,
       TIMESTAMPDIFF(HOUR, started_at, current_timestamp()) as hours_running
FROM onyx_control.pipeline_state.job_runs
WHERE status = 'RUNNING'
  AND started_at < current_timestamp() - INTERVAL 6 HOURS;

-- Verify these are actually dead (cross-reference with Databricks)
-- Then clear them:
UPDATE onyx_control.pipeline_state.job_runs
SET status = 'FAILED',
    error_message = 'Orphaned run cleared by automated recovery',
    completed_at = current_timestamp(),
    updated_at = current_timestamp()
WHERE status = 'RUNNING'
  AND started_at < current_timestamp() - INTERVAL 6 HOURS;
```

### 7.3 Rollback of Partial FHIR Loads

**⚠️ CRITICAL: FHIR rollbacks are complex. Always verify with the FHIR platform team before executing in production.**

**Scenario:** A partial upsert loaded incorrect data into the FHIR store.

**Procedure:**

```python
def rollback_fhir_load(run_id, family, dry_run=True):
    """
    Rollback FHIR resources loaded by a specific pipeline run.
    
    WARNING: This deletes resources from the FHIR store. 
    Always run with dry_run=True first.
    """
    
    # Step 1: Get all bundles from this run
    bundles = spark.sql(f"""
        SELECT bundle_id, bundle_content, status, resource_ids
        FROM onyx_control.pipeline_state.bundle_tracking
        WHERE run_id = '{run_id}' AND status = 'SUCCESS'
    """).collect()
    
    logger.info(f"Found {len(bundles)} successful bundles to rollback")
    
    resources_to_delete = []
    
    # Step 2: Extract resource IDs from successful bundles
    for bundle in bundles:
        resource_ids = json.loads(bundle.resource_ids)
        for rid in resource_ids:
            resources_to_delete.append(rid)
    
    logger.info(f"Total resources to delete: {len(resources_to_delete)}")
    
    if dry_run:
        logger.info("DRY RUN — no resources will be deleted")
        # Verify resources exist
        sample = resources_to_delete[:10]
        for rid in sample:
            resource_type, resource_id = rid.split("/")
            response = fhir_client.get(f"/{resource_type}/{resource_id}")
            logger.info(f"  {rid}: {'EXISTS' if response.status_code == 200 else 'NOT FOUND'}")
        return {"action": "dry_run", "resources_found": len(resources_to_delete)}
    
    # Step 3: Delete resources (with audit trail)
    deleted = []
    failed = []
    
    for rid in resources_to_delete:
        resource_type, resource_id = rid.split("/")
        try:
            # Soft delete (keeps history)
            response = fhir_client.delete(f"/{resource_type}/{resource_id}")
            if response.status_code in (200, 204):
                deleted.append(rid)
            else:
                failed.append({"id": rid, "status": response.status_code, "error": response.text})
        except Exception as e:
            failed.append({"id": rid, "error": str(e)})
    
    # Step 4: Update bundle tracking
    spark.sql(f"""
        UPDATE onyx_control.pipeline_state.bundle_tracking
        SET status = 'ROLLED_BACK',
            updated_at = current_timestamp()
        WHERE run_id = '{run_id}' AND status = 'SUCCESS'
    """)
    
    # Step 5: Log rollback event
    log_rollback_event(run_id, family, deleted, failed)
    
    return {
        "action": "rollback_executed",
        "deleted": len(deleted),
        "failed": len(failed),
        "failed_details": failed[:10]  # First 10 for review
    }
```

**Rollback via FHIR Batch Delete:**

```python
def batch_delete_fhir_resources(resource_ids, fhir_client, batch_size=50):
    """Delete multiple FHIR resources using a batch transaction."""
    
    for i in range(0, len(resource_ids), batch_size):
        batch = resource_ids[i:i+batch_size]
        
        bundle = {
            "resourceType": "Bundle",
            "type": "transaction",
            "entry": [
                {
                    "request": {
                        "method": "DELETE",
                        "url": rid
                    }
                }
                for rid in batch
            ]
        }
        
        response = fhir_client.post("/", json=bundle)
        
        if response.status_code != 200:
            logger.error(f"Batch delete failed: {response.text}")
            # Switch to individual deletes for this batch
            for rid in batch:
                individual_delete(rid, fhir_client)
```

### 7.4 Emergency Procedures for Production Data Issues

**Emergency Runbook:**

#### 🚨 SCENARIO 1: Incorrect Data Loaded to Production FHIR Store

```
SEVERITY: P1
TIME LIMIT: 4 hours to contain, 24 hours to resolve

STEP 1: CONTAIN (0-30 minutes)
├── Pause ALL affected family workflows immediately
│   └── databricks jobs pause --job-id {id}
├── Notify: #onyx-platform-alerts, on-call platform engineer, FHIR team
├── Identify scope: How many resources affected? Which members?
│   └── Query bundle_tracking table for run_id
└── Block downstream consumers (if applicable)
    └── Set FHIR store to read-only mode (if supported)

STEP 2: ASSESS (30-60 minutes)
├── Determine root cause (config error? code bug? bad source data?)
├── Quantify impact: affected member count, resource count
├── Determine if PHI exposure risk exists
│   └── If YES → escalate to Privacy Officer immediately
└── Document findings in incident ticket

STEP 3: REMEDIATE (1-4 hours)
├── Execute FHIR rollback (see 7.3)
├── Fix root cause (deploy fix or revert config)
├── Verify fix in dev/staging
└── Re-run with corrected data (if needed)

STEP 4: VERIFY (post-remediation)
├── Confirm rolled-back resources are gone
├── Confirm re-loaded data is correct
├── Run validation suite against affected resources
├── Spot-check 10 random affected members
└── Confirm downstream consumers see correct data

STEP 5: RESUME (after verification)
├── Resume paused workflows
├── Monitor first successful run end-to-end
└── Close incident ticket with timeline + lessons learned
```

#### 🚨 SCENARIO 2: Pipeline Stuck in Loop (Continuous Failures)

```
SEVERITY: P2
TIME LIMIT: 8 hours to resolve

STEP 1: STOP THE LOOP
├── Disable the workflow schedule
│   └── terraform apply -var="schedule_enabled=false"
│   └── OR: Databricks UI → Workflow → Pause schedule
├── Cancel any currently running instance
└── Check: Is the failure causing data corruption? (If yes → P1)

STEP 2: DIAGNOSE
├── Pull last 5 run logs
├── Identify pattern: Same error every time? Different errors?
├── Check: Is it a transient dependency issue? (FHIR store, source DB, auth)
├── Check: Did a recent deployment introduce the issue?
│   └── git log --oneline --since="24 hours ago" -- onyx/
└── Check: Is there a state table issue preventing progress?

STEP 3: FIX
├── If transient dependency → wait and retry
├── If code bug → revert deployment or hotfix
├── If config issue → correct config and redeploy
├── If state corruption → reset state table (7.2)
└── If cluster issue → recreate cluster / change instance type

STEP 4: VERIFY AND RESUME
├── Run manually once with monitoring
├── Confirm success
├── Re-enable schedule
└── Monitor next 3 automated runs
```

#### 🚨 SCENARIO 3: Data Duplication in Production

```
SEVERITY: P2
TIME LIMIT: 12 hours to resolve

STEP 1: IDENTIFY SCOPE
├── Run dedup detection queries (see 5.3)
├── Determine: SAM duplicates? FHIR store duplicates? Both?
├── Quantify: How many records? Which families? Which time period?
└── Determine root cause: Re-run? Source reload? Missing dedup key?

STEP 2: PREVENT FURTHER DUPLICATION
├── Pause affected workflows
├── Fix root cause (add dedup logic, fix watermark, etc.)
└── Deploy fix to dev/staging and verify

STEP 3: CLEAN UP EXISTING DUPLICATES

For SAM table duplicates:
```

```sql
-- Identify and remove SAM duplicates (keep latest)
MERGE INTO onyx_staging.{family}_sam.{table} AS target
USING (
    SELECT *, ROW_NUMBER() OVER (
        PARTITION BY {dedup_keys} 
        ORDER BY last_modified_ts DESC
    ) AS rn
    FROM onyx_staging.{family}_sam.{table}
) AS ranked
ON target._internal_id = ranked._internal_id
WHEN MATCHED AND ranked.rn > 1 THEN DELETE;
```

```
For FHIR store duplicates:
├── Export duplicate resource IDs
├── Determine which to keep (latest version, most complete)
├── Delete duplicates via batch transaction
└── Verify resolution

STEP 4: RESUME AND MONITOR
├── Resume workflows with fix deployed
├── Add alerting rule for duplicate detection
└── Monitor for 48 hours
```

---

## Appendix A: Quick Reference Commands

### Databricks CLI Commands

```bash
# List recent runs for a workflow
databricks jobs list-runs --job-id {job_id} --limit 10

# Get run details
databricks runs get --run-id {run_id}

# Cancel a run
databricks runs cancel --run-id {run_id}

# Repair (re-run from failed task)
databricks runs repair --run-id {run_id} --rerun-tasks '["transform"]'

# Export job definition
databricks jobs get --job-id {job_id} > job_definition.json

# List clusters
databricks clusters list --output JSON | jq '.clusters[] | {id: .cluster_id, name: .cluster_name, state: .state}'
```

### Useful SQL Queries

```sql
-- Pipeline health dashboard
SELECT 
    family,
    DATE(started_at) as run_date,
    COUNT(*) as runs,
    SUM(CASE WHEN status='SUCCESS' THEN 1 ELSE 0 END) as success,
    AVG(TIMESTAMPDIFF(MINUTE, started_at, completed_at)) as avg_duration_min
FROM onyx_control.pipeline_state.job_runs
WHERE environment = 'prod'
  AND started_at > current_date() - INTERVAL 7 DAYS
GROUP BY family, DATE(started_at)
ORDER BY family, run_date DESC;

-- SLA breach detection
SELECT *
FROM onyx_control.pipeline_state.job_runs
WHERE environment = 'prod'
  AND status = 'SUCCESS'
  AND TIMESTAMPDIFF(MINUTE, started_at, completed_at) > 120  -- SLA = 2 hours
  AND started_at > current_date() - INTERVAL 7 DAYS;

-- Data freshness check
SELECT 
    family,
    last_successful_watermark,
    DATEDIFF(current_date(), TO_DATE(last_successful_watermark)) as days_stale,
    CASE 
        WHEN DATEDIFF(current_date(), TO_DATE(last_successful_watermark)) > 2 THEN '🔴 STALE'
        WHEN DATEDIFF(current_date(), TO_DATE(last_successful_watermark)) > 1 THEN '🟡 BEHIND'
        ELSE '🟢 CURRENT'
    END as freshness_status
FROM onyx_control.pipeline_state.watermarks
WHERE environment = 'prod';
```

---

## Appendix B: Contact & Escalation

| Issue Type | First Responder | Escalation | SLA |
|------------|----------------|------------|-----|
| Pipeline failure (single) | On-call DE | DE Team Lead | 4 hours |
| Pipeline failure (multiple) | On-call DE | Platform Lead + DE Lead | 2 hours |
| Data corruption | On-call DE + Platform | Engineering Manager | 1 hour |
| FHIR store issues | Platform team | FHIR vendor support | 30 min |
| Regulatory/compliance | Platform Lead | Privacy Officer + Legal | Immediate |
| Cluster/infra issues | Platform team | Cloud platform team | 2 hours |

---

## Appendix C: Monitoring & Alerting

**Key Metrics to Monitor:**

| Metric | Alert Threshold | Dashboard |
|--------|----------------|-----------|
| Pipeline success rate | < 95% over 24h | Onyx Pipeline Health |
| Pipeline duration | > 2x normal | Onyx Pipeline Health |
| Watermark staleness | > 48 hours | Onyx Data Freshness |
| Quarantine volume | > 5% of total records | Onyx Data Quality |
| FHIR store latency | > 5s p99 | Onyx FHIR Performance |
| Cluster utilization | > 90% memory sustained | Onyx Infrastructure |
| Bundle rejection rate | > 2% | Onyx FHIR Performance |
| Duplicate detection rate | > 0.1% | Onyx Data Quality |

---

*End of Handbook — Last reviewed: 2026-07-07*
