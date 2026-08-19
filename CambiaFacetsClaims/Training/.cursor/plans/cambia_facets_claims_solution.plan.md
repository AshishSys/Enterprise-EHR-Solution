---
name: Cambia Facets Claims Solution
overview: Phased learning and implementation guide for Cambia Facets Claims — on-prem TriZetto Facets through VPN, bespoke CDC, Databricks medallion (bronze/silver/gold), dual FM outputs, and downstream SAM/FHIR + Snowflake + Reltio MDM. Tenant cambia02.
todos:
  - id: phase0-learn
    content: "Phase 0: Complete LEARN_FROM_STEP_1 Step 1 — architecture trace, repo map, local CI"
    status: pending
  - id: phase0-cheatsheet
    content: "Phase 0: Work through Cheat Sheet Sections A, C, G (Q1-10, Q29-45, Q113-124)"
    status: pending
  - id: phase1-cdc
    content: "Phase 1: Understand facets-core CDC, manifest contract, CdcGlobals lock, trigger files"
    status: pending
  - id: phase1-bronze
    content: "Phase 1: Bronze SCD2 loads — CMC_CLCL_CLAIM and key tables via AIR library"
    status: pending
  - id: phase2-silver
    content: "Phase 2: Silver unified timeline and claim_facets domain tables"
    status: pending
  - id: phase2-gold
    content: "Phase 2: Dual gold FM — Interop filtered vs CDP full mapping"
    status: pending
  - id: phase3-ops
    content: "Phase 3: Operate 4-hr incremental + nightly batch; troubleshoot Section M scenarios"
    status: pending
  - id: phase4-downstream
    content: "Phase 4: Trace gold → SAM/FHIR, Snowflake egress (XFORM-3515), Reltio MDM cutover"
    status: pending
isProject: true
---

# Cambia Facets Claims — Implementation Plan

## Context

Facets Claims is a **Cambia-specific** pipeline (TriZetto Facets on-prem → Abacus NextGen). Tenant label: **cambia02**. This is not a generic Transporters catalog service — it spans bespoke Facets CDC, SFTP/inbound, orchestration, and XFORM pipelines.

| Resource | Purpose |
|----------|---------|
| [README.md](../../README.md) | Architecture overview, quick-start |
| [implementation_details.md](../../implementation_details.md) | 5-stage component deep dive |
| [LEARN_FROM_STEP_1.md](../LEARN_FROM_STEP_1.md) | Day-by-day learning path |
| [Cheat Sheet](/Users/ashishsingh/Interview/Cambia_Facets_Claims_Interview_Cheat_Sheet.md) | 553 Q&A + Scripts + Glossary |
| [Architecture Map](../../facets-claims-e2e-architecture-map.html) | Tabbed HTML reference |
| Scope note PDF | Source context and volumes |

## Proficiency Guarantee

| Role | Primary Sections | Exit Proof |
|------|------------------|------------|
| Associate Solution Architect | A, C, H, L, M, AB | Whiteboard 5-stage + dual gold |
| Data Engineer | D, G, O, P, Q, T, U | SQL across medallion layers |
| FHIR Engineer | E, H | Dental filter → SAM path |
| Forward Deployed Engineer | F, I, S, Y | Incident scenario from Section M |
| DevOps Engineer | Z | run_ci_local.sh green |
| Integration Engineer | G, P, O | Manifest + SFTP trigger E2E |

## Phases

### Phase 0 — Foundation
- Run `phase0_architecture_trace.sh`, `phase0_repo_map.sh`, `run_ci_local.sh`
- Complete Cheat Sheet Sections A + Glossary
- Open architecture map HTML and canvas tabs

### Phase 1 — CDC & Bronze
- facets-core Step Functions + Batch flow
- Manifest validation (AIR library)
- Bronze SCD2: CMC_* tables

### Phase 2 — Silver & Gold
- unified_timeline_claim SCD2
- Interop vs CDP filtering rules
- compare_interop_cdp_counts.sh in dev/stg

### Phase 3 — Operations
- 4-hr schedule + nightly Facets_BatchJobComplete trigger
- CdcGlobals lock contention scenarios
- ng-orchestration-service delivery monitoring

### Phase 4 — Downstream
- ng-pipelines-onyx SAM/FHIR
- Snowflake chunked egress (XFORM-3515)
- Reltio MDM migration from 1.0 connector

## Key Architecture Facts

- **Historical:** ~99M claims, ~250M lines (from 1/1/2017)
- **Nightly:** 70k–120k claims
- **Incremental:** 500–1k tx per 15-min window
- **Bronze tables:** 420 in prod (Jun 2024)
- **JSON per batch:** ~25 files + manifest
- **Dental:** In bronze/silver; filtered from Interop gold only

## Confidence & Validation

High confidence: end-to-end architecture, layer/table names (Confluence + scope note).  
Medium: live schedules, 1.0 vs NextGen cutover — confirm with #xform-xport for cambia02 dev/stg/prd.
