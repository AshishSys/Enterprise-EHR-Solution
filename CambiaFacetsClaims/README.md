# Cambia Facets Claims — Complete Implementation Guide

> **Four proficiency pillars:** E2E Implementation · Facets/TriZetto SME · On-Prem→Cloud Migration · Postman API Role

## Proficiency Pillars

| Pillar | You prove it by... | Key artifacts |
|--------|-------------------|---------------|
| **P1 — E2E Implementation** | Owning CDC → medallion → downstream delivery | phase0 scripts, Databricks job chain, run_ci_local.sh |
| **P2 — Facets/TriZetto SME** | Speaking CMC tables, CLCL lifecycle, medical/dental grain | CMC_CLCL_CLAIM joins, status codes, volume profiles |
| **P3 — On-Prem→Cloud Migration** | Phased VPN/CDC/cutover with rollback gates | migration_cutover_checklist.sh, parallel-run parity |
| **P4 — Postman API Role** | Validating orchestration + FHIR contracts before promotion | Postman collections, newman smoke in CI |

## E2E Architecture

```
On-Prem TriZetto Facets (SQL Server CDC replica)
        │  [P3: VPN — Palo Alto → cambia-facets-networking]
        ▼
facets-core CDC → encrypted JSON + manifest  [P1: Step Functions + Batch]
        │  [P3: SFTP landing → cambia02 raw S3]
        ▼
Bronze SCD2 (44+ CMC_* tables) → Silver timeline → Dual Gold FM  [P1+P2]
        │  [P4: Postman orchestration + FHIR smoke]
        ▼
SAM/FHIR · Snowflake · Reltio MDM
```

## Quick Start

```bash
cd Training/facets-claims

# P1 — E2E implementation baseline
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/ci/run_ci_local.sh

# P3 — Migration cutover gate
./scripts/migration_cutover_checklist.sh

# P4 — Postman API smoke (requires Newman + env file)
./scripts/postman_smoke_check.sh
```

## Key Resources

| Resource | Pillar | Purpose |
|----------|--------|---------|
| [LEARN_FROM_STEP_1.md](Training/LEARN_FROM_STEP_1.md) | All | Day-by-day path aligned to 4 pillars |
| [Interview Cheat Sheet](/Users/ashishsingh/Interview/Cambia_Facets_Claims_Interview_Cheat_Sheet.md) | All | 553 Q&A with pillar tags |
| [POSTMAN_API_ROLE.md](docs/POSTMAN_API_ROLE.md) | P4 | Collections, environments, cutover gates |
| [implementation_details.md](implementation_details.md) | P1+P3 | Component deep dive |
| [Architecture Map](facets-claims-e2e-architecture-map.html) | All | Tabbed reference (4 pillars) |
| [Canvas](/Users/ashishsingh/.cursor/projects/Users-ashishsingh-CambiaFacetsClaims/canvases/cambia-facets-claims.canvas.tsx) | All | Interactive tabbed UI |

## TriZetto Facets SME Quick Reference (P2)

| Code | Meaning |
|------|---------|
| M / H | Medical claim |
| D | Dental claim |
| 11 | Pended |
| 15 | Error |
| 01 | Pre-final |
| 02 | Final |
| 91 | Adjusted |

| Table | Grain |
|-------|-------|
| `CMC_CLCL_CLAIM` | Claim header |
| `CMC_CDML_CL_LINE` | Medical lines |
| `CMC_CDDL_CL_LINE` | Dental lines |
| `CMC_CLST_STATUS` | Status history |
| `CMC_MEME_MEMBER` | Member |
| `CMC_SBSB_SUBSC` | Subscriber |

## Migration Cutover Gates (P3)

1. VPN tunnel stable ≥ 7 days
2. Historical backfill row-count parity (sample periods)
3. Incremental schedule matches on-prem batch timing
4. Bronze SCD2 + gold signature bitmap match
5. Postman smoke green on stg → prod promotion

## Postman Collections (P4)

| Collection | Validates |
|------------|-----------|
| `postman/cambia-facets-claims-smoke.json` | Orchestration manifest + job status |
| `postman/fhir-claims-interop.json` | Interop FHIR Claim reads (75-group filter) |
| `postman/fhir-claims-cdp.json` | CDP full claim set |
| `postman/cambia-facets-cutover-gate.json` | Pre-prod promotion gate (all folders) |
