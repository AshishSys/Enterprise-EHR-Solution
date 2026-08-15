# InterOperability with Onyx — Implementation Details

> Complete technical guide covering every component, what it does, why it exists, and how to use it.

> **Start here for learning:** [LEARN_FROM_STEP_1.md](Training/LEARN_FROM_STEP_1.md) — Learning is the primary objective; building proves you learned. Do Step 1 before any production phase.

---

## System Overview

This project implements a **complete CMS interoperability platform** that transforms raw healthcare data into FHIR R4-compliant resources and serves them through authenticated APIs — exactly mirroring the production Abacus/Onyx architecture.

```
┌─────────────────────────────────────────────────────────────────────┐
│                     FULL SYSTEM (6 Components)                       │
│                                                                     │
│  [Pipeline]──→[FHIR Store]──→[FITE :8080]──→[Consumer App]         │
│                                    ↑                                │
│                              [SLAP :9000]  (authenticates requests) │
│                                                                     │
│  [Onyx Insights :9001]  (monitors everything)                      │
│  [MDP :9002]            (config + service discovery)               │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Component 1: Data Pipeline (`interop_pipeline.py`)

### What It Does
Transforms raw CSV healthcare data through 5 layers into FHIR R4-compliant resources, mimicking the Abacus data engineering pipeline.

### Why It Exists
CMS rules (9115 & 0057) require payers to expose healthcare data via FHIR APIs. Raw payer data (claims, clinical records, enrollments) is NOT in FHIR format — it must be transformed through multiple stages to ensure data quality, normalization, and IG compliance before serving.

### Architecture Role
**Abacus-owned** — responsible for data correctness, transformation logic, and FHIR bundle generation.

### Pipeline Layers

| Layer | Name | What Happens | Why |
|-------|------|--------------|-----|
| 0 | **De-Identification** | HIPAA Safe Harbor (18 identifiers) or Expert Determination; split identified vs de-id paths | Analytics, Fabric, logs, and LLMs never see raw PHI. CMS APIs keep identified data behind SLAP |
| 0b | **MDM** | AHIMA / ISO 8000 / HL7 PA golden records, survivorship, tokenized crosswalk | Stable member/provider keys before FM joins; PVD golden before Claims refs |
| 1 | **Raw Ingestion** | Load CSV files as-is | Capture source data without modification |
| 2 | **Foundational Marts (FM)** | Validate, normalize, deduplicate | Create a canonical, stable data model. FM is NOT FHIR-shaped — optimized for reuse and incremental updates |
| 3 | **Subject Area Marts (SAM)** | Transform FM → IG-aligned structures | Bridge between canonical data and FHIR IG requirements. Each SAM maps to a CMS-0057 domain |
| 4 | **FHIR Generation** | Convert SAM → FHIR R4 JSON | Create compliant resources per US Core / CARIN BB profiles |
| 5 | **Bundle Packaging** | Create transaction bundles + NDJSON | Package for Firely (bundles) or HealthLake (NDJSON $import) |
| 6 | **Dual Engine** | Same de-id SAM on Databricks and Microsoft Fabric | Cost/speed bake-off without changing CMS path |
| 7 | **AI Observability** | RCA + anomaly models on de-id OpenTelemetry signals | Platform health without PHI in prompts |

### Use Cases

**Use Case 1: Initial Data Load (Historical)**
```bash
# Load all historical patient data for a new payer client
python interop_pipeline.py --input ./client_data --output ./fhir_output
```
- Processes all 8 CSV files at once
- Generates per-patient transaction bundles
- Creates NDJSON for HealthLake bulk import
- Result: 9,997 FHIR resources across 8 types

**Use Case 2: Incremental Update**
- New claims arrive daily
- Pipeline re-runs on new data only
- Upserts (PUT) existing resources, creates (POST) new ones

**Use Case 3: Multi-state Payer**
- Different states have different data volumes and schedules
- Pipeline is parameterized by input directory
- Each state run produces isolated output

### Input Files

| File | Records | Produces |
|------|---------|----------|
| Patients.csv | 10 | Patient (US Core) |
| Encounters.csv | 390 | Encounter (US Core) |
| Conditions.csv | 346 | Condition (US Core) |
| Medications.csv | 350 | MedicationRequest (US Core) |
| Observations.csv | 6,868 | Observation (US Core Lab/Vitals) |
| Procedures.csv | 1,285 | Procedure (US Core) |
| Allergies.csv | 8 | AllergyIntolerance (US Core) |
| Claims.csv | 740 | ExplanationOfBenefit (CARIN Blue Button) |

### Output

```
fhir_output/
├── bundles/                    # Per-patient transaction bundles (for Firely)
│   ├── bundle_Alberto639_Berge125.json (793 entries)
│   ├── bundle_Margarette462_Bogan287.json (4704 entries)
│   └── ... (10 bundles total)
└── ndjson/                     # Per-type NDJSON (for HealthLake $import)
    ├── Patient.ndjson          (10 resources)
    ├── Encounter.ndjson        (390 resources)
    ├── Condition.ndjson        (346 resources)
    ├── MedicationRequest.ndjson (350 resources)
    ├── Observation.ndjson      (6,868 resources)
    ├── Procedure.ndjson        (1,285 resources)
    ├── AllergyIntolerance.ndjson (8 resources)
    └── ExplanationOfBenefit.ndjson (740 resources)
```

### How to Run
```bash
python interop_pipeline.py --input ./source_data --output ./fhir_output
```

### Dependencies
- `pandas` (the only external dependency in the project)

---

## Component 2: SLAP (`slap_server.py` — Port 9000)

### What It Does
**SMART Launch Authentication Proxy** — handles all authentication and authorization for the interoperability platform. Issues OAuth2 tokens, validates PKCE challenges, enforces scopes, manages consent, and provides token introspection for FITE.

### Why It Exists
CMS-9115 and CMS-0057 **mandate** that all FHIR API access must be authenticated via SMART on FHIR (an OAuth2-based protocol). Patient apps need user-facing login flows; backend systems need machine-to-machine credentials. SLAP provides both.

### Architecture Role
**Onyx-owned** — responsible for security, consent enforcement, and SMART compliance.

### Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/.well-known/smart-configuration` | SMART discovery document (required by spec) |
| GET | `/auth/authorize` | Authorization endpoint (user login + consent) |
| POST | `/auth/token` | Token exchange (code → tokens, or client_credentials) |
| POST | `/auth/introspect` | Token validation (FITE calls this to verify requests) |
| POST | `/auth/revoke` | Revoke compromised or expired tokens |
| GET | `/auth/jwks` | Public signing keys for JWT validation |

### Authentication Flows

**Flow 1: Patient App (Standalone Launch + PKCE)**

| Step | What Happens | Why |
|------|--------------|-----|
| 1 | App generates code_verifier + code_challenge (S256) | PKCE prevents authorization code interception |
| 2 | App redirects user to `/auth/authorize` | User authenticates and consents |
| 3 | SLAP redirects back with authorization code | Short-lived code (60 seconds) |
| 4 | App exchanges code + code_verifier at `/auth/token` | PKCE verified, tokens issued |
| 5 | App uses access_token to call FITE | Bearer token, 5-minute expiry |

**Flow 2: Backend Services (Payer-to-Payer / Bulk Data)**

| Step | What Happens | Why |
|------|--------------|-----|
| 1 | System authenticates with JWT assertion or client_secret | No user involved |
| 2 | POST `/auth/token` with grant_type=client_credentials | System-level access |
| 3 | Token has `system/*` scopes | Full read access for bulk export |

**Flow 3: Token Refresh**

| Step | What Happens | Why |
|------|--------------|-----|
| 1 | Access token expires (5 min) | Short-lived for PHI security |
| 2 | App sends refresh_token to `/auth/token` | Get new access token without re-login |
| 3 | Old tokens revoked, new pair issued | Rotation prevents replay |

### Use Cases

**Use Case 1: Member Health App**
- A patient downloads a health app, logs in
- App gets `patient/Patient.read patient/Observation.read` scopes
- Can only see THEIR data (patient context binding)

**Use Case 2: Provider EHR Integration**
- Provider system authenticates with `user/*.read`
- Can access data for patients in their panel

**Use Case 3: Payer Bulk Export**
- Backend system uses client_credentials
- Gets `system/$export` scope
- Triggers bulk data export of all patients

### Registered Demo Clients

| Client ID | Type | Flow | Scopes |
|-----------|------|------|--------|
| `patient-app-001` | Patient App | authorization_code + PKCE | patient/*.read |
| `provider-app-001` | Provider EHR | authorization_code | user/*.read |
| `backend-system-001` | Payer System | client_credentials | system/*.read, $export |

### Security Features
- PKCE (S256) mandatory for public clients
- 5-minute access token expiry
- Scope enforcement per client registration
- Token revocation
- Audit logging (CMS compliance)

### How to Run
```bash
python slap_server.py --port 9000
```

---

## Component 3: FITE (`fhir_server.py` — Port 8080)

### What It Does
**FHIR Integration & Translation Engine** — the API gateway that serves FHIR resources to consumer applications. Handles FHIR search, read, $everything, and $export operations. Enforces IG-specific rules and validates requests.

### Why It Exists
CMS requires payers to expose data through standard FHIR R4 APIs. FITE is the single entry point — apps NEVER access Firely/HealthLake directly. This separation provides security isolation, IG enforcement, and response shaping.

### Architecture Role
**Onyx-owned** — responsible for API correctness, IG enforcement, and runtime performance.

### Endpoints

| Method | Endpoint | Description | CMS API |
|--------|----------|-------------|---------|
| GET | `/fhir/metadata` | CapabilityStatement | Required |
| GET | `/fhir/Patient` | Search patients | Patient Access |
| GET | `/fhir/Patient/{id}` | Read single patient | Patient Access |
| GET | `/fhir/Patient/{id}/$everything` | Full patient compartment | Patient Access |
| GET | `/fhir/Encounter?patient={id}` | Patient encounters | Patient Access |
| GET | `/fhir/Condition?patient={id}&clinical-status=active` | Active conditions | Patient Access |
| GET | `/fhir/Observation?patient={id}&category=laboratory` | Lab results | Patient Access |
| GET | `/fhir/MedicationRequest?patient={id}` | Medications | Patient Access |
| GET | `/fhir/Procedure?patient={id}` | Procedures | Patient Access |
| GET | `/fhir/AllergyIntolerance?patient={id}` | Allergies | Patient Access |
| GET | `/fhir/ExplanationOfBenefit?patient={id}` | Claims/EOB | Patient Access |
| GET | `/fhir/$export` | Bulk Data Export | Provider Access |

### Search Parameters Supported

| Resource | Parameters |
|----------|-----------|
| Patient | `_id`, `name`, `gender`, `birthdate` |
| Encounter | `patient`, `status`, `date` |
| Condition | `patient`, `clinical-status`, `code` |
| Observation | `patient`, `category`, `code`, `date` |
| MedicationRequest | `patient`, `status` |
| Procedure | `patient`, `code`, `date` |
| AllergyIntolerance | `patient`, `clinical-status` |
| ExplanationOfBenefit | `patient` |

### Use Cases

**Use Case 1: Patient Views Their Health Record**
```bash
# Get patient demographics
curl http://localhost:8080/fhir/Patient/4d9da5d3-358a-df49-9797-5bf5630206c0

# Get all their data
curl http://localhost:8080/fhir/Patient/4d9da5d3-358a-df49-9797-5bf5630206c0/\$everything
```

**Use Case 2: Provider Checks Lab Results**
```bash
# Get lab observations for a patient
curl "http://localhost:8080/fhir/Observation?patient=4d9da5d3&category=laboratory"
```

**Use Case 3: Payer Bulk Export**
```bash
# Get bulk data manifest (all resource types as NDJSON)
curl http://localhost:8080/fhir/\$export
```

**Use Case 4: Claims History**
```bash
# Get EOBs (explanation of benefits) for a patient
curl "http://localhost:8080/fhir/ExplanationOfBenefit?patient=4d9da5d3"
```

### How FITE Validates Requests (integration with SLAP)
```
1. App sends: GET /fhir/Patient with Authorization: [REDACTED_TOKEN]
2. FITE extracts token from header
3. FITE calls SLAP: POST http://localhost:9000/auth/introspect {token: "..."}
4. SLAP responds: {active: true, patient: "4d9da5d3", scope: "patient/Patient.read"}
5. FITE enforces: only return data for patient "4d9da5d3"
6. FITE returns: FHIR Bundle (searchset)
```

### How to Run
```bash
python fhir_server.py --port 8080 --data ./fhir_output/ndjson
```

---

## Component 4: Firely (Simulated inside FITE)

### What It Does
**.NET FHIR server backed by MongoDB** — stores and queries FHIR resources. In our implementation, Firely's role is simulated by the in-memory FHIR store inside FITE.

### Why It Exists
The production system needs a persistent FHIR-native database that supports:
- FHIR search with complex parameters
- Resource versioning
- Transaction bundle processing
- Profile validation

### Architecture Role
**Shared** — Abacus writes data into it, Onyx exposes it through FITE. No one accesses Firely directly.

### How It's Simulated
- FITE loads NDJSON files into memory at startup
- Provides search, read, and $everything operations
- Transaction bundles would be processed here in production

### Production vs. Our Implementation

| Feature | Production Firely | Our Simulation |
|---------|-------------------|----------------|
| Storage | MongoDB | In-memory dict |
| Search | Full FHIR search | Basic parameter matching |
| Validation | Profile validation | Structural checks |
| Versioning | Resource versions | No versioning |
| Scale | Multi-node | Single process |

### Use Case: Loading Data into Firely
In production:
```bash
# POST a transaction bundle to Firely
curl -X POST http://firely:4080/fhir \
  -H "Content-Type: application/fhir+json" \
  -d @bundle_Alberto639_Berge125.json
```

In our simulation: FITE reads NDJSON files at startup (same data, different loading mechanism).

---

## Component 5: HealthLake (NDJSON Export Ready)

### What It Does
**AWS managed FHIR store** — alternative/coexisting backend to Firely. Serverless, scales automatically, integrated with AWS services.

### Why It Exists
Some clients prefer a fully managed solution (no MongoDB operations). HealthLake provides:
- Automatic scaling
- Built-in $export
- AWS IAM integration
- S3-based bulk import

### Architecture Role
**Shared** — same as Firely. Coexists or replaces depending on client preference.

### How It's Simulated
- The pipeline generates `NDJSON` files ready for HealthLake `$import`
- FITE's `$export` endpoint returns a manifest mimicking HealthLake's async export

### Use Case: Bulk Import into HealthLake
```bash
# In production: upload NDJSON to S3, then trigger import
aws s3 cp ./fhir_output/ndjson/ s3://my-bucket/fhir-import/ --recursive

aws healthlake start-fhir-import-job \
  --datastore-id "abc123" \
  --input-data-config S3Uri="s3://my-bucket/fhir-import/" \
  --job-output-data-config S3Uri="s3://my-bucket/fhir-output/"
```

Our pipeline produces the exact NDJSON format HealthLake expects.

---

## Component 6: Onyx Insights (`onyx_insights_server.py` — Port 9001)

### What It Does
**Monitoring, analytics, and operational visibility** — tracks pipeline executions, API performance, auth events, and triggers alerts when something goes wrong.

### Why It Exists
CMS requires operational auditability. The team needs visibility into:
- Did the pipeline run successfully?
- Are APIs performing within SLA?
- Are auth failures indicating an attack?
- Which resources have validation issues?

### Architecture Role
**Onyx-owned** — responsible for observability across the entire platform.

### Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/metrics/summary` | High-level system health overview |
| GET | `/metrics/pipeline` | Pipeline run history (status, duration, errors) |
| GET | `/metrics/api` | API request stats (latency P50/P95, error rates) |
| GET | `/metrics/auth` | Auth success/failure rates by client |
| GET | `/metrics/resources` | FHIR resource counts + validation rates |
| GET | `/alerts` | Currently triggered alerts |
| POST | `/alerts/rules` | Define alert thresholds |
| POST | `/events` | Receive events from other components |
| GET | `/audit` | CMS compliance audit trail |
| GET | `/health` | Component health status |

### Use Cases

**Use Case 1: Pipeline Monitoring**
```bash
# Check if today's Claims pipeline succeeded
curl http://localhost:9001/metrics/pipeline
# Returns: run_id, family, status, duration, records_processed, errors
```

**Use Case 2: API Performance Tracking**
```bash
# Check API latency and error rates
curl http://localhost:9001/metrics/api
# Returns: endpoint, request_count, avg_latency_ms, p95_latency_ms, error_rate
```

**Use Case 3: Security Alert**
```bash
# Check if auth failure rate exceeded threshold
curl http://localhost:9001/alerts
# Returns: alert_id, rule, severity, message, triggered_at
```

**Use Case 4: CMS Audit**
```bash
# Pull audit trail for compliance review
curl http://localhost:9001/audit
# Returns: timestamp, actor, action, resource, outcome
```

**Use Case 5: Event Ingestion (from SLAP/FITE)**
```bash
# SLAP pushes auth events to Insights
curl -X POST http://localhost:9001/events \
  -d '{"source": "slap", "type": "token_issued", "client_id": "patient-app-001"}'
```

### How to Run
```bash
python onyx_insights_server.py --port 9001
```

---

## Component 7: MDP (`mdp_server.py` — Port 9002)

### What It Does
**Metadata & Discovery Platform** — central config store, service registry, IG registry, and workflow definitions. Think of it as the "brain" that knows where everything is and how it's configured.

### Why It Exists
In a distributed system with multiple services, you need:
- A place to discover other services (where is SLAP? what port?)
- Centralized configuration (what's the token expiry? which IGs are active?)
- Workflow definitions (what tasks run for Claims? what schedule?)
- Environment management (are we in dev or prod? which features are on?)

### Architecture Role
**Onyx-owned** — responsible for configuration, registry, and service discovery.

### Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/services` | List all registered services |
| GET | `/services/{name}` | Get service details (host, port, health) |
| POST | `/services/register` | Register a new service instance |
| GET | `/config/{component}` | Get all config for a component |
| GET | `/config/{component}/{key}` | Get specific config value |
| PUT | `/config/{component}/{key}` | Update config value |
| GET | `/igs` | List active Implementation Guides |
| GET | `/igs/{name}` | IG details (profiles, search params) |
| GET | `/workflows` | List all Databricks workflows |
| GET | `/workflows/{family}` | Workflow config (tasks, schedule, SAM tables) |
| GET | `/environment` | Current environment + feature flags |
| GET | `/health` | Aggregated health (pings all services) |
| GET | `/dependencies` | Component dependency graph |

### Use Cases

**Use Case 1: Service Discovery**
```bash
# Where is FITE running?
curl http://localhost:9002/services/fite
# Returns: {name: "fite", host: "localhost", port: 8080, status: "healthy"}
```

**Use Case 2: Configuration Lookup**
```bash
# What's the token expiry for SLAP?
curl http://localhost:9002/config/slap/access_token_expiry
# Returns: {key: "access_token_expiry", value: 300}

# What are all FITE configs?
curl http://localhost:9002/config/fite
```

**Use Case 3: IG Registry**
```bash
# What IGs are active?
curl http://localhost:9002/igs
# Returns: US Core 6.1.0, CARIN BB 2.0.0, Da Vinci Plan-Net 1.1.0, ...

# What profiles does CARIN BB define?
curl http://localhost:9002/igs/carin-bb
# Returns: profiles, required_search_params, resource_types
```

**Use Case 4: Workflow Definitions**
```bash
# What does the Claims workflow do?
curl http://localhost:9002/workflows/claims
# Returns: tasks (extract, transform, upload, upsert), schedule, SAM tables, owner
```

**Use Case 5: Health Check (All Services)**
```bash
# Are all services healthy?
curl http://localhost:9002/health
# Returns: {overall: "healthy", services: {slap: "up", fite: "up", ...}}
```

**Use Case 6: Dependency Graph**
```bash
curl http://localhost:9002/dependencies
# Returns: nodes + edges showing how components connect
```

### How to Run
```bash
python mdp_server.py --port 9002
```

---

## Complete Startup Sequence

```bash
#!/bin/bash
# start_all.sh — Launch the full InterOp platform

echo "=== InterOperability with Onyx — Starting All Components ==="

# Step 1: Generate FHIR data (if not already done)
if [ ! -d "./fhir_output" ]; then
    echo "[1/5] Running data pipeline..."
    python interop_pipeline.py --input ./source_data --output ./fhir_output
fi

# Step 2: Start MDP first (others register with it)
echo "[2/5] Starting MDP (Metadata & Discovery)..."
python mdp_server.py --port 9002 &
sleep 1

# Step 3: Start SLAP (auth must be up before FITE)
echo "[3/5] Starting SLAP (SMART Auth)..."
python slap_server.py --port 9000 &
sleep 1

# Step 4: Start FITE (FHIR API)
echo "[4/5] Starting FITE (FHIR API)..."
python fhir_server.py --port 8080 --data ./fhir_output/ndjson &
sleep 1

# Step 5: Start Onyx Insights (monitoring)
echo "[5/5] Starting Onyx Insights (Monitoring)..."
python onyx_insights_server.py --port 9001 &
sleep 1

echo ""
echo "=== All services running ==="
echo "  MDP:           http://localhost:9002"
echo "  SLAP:          http://localhost:9000"
echo "  FITE:          http://localhost:8080"
echo "  Onyx Insights: http://localhost:9001"
echo ""
echo "  Quick test:    curl http://localhost:9002/health"
echo "  FHIR test:     curl http://localhost:8080/fhir/Patient"
echo "  Auth test:     curl http://localhost:9000/.well-known/smart-configuration"
```

---

## Request Flow — End to End

### Scenario: Patient views their lab results in a mobile app

```
Step 1: App → MDP (:9002)
        GET /services/slap
        → Discovers SLAP is at localhost:9000

Step 2: App → SLAP (:9000)
        GET /auth/authorize?client_id=patient-app-001&scope=patient/Observation.read
        → User logs in, consents
        → Redirect with auth code

Step 3: App → SLAP (:9000)
        POST /auth/token (code + PKCE verifier)
        → Returns: access_token (5 min), refresh_token, patient_id

Step 4: App → FITE (:8080)
        GET /fhir/Observation?patient={id}&category=laboratory
        Authorization: [REDACTED_TOKEN]

Step 5: FITE → SLAP (:9000)
        POST /auth/introspect {token: "at_xxx"}
        → Returns: {active: true, patient: "4d9da5d3", scope: "patient/Observation.read"}

Step 6: FITE → FHIR Store (in-memory)
        Search Observations for patient, filter by category=laboratory
        → Returns matching resources

Step 7: FITE → App
        Returns: FHIR Bundle (searchset) with lab results

Step 8: FITE → Onyx Insights (:9001)
        POST /events {type: "api_request", endpoint: "/Observation", latency: 45ms}
        → Metrics recorded
```

---

## CMS Compliance Mapping

| CMS Requirement | Component | Implementation |
|-----------------|-----------|----------------|
| Patient Access API | FITE + Pipeline | US Core resources served via /fhir/Patient/$everything |
| Claims Data (EOB) | Pipeline + FITE | CARIN BB ExplanationOfBenefit via /fhir/ExplanationOfBenefit |
| Provider Directory | FITE (ready) | Da Vinci Plan-Net profiles (IG registered in MDP) |
| Payer-to-Payer | SLAP + FITE | Backend Services auth + $member-match |
| Prior Authorization | Architecture ready | Da Vinci PAS $submit (IG registered in MDP) |
| Bulk Data Export | FITE | GET /fhir/$export → NDJSON manifest |
| SMART on FHIR | SLAP | Standalone Launch, EHR Launch, Backend Services |
| PKCE Required | SLAP | S256 challenge verification |
| Audit Trail | Insights | GET /audit → all access events logged |
| Scope Enforcement | SLAP + FITE | Tokens carry scopes, FITE enforces per-patient access |

---

## Dependencies

| Component | External Dependencies |
|-----------|----------------------|
| interop_pipeline.py | `pandas` |
| slap_server.py | None (stdlib only) |
| fhir_server.py | None (stdlib only) |
| onyx_insights_server.py | None (stdlib only) |
| mdp_server.py | None (stdlib only) |

```bash
# One-time setup:
pip install pandas
```

---

## Port Map

| Port | Service | Owner |
|------|---------|-------|
| 8080 | FITE (FHIR API) | Onyx |
| 9000 | SLAP (Auth) | Onyx |
| 9001 | Onyx Insights (Monitoring) | Onyx |
| 9002 | MDP (Config & Discovery) | Onyx |

---

## Component 8: De-Identification Gate (`pipeline/deid_engine.py`)

HIPAA Safe Harbor (45 CFR 164.514(b)(2)) and Expert Determination (b)(1). Splits ingest into an **identified CMS path** (SLAP/FITE/Firely) and a **de-identified analytics path** (Databricks Gold, Fabric, logs, LLMs). HMAC tokens require `DEID_TOKEN_PEPPER` from a secret store — empty pepper fails closed. Never logs raw field values.

## Component 9: Master Data Management (`pipeline/mdm_engine.py`)

AHIMA Information Governance + ISO 8000 + HL7 Patient Administration. Golden records for member, provider, organization, coverage with deterministic/probabilistic match, survivorship, and a tokenized crosswalk. PVD golden IDs must exist before Claims references.

## Component 10: Dual Engine — Databricks ║ Fabric (`pipeline/fabric_benchmark.py`)

Same `deid_sam` contract on both engines. Compares elapsed time and estimated USD (DBU vs CU) per million rows. Databricks remains the CMS critical path; Fabric is the bake-off and Gold/BI path. OneLake shortcuts only the de-id prefix.

## Component 11: AI Observability (`observability/ai_observer.py`)

Cross-stack SRE brain: OTel traces, job/API/auth/deploy metrics, structured de-id logs, plus Claude/GPT RCA and anomaly explanation via Unity AI Gateway. Rejects payloads containing identifier keys. Distinct from Onyx Insights (CMS filings).

## Component 12: DevOps & CI/CD (`.gitlab-ci.yml`, `databricks.yml`, `scripts/ci/`)

### What It Does
Automates validate → test → security → build → deploy for every merge. Ensures no CMS-critical code reaches stage/prod without pytest green, FHIR baseline validation, and infra lint (Terraform, Helm, Databricks Asset Bundle).

### Why It Exists
CMS Jan 2027 deadline requires repeatable, auditable releases. Manual-only deploys do not scale across six workflow families, three ingestion rails, and EKS runtime — CI/CD is the quality gate between learning and production.

### Architecture Role
**Shared Platform/DevOps** — gates both Abacus (DAB deploy, pipeline tests) and Onyx (Helm/Seiji, smoke tests).

### Pipeline Stages

| Stage | Key Jobs | Purpose |
|-------|----------|---------|
| validate | lint, configs, terraform, helm, bundle-validate | Catch syntax/config errors early |
| test | pytest, fhir-baseline | Prove pipeline + unit logic |
| security | phi-scan, secrets-scan | Block PHI literals and leaked keys |
| build | fsi-image (manual) | Versioned FSI container |
| deploy-stage | DAB stage, Seiji stage (manual) | Soak before prod |
| deploy-prod | DAB prod, Seiji prod (manual) | CMS go-live with ticket |

### Local CI

```bash
cd Training/onyx-interop
./scripts/ci/run_ci_local.sh
```

### Full runbook
See [docs/DEVOPS_CICD.md](Training/onyx-interop/docs/DEVOPS_CICD.md)

---

## Component 13: AI Governance & Evaluation (`pipeline/ai/governance_metrics.py`)

### What It Does
Implements the **metrics-driven AI governance foundation** from the AI Governance MVP session: MLflow-style interaction tracing, **daily batch** computation of hallucination / bias / trustworthiness metrics, and reporting against a controlled query set (Synthea + golden eval questions).

### Why It Exists
Leadership aligned on: *"Governance = measurement of AI efficacy"* — not a broad backlog of duplicate controls. Phase 4 agents must ship with **repeatable, traceable metrics** before client-facing deployment. CCA working session reinforced: **define metrics early** to reduce hallucinations.

### Architecture Role
**Onyx AI Engineering (+ Abacus RAG)** — post-interaction batch pipeline; complements Unity AI Gateway (real-time policy) and Component 11 AI Observability (RCA on de-id telemetry).

### Phased metrics

| Phase | Metrics | Cadence |
|-------|---------|---------|
| 1 | Hallucination rate (alpha) | Daily batch |
| 2 | Bias, trustworthiness | Daily batch |
| 3 | Real-time embedded, drift, lineage | Future |

### Core flow

```
Agent interaction → Unity AI Gateway trace → MLflow → Delta interaction_traces
    → Daily job: governance_metrics → Delta metric_results → Notebook/CSV report
```

### Deprioritized (per governance session — do not duplicate)

- Standalone PHI screening → Gateway PII mask + HIPAA perimeter
- Governance-only de-ID workflows → Use controlled golden set on de-id summaries
- Custom RBAC → Unity Catalog + SLAP
- Version snapshots → GitLab CI + DAB artifacts

### CCA adjacency (separate product, shared platform)

Medical record summarization + DRG evidence is **not CMS interop scope** but reuses this component for eval. UI ownership, rules engine build-vs-buy, and Replit PDLC remain **leadership decisions** — see [AI_GOVERNANCE_ALIGNMENT.md](Training/onyx-interop/docs/AI_GOVERNANCE_ALIGNMENT.md).

### How to Run (local)

```bash
cd Training/onyx-interop
python3 pipeline/ai/governance_metrics.py --traces data/governance/sample_traces.json
cat data/governance/metrics_report.json
```

Config: `configs/ai/governance_metrics.yaml`

---

## Component 14: CMS-0057 Auth Paths (`configs/mdp/auth_paths.json`)

### What It Does
Documents and configures the **three distinct authentication paths** mandated by CMS-0057 — Patient Access (PAA), Provider Access (PVA), and Payer-to-Payer (P2P) — all converging on shared SLAP → FITE → Firely runtime but with different IGs, scopes, and auth models.

### Why It Exists
Production Onyx serves three API audiences with one FHIR store. Mixing auth paths (e.g., a member SMART token on `/pdexv2`) is a compliance and security failure. The auth-path diagram requires explicit route + scope binding at SLAP and FITE.

### Architecture Role
**Onyx runtime** — SLAP issues tokens; FITE routes by path; Apigee fronts machine-auth paths (PVA/P2P).

### Three paths

| Path | Auth model | FITE route | IGs | Actor |
|------|------------|------------|-----|-------|
| **PAA** | Member SAML → SMART PKCE | `/fhir` | US Core, CARIN BB | Member via third-party app |
| **PVA** | `client_credentials` (Backend Services) | `/atr-consumer` | PDex, US Core | External provider system |
| **P2P** | `client_credentials` + PDex scope | `/pdexv2` | PDex | External payer |

### Shared vs different

```
Shared:    SLAP + FITE + Firely
Different: IGs, scopes, gateway (Apigee for PVA/P2P), auth (member vs machine)
```

### How to Use

```bash
cat Training/onyx-interop/configs/mdp/auth_paths.json | python3 -m json.tool
# Read full runbook:
# Training/onyx-interop/docs/CMS0057_AUTH_PATHS.md
```

Local ports: PAA `:9000`, PVA `:9003`, P2P `:9004` (when reference services running).

---

## Component 15: ePA Option A/B (`docs/EPA_OPTION_A_B.md`)

### What It Does
Implements **Electronic Prior Authorization** via two deployment patterns sharing a common ingress: Provider EHR → AWS ALB → **APISIX** → CDS Service (`epa-appsvc`) with **dapr** sidecar.

### Why It Exists
Payers integrate PAS vendors differently — legacy batch (Gainwell/SFTP) vs real-time API (Wellmark/Jiva). CMS-0057 ePA requires CRD/DTR/PAS at point of care; the architecture must support both without duplicating FHIR generation.

### Option A — Gainwell (batch)

```
Routing-DIR → AWS Transfer SFTP → Gainwell PAS → ClaimResponse batch (837/275/CSV)
    → Databricks workflows → Firely
```

### Option B — Wellmark (real-time)

```
Auth table + 13 decision tables → Jiva PAS APIs + InterQual/Evicore DTR
    → Event notification → FHIR Subscription callback → Provider EHR
```

### Mandatory deploy order

```
onyx.provision → onyx.epa → onyx.deploy
    → databricks.provision → databricks_continuous_deployment → databricks.onyx
```

Each step gates the next — do not deploy Databricks ePA workflows before APISIX/CDS ingress is live.

### How to Use

```bash
curl -s http://localhost:9005/cds-services 2>/dev/null | head -5
grep -n cds-services $HOME/OnyxInterop/epa_burden_reduction_service.py | head -3
```

Full runbook: [EPA_OPTION_A_B.md](Training/onyx-interop/docs/EPA_OPTION_A_B.md)

---

## Component 16: Cambia BigQuery Ingestion — Rail D (`docs/CAMBIA_BIGQUERY_INGESTION.md`)

### What It Does
Cross-cloud **Rail D** connector: pulls Cambia pharmacy claims from **GCP BigQuery** into **AWS S3** as NDJSON via an **EKS CronJob** — no stored GCP service-account keys.

### Why It Exists
Partner data lives in GCP; Abacus primary PHI lake is AWS. XPORT-2596 defines a keyless auth chain (IRSA → WIF → BigQuery) and a strict S3 handoff so Bronze Databricks (`ng-pipelines-cambia`) remains a separate workflow.

### Auth chain (no stored credentials)

```
EKS IRSA → AWS STS → Google Workload Identity Federation
    → iamcredentials impersonation → BigQuery access token (1h TTL, memory only)
```

**Critical:** Export IRSA credentials before initializing Google auth libraries; pass GCP project explicitly.

### Load modes

| Mode | Purpose | Fail-closed rule |
|------|---------|------------------|
| **incremental** | Daily delta on `received_at` watermark | No checkpoint → abort (never auto-full) |
| **full** | Initial or manual backfill | Operator-triggered |
| **refresh** | Monthly correctness | Required — BQ change history unavailable to Abacus |
| **replay** | Operator window re-export | Writes to `replay/` prefix |

### S3 contract

| Bucket | Content |
|--------|---------|
| **PHI data-lake** | NDJSON under `raw/bigquery-claims/` (atomic staging publish) |
| **Metadata (non-PHI)** | Checkpoints, manifests, run status |

Connector **ends at S3** — Bronze Autoloader is out of scope for this service.

### Forbidden logging

Never log row values, claim/member/prescriber IDs, drug names, PHI query predicates, or access tokens — only `run_id`, counts, job id, safe error category.

### How to Use

```bash
grep -n 'IRSA\|Rail D\|Fail closed' Training/onyx-interop/docs/CAMBIA_BIGQUERY_INGESTION.md | head -10
```

---

## Summary

This implementation covers the **complete interoperability stack**:

1. **Data Pipeline** — De-ID → MDM → CSV → FM → SAM → FHIR (9,997 resources)
2. **SLAP** — OAuth2/SMART authentication with 3 flows
3. **FITE** — FHIR R4 API with search, read, $everything, $export
4. **Firely** — Simulated FHIR store (in-memory)
5. **HealthLake** — NDJSON export ready for AWS $import
6. **Onyx Insights** — Monitoring, metrics, alerts, audit
7. **MDP** — Service registry, config, IGs, workflows, dependencies
8. **De-ID Gate** — HIPAA Safe Harbor / Expert Determination (`pipeline/deid_engine.py`)
9. **MDM** — AHIMA / ISO 8000 golden records (`pipeline/mdm_engine.py`)
10. **Fabric ║ Databricks** — parallel de-id processing + cost/speed (`pipeline/fabric_benchmark.py`)
11. **AI Observability** — RCA/anomaly models on de-id telemetry (`observability/ai_observer.py`)
12. **DevOps & CI/CD** — GitLab CI, DAB deploy, Seiji gates, local `run_ci_local.sh`
13. **AI Governance & Evaluation** — MLflow traces, hallucination/bias/trust metrics, daily batch (`governance_metrics.py`)
14. **CMS-0057 Auth Paths** — PAA/PVA/P2P route + scope config (`auth_paths.json`)
15. **ePA Option A/B** — APISIX ingress, Gainwell batch vs Wellmark real-time PAS
16. **Cambia BigQuery Ingest (Rail D)** — EKS CronJob + IRSA/WIF → S3 NDJSON handoff

All components are **runnable locally** with just Python — giving engineers hands-on experience with the exact same architecture they'll work with in production. **Run `./scripts/ci/run_ci_local.sh` before every push.**

---

## PDF Alignment (Governance + CCA Sessions)

| Source document | Key concern | Solution response |
|-----------------|-------------|-------------------|
| AI Governance MVP | MLflow + 3 core metrics, daily batch | Component 13, Phase 4E |
| AI Governance MVP | Deprioritize duplicate PHI/RBAC/version controls | Gateway + UC + GitLab |
| CCA Dev Milestones | Metrics early, data before AI | Step 8 gate; Phase 1 before Phase 4 |
| CCA Dev Milestones | UI ownership, Replit, SecOps, implementation | [AI_GOVERNANCE_ALIGNMENT.md](Training/onyx-interop/docs/AI_GOVERNANCE_ALIGNMENT.md) decision log |
| CMS-0057 Auth Paths diagram | PAA/PVA/P2P distinct auth; shared SLAP/FITE/Firely | Component 14, `auth_paths.json`, [CMS0057_AUTH_PATHS.md](Training/onyx-interop/docs/CMS0057_AUTH_PATHS.md) |
| ePA Option A/B diagram | APISIX ingress; Gainwell SFTP vs Wellmark real-time; deploy order | Component 15, [EPA_OPTION_A_B.md](Training/onyx-interop/docs/EPA_OPTION_A_B.md) |
| Cambia BigQuery Ingestion (XPORT-2596) | Rail D cross-cloud; IRSA/WIF; fail-closed checkpoint; monthly refresh | Component 16, [CAMBIA_BIGQUERY_INGESTION.md](Training/onyx-interop/docs/CAMBIA_BIGQUERY_INGESTION.md) |

---

## Proficiency Guarantee Framework

> **Learning path:** Follow [LEARN_FROM_STEP_1.md](Training/LEARN_FROM_STEP_1.md) — 16-week Learn → Do → Check → Teach curriculum aligned to this implementation. Do not skip Step 1.

Completing this implementation end-to-end — and running the **Script** segment attached to each of the 553 interview Q&A entries — is designed to guarantee working proficiency (not just conceptual familiarity) in eight roles:

| Role | What You Will Do in This Implementation | Exit Criteria |
|------|------------------------------------------|---------------|
| **FHIR Engineer** | Map SAM → US Core/CARIN BB/Da Vinci resources; validate bundles; operate Firely/FSI; implement CMS-0057 APIs | `validate_fhir_output.py` pass; IG validation zero errors; `$everything` and `$export` work |
| **Data Engineer** | Build Raw→FM→SAM→Extract on Databricks; Autoloader medallion; Delta OPTIMIZE/VACUUM; multi-rail convergence | Six workflow families green; Bronze/Silver/Gold lag < SLA; SAM merge idempotent |
| **Kafka Engineer** | Design Rail B event transport (API Gateway→Lambda→Kafka/MSK→Bronze); schema contracts; DLQ/replay | Producer/consumer scripts run; lag alerts wired; zero schema violation in prod |
| **AI Engineer** | RAG indexes, MLflow traces, governance metrics, Unity AI Gateway, MCP tools, agents | Golden eval >85%; daily hallucination batch green; gateway blocks PHI |
| **Forward Deployed Engineer** | Terraform/EKS/Helm/Seiji deploys; customer onboarding; incident runbooks; Phase 0 checklists | Deploy dev stack solo; restore from incident in <4h; customer sign-off checklist |
| **Intermediate Associate Programmer** | Python transformers, bash automation, SQL MERGE/RLS, unit tests, CI pipelines | `pytest tests/` green; PRs pass lint; can patch `*_transformer.py` independently |
| **Associate Solution Architect** | Phase planning, Abacus/Onyx ownership split, CMS compliance traceability, hybrid cloud ADRs | Can whiteboard 3-rail ingestion + AI layer; map every CMS rule to component |
| **DevOps Engineer** | GitLab CI, DAB deploy, Seiji canary, secret management, CMS go-live checklist | `run_ci_local.sh` green; explain every CI stage; stage→prod gate drill |

### Phase-to-Role Matrix

```
Phase 0 ──► Solution Architect, Forward Deployed, Programmer, DevOps (local CI)
Phase 1 ──► Data Engineer, FHIR Engineer, Kafka Engineer (Rails A/B/C + APIs)
Phase 2 ──► FHIR Engineer, Solution Architect (CMS-0057 advanced APIs)
Phase 3 ──► Forward Deployed, Programmer, DevOps (CI/CD, Seiji, hardening)
Phase 4 ──► AI Engineer, Data Engineer (RAG, agents, governance)
```

### How to Use Scripts

1. Read **Answer** + **Example** for interview context.
2. Run **How to Check** commands to verify your environment.
3. Execute the **Script** block — each is tagged with target role(s).
4. If Script fails, follow **How to Fix**, then re-run until green.
5. Track completion: `grep -c "**Script:**" Healthcare_Interop_Interview_Cheat_Sheet.md` should equal 553.

Script source generator (regenerate after Q&A edits): `Training/tmp/add_scripts_to_cheat_sheet.py`

Glossary of all solution keywords: [Healthcare_Interop_Interview_Cheat_Sheet.md — Glossary tab](/Users/ashishsingh/Interview/Healthcare_Interop_Interview_Cheat_Sheet.md#glossary) (120+ terms, 16 categories)
