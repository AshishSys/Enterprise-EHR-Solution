---
name: Cambia Facets Claims Solution
overview: "4-pillar proficiency program: E2E Implementation · Facets/TriZetto SME · On-Prem→Cloud Migration · Postman API Role. cambia02 tenant."
todos:
  - id: p1-phase0
    content: "P1: E2E baseline — architecture trace, repo map, run_ci_local.sh green"
    status: pending
  - id: p2-sme
    content: "P2: TriZetto SME — CMC tables, CLCL lifecycle, medical/dental grain (Sections B, K, T)"
    status: pending
  - id: p3-migration
    content: "P3: Migration gates — VPN, historical backfill, migration_cutover_checklist.sh"
    status: pending
  - id: p1-medallion
    content: "P1: Medallion implementation — bronze SCD2 through dual gold FM"
    status: pending
  - id: p4-postman
    content: "P4: Postman collections + newman smoke for orchestration and FHIR (Sections E, O, AB)"
    status: pending
  - id: p3-cutover
    content: "P3+P4: stg→prd cutover — parallel-run parity + cutover-gate collection green"
    status: pending
isProject: true
---

# Cambia Facets Claims — 4-Pillar Implementation Plan

## Pillars

| Pillar | Focus | Cheat Sheet | Scripts |
|--------|-------|-------------|---------|
| **P1 E2E** | Full pipeline delivery | A, C, D, G, H, I, M, Q | phase0_*, run_ci_local.sh |
| **P2 SME** | TriZetto Facets domain | B, K, T, U, W | compare_interop_cdp_counts.sh |
| **P3 Migration** | On-prem → cloud cutover | F, L, N, P, R, S, AA | migration_cutover_checklist.sh |
| **P4 Postman** | API contract validation | E, O, AB | postman_smoke_check.sh |

## Phases

### Phase 0 — P1 E2E Baseline
- Run all phase0 scripts + run_ci_local.sh
- Whiteboard 5 stages with repo owners

### Phase 1 — P2 SME + P3 Migration Foundation
- Facets domain: CMC_* tables, CLCL status codes
- VPN + CDC path; HITRUST boundary documented

### Phase 2 — P1 Medallion Implementation
- Bronze SCD2 → silver unified timeline → dual gold
- Interop vs CDP filtering (P2 SME sign-off on dental)

### Phase 3 — P4 Postman API Role
- Build collections per docs/POSTMAN_API_ROLE.md
- newman smoke on dev/stg orchestration + FHIR

### Phase 4 — P3+P4 Cutover
- migration_cutover_checklist.sh all items checked
- cutover-gate collection green; #xform-xport sign-off
