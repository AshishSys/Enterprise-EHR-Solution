# Learn From Step 1 — Cambia Facets Claims

> **Learning is the primary objective. Building is how you prove you learned.**  
> Do not skip to prod workflows hoping to “pick it up later.” Every phase below is **Learn → Do → Check → Teach**.

---

## How This Guide Fits Together

| Resource | Use it for |
|----------|------------|
| **This file** | Day-by-day learning path and checkpoints |
| [Glossary](/Users/ashishsingh/Interview/Cambia_Facets_Claims_Interview_Cheat_Sheet.md#glossary) | Terms before you touch code |
| [Cheat Sheet Q&A + Scripts](/Users/ashishsingh/Interview/Cambia_Facets_Claims_Interview_Cheat_Sheet.md) | Interview depth + runnable proof |
| [implementation_details.md](../implementation_details.md) | What each component does and why |
| [Architecture Map](../facets-claims-e2e-architecture-map.html) | 5-stage visual reference |
| [Architecture Canvas](/Users/ashishsingh/.cursor/projects/Users-ashishsingh-CambiaFacetsClaims/canvases/cambia-facets-claims.canvas.tsx) | Tabbed interactive reference |
| [Plan v1](.cursor/plans/cambia_facets_claims_solution.plan.md) | Production phases when ready |

---

## The Learning Loop (Every Step)

```
  ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
  │  LEARN   │ ──► │   DO     │ ──► │  CHECK   │ ──► │  TEACH   │
  │ 15–45 min│     │ 30–90 min│     │ 15 min   │     │ 15 min   │
  └──────────┘     └──────────┘     └──────────┘     └──────────┘
       ▲                                                    │
       └──────────────── reflect / fix gaps ───────────────┘
```

---

## Step 1 — Your First Day (Non-Negotiable Foundation)

**Goal:** Understand the 5-stage pipeline and prove local trace scripts work.  
**Time:** 2–4 hours  
**Roles touched:** Solution Architect, Data Engineer (intro)

### 1A — Learn (45 min)

1. Read Glossary terms: **cambia02**, **Facets**, **facets-core**, **manifest.json**, **AIR library**, **CMC_CLCL_CLAIM**, **unified_timeline_claim**, **fm_claim**, **fm_claim_cambia**
2. Read [implementation_details.md — System Overview](../implementation_details.md)
3. Read Cheat Sheet **Q1–Q3** (Section A) — Answer + Example only

**Checkpoint:** Draw from memory: `Facets CDC → VPN → JSON+manifest → SFTP → Bronze → Silver → Gold (Interop ║ CDP) → SAM/FHIR`

### 1B — Do (60 min)

```bash
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
chmod +x scripts/*.sh scripts/ci/*.sh
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/ci/run_ci_local.sh
```

Run **Scripts** on Cheat Sheet **Q1** and **Q29**.

### 1C — Check (15 min)

| Check | Expected |
|-------|----------|
| Architecture trace | All 5 stages named with repos |
| Repo map | 7 repos/services listed |
| Local CI | Exit 0 |
| You can name dual gold paths | Interop filtered vs CDP full |

### 1D — Teach (15 min)

Write or say aloud:

- Why Facets Claims is not a generic Transporters service  
- What triggers CDC besides the 4-hour schedule  
- Why dental claims land in bronze but not Interop gold  

**Step 1 exit:** Local CI green + Glossary 10 terms + whiteboard diagram.  
**Do not touch prod Databricks until Step 1 exit is done.**

---

## Step 2 — Week 1: Facets Domain & CDC Language

**Goal:** Speak Facets claim domain and CDC vocabulary confidently.  
**Cheat Sheet:** Section B (Q11–28) + Section G (Q113–124)  
**Artifact:** Scope note PDF, Confluence Facets Medical & Dental Claims

| Day | Learn | Do | Exit criteria |
|-----|-------|-----|---------------|
| Mon | Claim types M/H/D, status codes | Map status 11/15/01/02/91 to lifecycle | Table in notes |
| Tue | CDC process types (Incremental, Historical, PPL) | Trace manifest path pattern | Pattern memorized |
| Wed | CdcGlobals lock, concurrency | Read Section G Q113–120 | Explain overlap drop |
| Thu | Teach-back: Stage 2 only | Present CDC → JSON flow | Team Q&A |
| Fri | Scripts Q113–Q120 | Run CDC trace scripts | Can explain ~25 files/batch |

---

## Step 3 — Week 2: Architecture & Ownership

**Goal:** Know every box in the diagram and who owns failures there.  
**Cheat Sheet:** Section C (Q29–45)  
**Artifact:** [facets-claims-e2e-architecture-map.html](../facets-claims-e2e-architecture-map.html)

| Day | Learn | Do | Exit criteria |
|-----|-------|-----|---------------|
| Mon | 5-stage map + 10-step Lucid flow | Trace stage 1→3 in repo names | Path list in notebook |
| Tue | HITRUST boundary (facets-core outside) | Document encryption handoff | Boundary rules written |
| Wed | ng-orchestration-service triggers | Read orchestration.yaml catalog | Manifest trigger explained |
| Thu | Teach-back: full E2E | Architecture + 5 failure points | Diagram with owners |
| Fri | Scripts Q29–Q35 | Architecture trace + repo map | All stages + repos |

---

## Step 4 — Weeks 3–4: Data Engineering (Bronze → Gold)

**Goal:** Own medallion layers mentally and in SQL.  
**Cheat Sheet:** Section D (Q46–73), Section Q (Q296–330), Section H (Q125–141)

| Week | Build slice | Learn focus | Proof |
|------|-------------|-------------|-------|
| W3 | Bronze SCD2 only | CMC_* tables, AIR library | SQL row counts on bronze.cmc_clcl_claim |
| W4 | Silver → dual gold | unified_timeline, Interop vs CDP filter | compare_interop_cdp_counts.sh |

**Hands-on sequence:**

1. Read ng-pipelines-cambia pipespecs for claims — 30 min  
2. Trace one claim from CMC_CLCL_CLAIM → silver.unified_timeline_claim — 60 min  
3. Compare gold.fm_claim vs gold.fm_claim_cambia row counts — 30 min  
4. Explain dental filter to a colleague — 15 min  

---

## Step 5 — Weeks 5–6: Landing, Orchestration & Operations

**Goal:** Operate nightly batch + incremental schedules.  
**Cheat Sheet:** Section O (Q206–250), Section P (Q251–295), Section I (Q142–154)

| Focus | Key artifact |
|-------|--------------|
| SFTP trigger file | Facets_BatchJobComplete_* pattern |
| Manifest validation | AIR library contract |
| Missed batch scenario | Section M troubleshooting |

---

## Step 6 — Weeks 7–8: Downstream & Cutover

**Goal:** Trace gold → SAM/FHIR, Snowflake, Reltio.  
**Cheat Sheet:** Section E (Q74–94), Section N (Q196–205), Section R (Q331–360), Section AB (Q536–553)

Confirm live schedule and 1.0 vs NextGen cutover with #xform-xport for your env.

---

## Proficiency Checklist (All Steps Complete)

| Role | Sections | Exit proof |
|------|----------|------------|
| Associate Solution Architect | A, C, H, L, M, AB | Whiteboard 5-stage + dual gold without notes |
| Data Engineer | D, G, O, P, Q, T | SQL counts across all medallion layers |
| FHIR Engineer | E, H | Explain dental filter → SAM path |
| Forward Deployed Engineer | F, I, S, Y | Run incident scenario from Section M |
| DevOps Engineer | Z | run_ci_local.sh green; facets-infrastructure trace |
| Integration Engineer | G, P, O | Manifest + SFTP trigger end-to-end |

---

## Section → Cheat Sheet Map

| Step | Sections | Questions |
|------|----------|-----------|
| 1 | A | Q1–10 |
| 2 | B, G | Q11–28, Q113–124 |
| 3 | C | Q29–45 |
| 4 | D, H, Q | Q46–73, Q125–141, Q296–330 |
| 5 | I, O, P, M | Q142–154, Q186–195, Q206–295 |
| 6 | E, N, R, AB | Q74–94, Q196–205, Q331–360, Q536–553 |
| Security | F, V, AA | Q95–112, Q446–455, Q516–535 |
| Scale | T, U, Y | Q391–445, Q474–485 |
| DevOps | S, Z | Q361–390, Q486–515 |
| MDM | W, R | Q456–465, Q331–360 |
| Compare | X | Q466–473 |
