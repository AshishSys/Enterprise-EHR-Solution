# Onyx Interop — Production Implementation

CMS-compliant healthcare interoperability platform (Abacus/Onyx architecture).

## Quick Start

```bash
# Phase 0: Environment access + production repo clone
./scripts/phase0_access.sh

# Or step-by-step:
./scripts/setup_environment.sh      # venv, access.env, repo-shims, clone repos
./scripts/configure_access.sh       # AWS/Databricks/GitLab/Seiji credentials
./scripts/clone_production_repos.sh # ng-onyx-runtime, onyx-helmsman, etc.
./scripts/setup_repo_shims.sh       # Helm chart shims (Kitchen Sous Chef)
./scripts/phase0_access_checklist.sh

# Phase 0: Local baseline validation
./scripts/run_local_baseline.sh

# Start all runtime services (local)
./scripts/start_all_services.sh

# Dual-engine cost/speed bake-off (de-id SAM only)
./scripts/run_engine_benchmark.sh

# Run acceptance tests
python -m pytest tests/ -v

# DevOps: run full local CI before push (mirrors GitLab pipeline)
chmod +x scripts/ci/run_ci_local.sh
./scripts/ci/run_ci_local.sh
```

See [docs/DEVOPS_CICD.md](docs/DEVOPS_CICD.md) for GitLab CI stages, secrets, and CMS go-live gates.

## Architecture

```
Client Data
    │
    ▼
 De-ID Gate (HIPAA Safe Harbor / Expert Determination)
    ├─ Identified path (CMS APIs only) ──► FM ──► SAM ──► Extract ──► Firely
    │                                                              ↓
    │                                         Consumer Apps → SLAP → FITE
    └─ De-identified path ──► MDM golden ──► Databricks ║ Fabric (parallel)
                              │                         └─ cost/speed bake-off
                              ▼
                     AI Observability (de-id traces/metrics only)
```

## Directory Structure

| Path | Purpose |
|------|---------|
| `terraform/` | AWS infrastructure (S3, EKS, DocumentDB, DynamoDB, API Gateway) |
| `configs/workflows/` | Extract configs per Databricks workflow family |
| `configs/mdp/` | MDP service registry and IG registry |
| `pipeline/` | ETL jobs (ingestion, FM, SAM, extract, transform, load) |
| `helm/` | Kubernetes charts (Firely, SLAP, FITE) |
| `stepfunctions/` | Incremental and FSI bulk orchestration |
| `apis/` | Consumer API Lambda handlers |
| `scripts/` | Setup, validation, and orchestration scripts |
| `tests/` | Acceptance, security, and cross-family dependency tests |
| `monitoring/` | CloudWatch dashboards and CMS metrics reporter |
| `configs/deid/` | HIPAA Safe Harbor 18-identifier rules |
| `configs/mdm/` | AHIMA / ISO 8000 golden-record rules |
| `configs/fabric/` | Fabric workspace + parallel-engine contract |
| `configs/observability/` | AI observability model registry |
| `pipeline/deid_engine.py` | De-identification gate |
| `pipeline/mdm_engine.py` | Member/provider MDM |
| `pipeline/fabric_benchmark.py` | Databricks vs Fabric cost/speed |
| `observability/` | AI RCA / anomaly observer |
| `fabric/` | Fabric notebooks on the de-id SAM contract |

## Service Ports (Local)

| Service | Port |
|---------|------|
| FITE (FHIR API) | 8080 |
| SLAP (Auth) | 9000 |
| Onyx Insights | 9001 |
| MDP | 9002 |
| P2P Member Match | 9004 |
| ePA (CRD/PAS) | 9005 |
| Developer Portal | 9010 |

## CMS API Coverage

- **Phase 1 (CMS-9115):** Patient Access, Provider Directory, Formulary
- **Phase 2 (CMS-0057):** Provider Access, Payer-to-Payer, ePA, PA data in Patient Access
