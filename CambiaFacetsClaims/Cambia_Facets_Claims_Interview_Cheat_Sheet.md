# Cambia Facets Claims — Interview Answer Cheat Sheet

> TriZetto Facets on-prem → Abacus NextGen (cambia02) | 553 questions + Glossary
> **Aligned to 4 proficiency pillars:** E2E Implementation · Facets/TriZetto SME · On-Prem→Cloud Migration · Postman API Role
> **Learn first:** [LEARN_FROM_STEP_1.md](/Users/ashishsingh/CambiaFacetsClaims/Training/LEARN_FROM_STEP_1.md)

## Four Proficiency Pillars

| Pillar | Focus | Primary Sections | Exit Proof |
|--------|-------|------------------|------------|
| **P1 — E2E Implementation** | Own full pipeline delivery | A, C, D, G, H, I, M, Q, X, Y, Z | All phase0 scripts green; Databricks chain validated |
| **P2 — Facets/TriZetto SME** | Claim domain, CMC tables, volumes | B, K, T, U, W | Explain CLCL lifecycle + table joins without notes |
| **P3 — On-Prem→Cloud Migration** | VPN, cutover, phased gates | F, L, N, P, R, S, V, AA, AB | migration_cutover_checklist.sh + parallel-run parity |
| **P4 — Postman API Role** | Orchestration + FHIR contract testing | E, O, AB | newman smoke green on dev/stg before promotion |

## Answer Format

| Segment | Purpose |
|---------|---------|
| **Pillar** | Which proficiency area this question proves |
| **Answer** | What to say (ownership voice) |
| **Example** | Real Cambia Facets scenario |
| **How to Check** | Verification steps / Postman / SQL |
| **How to Fix** | Remediation if check fails |
| **Script** | Runnable proof for role proficiency |

## Role Map (by Pillar)

| Target Role | Pillars | Primary Sections |
|-------------|---------|------------------|
| **E2E Implementation Lead** | P1 | A, C, D, G, H, I, M, Q, Y |
| **Facets/TriZetto SME** | P2 | B, K, T, U, W |
| **Migration Engineer** | P3 | F, L, N, P, R, S, AA |
| **Postman/API Engineer** | P4 | E, O, AB |
| **Data Engineer** | P1+P2 | D, Q, H, X |
| **Forward Deployed Engineer** | P1+P3 | I, M, S, P |
| **DevOps Engineer** | P1+P3 | Z |

## Implementation Phases

| Phase | Pillar | You Will Proficiently... |
|-------|--------|--------------------------|
| **Phase 0** | P1 | Trace E2E architecture; run local CI; map repos |
| **Phase 1** | P2+P3 | Speak Facets domain; implement CDC + VPN path |
| **Phase 2** | P1 | Build bronze→gold medallion; dual FM paths |
| **Phase 3** | P4 | Postman collections for orchestration + FHIR smoke |
| **Phase 4** | P3+P4 | Migration cutover gates; newman prod smoke; Snowflake/Reltio |

## Table of Contents

- [Learn From Step 1](/Users/ashishsingh/CambiaFacetsClaims/Training/LEARN_FROM_STEP_1.md)
- [Postman API Role Guide](/Users/ashishsingh/CambiaFacetsClaims/docs/POSTMAN_API_ROLE.md)
- [Glossary](#glossary)
- [Section A: Opening & E2E Implementation Role Fit (Q1–10) · P1](#section-a-opening-e2e-implementation-role-fit-q110)
- [Section B: TriZetto Facets Claims Domain SME (Q11–28) · P2](#section-b-trizetto-facets-claims-domain-sme-q1128)
- [Section C: E2E Architecture & Implementation Design (Q29–45) · P1](#section-c-e2e-architecture-implementation-design-q2945)
- [Section D: Medallion Implementation — Bronze/Silver/Gold (Q46–73) · P1](#section-d-medallion-implementation-bronzesilvergold-q4673)
- [Section E: FHIR/SAM API Implementation & Postman Validation (Q74–94) · P1+P4](#section-e-fhirsam-api-implementation-postman-validation-q7494)
- [Section F: Migration Security & On-Prem Compliance (Q95–112) · P3](#section-f-migration-security-on-prem-compliance-q95112)
- [Section G: CDC Implementation — facets-core (Q113–124) · P1+P3](#section-g-cdc-implementation-facets-core-q113124)
- [Section H: Dual Gold Implementation Paths (Q125–141) · P1](#section-h-dual-gold-implementation-paths-q125141)
- [Section I: E2E Operations & Troubleshooting (Q142–154) · P1](#section-i-e2e-operations-troubleshooting-q142154)
- [Section J: Implementation KPIs & Delivery Metrics (Q155–162) · P1](#section-j-implementation-kpis-delivery-metrics-q155162)
- [Section K: Facets Claim Lifecycle & RCM SME (Q163–172) · P2](#section-k-facets-claim-lifecycle-rcm-sme-q163172)
- [Section L: On-Prem → Cloud Migration Program Leadership (Q173–185) · P3](#section-l-on-prem-to-cloud-migration-program-leadership-q173185)
- [Section M: E2E Scenario Troubleshooting (Q186–195) · P1](#section-m-e2e-scenario-troubleshooting-q186195)
- [Section N: Snowflake Egress Cloud Migration (Q196–205) · P3](#section-n-snowflake-egress-cloud-migration-q196205)
- [Section O: Orchestration APIs — ng-orchestration-service (Q206–250) · P1+P4](#section-o-orchestration-apis-ng-orchestration-service-q206250)
- [Section P: On-Prem Handoff — SFTP & Landing Zone (Q251–295) · P3](#section-p-on-prem-handoff-sftp-landing-zone-q251295)
- [Section Q: Databricks Engineering Implementation (Q296–330) · P1](#section-q-databricks-engineering-implementation-q296330)
- [Section R: MDM/Reltio Cloud Migration (Q331–360) · P3](#section-r-mdmreltio-cloud-migration-q331360)
- [Section S: VPN & On-Prem Network Migration (Q361–390) · P3](#section-s-vpn-on-prem-network-migration-q361390)
- [Section T: SQL Server CDC & Facets Source SME (Q391–415) · P2+P3](#section-t-sql-server-cdc-facets-source-sme-q391415)
- [Section U: Production Scale & TriZetto Volume Profiles (Q416–445) · P2](#section-u-production-scale-trizetto-volume-profiles-q416445)
- [Section V: De-Identification for Migration Analytics (Q446–455) · P3](#section-v-de-identification-for-migration-analytics-q446455)
- [Section W: Master Data Management — Facets Entities (Q456–465) · P2+P3](#section-w-master-data-management-facets-entities-q456465)
- [Section X: Interop vs CDP Implementation Comparison (Q466–473) · P1](#section-x-interop-vs-cdp-implementation-comparison-q466473)
- [Section Y: Observability & Delivery Monitoring (Q474–485) · P1](#section-y-observability-delivery-monitoring-q474485)
- [Section Z: DevOps & CI/CD for Cloud Migration (Q486–515) · P1+P3](#section-z-devops-cicd-for-cloud-migration-q486515)
- [Section AA: Governance & Migration Compliance (Q516–535) · P3](#section-aa-governance-migration-compliance-q516535)
- [Section AB: Postman Collections & Cambia Cutover (Q536–553) · P4+P3](#section-ab-postman-collections-cambia-cutover-q536553)

## Section A: Opening & E2E Implementation Role Fit

> **Pillar:** P1 — E2E Implementation Proficiency

### Q1. Tell me about your end-to-end implementation experience with payer claims migration pipelines.

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I led Cambia Facets Claims implementation from on-prem TriZetto Facets through VPN, bespoke CDC, encrypted landing, Databricks medallion, dual gold FM, and downstream SAM/FHIR + Snowflake. I personally owned manifest triggers, bronze SCD2 loads, and Postman-validated API handoffs—not architecture slides alone.

**Example:** Nightly Facets_BatchJobComplete trigger → ng-orchestration-service → bronze CMC_CLCL_CLAIM → silver.unified_timeline_claim → gold.fm_claim → Postman-validated FHIR Claim resources.

**How to Check:**
- Run phase0_architecture_trace.sh; verify Databricks job chain green for cambia02; Postman collection smoke on orchestration + FHIR endpoints.

**How to Fix:**
- Map all 5 implementation stages to owners and Postman smoke tests before sprint 1.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q1: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q2. What makes you a TriZetto Facets SME for this migration?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I know Facets claim grain (CMC_CLCL_CLAIM header, CMC_CDML/CMC_CDDL line tables), CLCL status lifecycle (11/15/01/02/91), medical vs dental types (M/H vs D), and how Cambia nightly batch timing drives CDC trigger files—not just cloud pipeline mechanics.

**Example:** A pended claim (status 11) adjusting to final (02) creates two SCD2 versions in bronze and a new row in silver.unified_timeline_claim.

**How to Check:**
- Query bronze.cmc_clst_status joins; compare CLCL status distribution pre/post batch.

**How to Fix:**
- Pair with Cambia claims ops for status code changes; never assume CMS semantics map 1:1 to Facets CLCL codes.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q2: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q3. How do you approach on-prem client migration to cloud for Facets claims?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I treat migration as phased cutover: VPN connectivity first, then historical CDC backfill (~99M claims), then incremental + nightly trigger parity, then medallion validation, then downstream Snowflake/Reltio with rollback checkpoints at each gate.

**Example:** facets-core runs outside HITRUST; encryption at CDC output before SFTP landing in cambia02 NextGen zone.

**How to Check:**
- Document 1.0 vs NextGen cutover state with #xform-xport; verify VPN uptime and CdcGlobals lock behavior during parallel run.

**How to Fix:**
- Never big-bang cutover; maintain parallel validation window with row-count and signature bitmap checks.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q3: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q4. What is your Postman API role in the Facets Claims implementation?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I use Postman to validate orchestration callbacks, manifest-trigger endpoints, SAM/FHIR resource shapes, and cutover smoke tests—before declaring a migration phase complete. Collections are environment-scoped (dev/stg/prd) with no PHI in saved examples.

**Example:** Postman collection: orchestration manifest-received → Databricks job status poll → FHIR Claim GET by resource ID → assert US Core profiles.

**How to Check:**
- newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json

**How to Fix:**
- Store tokens in Postman environment secrets; never commit credentials or member IDs to collection JSON.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q4: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q5. How do you demonstrate proficiency in E2E implementation ownership and delivery accountability?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E implementation ownership and delivery accountability with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q5: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q6. How do you demonstrate proficiency in E2E implementation ownership and delivery accountability?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E implementation ownership and delivery accountability with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q6: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q7. How do you demonstrate proficiency in E2E implementation ownership and delivery accountability?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E implementation ownership and delivery accountability with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q7: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q8. How do you demonstrate proficiency in E2E implementation ownership and delivery accountability?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E implementation ownership and delivery accountability with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q8: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q9. How do you demonstrate proficiency in E2E implementation ownership and delivery accountability?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E implementation ownership and delivery accountability with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q9: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q10. How do you demonstrate proficiency in E2E implementation ownership and delivery accountability?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E implementation ownership and delivery accountability with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q10: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```


## Section B: TriZetto Facets Claims Domain SME

> **Pillar:** P2 — Facets & TriZetto SME

### Q11. Explain TriZetto Facets claim header and line table relationships.

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** CMC_CLCL_CLAIM is the claim header grain. Medical lines live in CMC_CDML_CL_LINE (M/H types); dental in CMC_CDDL_CL_LINE (D type). Diagnosis, status, member, and subscriber tables join at claim_id. This is the source shape facets-core partitions into ~25 JSON files per CDC batch.

**Example:** One CLCL claim with 3 medical lines and 1 dental line → header JSON + CDML partition + CDDL partition + diagnosis partition in manifest.

**How to Check:**
- SELECT claim_id, COUNT(*) FROM bronze.cmc_cdml_cl_line GROUP BY claim_id LIMIT 10

**How to Fix:**
- Never flatten dental into medical lines; Interop gold filters dental at FM layer, CDP retains all.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q11: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q12. How do you demonstrate proficiency in TriZetto Facets claim domain, CMC tables, and status lifecycle?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto Facets claim domain, CMC tables, and status lifecycle with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q12: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q13. How do you demonstrate proficiency in TriZetto Facets claim domain, CMC tables, and status lifecycle?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto Facets claim domain, CMC tables, and status lifecycle with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q13: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q14. How do you demonstrate proficiency in TriZetto Facets claim domain, CMC tables, and status lifecycle?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto Facets claim domain, CMC tables, and status lifecycle with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q14: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q15. How do you demonstrate proficiency in TriZetto Facets claim domain, CMC tables, and status lifecycle?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto Facets claim domain, CMC tables, and status lifecycle with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q15: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q16. How do you demonstrate proficiency in TriZetto Facets claim domain, CMC tables, and status lifecycle?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto Facets claim domain, CMC tables, and status lifecycle with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q16: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q17. How do you demonstrate proficiency in TriZetto Facets claim domain, CMC tables, and status lifecycle?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto Facets claim domain, CMC tables, and status lifecycle with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q17: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q18. How do you demonstrate proficiency in TriZetto Facets claim domain, CMC tables, and status lifecycle?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto Facets claim domain, CMC tables, and status lifecycle with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q18: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q19. How do you demonstrate proficiency in TriZetto Facets claim domain, CMC tables, and status lifecycle?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto Facets claim domain, CMC tables, and status lifecycle with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q19: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q20. How do you demonstrate proficiency in TriZetto Facets claim domain, CMC tables, and status lifecycle?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto Facets claim domain, CMC tables, and status lifecycle with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q20: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q21. How do you demonstrate proficiency in TriZetto Facets claim domain, CMC tables, and status lifecycle?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto Facets claim domain, CMC tables, and status lifecycle with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q21: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q22. How do you demonstrate proficiency in TriZetto Facets claim domain, CMC tables, and status lifecycle?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto Facets claim domain, CMC tables, and status lifecycle with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q22: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q23. How do you demonstrate proficiency in TriZetto Facets claim domain, CMC tables, and status lifecycle?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto Facets claim domain, CMC tables, and status lifecycle with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q23: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q24. How do you demonstrate proficiency in TriZetto Facets claim domain, CMC tables, and status lifecycle?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto Facets claim domain, CMC tables, and status lifecycle with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q24: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q25. How do you demonstrate proficiency in TriZetto Facets claim domain, CMC tables, and status lifecycle?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto Facets claim domain, CMC tables, and status lifecycle with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q25: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q26. How do you demonstrate proficiency in TriZetto Facets claim domain, CMC tables, and status lifecycle?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto Facets claim domain, CMC tables, and status lifecycle with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q26: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q27. How do you demonstrate proficiency in TriZetto Facets claim domain, CMC tables, and status lifecycle?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto Facets claim domain, CMC tables, and status lifecycle with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q27: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q28. How do you demonstrate proficiency in TriZetto Facets claim domain, CMC tables, and status lifecycle?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto Facets claim domain, CMC tables, and status lifecycle with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q28: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```


## Section C: E2E Architecture & Implementation Design

> **Pillar:** P1 — E2E Implementation Proficiency

### Q29. Walk through the E2E implementation architecture you would own.

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** Stage 1: on-prem Facets SQL Server via Palo Alto VPN. Stage 2: facets-core CDC → encrypted JSON + manifest. Stage 3: SFTP landing → bronze SCD2 (AIR). Stage 4: silver unified timeline → dual gold FM. Stage 5: SAM/FHIR + Snowflake + Reltio. Postman validates each handoff.

**Example:** Implementation exit criteria per stage: VPN up, CDC manifest valid, bronze row counts match, gold Interop/CDP ratio expected, Postman FHIR smoke green.

**How to Check:**
- Run all phase0 scripts + Postman smoke collection against dev.

**How to Fix:**
- Whiteboard all 5 stages with repo, owner, and Postman check at each boundary.

**Script:** *(builds proficiency: E2E Implementation Lead | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q29: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q30. How do you demonstrate proficiency in E2E architecture design and implementation boundaries?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E architecture design and implementation boundaries with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q30: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q31. How do you demonstrate proficiency in E2E architecture design and implementation boundaries?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E architecture design and implementation boundaries with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q31: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q32. How do you demonstrate proficiency in E2E architecture design and implementation boundaries?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E architecture design and implementation boundaries with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q32: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q33. How do you demonstrate proficiency in E2E architecture design and implementation boundaries?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E architecture design and implementation boundaries with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q33: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q34. How do you demonstrate proficiency in E2E architecture design and implementation boundaries?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E architecture design and implementation boundaries with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q34: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q35. How do you demonstrate proficiency in E2E architecture design and implementation boundaries?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E architecture design and implementation boundaries with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q35: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q36. How do you demonstrate proficiency in E2E architecture design and implementation boundaries?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E architecture design and implementation boundaries with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q36: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q37. How do you demonstrate proficiency in E2E architecture design and implementation boundaries?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E architecture design and implementation boundaries with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q37: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q38. How do you demonstrate proficiency in E2E architecture design and implementation boundaries?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E architecture design and implementation boundaries with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q38: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q39. How do you demonstrate proficiency in E2E architecture design and implementation boundaries?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E architecture design and implementation boundaries with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q39: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q40. How do you demonstrate proficiency in E2E architecture design and implementation boundaries?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E architecture design and implementation boundaries with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q40: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q41. How do you demonstrate proficiency in E2E architecture design and implementation boundaries?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E architecture design and implementation boundaries with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q41: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q42. How do you demonstrate proficiency in E2E architecture design and implementation boundaries?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E architecture design and implementation boundaries with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q42: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q43. How do you demonstrate proficiency in E2E architecture design and implementation boundaries?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E architecture design and implementation boundaries with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q43: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q44. How do you demonstrate proficiency in E2E architecture design and implementation boundaries?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E architecture design and implementation boundaries with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q44: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q45. How do you demonstrate proficiency in E2E architecture design and implementation boundaries?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E architecture design and implementation boundaries with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q45: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```


## Section D: Medallion Implementation — Bronze/Silver/Gold

> **Pillar:** P1 — E2E Implementation Proficiency

### Q46. How do you implement bronze ingestion for Facets claims?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** Manifest-triggered Databricks workflows load encrypted JSON into 44+ bronze SCD2 tables via AIR library. I validate each batch: manifest file count (~25), checksums, and CMC_CLCL_CLAIM row delta vs CDC change IDs before promoting silver.

**Example:** 420 Facets bronze tables in prod; key tables: CMC_CLCL_CLAIM, CMC_CDML_CL_LINE, CMC_CDDL_CL_LINE, CMC_CLST_STATUS, CMC_MEME_MEMBER, CMC_SBSB_SUBSC.

**How to Check:**
- SELECT COUNT(*) FROM bronze.cmc_clcl_claim WHERE _is_current = true

**How to Fix:**
- Fail closed on manifest/schema mismatch; never run bronze without valid manifest.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q46: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q47. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q47: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q48. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q48: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q49. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q49: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q50. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q50: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q51. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q51: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q52. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q52: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q53. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q53: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q54. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q54: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q55. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q55: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q56. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q56: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q57. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q57: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q58. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q58: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q59. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q59: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q60. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q60: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q61. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q61: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q62. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q62: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q63. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q63: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q64. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q64: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q65. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q65: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q66. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q66: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q67. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q67: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q68. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q68: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q69. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q69: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q70. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q70: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q71. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q71: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q72. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q72: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q73. How do you demonstrate proficiency in medallion layer implementation — bronze SCD2 through dual gold?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own medallion layer implementation — bronze SCD2 through dual gold with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q73: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```


## Section E: FHIR/SAM API Implementation & Postman Validation

> **Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

### Q74. How do you use Postman to validate FHIR/SAM output from gold Facets tables?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** After gold.fm_claim load, I run Postman requests against FITE/Firely (or dev FHIR gateway): GET Claim, ClaimCoverage, ClaimDiagnosis by test member; assert meta.profile US Core URLs; verify dental claims absent from Interop path but present in CDP validation collection.

**Example:** Collection folder: Interop Claims (75-group filter) vs CDP Claims (full set); separate environment variables for each path.

**How to Check:**
- newman run postman/fhir-claims-interop.json --folder 'Claim Read' -e postman/env/stg.json

**How to Fix:**
- Rotate test patient IDs via environment; never hardcode PHI in collection bodies.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q74: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q75. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q75: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q76. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q76: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q77. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q77: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q78. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q78: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q79. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q79: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q80. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q80: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q81. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q81: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q82. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q82: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q83. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q83: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q84. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q84: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q85. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q85: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q86. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q86: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q87. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q87: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q88. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q88: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q89. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q89: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q90. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q90: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q91. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q91: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q92. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q92: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q93. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q93: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q94. How do you demonstrate proficiency in FHIR/SAM API implementation and Postman contract validation?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own FHIR/SAM API implementation and Postman contract validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q94: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```


## Section F: Migration Security & On-Prem Compliance

> **Pillar:** P3 — On-Prem → Cloud Migration

### Q95. What security controls apply during on-prem to cloud migration?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** facets-core CDC is outside HITRUST boundary. Encryption before landing; VPN-only path to on-prem replica; IAM least privilege for air-cd on KMS keys; audit logs without PHI; Postman environments use synthetic test IDs only.

**Example:** KMS decrypt on landing zone keys granted to air-cd deployment role per workspace rules.

**How to Check:**
- Verify encryption on intermediate S3 objects; confirm no plaintext secrets in facets-infrastructure Terraform.

**How to Fix:**
- Obtain security/compliance review before prod cutover; fail closed on missing secrets.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q95: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q95: migration gate checklist complete
```

### Q96. How do you demonstrate proficiency in migration security, HITRUST boundary, and encryption handoff?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own migration security, HITRUST boundary, and encryption handoff with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q96: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q96: migration gate checklist complete
```

### Q97. How do you demonstrate proficiency in migration security, HITRUST boundary, and encryption handoff?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own migration security, HITRUST boundary, and encryption handoff with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q97: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q97: migration gate checklist complete
```

### Q98. How do you demonstrate proficiency in migration security, HITRUST boundary, and encryption handoff?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own migration security, HITRUST boundary, and encryption handoff with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q98: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q98: migration gate checklist complete
```

### Q99. How do you demonstrate proficiency in migration security, HITRUST boundary, and encryption handoff?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own migration security, HITRUST boundary, and encryption handoff with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q99: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q99: migration gate checklist complete
```

### Q100. How do you demonstrate proficiency in migration security, HITRUST boundary, and encryption handoff?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own migration security, HITRUST boundary, and encryption handoff with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q100: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q100: migration gate checklist complete
```

### Q101. How do you demonstrate proficiency in migration security, HITRUST boundary, and encryption handoff?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own migration security, HITRUST boundary, and encryption handoff with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q101: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q101: migration gate checklist complete
```

### Q102. How do you demonstrate proficiency in migration security, HITRUST boundary, and encryption handoff?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own migration security, HITRUST boundary, and encryption handoff with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q102: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q102: migration gate checklist complete
```

### Q103. How do you demonstrate proficiency in migration security, HITRUST boundary, and encryption handoff?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own migration security, HITRUST boundary, and encryption handoff with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q103: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q103: migration gate checklist complete
```

### Q104. How do you demonstrate proficiency in migration security, HITRUST boundary, and encryption handoff?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own migration security, HITRUST boundary, and encryption handoff with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q104: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q104: migration gate checklist complete
```

### Q105. How do you demonstrate proficiency in migration security, HITRUST boundary, and encryption handoff?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own migration security, HITRUST boundary, and encryption handoff with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q105: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q105: migration gate checklist complete
```

### Q106. How do you demonstrate proficiency in migration security, HITRUST boundary, and encryption handoff?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own migration security, HITRUST boundary, and encryption handoff with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q106: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q106: migration gate checklist complete
```

### Q107. How do you demonstrate proficiency in migration security, HITRUST boundary, and encryption handoff?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own migration security, HITRUST boundary, and encryption handoff with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q107: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q107: migration gate checklist complete
```

### Q108. How do you demonstrate proficiency in migration security, HITRUST boundary, and encryption handoff?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own migration security, HITRUST boundary, and encryption handoff with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q108: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q108: migration gate checklist complete
```

### Q109. How do you demonstrate proficiency in migration security, HITRUST boundary, and encryption handoff?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own migration security, HITRUST boundary, and encryption handoff with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q109: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q109: migration gate checklist complete
```

### Q110. How do you demonstrate proficiency in migration security, HITRUST boundary, and encryption handoff?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own migration security, HITRUST boundary, and encryption handoff with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q110: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q110: migration gate checklist complete
```

### Q111. How do you demonstrate proficiency in migration security, HITRUST boundary, and encryption handoff?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own migration security, HITRUST boundary, and encryption handoff with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q111: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q111: migration gate checklist complete
```

### Q112. How do you demonstrate proficiency in migration security, HITRUST boundary, and encryption handoff?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own migration security, HITRUST boundary, and encryption handoff with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q112: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q112: migration gate checklist complete
```


## Section G: CDC Implementation — facets-core

> **Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

### Q113. How do you implement Facets CDC extraction?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** SQL Server CDC on read replica → unique change IDs → partitioned JSON → encryption → manifest.json. Step Functions + Lambda + Batch. One job per domain via DynamoDB CdcGlobals lock. Nightly Facets_BatchJobComplete trigger file kicks CDC after Cambia batch.

**Example:** ~25 JSON files per batch; intermediate S3 abacus-facets-intermediate-<env>/claims-incremental/.

**How to Check:**
- Step Functions execution history; CdcGlobals lock state; manifest at cambia/facets/cambia/claims/extension/incremental/*/*manifest.json

**How to Fix:**
- Never query Facets primary; replica only. Drop overlapping CDC runs when lock held.

**Script:** *(builds proficiency: E2E Implementation Lead | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q113: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q113: CDC + VPN path verified
```

### Q114. How do you demonstrate proficiency in facets-core CDC implementation and Batch orchestration?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own facets-core CDC implementation and Batch orchestration with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q114: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q114: CDC + VPN path verified
```

### Q115. How do you demonstrate proficiency in facets-core CDC implementation and Batch orchestration?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own facets-core CDC implementation and Batch orchestration with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q115: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q115: CDC + VPN path verified
```

### Q116. How do you demonstrate proficiency in facets-core CDC implementation and Batch orchestration?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own facets-core CDC implementation and Batch orchestration with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q116: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q116: CDC + VPN path verified
```

### Q117. How do you demonstrate proficiency in facets-core CDC implementation and Batch orchestration?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own facets-core CDC implementation and Batch orchestration with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q117: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q117: CDC + VPN path verified
```

### Q118. How do you demonstrate proficiency in facets-core CDC implementation and Batch orchestration?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own facets-core CDC implementation and Batch orchestration with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q118: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q118: CDC + VPN path verified
```

### Q119. How do you demonstrate proficiency in facets-core CDC implementation and Batch orchestration?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own facets-core CDC implementation and Batch orchestration with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q119: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q119: CDC + VPN path verified
```

### Q120. How do you demonstrate proficiency in facets-core CDC implementation and Batch orchestration?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own facets-core CDC implementation and Batch orchestration with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q120: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q120: CDC + VPN path verified
```

### Q121. How do you demonstrate proficiency in facets-core CDC implementation and Batch orchestration?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own facets-core CDC implementation and Batch orchestration with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q121: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q121: CDC + VPN path verified
```

### Q122. How do you demonstrate proficiency in facets-core CDC implementation and Batch orchestration?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own facets-core CDC implementation and Batch orchestration with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q122: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q122: CDC + VPN path verified
```

### Q123. How do you demonstrate proficiency in facets-core CDC implementation and Batch orchestration?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own facets-core CDC implementation and Batch orchestration with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q123: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q123: CDC + VPN path verified
```

### Q124. How do you demonstrate proficiency in facets-core CDC implementation and Batch orchestration?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own facets-core CDC implementation and Batch orchestration with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q124: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q124: CDC + VPN path verified
```


## Section H: Dual Gold Implementation Paths

> **Pillar:** P1 — E2E Implementation Proficiency

### Q125. How do you demonstrate proficiency in Interop vs CDP dual gold implementation and filtering?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP dual gold implementation and filtering with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```bash
#!/usr/bin/env bash
# Q125: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q126. How do you demonstrate proficiency in Interop vs CDP dual gold implementation and filtering?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP dual gold implementation and filtering with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```bash
#!/usr/bin/env bash
# Q126: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q127. How do you demonstrate proficiency in Interop vs CDP dual gold implementation and filtering?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP dual gold implementation and filtering with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```bash
#!/usr/bin/env bash
# Q127: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q128. How do you demonstrate proficiency in Interop vs CDP dual gold implementation and filtering?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP dual gold implementation and filtering with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```bash
#!/usr/bin/env bash
# Q128: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q129. How do you demonstrate proficiency in Interop vs CDP dual gold implementation and filtering?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP dual gold implementation and filtering with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```bash
#!/usr/bin/env bash
# Q129: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q130. How do you demonstrate proficiency in Interop vs CDP dual gold implementation and filtering?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP dual gold implementation and filtering with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```bash
#!/usr/bin/env bash
# Q130: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q131. How do you demonstrate proficiency in Interop vs CDP dual gold implementation and filtering?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP dual gold implementation and filtering with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```bash
#!/usr/bin/env bash
# Q131: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q132. How do you demonstrate proficiency in Interop vs CDP dual gold implementation and filtering?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP dual gold implementation and filtering with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```bash
#!/usr/bin/env bash
# Q132: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q133. How do you demonstrate proficiency in Interop vs CDP dual gold implementation and filtering?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP dual gold implementation and filtering with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```bash
#!/usr/bin/env bash
# Q133: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q134. How do you demonstrate proficiency in Interop vs CDP dual gold implementation and filtering?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP dual gold implementation and filtering with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```bash
#!/usr/bin/env bash
# Q134: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q135. How do you demonstrate proficiency in Interop vs CDP dual gold implementation and filtering?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP dual gold implementation and filtering with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```bash
#!/usr/bin/env bash
# Q135: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q136. How do you demonstrate proficiency in Interop vs CDP dual gold implementation and filtering?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP dual gold implementation and filtering with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```bash
#!/usr/bin/env bash
# Q136: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q137. How do you demonstrate proficiency in Interop vs CDP dual gold implementation and filtering?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP dual gold implementation and filtering with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```bash
#!/usr/bin/env bash
# Q137: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q138. How do you demonstrate proficiency in Interop vs CDP dual gold implementation and filtering?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP dual gold implementation and filtering with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```bash
#!/usr/bin/env bash
# Q138: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q139. How do you demonstrate proficiency in Interop vs CDP dual gold implementation and filtering?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP dual gold implementation and filtering with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```bash
#!/usr/bin/env bash
# Q139: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q140. How do you demonstrate proficiency in Interop vs CDP dual gold implementation and filtering?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP dual gold implementation and filtering with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```bash
#!/usr/bin/env bash
# Q140: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q141. How do you demonstrate proficiency in Interop vs CDP dual gold implementation and filtering?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP dual gold implementation and filtering with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```bash
#!/usr/bin/env bash
# Q141: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```


## Section I: E2E Operations & Troubleshooting

> **Pillar:** P1 — E2E Implementation Proficiency

### Q142. How do you demonstrate proficiency in E2E deploy, monitor, restore, and incident response?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E deploy, monitor, restore, and incident response with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q142: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q143. How do you demonstrate proficiency in E2E deploy, monitor, restore, and incident response?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E deploy, monitor, restore, and incident response with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q143: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q144. How do you demonstrate proficiency in E2E deploy, monitor, restore, and incident response?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E deploy, monitor, restore, and incident response with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q144: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q145. How do you demonstrate proficiency in E2E deploy, monitor, restore, and incident response?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E deploy, monitor, restore, and incident response with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q145: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q146. How do you demonstrate proficiency in E2E deploy, monitor, restore, and incident response?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E deploy, monitor, restore, and incident response with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q146: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q147. How do you demonstrate proficiency in E2E deploy, monitor, restore, and incident response?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E deploy, monitor, restore, and incident response with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q147: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q148. How do you demonstrate proficiency in E2E deploy, monitor, restore, and incident response?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E deploy, monitor, restore, and incident response with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q148: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q149. How do you demonstrate proficiency in E2E deploy, monitor, restore, and incident response?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E deploy, monitor, restore, and incident response with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q149: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q150. How do you demonstrate proficiency in E2E deploy, monitor, restore, and incident response?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E deploy, monitor, restore, and incident response with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q150: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q151. How do you demonstrate proficiency in E2E deploy, monitor, restore, and incident response?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E deploy, monitor, restore, and incident response with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q151: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q152. How do you demonstrate proficiency in E2E deploy, monitor, restore, and incident response?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E deploy, monitor, restore, and incident response with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q152: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q153. How do you demonstrate proficiency in E2E deploy, monitor, restore, and incident response?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E deploy, monitor, restore, and incident response with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q153: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q154. How do you demonstrate proficiency in E2E deploy, monitor, restore, and incident response?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E deploy, monitor, restore, and incident response with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q154: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```


## Section J: Implementation KPIs & Delivery Metrics

> **Pillar:** P1 — E2E Implementation Proficiency

### Q155. How do you demonstrate proficiency in implementation KPIs, batch SLAs, and delivery metrics?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own implementation KPIs, batch SLAs, and delivery metrics with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q155: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q156. How do you demonstrate proficiency in implementation KPIs, batch SLAs, and delivery metrics?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own implementation KPIs, batch SLAs, and delivery metrics with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q156: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q157. How do you demonstrate proficiency in implementation KPIs, batch SLAs, and delivery metrics?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own implementation KPIs, batch SLAs, and delivery metrics with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q157: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q158. How do you demonstrate proficiency in implementation KPIs, batch SLAs, and delivery metrics?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own implementation KPIs, batch SLAs, and delivery metrics with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q158: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q159. How do you demonstrate proficiency in implementation KPIs, batch SLAs, and delivery metrics?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own implementation KPIs, batch SLAs, and delivery metrics with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q159: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q160. How do you demonstrate proficiency in implementation KPIs, batch SLAs, and delivery metrics?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own implementation KPIs, batch SLAs, and delivery metrics with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q160: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q161. How do you demonstrate proficiency in implementation KPIs, batch SLAs, and delivery metrics?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own implementation KPIs, batch SLAs, and delivery metrics with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q161: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q162. How do you demonstrate proficiency in implementation KPIs, batch SLAs, and delivery metrics?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own implementation KPIs, batch SLAs, and delivery metrics with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q162: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```


## Section K: Facets Claim Lifecycle & RCM SME

> **Pillar:** P2 — Facets & TriZetto SME

### Q163. How do you demonstrate proficiency in Facets claim lifecycle, adjustment logic, and RCM bridge?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own Facets claim lifecycle, adjustment logic, and RCM bridge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Solution Architect)*

```sql
-- Q163: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q164. How do you demonstrate proficiency in Facets claim lifecycle, adjustment logic, and RCM bridge?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own Facets claim lifecycle, adjustment logic, and RCM bridge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Solution Architect)*

```sql
-- Q164: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q165. How do you demonstrate proficiency in Facets claim lifecycle, adjustment logic, and RCM bridge?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own Facets claim lifecycle, adjustment logic, and RCM bridge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Solution Architect)*

```sql
-- Q165: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q166. How do you demonstrate proficiency in Facets claim lifecycle, adjustment logic, and RCM bridge?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own Facets claim lifecycle, adjustment logic, and RCM bridge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Solution Architect)*

```sql
-- Q166: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q167. How do you demonstrate proficiency in Facets claim lifecycle, adjustment logic, and RCM bridge?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own Facets claim lifecycle, adjustment logic, and RCM bridge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Solution Architect)*

```sql
-- Q167: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q168. How do you demonstrate proficiency in Facets claim lifecycle, adjustment logic, and RCM bridge?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own Facets claim lifecycle, adjustment logic, and RCM bridge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Solution Architect)*

```sql
-- Q168: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q169. How do you demonstrate proficiency in Facets claim lifecycle, adjustment logic, and RCM bridge?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own Facets claim lifecycle, adjustment logic, and RCM bridge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Solution Architect)*

```sql
-- Q169: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q170. How do you demonstrate proficiency in Facets claim lifecycle, adjustment logic, and RCM bridge?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own Facets claim lifecycle, adjustment logic, and RCM bridge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Solution Architect)*

```sql
-- Q170: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q171. How do you demonstrate proficiency in Facets claim lifecycle, adjustment logic, and RCM bridge?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own Facets claim lifecycle, adjustment logic, and RCM bridge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Solution Architect)*

```sql
-- Q171: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q172. How do you demonstrate proficiency in Facets claim lifecycle, adjustment logic, and RCM bridge?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own Facets claim lifecycle, adjustment logic, and RCM bridge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Solution Architect)*

```sql
-- Q172: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```


## Section L: On-Prem → Cloud Migration Program Leadership

> **Pillar:** P3 — On-Prem → Cloud Migration

### Q173. How do you lead an on-prem Facets client migration program?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I run phased gates: (1) network/VPN, (2) historical backfill parity, (3) incremental schedule parity, (4) medallion validation, (5) downstream cutover. Each gate has row-count acceptance, Postman smoke, and rollback plan documented with Cambia + Abacus owners.

**Example:** Parallel run window: compare on-prem Facets report totals vs cambia02 gold.fm_claim_cambia signature bitmap for sample periods.

**How to Check:**
- Migration checklist in plan.md; sign-off from #xform-xport before prod promotion.

**How to Fix:**
- Weekly steering with claim ops (Facets SME) and platform (E2E owner); escalate VPN/CDC as P1.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q173: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q173: migration gate checklist complete
```

### Q174. How do you demonstrate proficiency in on-prem to cloud migration program leadership and cutover gates?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem to cloud migration program leadership and cutover gates with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q174: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q174: migration gate checklist complete
```

### Q175. How do you demonstrate proficiency in on-prem to cloud migration program leadership and cutover gates?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem to cloud migration program leadership and cutover gates with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q175: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q175: migration gate checklist complete
```

### Q176. How do you demonstrate proficiency in on-prem to cloud migration program leadership and cutover gates?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem to cloud migration program leadership and cutover gates with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q176: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q176: migration gate checklist complete
```

### Q177. How do you demonstrate proficiency in on-prem to cloud migration program leadership and cutover gates?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem to cloud migration program leadership and cutover gates with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q177: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q177: migration gate checklist complete
```

### Q178. How do you demonstrate proficiency in on-prem to cloud migration program leadership and cutover gates?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem to cloud migration program leadership and cutover gates with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q178: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q178: migration gate checklist complete
```

### Q179. How do you demonstrate proficiency in on-prem to cloud migration program leadership and cutover gates?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem to cloud migration program leadership and cutover gates with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q179: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q179: migration gate checklist complete
```

### Q180. How do you demonstrate proficiency in on-prem to cloud migration program leadership and cutover gates?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem to cloud migration program leadership and cutover gates with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q180: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q180: migration gate checklist complete
```

### Q181. How do you demonstrate proficiency in on-prem to cloud migration program leadership and cutover gates?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem to cloud migration program leadership and cutover gates with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q181: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q181: migration gate checklist complete
```

### Q182. How do you demonstrate proficiency in on-prem to cloud migration program leadership and cutover gates?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem to cloud migration program leadership and cutover gates with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q182: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q182: migration gate checklist complete
```

### Q183. How do you demonstrate proficiency in on-prem to cloud migration program leadership and cutover gates?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem to cloud migration program leadership and cutover gates with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q183: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q183: migration gate checklist complete
```

### Q184. How do you demonstrate proficiency in on-prem to cloud migration program leadership and cutover gates?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem to cloud migration program leadership and cutover gates with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q184: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q184: migration gate checklist complete
```

### Q185. How do you demonstrate proficiency in on-prem to cloud migration program leadership and cutover gates?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem to cloud migration program leadership and cutover gates with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q185: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q185: migration gate checklist complete
```


## Section M: E2E Scenario Troubleshooting

> **Pillar:** P1 — E2E Implementation Proficiency

### Q186. How do you demonstrate proficiency in E2E incident scenarios — missed batch, lock contention, manifest mismatch?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E incident scenarios — missed batch, lock contention, manifest mismatch with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q186: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q187. How do you demonstrate proficiency in E2E incident scenarios — missed batch, lock contention, manifest mismatch?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E incident scenarios — missed batch, lock contention, manifest mismatch with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q187: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q188. How do you demonstrate proficiency in E2E incident scenarios — missed batch, lock contention, manifest mismatch?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E incident scenarios — missed batch, lock contention, manifest mismatch with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q188: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q189. How do you demonstrate proficiency in E2E incident scenarios — missed batch, lock contention, manifest mismatch?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E incident scenarios — missed batch, lock contention, manifest mismatch with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q189: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q190. How do you demonstrate proficiency in E2E incident scenarios — missed batch, lock contention, manifest mismatch?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E incident scenarios — missed batch, lock contention, manifest mismatch with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q190: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q191. How do you demonstrate proficiency in E2E incident scenarios — missed batch, lock contention, manifest mismatch?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E incident scenarios — missed batch, lock contention, manifest mismatch with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q191: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q192. How do you demonstrate proficiency in E2E incident scenarios — missed batch, lock contention, manifest mismatch?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E incident scenarios — missed batch, lock contention, manifest mismatch with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q192: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q193. How do you demonstrate proficiency in E2E incident scenarios — missed batch, lock contention, manifest mismatch?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E incident scenarios — missed batch, lock contention, manifest mismatch with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q193: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q194. How do you demonstrate proficiency in E2E incident scenarios — missed batch, lock contention, manifest mismatch?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E incident scenarios — missed batch, lock contention, manifest mismatch with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q194: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q195. How do you demonstrate proficiency in E2E incident scenarios — missed batch, lock contention, manifest mismatch?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own E2E incident scenarios — missed batch, lock contention, manifest mismatch with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q195: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```


## Section N: Snowflake Egress Cloud Migration

> **Pillar:** P3 — On-Prem → Cloud Migration

### Q196. How do you demonstrate proficiency in Snowflake egress as part of cloud migration cutover?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Snowflake egress as part of cloud migration cutover with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```sql
-- Q196: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q197. How do you demonstrate proficiency in Snowflake egress as part of cloud migration cutover?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Snowflake egress as part of cloud migration cutover with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```sql
-- Q197: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q198. How do you demonstrate proficiency in Snowflake egress as part of cloud migration cutover?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Snowflake egress as part of cloud migration cutover with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```sql
-- Q198: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q199. How do you demonstrate proficiency in Snowflake egress as part of cloud migration cutover?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Snowflake egress as part of cloud migration cutover with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```sql
-- Q199: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q200. How do you demonstrate proficiency in Snowflake egress as part of cloud migration cutover?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Snowflake egress as part of cloud migration cutover with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```sql
-- Q200: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q201. How do you demonstrate proficiency in Snowflake egress as part of cloud migration cutover?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Snowflake egress as part of cloud migration cutover with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```sql
-- Q201: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q202. How do you demonstrate proficiency in Snowflake egress as part of cloud migration cutover?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Snowflake egress as part of cloud migration cutover with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```sql
-- Q202: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q203. How do you demonstrate proficiency in Snowflake egress as part of cloud migration cutover?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Snowflake egress as part of cloud migration cutover with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```sql
-- Q203: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q204. How do you demonstrate proficiency in Snowflake egress as part of cloud migration cutover?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Snowflake egress as part of cloud migration cutover with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```sql
-- Q204: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q205. How do you demonstrate proficiency in Snowflake egress as part of cloud migration cutover?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Snowflake egress as part of cloud migration cutover with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```sql
-- Q205: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```


## Section O: Orchestration APIs — ng-orchestration-service

> **Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

### Q206. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q206: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q207. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q207: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q208. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q208: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q209. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q209: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q210. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q210: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q211. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q211: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q212. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q212: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q213. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q213: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q214. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q214: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q215. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q215: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q216. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q216: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q217. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q217: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q218. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q218: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q219. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q219: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q220. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q220: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q221. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q221: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q222. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q222: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q223. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q223: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q224. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q224: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q225. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q225: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q226. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q226: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q227. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q227: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q228. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q228: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q229. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q229: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q230. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q230: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q231. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q231: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q232. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q232: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q233. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q233: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q234. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q234: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q235. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q235: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q236. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q236: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q237. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q237: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q238. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q238: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q239. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q239: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q240. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q240: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q241. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q241: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q242. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q242: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q243. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q243: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q244. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q244: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q245. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q245: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q246. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q246: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q247. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q247: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q248. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q248: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q249. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q249: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q250. How do you demonstrate proficiency in orchestration API contracts and Postman validation for ng-orchestration-service?

**Pillar:** P1+P4 — E2E Implementation Proficiency, Postman API Role

**Answer:** I own orchestration API contracts and Postman validation for ng-orchestration-service with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q250: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```


## Section P: On-Prem Handoff — SFTP & Landing Zone

> **Pillar:** P3 — On-Prem → Cloud Migration

### Q251. How does on-prem handoff work via SFTP and landing zone?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** Encrypted JSON + manifest land on Abacus SFTP / connector zone → NextGen raw S3 (cambia02). ng-abacus-inbound-infra owns landing infra. Nightly trigger file Facets_BatchJobComplete_* on SFTP signals Cambia batch complete and kicks CDC immediately.

**Example:** Validate ~25 files match manifest before ng-orchestration-service triggers bronze.

**How to Check:**
- SFTP connector logs; S3 listing under cambia02 raw prefix; Postman callback to orchestration manifest-received endpoint.

**How to Fix:**
- Reject batches with manifest/file count mismatch; quarantine for facets-core replay.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q251: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q251: migration gate checklist complete
```

### Q252. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q252: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q252: migration gate checklist complete
```

### Q253. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q253: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q253: migration gate checklist complete
```

### Q254. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q254: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q254: migration gate checklist complete
```

### Q255. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q255: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q255: migration gate checklist complete
```

### Q256. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q256: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q256: migration gate checklist complete
```

### Q257. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q257: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q257: migration gate checklist complete
```

### Q258. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q258: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q258: migration gate checklist complete
```

### Q259. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q259: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q259: migration gate checklist complete
```

### Q260. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q260: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q260: migration gate checklist complete
```

### Q261. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q261: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q261: migration gate checklist complete
```

### Q262. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q262: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q262: migration gate checklist complete
```

### Q263. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q263: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q263: migration gate checklist complete
```

### Q264. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q264: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q264: migration gate checklist complete
```

### Q265. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q265: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q265: migration gate checklist complete
```

### Q266. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q266: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q266: migration gate checklist complete
```

### Q267. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q267: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q267: migration gate checklist complete
```

### Q268. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q268: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q268: migration gate checklist complete
```

### Q269. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q269: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q269: migration gate checklist complete
```

### Q270. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q270: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q270: migration gate checklist complete
```

### Q271. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q271: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q271: migration gate checklist complete
```

### Q272. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q272: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q272: migration gate checklist complete
```

### Q273. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q273: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q273: migration gate checklist complete
```

### Q274. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q274: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q274: migration gate checklist complete
```

### Q275. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q275: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q275: migration gate checklist complete
```

### Q276. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q276: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q276: migration gate checklist complete
```

### Q277. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q277: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q277: migration gate checklist complete
```

### Q278. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q278: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q278: migration gate checklist complete
```

### Q279. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q279: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q279: migration gate checklist complete
```

### Q280. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q280: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q280: migration gate checklist complete
```

### Q281. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q281: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q281: migration gate checklist complete
```

### Q282. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q282: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q282: migration gate checklist complete
```

### Q283. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q283: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q283: migration gate checklist complete
```

### Q284. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q284: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q284: migration gate checklist complete
```

### Q285. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q285: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q285: migration gate checklist complete
```

### Q286. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q286: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q286: migration gate checklist complete
```

### Q287. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q287: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q287: migration gate checklist complete
```

### Q288. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q288: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q288: migration gate checklist complete
```

### Q289. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q289: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q289: migration gate checklist complete
```

### Q290. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q290: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q290: migration gate checklist complete
```

### Q291. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q291: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q291: migration gate checklist complete
```

### Q292. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q292: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q292: migration gate checklist complete
```

### Q293. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q293: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q293: migration gate checklist complete
```

### Q294. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q294: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q294: migration gate checklist complete
```

### Q295. How do you demonstrate proficiency in on-prem SFTP handoff, landing zone, and migration file validation?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own on-prem SFTP handoff, landing zone, and migration file validation with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Integration Engineer)*

```bash
#!/usr/bin/env bash
# Q295: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q295: migration gate checklist complete
```


## Section Q: Databricks Engineering Implementation

> **Pillar:** P1 — E2E Implementation Proficiency

### Q296. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q296: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q297. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q297: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q298. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q298: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q299. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q299: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q300. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q300: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q301. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q301: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q302. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q302: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q303. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q303: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q304. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q304: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q305. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q305: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q306. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q306: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q307. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q307: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q308. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q308: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q309. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q309: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q310. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q310: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q311. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q311: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q312. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q312: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q313. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q313: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q314. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q314: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q315. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q315: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q316. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q316: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q317. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q317: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q318. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q318: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q319. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q319: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q320. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q320: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q321. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q321: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q322. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q322: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q323. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q323: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q324. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q324: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q325. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q325: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q326. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q326: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q327. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q327: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q328. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q328: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q329. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q329: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q330. How do you demonstrate proficiency in ng-pipelines-cambia Databricks implementation and pipespecs?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own ng-pipelines-cambia Databricks implementation and pipespecs with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Data Engineer | E2E Implementation Lead)*

```sql
-- Q330: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```


## Section R: MDM/Reltio Cloud Migration

> **Pillar:** P3 — On-Prem → Cloud Migration

### Q331. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q331: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q332. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q332: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q333. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q333: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q334. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q334: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q335. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q335: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q336. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q336: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q337. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q337: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q338. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q338: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q339. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q339: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q340. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q340: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q341. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q341: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q342. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q342: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q343. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q343: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q344. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q344: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q345. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q345: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q346. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q346: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q347. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q347: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q348. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q348: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q349. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q349: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q350. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q350: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q351. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q351: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q352. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q352: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q353. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q353: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q354. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q354: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q355. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q355: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q356. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q356: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q357. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q357: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q358. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q358: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q359. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q359: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q360. How do you demonstrate proficiency in Reltio MDM cloud migration from Facets silver feeds?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own Reltio MDM cloud migration from Facets silver feeds with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Facets/TriZetto SME)*

```bash
#!/usr/bin/env bash
# Q360: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```


## Section S: VPN & On-Prem Network Migration

> **Pillar:** P3 — On-Prem → Cloud Migration

### Q361. How do you implement VPN connectivity for on-prem Facets migration?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** Site-to-site VPN via Palo Alto firewalls into dedicated AWS account cambia-facets-networking (697410135799). This is the only path from cloud CDC to on-prem SQL Server 2016 read replica. VPN flap = CDC stall; monitor as migration P1.

**Example:** Network diagram: Cambia on-prem → Palo Alto → cambia-facets-networking → facets-core Step Functions.

**How to Check:**
- VPN tunnel status dashboard; CDC lag metric correlated with tunnel uptime.

**How to Fix:**
- Runbook for VPN failover; never route Facets queries over public internet.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q361: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q361: CDC + VPN path verified
```

### Q362. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q362: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q362: CDC + VPN path verified
```

### Q363. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q363: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q363: CDC + VPN path verified
```

### Q364. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q364: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q364: CDC + VPN path verified
```

### Q365. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q365: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q365: CDC + VPN path verified
```

### Q366. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q366: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q366: CDC + VPN path verified
```

### Q367. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q367: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q367: CDC + VPN path verified
```

### Q368. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q368: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q368: CDC + VPN path verified
```

### Q369. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q369: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q369: CDC + VPN path verified
```

### Q370. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q370: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q370: CDC + VPN path verified
```

### Q371. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q371: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q371: CDC + VPN path verified
```

### Q372. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q372: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q372: CDC + VPN path verified
```

### Q373. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q373: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q373: CDC + VPN path verified
```

### Q374. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q374: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q374: CDC + VPN path verified
```

### Q375. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q375: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q375: CDC + VPN path verified
```

### Q376. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q376: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q376: CDC + VPN path verified
```

### Q377. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q377: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q377: CDC + VPN path verified
```

### Q378. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q378: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q378: CDC + VPN path verified
```

### Q379. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q379: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q379: CDC + VPN path verified
```

### Q380. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q380: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q380: CDC + VPN path verified
```

### Q381. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q381: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q381: CDC + VPN path verified
```

### Q382. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q382: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q382: CDC + VPN path verified
```

### Q383. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q383: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q383: CDC + VPN path verified
```

### Q384. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q384: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q384: CDC + VPN path verified
```

### Q385. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q385: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q385: CDC + VPN path verified
```

### Q386. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q386: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q386: CDC + VPN path verified
```

### Q387. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q387: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q387: CDC + VPN path verified
```

### Q388. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q388: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q388: CDC + VPN path verified
```

### Q389. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q389: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q389: CDC + VPN path verified
```

### Q390. How do you demonstrate proficiency in VPN and on-prem network migration for Facets connectivity?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own VPN and on-prem network migration for Facets connectivity with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q390: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q390: CDC + VPN path verified
```


## Section T: SQL Server CDC & Facets Source SME

> **Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

### Q391. As a Facets source SME, how does SQL Server CDC work on the read replica?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** CDC captures I/U/D on Facets tables; facets-core converts LSN watermarks to unique change IDs for idempotent JSON. Claim types: M/H medical, D dental. Status: 11=pended, 15=error, 01=pre-final, 02=final, 91=adjusted.

**Example:** Incremental: 500–1000 tx per 15-min window daytime; nightly batch 70k–120k claims spikes CDC volume.

**How to Check:**
- Compare CdcGlobals LSN watermark vs replica CDC latency; validate change ID monotonicity.

**How to Fix:**
- Read replica only; coordinate with Cambia DBA for CDC retention and disk capacity during historical backfill.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q391: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q391: CDC + VPN path verified
```

### Q392. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q392: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q392: CDC + VPN path verified
```

### Q393. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q393: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q393: CDC + VPN path verified
```

### Q394. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q394: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q394: CDC + VPN path verified
```

### Q395. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q395: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q395: CDC + VPN path verified
```

### Q396. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q396: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q396: CDC + VPN path verified
```

### Q397. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q397: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q397: CDC + VPN path verified
```

### Q398. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q398: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q398: CDC + VPN path verified
```

### Q399. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q399: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q399: CDC + VPN path verified
```

### Q400. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q400: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q400: CDC + VPN path verified
```

### Q401. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q401: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q401: CDC + VPN path verified
```

### Q402. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q402: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q402: CDC + VPN path verified
```

### Q403. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q403: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q403: CDC + VPN path verified
```

### Q404. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q404: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q404: CDC + VPN path verified
```

### Q405. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q405: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q405: CDC + VPN path verified
```

### Q406. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q406: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q406: CDC + VPN path verified
```

### Q407. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q407: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q407: CDC + VPN path verified
```

### Q408. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q408: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q408: CDC + VPN path verified
```

### Q409. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q409: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q409: CDC + VPN path verified
```

### Q410. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q410: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q410: CDC + VPN path verified
```

### Q411. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q411: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q411: CDC + VPN path verified
```

### Q412. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q412: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q412: CDC + VPN path verified
```

### Q413. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q413: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q413: CDC + VPN path verified
```

### Q414. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q414: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q414: CDC + VPN path verified
```

### Q415. How do you demonstrate proficiency in SQL Server CDC and Facets source table SME knowledge?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own SQL Server CDC and Facets source table SME knowledge with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q415: CDC / on-prem source implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q415: CDC + VPN path verified
```


## Section U: Production Scale & TriZetto Volume Profiles

> **Pillar:** P2 — Facets & TriZetto SME

### Q416. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q416: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q417. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q417: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q418. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q418: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q419. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q419: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q420. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q420: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q421. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q421: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q422. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q422: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q423. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q423: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q424. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q424: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q425. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q425: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q426. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q426: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q427. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q427: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q428. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q428: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q429. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q429: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q430. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q430: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q431. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q431: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q432. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q432: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q433. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q433: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q434. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q434: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q435. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q435: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q436. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q436: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q437. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q437: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q438. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q438: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q439. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q439: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q440. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q440: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q441. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q441: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q442. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q442: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q443. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q443: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q444. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q444: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q445. How do you demonstrate proficiency in TriZetto production volumes and scale profiles?

**Pillar:** P2 — Facets & TriZetto SME

**Answer:** I own TriZetto production volumes and scale profiles with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Data Engineer)*

```sql
-- Q445: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```


## Section V: De-Identification for Migration Analytics

> **Pillar:** P3 — On-Prem → Cloud Migration

### Q446. How do you demonstrate proficiency in de-identification for migration analytics and safe harbor?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own de-identification for migration analytics and safe harbor with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q446: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q447. How do you demonstrate proficiency in de-identification for migration analytics and safe harbor?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own de-identification for migration analytics and safe harbor with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q447: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q448. How do you demonstrate proficiency in de-identification for migration analytics and safe harbor?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own de-identification for migration analytics and safe harbor with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q448: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q449. How do you demonstrate proficiency in de-identification for migration analytics and safe harbor?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own de-identification for migration analytics and safe harbor with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q449: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q450. How do you demonstrate proficiency in de-identification for migration analytics and safe harbor?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own de-identification for migration analytics and safe harbor with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q450: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q451. How do you demonstrate proficiency in de-identification for migration analytics and safe harbor?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own de-identification for migration analytics and safe harbor with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q451: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q452. How do you demonstrate proficiency in de-identification for migration analytics and safe harbor?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own de-identification for migration analytics and safe harbor with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q452: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q453. How do you demonstrate proficiency in de-identification for migration analytics and safe harbor?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own de-identification for migration analytics and safe harbor with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q453: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q454. How do you demonstrate proficiency in de-identification for migration analytics and safe harbor?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own de-identification for migration analytics and safe harbor with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q454: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q455. How do you demonstrate proficiency in de-identification for migration analytics and safe harbor?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own de-identification for migration analytics and safe harbor with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q455: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```


## Section W: Master Data Management — Facets Entities

> **Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

### Q456. How do you demonstrate proficiency in MDM golden records from Facets member and provider entities?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own MDM golden records from Facets member and provider entities with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```sql
-- Q456: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q457. How do you demonstrate proficiency in MDM golden records from Facets member and provider entities?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own MDM golden records from Facets member and provider entities with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```sql
-- Q457: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q458. How do you demonstrate proficiency in MDM golden records from Facets member and provider entities?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own MDM golden records from Facets member and provider entities with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```sql
-- Q458: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q459. How do you demonstrate proficiency in MDM golden records from Facets member and provider entities?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own MDM golden records from Facets member and provider entities with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```sql
-- Q459: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q460. How do you demonstrate proficiency in MDM golden records from Facets member and provider entities?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own MDM golden records from Facets member and provider entities with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```sql
-- Q460: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q461. How do you demonstrate proficiency in MDM golden records from Facets member and provider entities?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own MDM golden records from Facets member and provider entities with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```sql
-- Q461: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q462. How do you demonstrate proficiency in MDM golden records from Facets member and provider entities?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own MDM golden records from Facets member and provider entities with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```sql
-- Q462: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q463. How do you demonstrate proficiency in MDM golden records from Facets member and provider entities?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own MDM golden records from Facets member and provider entities with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```sql
-- Q463: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q464. How do you demonstrate proficiency in MDM golden records from Facets member and provider entities?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own MDM golden records from Facets member and provider entities with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```sql
-- Q464: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```

### Q465. How do you demonstrate proficiency in MDM golden records from Facets member and provider entities?

**Pillar:** P2+P3 — Facets & TriZetto SME, On-Prem → Cloud Migration

**Answer:** I own MDM golden records from Facets member and provider entities with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Facets & TriZetto SME.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Facets/TriZetto SME | Migration Engineer)*

```sql
-- Q465: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;
```


## Section X: Interop vs CDP Implementation Comparison

> **Pillar:** P1 — E2E Implementation Proficiency

### Q466. How do you demonstrate proficiency in Interop vs CDP implementation path selection?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP implementation path selection with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q466: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q467. How do you demonstrate proficiency in Interop vs CDP implementation path selection?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP implementation path selection with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q467: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q468. How do you demonstrate proficiency in Interop vs CDP implementation path selection?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP implementation path selection with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q468: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q469. How do you demonstrate proficiency in Interop vs CDP implementation path selection?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP implementation path selection with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q469: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q470. How do you demonstrate proficiency in Interop vs CDP implementation path selection?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP implementation path selection with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q470: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q471. How do you demonstrate proficiency in Interop vs CDP implementation path selection?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP implementation path selection with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q471: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q472. How do you demonstrate proficiency in Interop vs CDP implementation path selection?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP implementation path selection with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q472: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q473. How do you demonstrate proficiency in Interop vs CDP implementation path selection?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own Interop vs CDP implementation path selection with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q473: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```


## Section Y: Observability & Delivery Monitoring

> **Pillar:** P1 — E2E Implementation Proficiency

### Q474. How do you demonstrate proficiency in observability, delivery monitoring, and migration health dashboards?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own observability, delivery monitoring, and migration health dashboards with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q474: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q475. How do you demonstrate proficiency in observability, delivery monitoring, and migration health dashboards?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own observability, delivery monitoring, and migration health dashboards with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q475: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q476. How do you demonstrate proficiency in observability, delivery monitoring, and migration health dashboards?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own observability, delivery monitoring, and migration health dashboards with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q476: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q477. How do you demonstrate proficiency in observability, delivery monitoring, and migration health dashboards?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own observability, delivery monitoring, and migration health dashboards with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q477: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q478. How do you demonstrate proficiency in observability, delivery monitoring, and migration health dashboards?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own observability, delivery monitoring, and migration health dashboards with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q478: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q479. How do you demonstrate proficiency in observability, delivery monitoring, and migration health dashboards?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own observability, delivery monitoring, and migration health dashboards with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q479: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q480. How do you demonstrate proficiency in observability, delivery monitoring, and migration health dashboards?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own observability, delivery monitoring, and migration health dashboards with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q480: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q481. How do you demonstrate proficiency in observability, delivery monitoring, and migration health dashboards?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own observability, delivery monitoring, and migration health dashboards with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q481: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q482. How do you demonstrate proficiency in observability, delivery monitoring, and migration health dashboards?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own observability, delivery monitoring, and migration health dashboards with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q482: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q483. How do you demonstrate proficiency in observability, delivery monitoring, and migration health dashboards?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own observability, delivery monitoring, and migration health dashboards with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q483: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q484. How do you demonstrate proficiency in observability, delivery monitoring, and migration health dashboards?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own observability, delivery monitoring, and migration health dashboards with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q484: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```

### Q485. How do you demonstrate proficiency in observability, delivery monitoring, and migration health dashboards?

**Pillar:** P1 — E2E Implementation Proficiency

**Answer:** I own observability, delivery monitoring, and migration health dashboards with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: E2E Implementation Lead | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q485: E2E implementation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh
```


## Section Z: DevOps & CI/CD for Cloud Migration

> **Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

### Q486. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q486: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q487. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q487: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q488. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q488: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q489. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q489: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q490. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q490: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q491. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q491: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q492. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q492: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q493. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q493: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q494. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q494: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q495. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q495: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q496. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q496: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q497. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q497: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q498. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q498: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q499. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q499: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q500. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q500: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q501. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q501: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q502. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q502: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q503. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q503: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q504. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q504: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q505. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q505: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q506. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q506: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q507. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q507: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q508. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q508: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q509. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q509: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q510. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q510: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q511. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q511: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q512. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q512: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q513. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q513: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q514. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q514: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```

### Q515. How do you demonstrate proficiency in DevOps, CI/CD, and IaC for cloud migration promotion?

**Pillar:** P1+P3 — E2E Implementation Proficiency, On-Prem → Cloud Migration

**Answer:** I own DevOps, CI/CD, and IaC for cloud migration promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: E2E Implementation Proficiency.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: DevOps Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q515: DevOps / migration CI gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
```


## Section AA: Governance & Migration Compliance

> **Pillar:** P3 — On-Prem → Cloud Migration

### Q516. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q516: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q516: migration gate checklist complete
```

### Q517. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q517: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q517: migration gate checklist complete
```

### Q518. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q518: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q518: migration gate checklist complete
```

### Q519. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q519: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q519: migration gate checklist complete
```

### Q520. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q520: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q520: migration gate checklist complete
```

### Q521. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q521: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q521: migration gate checklist complete
```

### Q522. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q522: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q522: migration gate checklist complete
```

### Q523. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q523: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q523: migration gate checklist complete
```

### Q524. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q524: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q524: migration gate checklist complete
```

### Q525. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q525: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q525: migration gate checklist complete
```

### Q526. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q526: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q526: migration gate checklist complete
```

### Q527. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q527: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q527: migration gate checklist complete
```

### Q528. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q528: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q528: migration gate checklist complete
```

### Q529. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q529: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q529: migration gate checklist complete
```

### Q530. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q530: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q530: migration gate checklist complete
```

### Q531. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q531: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q531: migration gate checklist complete
```

### Q532. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q532: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q532: migration gate checklist complete
```

### Q533. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q533: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q533: migration gate checklist complete
```

### Q534. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q534: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q534: migration gate checklist complete
```

### Q535. How do you demonstrate proficiency in governance, audit, and migration compliance sign-off?

**Pillar:** P3 — On-Prem → Cloud Migration

**Answer:** I own governance, audit, and migration compliance sign-off with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: On-Prem → Cloud Migration.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Migration Engineer | Solution Architect)*

```bash
#!/usr/bin/env bash
# Q535: On-prem → cloud migration gate check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/migration_cutover_checklist.sh
echo "Q535: migration gate checklist complete
```


## Section AB: Postman Collections & Cambia Cutover

> **Pillar:** P4+P3 — Postman API Role, On-Prem → Cloud Migration

### Q536. What Postman collections do you maintain for Cambia Facets cutover?

**Pillar:** P4+P3 — Postman API Role, On-Prem → Cloud Migration

**Answer:** Three collections: (1) Orchestration — manifest trigger, job status, delivery monitor; (2) FHIR Interop — Claim/Coverage/Diagnosis reads for 75-group filter; (3) FHIR CDP — full claim set validation. Environment files per cambia02 dev/stg/prd with synthetic IDs.

**Example:** newman run postman/cambia-facets-cutover-gate.json -e postman/env/prd-smoke.json --bail

**How to Check:**
- Cutover gate: all Postman folders green + row-count parity + no open P1 incidents.

**How to Fix:**
- Confirm workflow IDs and base URLs with #xform-xport before updating environment variables.

**Script:** *(builds proficiency: Postman/API Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q536: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q537. How do you demonstrate proficiency in Postman collections, cutover smoke tests, and cambia02 env promotion?

**Pillar:** P4+P3 — Postman API Role, On-Prem → Cloud Migration

**Answer:** I own Postman collections, cutover smoke tests, and cambia02 env promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Postman API Role.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q537: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q538. How do you demonstrate proficiency in Postman collections, cutover smoke tests, and cambia02 env promotion?

**Pillar:** P4+P3 — Postman API Role, On-Prem → Cloud Migration

**Answer:** I own Postman collections, cutover smoke tests, and cambia02 env promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Postman API Role.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q538: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q539. How do you demonstrate proficiency in Postman collections, cutover smoke tests, and cambia02 env promotion?

**Pillar:** P4+P3 — Postman API Role, On-Prem → Cloud Migration

**Answer:** I own Postman collections, cutover smoke tests, and cambia02 env promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Postman API Role.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q539: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q540. How do you demonstrate proficiency in Postman collections, cutover smoke tests, and cambia02 env promotion?

**Pillar:** P4+P3 — Postman API Role, On-Prem → Cloud Migration

**Answer:** I own Postman collections, cutover smoke tests, and cambia02 env promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Postman API Role.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q540: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q541. How do you demonstrate proficiency in Postman collections, cutover smoke tests, and cambia02 env promotion?

**Pillar:** P4+P3 — Postman API Role, On-Prem → Cloud Migration

**Answer:** I own Postman collections, cutover smoke tests, and cambia02 env promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Postman API Role.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q541: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q542. How do you demonstrate proficiency in Postman collections, cutover smoke tests, and cambia02 env promotion?

**Pillar:** P4+P3 — Postman API Role, On-Prem → Cloud Migration

**Answer:** I own Postman collections, cutover smoke tests, and cambia02 env promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Postman API Role.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q542: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q543. How do you demonstrate proficiency in Postman collections, cutover smoke tests, and cambia02 env promotion?

**Pillar:** P4+P3 — Postman API Role, On-Prem → Cloud Migration

**Answer:** I own Postman collections, cutover smoke tests, and cambia02 env promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Postman API Role.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q543: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q544. How do you demonstrate proficiency in Postman collections, cutover smoke tests, and cambia02 env promotion?

**Pillar:** P4+P3 — Postman API Role, On-Prem → Cloud Migration

**Answer:** I own Postman collections, cutover smoke tests, and cambia02 env promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Postman API Role.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q544: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q545. How do you demonstrate proficiency in Postman collections, cutover smoke tests, and cambia02 env promotion?

**Pillar:** P4+P3 — Postman API Role, On-Prem → Cloud Migration

**Answer:** I own Postman collections, cutover smoke tests, and cambia02 env promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Postman API Role.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q545: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q546. How do you demonstrate proficiency in Postman collections, cutover smoke tests, and cambia02 env promotion?

**Pillar:** P4+P3 — Postman API Role, On-Prem → Cloud Migration

**Answer:** I own Postman collections, cutover smoke tests, and cambia02 env promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Postman API Role.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q546: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q547. How do you demonstrate proficiency in Postman collections, cutover smoke tests, and cambia02 env promotion?

**Pillar:** P4+P3 — Postman API Role, On-Prem → Cloud Migration

**Answer:** I own Postman collections, cutover smoke tests, and cambia02 env promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Postman API Role.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q547: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q548. How do you demonstrate proficiency in Postman collections, cutover smoke tests, and cambia02 env promotion?

**Pillar:** P4+P3 — Postman API Role, On-Prem → Cloud Migration

**Answer:** I own Postman collections, cutover smoke tests, and cambia02 env promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Postman API Role.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q548: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q549. How do you demonstrate proficiency in Postman collections, cutover smoke tests, and cambia02 env promotion?

**Pillar:** P4+P3 — Postman API Role, On-Prem → Cloud Migration

**Answer:** I own Postman collections, cutover smoke tests, and cambia02 env promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Postman API Role.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q549: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q550. How do you demonstrate proficiency in Postman collections, cutover smoke tests, and cambia02 env promotion?

**Pillar:** P4+P3 — Postman API Role, On-Prem → Cloud Migration

**Answer:** I own Postman collections, cutover smoke tests, and cambia02 env promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Postman API Role.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q550: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q551. How do you demonstrate proficiency in Postman collections, cutover smoke tests, and cambia02 env promotion?

**Pillar:** P4+P3 — Postman API Role, On-Prem → Cloud Migration

**Answer:** I own Postman collections, cutover smoke tests, and cambia02 env promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Postman API Role.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q551: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q552. How do you demonstrate proficiency in Postman collections, cutover smoke tests, and cambia02 env promotion?

**Pillar:** P4+P3 — Postman API Role, On-Prem → Cloud Migration

**Answer:** I own Postman collections, cutover smoke tests, and cambia02 env promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Postman API Role.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q552: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```

### Q553. How do you demonstrate proficiency in Postman collections, cutover smoke tests, and cambia02 env promotion?

**Pillar:** P4+P3 — Postman API Role, On-Prem → Cloud Migration

**Answer:** I own Postman collections, cutover smoke tests, and cambia02 env promotion with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: Postman API Role.

**Example:** cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.

**How to Check:**
- Run relevant Script below; verify Databricks job history and Postman/newman exit 0.

**How to Fix:**
- Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.

**Script:** *(builds proficiency: Postman/API Engineer | Migration Engineer)*

```bash
#!/usr/bin/env bash
# Q553: Postman API validation drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail
```


## Glossary

> Glossary organized by proficiency pillar.

| Term | Pillar | Description | Example |
|------|--------|-------------|---------|
| **E2E Implementation** | P1 | Full pipeline delivery ownership from CDC through downstream | Phase gates with script + Postman proof at each stage |
| **TriZetto Facets** | P2 | Cambia on-prem claims admin system on SQL Server 2016 | CMC_CLCL_CLAIM header; M/H medical, D dental |
| **CMC_CLCL_CLAIM** | P2 | Facets claim header bronze SCD2 table | Primary grain for unified_timeline_claim |
| **CLCL status 02** | P2 | Facets final claim status | 11=pended, 15=error, 01=pre-final, 91=adjusted |
| **On-Prem Migration** | P3 | Phased cutover from Facets on-prem to cambia02 cloud | VPN → historical backfill → incremental parity → downstream |
| **HITRUST boundary** | P3 | facets-core CDC outside HITRUST; encrypt before landing | Encryption at JSON output before SFTP |
| **cambia-facets-networking** | P3 | AWS account 697410135799 for Palo Alto VPN | Only cloud path to on-prem Facets replica |
| **Postman Collection** | P4 | API contract tests for orchestration and FHIR endpoints | newman run with env-scoped synthetic IDs |
| **ng-orchestration-service** | P4 | Manifest-triggered workflow API | Postman: manifest-received → job status poll |
| **FHIR Claim validation** | P4 | Postman GET Claim resources from gold.fm_claim SAM load | Assert US Core meta.profile URLs |
| **facets-core** | P1+P3 | Bespoke CDC: SQL Server → JSON + manifest | Step Functions + Batch |
| **manifest.json** | P1+P3 | Batch metadata for encrypted JSON files | cambia/facets/cambia/claims/extension/incremental/*/*manifest.json |
| **gold.fm_claim** | P1 | Interop FM — filtered for CMS-9115 SAM/FHIR | 75 groups, Medicare; dental excluded |
| **gold.fm_claim_cambia** | P1 | CDP FM — full silver mapping + signature bitmap | All claim types for migration parity checks |
| **Facets_BatchJobComplete** | P2+P3 | Nightly trigger file after Cambia batch | Kicks CDC immediately post batch |
| **newman** | P4 | CLI runner for Postman collections in CI/cutover gates | newman run collection.json -e env.json --bail |

---
