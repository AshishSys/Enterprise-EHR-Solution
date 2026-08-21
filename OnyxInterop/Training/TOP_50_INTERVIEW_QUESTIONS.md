# Top 50 Healthcare Interop Interview Questions

> **Curated from 553-question cheat sheet** — highest probability for Abacus/Onyx CMS interoperability interviews.  
> **Full answers + scripts:** [Healthcare_Interop_Interview_Cheat_Sheet.md](/Users/ashishsingh/Interview/Healthcare_Interop_Interview_Cheat_Sheet.md)  
> **Learn path:** [LEARN_FROM_STEP_1.md](./LEARN_FROM_STEP_1.md)

---

## How to use this file

1. **Memorize the one-line answer** under each question first.
2. **Practice the example** aloud — interviewers probe for concrete delivery, not theory.
3. **Drill the full Q** in the cheat sheet when you have 15+ minutes per topic.
4. **Priority order:** Sections 1–4 first (platform + CMS + architecture + pipeline), then FHIR/auth, then advanced.

---

## Quick index

| # | Q | Topic | Section |
|---|-----|-------|---------|
| 1 | Q1 | Opening — E2E platform experience | A |
| 2 | Q2 | Abacus vs Onyx components | A |
| 3 | Q7 | CXO two-minute pitch | A |
| 4 | Q11 | CMS-9115 APIs | B |
| 5 | Q12 | CMS-0057 extends 9115 | B |
| 6 | Q13 | CMS deadlines (2026/2027) | B |
| 7 | Q15 | Patient Access vs Provider Access | B |
| 8 | Q23 | P2P when member switches plans | B |
| 9 | Q29 | E2E architecture walkthrough | C |
| 10 | Q30 | Abacus vs Onyx ownership | C |
| 11 | Q31 | Why not Firely directly | C |
| 12 | Q32 | SLAP role | C |
| 13 | Q33 | FITE gateway | C |
| 14 | Q36 | SAM as IG bridge | C |
| 15 | Q39 | PVD before Claims dependency | C |
| 16 | Q46 | Six Databricks workflow families | D |
| 17 | Q48 | FM vs SAM | D |
| 18 | Q53 | Daily claims flow | D |
| 19 | Q56 | Incremental watermarks | D |
| 20 | Q58 | Common pipeline failures | D |
| 21 | Q74 | FHIR R4 for CMS | E |
| 22 | Q75 | Resource, Bundle, NDJSON | E |
| 23 | Q76 | Patient `$everything` | E |
| 24 | Q77 | Bulk `$export` | E |
| 25 | Q80 | Implementation Guides | E |
| 26 | Q82 | CARIN Blue Button | E |
| 27 | Q84 | PDex | E |
| 28 | Q85 | CRD, DTR, PAS (ePA) | E |
| 29 | Q87 | SMART Backend Services | E |
| 30 | Q88 | PKCE | E |
| 31 | Q91 | IG validation failure | E |
| 32 | Q95 | SMART Standalone PKCE flow | F |
| 33 | Q97 | Scopes per API | F |
| 34 | Q100 | P2P opt-in vs PVA opt-out | F |
| 35 | Q103 | PHI in logs/metrics | F |
| 36 | Q113 | Why Firely | G |
| 37 | Q116 | Lambda incremental vs FSI bulk | G |
| 38 | Q125 | Attribution lists | H |
| 39 | Q126 | Group `$export` (Provider Access) | H |
| 40 | Q142 | Seiji deploy | I |
| 41 | Q186 | Scenario: missing Practitioner refs | M |
| 42 | Q251 | Multi-rail v3 — keep CSV path | P |
| 43 | Q252 | Rails A / B / C | P |
| 44 | Q296 | Databricks Asset Bundles | Q |
| 45 | Q446 | De-ID at layer 0 | V |
| 46 | Q456 | MDM standards | W |
| 47 | Q486 | CI/CD architecture | Z |
| 48 | Q536 | Three CMS-0057 auth paths | AB |
| 49 | Q541 | Shared vs different auth paths | AB |
| 50 | Q543 | ePA Option A (Gainwell batch) | AB |

---

## Section 1 — Opening & platform (must-know)

### 1. Q1 — Tell me about your E2E healthcare data platform experience

**Answer:** I led CMS interoperability delivery end-to-end: ingestion → FM/SAM → FHIR → Firely → SLAP/FITE. I owned Databricks workflows and API runtime wiring, not just architecture slides. Success = CMS API uptime, bundle validation pass rate, Patient Access metrics.

**Example:** Raw → FM → SAM → FHIR for six workflow families; 10 Synthea patients → 9,997 FHIR resources live behind SMART APIs.

---

### 2. Q2 — What is Abacus/Onyx and how do components fit?

**Answer:** **Abacus** = data plane (ingestion, FM/SAM, ETL, bundles). **Onyx** = API plane (SLAP, FITE, Developer Portal, Insights). Bundles land in Firely/HealthLake; **only FITE** exposes FHIR externally.

**Example:** S3 Bronze → FM/SAM → Extract → FSI/Firely → Consumer App → SLAP (:9000) → FITE (:8080) → Firely.

---

### 3. Q7 — Explain the platform to a CXO in two minutes

**Answer:** We ingest payer data, standardize to FHIR, and expose federally mandated APIs so members, providers, and payers access claims, clinical, formulary, and directory data securely. Abacus guarantees **data**; Onyx guarantees **API compliance**. Jan 2027 CMS-0057 is the forcing function.

**Example:** 12-step AWS flow: S3 Bronze → FM/SAM → bundle upload → Firely → SLAP/FITE → CMS metrics reporter.

---

## Section 2 — CMS rules (almost always asked)

### 4. Q11 — What is CMS-9115?

**Answer:** Final rule requiring payers to expose **Patient Access**, **Provider Directory**, and **Drug Formulary** via FHIR R4 SMART APIs using US Core, CARIN BB, and Plan-Net profiles.

**Example:** Patient Access serves EOB/clinical via FITE; public directory uses PVD workflow; formulary uses MedicationKnowledge.

---

### 5. Q12 — What is CMS-0057 and how does it extend CMS-9115?

**Answer:** Adds **Provider Access**, **Payer-to-Payer (P2P)**, **ePA (CRD/DTR/PAS)**, and PA data in Patient Access. Uses Backend Services auth, attribution Groups, `$bulk-member-match`, bulk export — **Jan 1, 2027** deadline.

**Example:** Provider Access = Group `$export`; P2P = opt-in consent + NDJSON export; ePA CRD at :9005.

---

### 6. Q13 — Key CMS interoperability deadlines?

**Answer:** **Jan 1, 2026** — PA operational reforms (API availability, metrics). **Jan 1, 2027** — full CMS-0057 (Provider Access, P2P, ePA). CMS-9115 APIs already in force and maintained.

**Example:** Provider Access/P2P production by Q4 2026 for Jan 2027 buffer.

---

### 7. Q15 — Patient Access vs Provider Access?

**Answer:** **Patient Access** = member-facing SMART PKCE, individual patient context (EOB, clinical, PA). **Provider Access** = provider-facing Backend Services, **attribution Groups**, Group `$export` for in-network providers (opt-out model).

**Example:** SLAP issues `patient/*.read` tokens for apps; Provider Access uses `system/*.read` on attributed Group export.

---

### 8. Q23 — Member switches plans under P2P?

**Answer:** New payer requests prior payer data via **`$bulk-member-match`** after **member opt-in**. Consent tracked; demographic/identifier matching; NDJSON export per CMS window.

**Example:** MatchInput with MBI/subscriber id → MatchResponse → bulk export of prior payer clinical/claims.

---

## Section 3 — Architecture (whiteboard favorites)

### 9. Q29 — E2E architecture: raw data to API response

**Answer:** Raw → FM → SAM → Extract → Transform → Load (FSI/Firely) → SLAP → FITE → consumer. Abacus owns data correctness; Onyx owns API security and IG enforcement.

**Example:** 10 patients → 9,997 resources → SLAP :9000 → FITE :8080 → `$everything`.

---

### 10. Q30 — Abacus vs Onyx ownership split

**Answer:** **Abacus:** ingestion, FM/SAM, Databricks jobs, extract/transform/load, data DQ. **Onyx:** SLAP, FITE, Developer Portal, Insights, IG config, external API contracts.

**Example:** Data team commits to `pipeline/` and extract YAML; Onyx owns `helm/firely-server/` and `apis/consumer/`.

---

### 11. Q31 — Why must consumers not access Firely directly?

**Answer:** Bypasses SLAP auth, scope enforcement, audit logging, and IG-aware routing in FITE. All external traffic goes through FITE with **deny-by-default** policies.

**Example:** Production blocks Firely ingress except from FITE service account.

---

### 12. Q32 — What is SLAP?

**Answer:** SMART-on-FHIR **OAuth2 authorization server**: PKCE for patient apps, Backend Services for P2P/Provider Access. Issues scoped tokens; FITE introspects before serving FHIR.

**Example:** `slap_server.py :9000` → token → FITE validates → FHIR response.

---

### 13. Q33 — What is FITE?

**Answer:** **FHIR API gateway**: validates tokens, binds patient context, IG-aware routing, proxies to Firely/HealthLake, unified CapabilityStatement, audit trail.

**Example:** FITE :8080 serves `/Patient`, `/ExplanationOfBenefit`, `$everything` after SLAP validation.

---

### 14. Q36 — What is the SAM IG bridge?

**Answer:** Subject Area Marts shaped for FHIR mapping — each SAM table aligns to IG resources. Extract reads SAM → S3; transform builds US Core/CARIN BB/Plan-Net bundles.

**Example:** `claims_sam.eob_records` → CARIN BB EOB; `pvd_sam.provider_directory` → Plan-Net PractitionerRole.

---

### 15. Q39 — Why must PVD complete before Claims?

**Answer:** EOB references Practitioner/Organization. If PVD hasn't loaded, references fail IG validation and Patient Access breaks. Enforced in orchestrator and Step Functions.

**Example:** Claims EOB with missing Practitioner NPI → 422 until PVD incremental completes.

---

## Section 4 — Data engineering (Databricks interviews)

### 16. Q46 — Six Databricks workflow families?

**Answer:** **Claims**, **Clinical**, **Formulary**, **PVD**, **CMS-0057** (Provider Access/P2P), **CMS-9115/ePA** — each: preprocess → transform → extract → upload/upsert → terminate.

**Example:** `claims_transformer.py`, `clinical_transformer.py`, `pvd_transformer.py`, `cms0057_transformer.py`, `epa_transformer.py`.

---

### 17. Q48 — FM vs SAM?

**Answer:** **FM (Foundational Mart)** = cleansed, typed, source-aligned — NOT FHIR-shaped. **SAM (Subject Area Mart)** = business aggregates shaped for FHIR extract.

**Example:** `claims_fm.claim_lines` → adjudication logic → `claims_sam.eob_records`.

---

### 18. Q53 — Daily claims flow?

**Answer:** Bronze new files → preprocess → FM update → SAM eob_records → extract delta → transform CARIN BB bundles → Lambda POST → update metadata_v1 and watermark.

**Example:** After PVD freshness check, Claims incremental runs nightly.

---

### 19. Q56 — How do watermarks work?

**Answer:** Stored in **`onyx_job_state`** (DynamoDB) — typically max `updated_at` from last successful extract. Next run: `WHERE updated_at > watermark`. Advanced only on successful terminate.

**Example:** Claims watermark stuck = replay from last good checkpoint, not full reload.

---

### 20. Q58 — Common pipeline failure modes?

**Answer:** Config mismatch (YAML vs transformer), missing references (PVD lag), IG validation failures, Firely 413 (bundle too large), FSI OOM, watermark stuck, wheel version drift.

**Example:** Missing Practitioner ref → Claims upload 422 → fix by PVD re-run.

---

## Section 5 — FHIR & standards (FHIR engineer core)

### 21. Q74 — FHIR R4 and why R4 for CMS?

**Answer:** FHIR **R4 (4.0.1)** is the stable normative base CMS mandates. Standardize on R4 resources, search parameters, and bundles.

**Example:** All Synthea output targets R4 Patient, EOB, Observation.

---

### 22. Q75 — Resource, Bundle, NDJSON in load path?

**Answer:** **Resource** = single FHIR JSON object. **Bundle** = transaction/batch wrapper for POST/PUT. **NDJSON** = one resource per line for FSI `$import` historical loads.

**Example:** Incremental = transaction Bundle (50–150 resources). Historical = NDJSON via FSI.

---

### 23. Q76 — Patient `$everything`?

**Answer:** Returns Bundle of all patient-related resources (EOB, clinical, coverage) for Patient Access apps. FITE aggregates Firely searches.

**Example:** `GET /Patient/{id}/$everything` after SMART PKCE token with patient context.

---

### 24. Q77 — Bulk `$export`?

**Answer:** Async export (Group or Patient `$export`) → NDJSON files at signed URLs. Used for Provider Access attribution exports and P2P.

**Example:** `GET /Group/{attributionGroup}/$export` → poll `_status` → download manifest + NDJSON.

---

### 25. Q80 — Which Implementation Guides?

**Answer:** US Core 6.1.0, CARIN BB 2.0, Plan-Net, Da Vinci CRD/DTR/PAS, PDex, Formulary — pinned in `configs/mdp/ig_registry.json`.

**Example:** EOB = CARIN BB; directory = Plan-Net; vitals = US Core Observation.

---

### 26. Q82 — What is CARIN BB?

**Answer:** Consumer Directed Payer Blue Button — consumer-facing payer resources (EOB, Coverage) required for Patient Access claims/coverage data.

**Example:** Claims transformer targets CARIN BB EOB with patient-friendly adjudication fields.

---

### 27. Q84 — What is PDex?

**Answer:** Payer Data Exchange IG — payer-to-payer exchange patterns complementing CMS-0057 P2P (member match, bulk export formats).

**Example:** P2P NDJSON export aligns with PDex bulk export patterns; FITE route `/pdexv2`.

---

### 28. Q85 — CRD, DTR, PAS?

**Answer:** **CRD** = Coverage Requirements Discovery (EHR hook: is PA needed?). **DTR** = Documentation Templates (adaptive PA forms). **PAS** = Prior Authorization Support (`$submit` → ClaimResponse). Da Vinci ePA workflows.

**Example:** EHR CRD → payer returns DTR questionnaire → PAS returns ClaimResponse decision.

---

### 29. Q87 — SMART Backend Services?

**Answer:** OAuth2 **client_credentials** with signed JWT for system-level access — P2P, Provider Access `$export`. **Not** for patient-facing apps.

**Example:** Payer B2B client calls `$bulk-member-match` with `system/Patient.read`.

---

### 30. Q88 — PKCE and why?

**Answer:** Proof Key for Code Exchange prevents auth code interception for **public** patient apps. Require **S256** `code_challenge` on all SMART Standalone launches.

**Example:** App sends `code_verifier` on token exchange after authorization redirect.

---

### 31. Q91 — IG validation fails — what do you do?

**Answer:** Capture OperationOutcome, classify mustSupport vs binding vs reference error, **quarantine** bundle, fix transform or upstream SAM, re-validate before upload.

**Example:** CARIN BB missing adjudication category blocked nightly Claims upload until transformer fix.

---

## Section 6 — Security & auth (compliance probes)

### 32. Q95 — SMART Standalone PKCE flow?

**Answer:** App registers → user authorizes → auth code redirect → exchange code + `code_verifier` for access token → FITE validates token + patient context → FHIR request.

**Example:** Local: `slap_server.py :9000` + `fhir_server.py :8080` simulate full flow.

---

### 33. Q97 — Scopes per API?

**Answer:** Patient Access: `patient/*.read`, `openid`, `fhirUser`. Provider Access: `system/*.read` on Group export. P2P: `system/Patient.read`, bulk scopes. Formulary: public or `system/Formulary.read`.

**Example:** Scope matrix in Developer Portal per CMS API phase.

---

### 34. Q100 — P2P opt-in vs Provider Access opt-out?

**Answer:** **P2P** requires **member opt-in** to export to new payer. **Provider Access** allows in-network providers unless they **opt out** of sharing attributed records.

**Example:** Consent table gates P2P export; opt-out list filters Provider Access `$export`.

---

### 35. Q103 — Protect PHI in logs and metrics?

**Answer:** Structured logging with IDs hashed/omitted; aggregate metrics only; no raw FHIR in debug logs; Wiz flags secret/PHI patterns.

**Example:** CMS metrics reporter outputs counts/latency only — never member IDs.

---

## Section 7 — FHIR store & CMS-0057 APIs

### 36. Q113 — Why Firely as primary FHIR server?

**Answer:** Firely Server 5.2: full R4 transaction support, FSI `$import`, rich search, IG validation for CMS bundles. HealthLake optional for specific CMS metric endpoints.

**Example:** Firely on EKS loads 9,997 Synthea resources via FSI + incremental Lambda.

---

### 37. Q116 — Incremental Lambda vs FSI bulk?

**Answer:** **Lambda:** daily deltas, transaction bundles, fast fail, 50–150 resources. **FSI:** millions of resources, NDJSON, long-running `$import`.

**Example:** Synthea initial historical via FSI; daily Claims via incremental Step Functions.

---

### 38. Q125 — Attribution lists?

**Answer:** Roster of members attributed to in-network providers for Provider Access. Stored in SAM, exposed as **Group** resources with member Patient references.

**Example:** Attribution SAM feeds `Group/{id}` with member list for `$export`.

---

### 39. Q126 — Group `$export` for Provider Access?

**Answer:** Provider with Backend Services token requests Group `$export` for attributed population — async NDJSON of Patient, clinical, EOB per CMS scope.

**Example:** Onboarding doc includes attribution Group id for `$export` testing.

---

## Section 8 — Ops, scenarios & modern stack

### 40. Q142 — What is Seiji?

**Answer:** GitLab-integrated deploy tool for Helm releases to EKS (Firely, SLAP, FITE, FSI). Targeted deploys for hotfixes; full deploys for releases. dev → stage → prod with Wiz gate.

**Example:** `seiji deploy --service firely --env stage` after CI green.

---

### 41. Q186 — Scenario: Claims missing Practitioner references?

**Answer:** Symptom: EOB validation 422. Check PVD load order, NPI in metadata_v1, Firely Practitioner count. Fix: run PVD incremental, replay Claims upload.

**Example:** Claims ran before PVD — classic cross-family dependency failure.

---

### 42. Q251 — Multi-rail v3 — why keep CSV pipeline?

**Answer:** v3 adds Rails B/C converging at SAM **without** changing proven CSV → FM → SAM → FHIR → Firely → SLAP/FITE path. Rails B/C are additive.

**Example:** `interop_pipeline.py` still produces 9,997 resources from CSV; PulseEHR loads on Rail C in parallel.

---

### 43. Q252 — Rails A, B, C — when to use each?

**Answer:** **Rail A** = CSV/batch (Synthea, payer flat files). **Rail B** = serverless webhook (NASCO real-time events). **Rail C** = native FHIR JSON (PulseEHR bulk). All converge at SAM.

**Example:** Claims CSV → A. NASCO webhook → B. PulseEHR 8.9M JSON → C.

---

### 44. Q296 — Databricks Asset Bundles (DABs)?

**Answer:** Package each workflow family as DAB with dev/stage/prod targets, Unity Catalog schemas per env, deploy via `databricks bundle deploy -t prod`. Jobs, cluster policies, SP permissions in `databricks.yml`.

**Example:** `claims_workflow` DAB → prod with `catalog=prod_interop`, GitLab CI gate on `bundle validate`.

---

### 45. Q446 — Where does de-identification sit?

**Answer:** **Layer 0** — before FM/SAM/analytics. Identified PHI stays on CMS API path behind SLAP. Fabric, Gold BI, logs, LLMs consume **de-id path only**.

**Example:** Raw → De-ID Gate → {identified→FM→Firely; de-id→MDM→Databricks║Fabric}.

---

### 46. Q456 — MDM standards?

**Answer:** AHIMA Information Governance, ISO 8000, HL7 PA match/merge. Golden keys, survivorship, stewardship, tokenized crosswalk — **no raw PHI in MDM tables**.

**Example:** `configs/mdm/mdm_rules.yaml` — entities: member, provider, organization, coverage.

---

### 47. Q486 — CI/CD architecture?

**Answer:** GitLab CI: validate → test → security → build → deploy-stage → deploy-prod. Every MR runs pytest + FHIR baseline; main unlocks manual Seiji and DAB deploys. No prod without green CI on commit SHA.

**Example:** MR validate+test green → manual stage Seiji → CMS smoke → prod gate.

---

## Section 9 — Latest attachments (2026 hot topics)

### 48. Q536 — Three CMS-0057 auth paths?

**Answer:** **PAA:** member SAML → SMART PKCE → FITE us-core/carin-bb. **PVA:** Apigee → SLAP client_credentials → FITE `/atr-consumer`. **P2P:** Apigee → SLAP PDex token → FITE `/pdexv2` bulk match/export.

**Example:** Shared: SLAP + FITE + Firely. Different: IGs, scopes, auth models. See `configs/mdp/auth_paths.json`.

---

### 49. Q541 — Shared vs different across PAA, PVA, P2P?

**Answer:** **Shared:** SLAP, FITE, Firely. **Different:** IGs (US Core/CARIN vs PDex), scopes, auth (member SMART vs client_credentials), gateway (Apigee for PVA/P2P).

**Example:** Never mix — member SMART token cannot call `/pdexv2`.

---

### 50. Q543 — ePA Option A (Gainwell pattern)?

**Answer:** Batch/SFTP path: Routing-DIR → AWS Transfer SFTP → Gainwell PAS vendor → ClaimResponse batch (837/275/CSV) → Databricks → Firely. Legacy PAS; no real-time PAS API.

**Example:** Contrast with Option B (Wellmark): real-time Jiva PAS APIs + FHIR Subscription callbacks. Shared ingress: ALB → APISIX → CDS + dapr.

---

## 30-second cram sheet (memorize last)

| If they ask… | Say this |
|--------------|----------|
| Platform | Abacus = data, Onyx = APIs, FITE gates Firely |
| CMS-9115 vs 0057 | 9115 = Patient/Directory/Formulary; 0057 adds Provider Access, P2P, ePA |
| Deadline | Jan 2027 full CMS-0057 |
| Data layers | Raw → FM → SAM → FHIR → Firely |
| Auth | Patient = SMART PKCE; Provider/P2P = Backend Services |
| Three auth paths | PAA member SAML; PVA `/atr-consumer`; P2P `/pdexv2` |
| ePA | CRD → DTR → PAS; Option A = SFTP batch, Option B = real-time |
| Failure #1 | PVD before Claims — Practitioner references |
| Incremental | Watermark in `onyx_job_state` |
| PHI | Never in logs; de-id before analytics/LLM |

---

*Generated from Healthcare Interop Interview Cheat Sheet (553 Q). For runnable drills, use the **Script** block on each full Q entry.*
