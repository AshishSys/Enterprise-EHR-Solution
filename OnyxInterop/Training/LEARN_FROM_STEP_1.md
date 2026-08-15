# Learn From Step 1 — Healthcare Interop Solution

> **Learning is the primary objective. Building is how you prove you learned.**  
> Do not skip to production deploy hoping to “pick it up later.” Every phase below is **Learn → Do → Check → Teach**.

---

## How This Guide Fits Together

| Resource | Use it for |
|----------|------------|
| **This file** | Day-by-day learning path and checkpoints |
| [Glossary](../Interview/Healthcare_Interop_Interview_Cheat_Sheet.md#glossary) | Terms before you touch code |
| [Cheat Sheet Q&A + Scripts](../Interview/Healthcare_Interop_Interview_Cheat_Sheet.md) | Interview depth + runnable proof |
| [implementation_details.md](../implementation_details.md) | What each component does and why |
| [docs/DEVOPS_CICD.md](onyx-interop/docs/DEVOPS_CICD.md) | GitLab CI stages, secrets, go-live gates |
| [Plan v3.1](.cursor/plans/healthcare_interop_solution_6dadfbad.plan.md) | Production phases when you are ready |
| [7-Module Plan](../interop_onyx_project_plan.md) | Teach-back topics and artifacts |
| [teach_back_schedule.md](../teach_back_schedule.md) | Present-to-learn format |

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

- **Learn:** Glossary + one cheat-sheet section + one artifact page  
- **Do:** Run the **Script** for that step; change one thing and re-run  
- **Check:** Pass the step’s exit criteria (commands, counts, tests)  
- **Teach:** Explain it aloud or in 5 bullets — if you cannot teach it, you have not learned it  

---

## Step 1 — Your First Day (Non-Negotiable Foundation)

**Goal:** Understand *what* the platform is and *prove* the local stack works.  
**Time:** 2–4 hours  
**Roles touched:** Solution Architect, Programmer, FHIR Engineer (intro)

### 1A — Learn (45 min)

1. Read Glossary terms (in order): **Abacus**, **Onyx**, **FM**, **SAM**, **SLAP**, **FITE**, **Firely**, **CMS-9115**, **FHIR R4**, **US Core**
2. Read [implementation_details.md — System Overview](../implementation_details.md) (first diagram only)
3. Read Cheat Sheet **Q1–Q3** (Section A) — Answer + Example only (not full memorization)

**Checkpoint:** Draw from memory: `CSV → ? → ? → FHIR → ? → SLAP → FITE → App`

### 1B — Do (60 min)

```bash
cd /Users/ashishsingh/OnyxInterop/Training/onyx-interop

# Environment + baseline + local CI (DevOps gate from Day 1)
./scripts/phase0_access_checklist.sh
./scripts/setup_environment.sh
chmod +x scripts/ci/run_ci_local.sh
./scripts/ci/run_ci_local.sh
```

Run **Scripts** on Cheat Sheet **Q1** and **Q8**.

### 1C — Check (15 min)

| Check | Expected |
|-------|----------|
| FHIR JSON files exist | ~9,997 resources across 8 types |
| `validate_fhir_output.py` | Exit 0 |
| `pytest tests/` | All green |
| You can name 6 components | Pipeline, SLAP, FITE, Firely, Insights, MDP |

### 1D — Teach (15 min)

Write or say aloud:

- What Abacus owns vs what Onyx owns  
- Why raw CSV is not FHIR-shaped at ingest  
- What success looks like on Day 1 (local baseline green)

**Step 1 exit:** Baseline green + Glossary 10 terms + whiteboard diagram.  
**Do not start Phase 1 Databricks until Step 1 exit is done.**

---

## Step 2 — Week 1: CMS Rules & FHIR Language

**Goal:** Speak CMS and FHIR confidently before writing transforms.  
**Cheat Sheet:** Section B (Q11–28) + Section E (Q74–94)  
**Artifact:** [cms_9115_vs_0057_implementation_map.md](../cms_9115_vs_0057_implementation_map.md), [fhir_ig_quick_reference_guide.md](../fhir_ig_quick_reference_guide.md)

| Day | Learn | Do | Exit criteria |
|-----|-------|-----|---------------|
| Mon | CMS-9115 vs CMS-0057 map | List which APIs are Phase 1 vs 2 | Table completed in your notes |
| Tue | US Core + CARIN BB profiles | Inspect 3 resources in `fhir_output/` for `meta.profile` | Profiles match IG URLs |
| Wed | Da Vinci Plan-Net, Formulary | Read PVD + Formulary extract configs | Map SAM table → resource type |
| Thu | Teach-back M1 (30 min) | Present CMS → component map | Team Q&A |
| Fri | Cheat Sheet Q11–Q20 Scripts | Run FHIR validation script (Q74 area) | Can explain one Must Support failure |

---

## Step 3 — Week 2: Architecture & Ownership

**Goal:** Know every box in the diagram and who owns failures there.  
**Cheat Sheet:** Section C (Q29–45)  
**Artifact:** [onyx_component_ownership_matrix.md](../onyx_component_ownership_matrix.md), [sam-firely-e2e-aws-implementation-map.html](../sam-firely-e2e-aws-implementation-map.html)

| Day | Learn | Do | Exit criteria |
|-----|-------|-----|---------------|
| Mon | 12-step AWS map | Trace step ①→⑥ in repo paths | Path list in notebook |
| Tue | Abacus vs Onyx boundary | Find 3 violations of “no direct Firely” in docs | Boundary rules documented |
| Wed | MDP + job state | `curl localhost:9002/services`; read `onyx_job_state` pattern | Registry + watermark explained |
| Thu | Teach-back M2 | Architecture + failure-point map | Diagram with 5 failure points |
| Fri | Scripts Q29–Q35 | `./scripts/start_all_services.sh` + smoke curls | FITE + SLAP respond |

---

## Step 4 — Weeks 3–4: Data Engineering (Learn by Breaking Things Safely)

**Goal:** Own FM → SAM → Extract mentally and in code.  
**Cheat Sheet:** Section D (Q46–73), Section P (Q251–295), Section Q (Q296–330)  
**Artifact:** [databricks_workflow_troubleshooting_handbook.md](../databricks_workflow_troubleshooting_handbook.md)

**Learning principle:** Change one transformer → re-run pipeline → observe diff. Never bulk-copy prod configs without reading.

| Week | Build slice | Learn focus | Proof |
|------|-------------|-------------|-------|
| W3 | Claims family only | FM keys, watermark, incremental | Patch `claims_transformer.py` field mapping; pytest green |
| W4 | PVD → Claims dependency | Reference integrity (Practitioner on EOB) | EOB bundle references resolve in validator |

**Hands-on sequence:**

1. Read `pipeline/base_transformer.py` — 30 min  
2. Read `claims_transformer.py` — trace one claim line to EOB JSON — 60 min  
3. Introduce intentional bug (wrong column) → see validation fail → fix — 30 min  
4. Run Rail A end-to-end script from Q251  

**Kafka learning (Rail B) — parallel track, Week 4:**

- Learn Glossary: **Rail B**, **MSK**, **Schema Contract**, **SQS DLQ**  
- Run Kafka producer/consumer Script (Q251) locally or against dev MSK  
- Draw webhook path without looking at docs  

---

## Step 5 — Weeks 5–6: FHIR Store & Runtime APIs

**Goal:** Load bundles, authenticate, query APIs — the member-facing path.  
**Cheat Sheet:** Section F (Q95–112), Section G (Q113–124)  
**Artifact:** [firely_vs_healthlake_support_matrix.md](../firely_vs_healthlake_support_matrix.md)

| Day | Learn | Do | Exit criteria |
|-----|-------|-----|---------------|
| Mon | FSI bulk vs incremental | Walk `stepfunctions/fsi_bulk_workflow.json` | Explain when each runs |
| Tue | SMART + PKCE | Run SLAP token Script (Q95 area) | Token exchanged successfully |
| Wed | FITE search + `$everything` | curl with Bearer token | JSON returns US Core resources |
| Thu | Teach-back M4 | Firely vs HealthLake decision | When to use which |
| Fri | Patient Access smoke test | Full path: SLAP → FITE → resource read | Document latency + errors |

---

## Step 6 — Weeks 7–8: CMS-0057 Advanced + Multi-Rail

**Goal:** Provider Access, P2P, ePA concepts + Rail C PulseEHR path.  
**Cheat Sheet:** Section H (Q125–141), Section P (Q260–295)

| Build | Learn first | Proof |
|-------|-------------|-------|
| Provider Access `$export` | Attribution + Group resources | Export manifest validates |
| P2P `$bulk-member-match` | Consent + opt-in model | Postman collection runs in dev |
| ePA CRD/DTR/PAS | Da Vinci flow diagram | `epa_transformer.py` output validates |
| Rail C Autoloader | PulseEHR scale (129K / 8.9M) | Bronze lag dashboard + quarantine rate < 1% |

---

## Step 7 — Weeks 9–10: DevOps, CI/CD & Forward Deployed Skills

**Goal:** Every merge is tested; stage/prod deploys are gated and repeatable.  
**Cheat Sheet:** Section I (Q142–154), **Section Z (Q486–515)**  
**Artifacts:** [docs/DEVOPS_CICD.md](onyx-interop/docs/DEVOPS_CICD.md), `.gitlab-ci.yml`, [seiji_deploy_rollback_runbook.md](../seiji_deploy_rollback_runbook.md)

| Skill | Learn | Do | Exit |
|-------|-------|-----|------|
| GitLab CI | Read `.gitlab-ci.yml` stages | `./scripts/ci/run_ci_local.sh` every PR | validate + test green locally |
| DAB deploy | `databricks.yml` targets | `databricks bundle validate -t dev` | dev/stage/prod catalog explained |
| Seiji/Helm | Firely chart + runbook | `helm lint` + canary drill | Rollback documented |
| CMS go-live | DEVOPS_CICD checklist | Tabletop: CI red blocks hotfix | 12-point gate from memory |

---

## Step 8 — Weeks 11–12: AI Layer (After Data Path Is Solid)

**Goal:** RAG and agents on governed data — not chatbots on raw PHI.  
**Cheat Sheet:** Section O (Q206–250), Section R (Q331–360)

**Prerequisite gate:** Steps 1–6 exit criteria met. AI without FHIR/SAM understanding produces dangerous demos.

| Week | Learn | Build | Proof |
|------|-------|-------|-------|
| W11 | Unity AI Gateway policies | Enable dev gateway + one policy | PHI mask blocks test prompt |
| W12 | RAG + MCP + ai_events | Index formulary slice; one agent notification | Golden eval ≥ 85% on 20 questions |

---

## Step 10 — Weeks 15–16: Fabric, SQL, Hybrid + Capstone

**Goal:** Analytics path + SQL warehouse + architect judgment.  
**Cheat Sheet:** Sections N, S, T, U (Q196–205, Q361–445)

**Capstone (Week 16):** One engineer plays “payer go-live”:

1. Rail A CSV + Rail B webhook event land same day  
2. SAM merge completes  
3. Patient Access API returns EOB  
4. CMS metrics row populated  
5. Payer Ops Agent fires on synthetic lag (optional)  
6. 15-min exec + 15-min engineering teach-back  

---

## Role-Based Learning Paths (Pick Primary + Secondary)

| Primary role | Start Steps | Deepen in | Capstone focus |
|--------------|-------------|-----------|----------------|
| **FHIR Engineer** | 1 → 2 → 5 → 6 | E, G, H | IG validation zero errors; `$export` |
| **Data Engineer** | 1 → 3 → 4 → 6 | D, P, Q | Three rails converge at SAM |
| **Kafka Engineer** | 1 → 4 (Rail B track) | P, Q296+ | Producer/consumer + DLQ replay |
| **AI Engineer** | 1 → 4 (SAM) → 8 | O, R | RAG + gateway + agent eval |
| **Forward Deployed** | 1 → 3 → 7 | I, M | Solo deploy + incident restore |
| **Programmer** | 1 → 4 → 5 | D, F, U | pytest green; patch transformer solo |
| **Solution Architect** | 1 → 2 → 3 → 6 | C, H, K, L | CMS traceability whiteboard |
| **DevOps Engineer** | 1 → 7 (Z) | I, Z | run_ci_local.sh + CI stage diagram |

---

## Weekly Rhythm (Recommended)

| Day | Time | Activity |
|-----|------|----------|
| Mon | 45 min | Learn — Glossary + new section + artifact |
| Tue | 90 min | Do — build/run Scripts for that section |
| Wed | 60 min | Check — fix failures; update personal runbook |
| Thu | 30 min | Teach — bullet notes or peer teach-back |
| Fri | 45 min | Reflect — 3 things learned, 1 gap, next week plan |

**Minimum viable learning:** 5 hrs/week. **Proficiency target:** 8–10 hrs/week.

---

## Personal Learning Tracker

Copy into your notes and tick weekly:

```
[ ] Step 1  — Local baseline green (Day 1)
[ ] Step 2  — CMS + FHIR vocabulary (Week 1)
[ ] Step 3  — Architecture ownership (Week 2)
[ ] Step 4  — Data engineering + Kafka (Weeks 3–4)
[ ] Step 5  — FHIR store + SMART APIs (Weeks 5–6)
[ ] Step 6  — CMS-0057 + multi-rail (Weeks 7–8)
[ ] Step 7  — DevOps/CI/CD + deploy (Weeks 9–10)
[ ] Step 8  — AI layer (Weeks 11–12)
[ ] Step 9  — Fabric/SQL + capstone (Weeks 13–16)
[ ] Glossary — all 115 terms can explain with example
[ ] Scripts  — ___ / 485 cheat sheet Scripts run green
[ ] Teach-backs — M1–M7 + capstone delivered
```

---

## What Not To Do (Common Learning Failures)

| Mistake | Why it fails | Instead |
|---------|--------------|---------|
| Skip Step 1, jump to Databricks | No mental model; configs are magic strings | Baseline local pipeline first |
| Read cheat sheet only, never run Scripts | Interview answers without skill | Every section: run ≥3 Scripts |
| Learn AI before SAM/FHIR | Agents hallucinate on data you do not understand | Step 8 only after Step 6 |
| Copy prod YAML without tracing | One column rename breaks Extract silently | Read transformer + SAM schema together |
| Solo study only | False confidence | Teach-back every 1–2 weeks |

---

## When to Start Production Phases (Plan v3.1)

| Plan phase | Start only after |
|------------|------------------|
| Phase 0 access | Step 1 complete |
| Phase 1 pipelines | Steps 3–4 complete |
| Phase 1 runtime | Step 5 complete |
| Phase 2 CMS-0057 | Step 6 complete |
| Phase 3 hardening | Step 7 complete |
| Phase 4 AI | Step 8 complete |

**Rule:** Production work *extends* learning; it does not replace it. If deploy outpaces teach-back, pause deploy.

---

## Your Next Action (Today)

1. Open [Glossary](../Interview/Healthcare_Interop_Interview_Cheat_Sheet.md#glossary) — read 10 terms  
2. Run Step 1B commands — all green  
3. Run Cheat Sheet **Q1 Script** — save log to `~/interop-learning/step1.log`  
4. Block Thu 30 min — teach Abacus/Onyx split to yourself or a peer  
5. Tick Step 1 on your tracker  

Learning is the product. The interoperable platform is the proof.
