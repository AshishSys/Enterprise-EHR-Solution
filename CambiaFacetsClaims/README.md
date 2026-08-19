# Cambia Facets Claims — Complete Implementation Guide

> End-to-end Cambia-specific pipeline: On-Prem TriZetto Facets → VPN → CDC → Encrypted Landing → Databricks Medallion → SAM/FHIR + Snowflake

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CAMBIA FACETS CLAIMS (cambia02 tenant)                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────── STAGE 1–2: SOURCE & CDC (facets-core) ──────────────────┐   │
│  │  Facets SQL Server CDC → VPN → Step Functions → Encrypted JSON       │   │
│  │  + manifest.json → intermediate S3                                  │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                              ↓                                              │
│  ┌──────────── STAGE 3: LANDING & BRONZE ───────────────────────────────┐   │
│  │  SFTP landing → NextGen raw S3 → Databricks bronze (44+ SCD2 tables) │   │
│  │  ng-orchestration-service + AIR library                              │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                              ↓                                              │
│  ┌──────────── STAGE 4: SILVER & GOLD ──────────────────────────────────┐   │
│  │  unified timeline → silver.claim_facets* → dual gold FM              │   │
│  │  Interop (filtered) ║ CDP (full 1:1 + signature bitmap)              │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                              ↓                                              │
│  ┌──────────── STAGE 5: DOWNSTREAM ─────────────────────────────────────┐   │
│  │  Onyx SAM/FHIR (CMS-9115) │ Snowflake egress │ Reltio MDM            │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Quick Start

```bash
cd Training/facets-claims

# 1. Architecture trace (5 stages + repos)
./scripts/phase0_architecture_trace.sh

# 2. Repo map and catalog paths
./scripts/phase0_repo_map.sh

# 3. Manifest pattern validation
./scripts/validate_manifest_pattern.sh

# 4. Local CI gate
./scripts/ci/run_ci_local.sh
```

## Key Resources

| Resource | Purpose |
|----------|---------|
| [LEARN_FROM_STEP_1.md](Training/LEARN_FROM_STEP_1.md) | Day-by-day learning path — **start here** |
| [Interview Cheat Sheet](/Users/ashishsingh/Interview/Cambia_Facets_Claims_Interview_Cheat_Sheet.md) | 553 Q&A + Scripts + Glossary |
| [implementation_details.md](implementation_details.md) | Component deep dive |
| [facets-claims-e2e-architecture-map.html](facets-claims-e2e-architecture-map.html) | Interactive architecture map |
| [Architecture Canvas](/Users/ashishsingh/.cursor/projects/Users-ashishsingh-CambiaFacetsClaims/canvases/cambia-facets-claims.canvas.tsx) | Tabbed reference UI |

## Repositories

| Repo | Role |
|------|------|
| `facets-core` | Bespoke CDC — SQL Server → JSON + manifest |
| `facets-infrastructure` | AWS CDC infra (Step Functions, Batch, S3, DynamoDB) |
| `ng-abacus-inbound-infra` | SFTP / connector landing zone |
| `ng-orchestration-service` | Manifest-triggered workflow orchestration |
| `ng-pipelines-cambia` | Bronze/silver/gold Databricks pipelines |
| `ng-abacus-insights-runtime` | AIR library (encryption, SCD2, manifest validation) |
| `ng-pipelines-onyx` | DM 2.0 → FHIR downstream |

## Volumes

| Metric | Value |
|--------|-------|
| Historical claims | ~99M (from 1/1/2017) |
| Historical claim lines | ~250M |
| Nightly batch | 70k–120k claims |
| Incremental window | 500–1,000 tx / 15 min (daytime) |
| Bronze tables (prod) | 420 Facets tables (Jun 2024) |
| JSON files per batch | ~25 + manifest |

## Dual Gold Paths

| Path | Tables | Filtering | Consumer |
|------|--------|-----------|----------|
| **Interop** | `gold.fm_claim`, `gold.fm_claim_item` | 75 groups, Medicare, no dental | SAM → FHIR (CMS-9115) |
| **CDP** | `gold.fm_claim_cambia`, `gold.fm_claim_item_cambia` | None — full silver mapping | Customer data platform |
