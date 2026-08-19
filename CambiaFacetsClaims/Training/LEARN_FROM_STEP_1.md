# Learn From Step 1 — Cambia Facets Claims

> **Four pillars drive every step:** E2E Implementation · Facets/TriZetto SME · On-Prem→Cloud Migration · Postman API Role

---

## How This Guide Fits Together

| Resource | Pillar | Use it for |
|----------|--------|------------|
| **This file** | All | Day-by-day learning by pillar |
| [Cheat Sheet](/Users/ashishsingh/Interview/Cambia_Facets_Claims_Interview_Cheat_Sheet.md) | All | 553 Q&A — each tagged P1–P4 |
| [POSTMAN_API_ROLE.md](../docs/POSTMAN_API_ROLE.md) | P4 | Collections, environments, newman gates |
| [Architecture Map](../facets-claims-e2e-architecture-map.html) | All | 4-pillar tabbed reference |

---

## Step 1 — E2E Implementation Baseline (P1)

**Goal:** Trace full pipeline and run all baseline scripts.  
**Cheat Sheet:** Section A (Q1–10), Section C (Q29–35)

```bash
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
chmod +x scripts/*.sh scripts/ci/*.sh
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/ci/run_ci_local.sh
```

**Exit:** Draw E2E flow from memory; all scripts exit 0.

---

## Step 2 — TriZetto Facets SME Foundation (P2)

**Goal:** Speak Facets claim domain fluently.  
**Cheat Sheet:** Section B (Q11–28), Section K (Q163–172), Section T (Q391–400)

| Day | Learn | Exit criteria |
|-----|-------|---------------|
| Mon | CMC_CLCL_CLAIM + line table joins | Draw header→line ER without notes |
| Tue | CLCL status lifecycle 11→02→91 | Map status transitions to SCD2 behavior |
| Wed | Medical (M/H) vs dental (D) filtering | Explain why dental in CDP gold only |
| Thu | Nightly batch volumes (70k–120k) | Cite incremental vs batch tx rates |
| Fri | Teach-back to colleague | 15-min Facets domain presentation |

---

## Step 3 — On-Prem → Cloud Migration (P3)

**Goal:** Understand phased migration and cutover gates.  
**Cheat Sheet:** Section F (Q95–112), Section L (Q173–185), Section S (Q361–375), Section P (Q251–265)

```bash
./scripts/migration_cutover_checklist.sh
```

| Gate | Check |
|------|-------|
| VPN | cambia-facets-networking tunnel up |
| Historical | ~99M claims backfill parity sample |
| Incremental | 4-hr schedule + Facets_BatchJobComplete trigger |
| HITRUST | facets-core outside boundary; encryption before landing |
| Parallel run | gold.fm_claim_cambia signature bitmap match |

---

## Step 4 — Medallion Implementation (P1 + P2)

**Goal:** Implement and validate bronze→gold.  
**Cheat Sheet:** Section D (Q46–73), Section H (Q125–141), Section Q (Q296–315)

```bash
./scripts/compare_interop_cdp_counts.sh
```

Trace one claim: `CMC_CLCL_CLAIM` → `silver.unified_timeline_claim` → `gold.fm_claim` / `gold.fm_claim_cambia`.

---

## Step 5 — Postman API Role (P4)

**Goal:** Build and run API validation collections.  
**Cheat Sheet:** Section E (Q74–94), Section O (Q206–230), Section AB (Q536–553)

```bash
./scripts/postman_smoke_check.sh
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

| Collection | When to run |
|------------|-------------|
| Orchestration smoke | After every manifest-triggered batch |
| FHIR Interop | After gold.fm_claim load |
| FHIR CDP | After gold.fm_claim_cambia load |
| Cutover gate | Before stg→prd promotion |

---

## Step 6 — E2E Operations & Cutover (P1 + P3 + P4)

**Goal:** Operate production pipeline and execute cutover.  
**Cheat Sheet:** Section I, M, Y, AA, AB

Confirm live workflow IDs with #xform-xport for cambia02 dev/stg/prd.

---

## Proficiency Exit Checklist

| Pillar | Exit proof |
|--------|------------|
| **P1 E2E** | Whiteboard 5 stages + repos; run_ci_local.sh green |
| **P2 SME** | Explain CLCL lifecycle + CMC joins; cite volume profiles |
| **P3 Migration** | migration_cutover_checklist.sh; parallel-run parity documented |
| **P4 Postman** | newman smoke green on stg; no PHI in collections |

---

## Section → Pillar Map

| Pillar | Sections |
|--------|----------|
| P1 E2E | A, C, D, G, H, I, J, M, Q, X, Y, Z |
| P2 SME | B, K, T, U, W |
| P3 Migration | F, L, N, P, R, S, V, AA |
| P4 Postman | E, O, AB |
