# Cambia Facets Claims — Interview Answer Cheat Sheet

> Cambia on-prem TriZetto Facets → Abacus NextGen (cambia02) | 553 questions + Glossary | First-person, hands-on owner voice
> **Learn first:** [LEARN_FROM_STEP_1.md](/Users/ashishsingh/CambiaFacetsClaims/Training/LEARN_FROM_STEP_1.md) — start Day 1 before touching prod workflows.
> **Proficiency guarantee:** Complete learning steps + run every **Script** below to reach working proficiency across eight roles.

## Answer Format

Each question includes five segments:

| Segment | Purpose |
|---------|---------|
| **Answer** | What to say in the interview (ownership voice) |
| **Example** | Real scenario from Cambia Facets Claims |
| **How to Check** | Verification steps / commands |
| **How to Fix** | Remediation if check fails |
| **Script** | Runnable code to build role proficiency |

## Proficiency Role Map (by Section)

| Target Role | Primary Sections | Script Languages |
|-------------|------------------|------------------|
| **Associate Solution Architect** | A, C, H, J, K, L, M, AB | bash, architecture trace |
| **FHIR Engineer** | E, H, AB | bash, FHIR validation |
| **Data Engineer** | D, G, J, N, O, P, Q, R, T, U, AB | PySpark, SQL, Delta |
| **Forward Deployed Engineer** | A, F, I, L, M, P, S, Y, AB | bash, Terraform, VPN runbooks |
| **Intermediate Associate Programmer** | D, G, O, P, Q, T, Z | Python, bash, SQL, YAML |
| **DevOps Engineer** | I, S, Z, AB | GitLab CI, Terraform, facets-infrastructure |
| **MDM Engineer** | R, W | SQL, Reltio API patterns |
| **Integration Engineer** | G, P, O | Step Functions, SFTP, manifest contracts |

## Implementation Phases → Role Outcomes

| Phase | You Will Proficiently... |
|-------|--------------------------|
| **Phase 0** | Trace 5-stage architecture; map repos; validate manifest patterns; local CI green |
| **Phase 1** | Understand CDC extraction, SFTP landing, bronze SCD2 loads |
| **Phase 2** | Own silver unified timeline and dual gold FM paths |
| **Phase 3** | Operate nightly batch + 4-hr incremental; troubleshoot locks and manifests |
| **Phase 4** | Downstream SAM/FHIR, Snowflake egress, Reltio MDM cutover |

## Table of Contents

- [Learn From Step 1 — Learning Guide (start here)](/Users/ashishsingh/CambiaFacetsClaims/Training/LEARN_FROM_STEP_1.md)
- [Glossary — Key Terms (A–Z)](#glossary)
- [Section A: Opening & Role Fit (Q1–10)](#section-a-opening-role-fit-q110)
- [Section B: Facets Domain & Cambia Context (Q11–28)](#section-b-facets-domain-cambia-context-q1128)
- [Section C: Architecture & System Design (Q29–45)](#section-c-architecture-system-design-q2945)
- [Section D: Data Engineering & Databricks (Q46–73)](#section-d-data-engineering-databricks-q4673)
- [Section E: FHIR & Downstream Interop (Q74–94)](#section-e-fhir-downstream-interop-q7494)
- [Section F: Security, Auth & Compliance (Q95–112)](#section-f-security,-auth-compliance-q95112)
- [Section G: CDC Extraction & facets-core (Q113–124)](#section-g-cdc-extraction-facets-core-q113124)
- [Section H: Dual Gold Paths — Interop vs CDP (Q125–141)](#section-h-dual-gold-paths-interop-vs-cdp-q125141)
- [Section I: Deployment, Operations & Troubleshooting (Q142–154)](#section-i-deployment,-operations-troubleshooting-q142154)
- [Section J: Reporting, Analytics & KPIs (Q155–162)](#section-j-reporting,-analytics-kpis-q155162)
- [Section K: Claims & RCM Bridge (Q163–172)](#section-k-claims-rcm-bridge-q163172)
- [Section L: Leadership & Program Management (Q173–185)](#section-l-leadership-program-management-q173185)
- [Section M: Scenario Troubleshooting (Q186–195)](#section-m-scenario-troubleshooting-q186195)
- [Section N: Snowflake Egress (Q196–205)](#section-n-snowflake-egress-q196205)
- [Section O: Orchestration & ng-orchestration-service (Q206–250)](#section-o-orchestration-ng-orchestration-service-q206250)
- [Section P: SFTP/Inbound & Landing Zone (Q251–295)](#section-p-sftpinbound-landing-zone-q251295)
- [Section Q: Databricks Engineering — Facets Claims (Q296–330)](#section-q-databricks-engineering-facets-claims-q296330)
- [Section R: MDM & Reltio Integration (Q331–360)](#section-r-mdm-reltio-integration-q331360)
- [Section S: AWS Networking & VPN (Q361–390)](#section-s-aws-networking-vpn-q361390)
- [Section T: SQL Server CDC & Facets Source (Q391–415)](#section-t-sql-server-cdc-facets-source-q391415)
- [Section U: Operations at Scale & Volumes (Q416–445)](#section-u-operations-at-scale-volumes-q416445)
- [Section V: De-Identification & Safe Harbor (Q446–455)](#section-v-de-identification-safe-harbor-q446455)
- [Section W: Master Data Management (Q456–465)](#section-w-master-data-management-q456465)
- [Section X: Interop vs CDP Path Comparison (Q466–473)](#section-x-interop-vs-cdp-path-comparison-q466473)
- [Section Y: Observability & Monitoring (Q474–485)](#section-y-observability-monitoring-q474485)
- [Section Z: DevOps & CI/CD (Q486–515)](#section-z-devops-cicd-q486515)
- [Section AA: Governance & Compliance (Q516–535)](#section-aa-governance-compliance-q516535)
- [Section AB: Cambia-Specific Integrations & Cutover (Q536–553)](#section-ab-cambia-specific-integrations-cutover-q536553)

## Section A: Opening & Role Fit

### Q1. Tell me about your experience building end-to-end payer claims pipelines.

**Answer:** I led Cambia Facets Claims from on-prem TriZetto Facets through VPN, bespoke CDC, encrypted landing, Databricks bronze/silver/gold, and dual FM outputs to SAM/FHIR and Snowflake. I owned manifest-triggered orchestration and SCD2 bronze loads—not just pipeline diagrams.

**Example:** Nightly batch trigger file arrives on SFTP → ng-orchestration-service kicks bronze → silver unified timeline → gold.fm_claim for 75 Medicare groups.

**How to Check:**
- Databricks job history for cambia02 claims workflows; manifest path cambia/facets/cambia/claims/extension/incremental/*/*manifest.json

**How to Fix:**
- Map each of the 5 stages to an owner before sprint 1; run architecture trace script below.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q1: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q1: 5-stage trace + repo map complete"
```

### Q2. What is the Cambia Facets Claims platform and how do components fit together?

**Answer:** Facets Claims is cambia02-specific: facets-core CDC (outside HITRUST) → encrypted JSON + manifest → Abacus SFTP landing → NextGen raw S3 → Databricks bronze (44+ SCD2 tables) → silver unified timeline → dual gold (Interop filtered vs CDP full) → Onyx SAM/FHIR + Snowflake.

**Example:** ng-orchestration-service orchestrates CDC delivery monitoring and manifest-triggered Databricks workflows; AIR library handles encryption, manifest validation, SCD2 sinks.

**How to Check:**
- Catalog entries: config/repo-rules/transporters/sftp.yaml, orchestration.yaml, config/repo-rules/xform/pipelines.yaml

**How to Fix:**
- Document repo ownership: facets-core, facets-infrastructure, ng-pipelines-cambia, ng-orchestration-service, ng-abacus-insights-runtime

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q2: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q2: 5-stage trace + repo map complete"
```

### Q3. How is Facets Claims different from a generic Transporters catalog service?

**Answer:** It spans bespoke Facets CDC (Step Functions + Batch), VPN networking, SFTP trigger files, and XFORM medallion pipelines—not a single transporter YAML. Tenant is cambia02; source is on-prem SQL Server 2016 CDC replica.

**Example:** Claims Incremental (~4 hr), Historical, and PPL variants each have distinct S3 prefixes and DynamoDB locks in CdcGlobals.

**How to Check:**
- grep -r 'cambia02' config/repo-rules/xform/pipelines.yaml

**How to Fix:**
- Never treat Facets as Airbyte-only; CDC concurrency is one job per domain via DynamoDB lock.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q3: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q3: 5-stage trace + repo map complete"
```

### Q4. How do you handle platform ownership and Cambia Facets delivery in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on platform ownership and Cambia Facets delivery: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q4: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q4: 5-stage trace + repo map complete"
```

### Q5. How do you handle platform ownership and Cambia Facets delivery in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on platform ownership and Cambia Facets delivery: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q5: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q5: 5-stage trace + repo map complete"
```

### Q6. How do you handle platform ownership and Cambia Facets delivery in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on platform ownership and Cambia Facets delivery: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q6: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q6: 5-stage trace + repo map complete"
```

### Q7. How do you handle platform ownership and Cambia Facets delivery in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on platform ownership and Cambia Facets delivery: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q7: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q7: 5-stage trace + repo map complete"
```

### Q8. How do you handle platform ownership and Cambia Facets delivery in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on platform ownership and Cambia Facets delivery: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q8: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q8: 5-stage trace + repo map complete"
```

### Q9. How do you handle platform ownership and Cambia Facets delivery in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on platform ownership and Cambia Facets delivery: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q9: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q9: 5-stage trace + repo map complete"
```

### Q10. How do you handle platform ownership and Cambia Facets delivery in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on platform ownership and Cambia Facets delivery: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q10: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q10: 5-stage trace + repo map complete"
```


## Section B: Facets Domain & Cambia Context

### Q11. How do you handle TriZetto Facets claim domain, statuses, and Cambia specifics in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on TriZetto Facets claim domain, statuses, and Cambia specifics: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q11: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q11: 5-stage trace + repo map complete"
```

### Q12. How do you handle TriZetto Facets claim domain, statuses, and Cambia specifics in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on TriZetto Facets claim domain, statuses, and Cambia specifics: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q12: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q12: 5-stage trace + repo map complete"
```

### Q13. How do you handle TriZetto Facets claim domain, statuses, and Cambia specifics in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on TriZetto Facets claim domain, statuses, and Cambia specifics: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q13: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q13: 5-stage trace + repo map complete"
```

### Q14. How do you handle TriZetto Facets claim domain, statuses, and Cambia specifics in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on TriZetto Facets claim domain, statuses, and Cambia specifics: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q14: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q14: 5-stage trace + repo map complete"
```

### Q15. How do you handle TriZetto Facets claim domain, statuses, and Cambia specifics in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on TriZetto Facets claim domain, statuses, and Cambia specifics: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q15: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q15: 5-stage trace + repo map complete"
```

### Q16. How do you handle TriZetto Facets claim domain, statuses, and Cambia specifics in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on TriZetto Facets claim domain, statuses, and Cambia specifics: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q16: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q16: 5-stage trace + repo map complete"
```

### Q17. How do you handle TriZetto Facets claim domain, statuses, and Cambia specifics in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on TriZetto Facets claim domain, statuses, and Cambia specifics: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q17: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q17: 5-stage trace + repo map complete"
```

### Q18. How do you handle TriZetto Facets claim domain, statuses, and Cambia specifics in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on TriZetto Facets claim domain, statuses, and Cambia specifics: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q18: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q18: 5-stage trace + repo map complete"
```

### Q19. How do you handle TriZetto Facets claim domain, statuses, and Cambia specifics in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on TriZetto Facets claim domain, statuses, and Cambia specifics: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q19: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q19: 5-stage trace + repo map complete"
```

### Q20. How do you handle TriZetto Facets claim domain, statuses, and Cambia specifics in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on TriZetto Facets claim domain, statuses, and Cambia specifics: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q20: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q20: 5-stage trace + repo map complete"
```

### Q21. How do you handle TriZetto Facets claim domain, statuses, and Cambia specifics in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on TriZetto Facets claim domain, statuses, and Cambia specifics: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q21: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q21: 5-stage trace + repo map complete"
```

### Q22. How do you handle TriZetto Facets claim domain, statuses, and Cambia specifics in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on TriZetto Facets claim domain, statuses, and Cambia specifics: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q22: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q22: 5-stage trace + repo map complete"
```

### Q23. How do you handle TriZetto Facets claim domain, statuses, and Cambia specifics in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on TriZetto Facets claim domain, statuses, and Cambia specifics: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q23: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q23: 5-stage trace + repo map complete"
```

### Q24. How do you handle TriZetto Facets claim domain, statuses, and Cambia specifics in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on TriZetto Facets claim domain, statuses, and Cambia specifics: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q24: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q24: 5-stage trace + repo map complete"
```

### Q25. How do you handle TriZetto Facets claim domain, statuses, and Cambia specifics in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on TriZetto Facets claim domain, statuses, and Cambia specifics: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q25: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q25: 5-stage trace + repo map complete"
```

### Q26. How do you handle TriZetto Facets claim domain, statuses, and Cambia specifics in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on TriZetto Facets claim domain, statuses, and Cambia specifics: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q26: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q26: 5-stage trace + repo map complete"
```

### Q27. How do you handle TriZetto Facets claim domain, statuses, and Cambia specifics in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on TriZetto Facets claim domain, statuses, and Cambia specifics: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q27: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q27: 5-stage trace + repo map complete"
```

### Q28. How do you handle TriZetto Facets claim domain, statuses, and Cambia specifics in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on TriZetto Facets claim domain, statuses, and Cambia specifics: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q28: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q28: 5-stage trace + repo map complete"
```


## Section C: Architecture & System Design

### Q29. Walk through the 5-stage end-to-end architecture.

**Answer:** Stage 1: on-prem Facets SQL Server via Palo Alto VPN to cambia-facets-networking AWS account. Stage 2: Step Functions CDC → encrypted JSON + manifest to intermediate S3. Stage 3: SFTP landing → NextGen raw → bronze SCD2. Stage 4: silver unified timeline → dual gold FM. Stage 5: SAM/FHIR (Onyx) + Snowflake egress + Reltio MDM.

**Example:** Architecture diagram: 10-step flow from CDC read replica through bronze CMC_CLCL_CLAIM to gold.fm_claim and gold.fm_claim_cambia.

**How to Check:**
- Confluence: Facets-Claims-Implementation-Bronze-Silver-Gold; Lucid Facets Claims Overall Flow Chart

**How to Fix:**
- Whiteboard all 5 stages with repo names at each box.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q29: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q29: 5-stage trace + repo map complete"
```

### Q30. How do you handle 5-stage architecture and component boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on 5-stage architecture and component boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q30: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q30: 5-stage trace + repo map complete"
```

### Q31. How do you handle 5-stage architecture and component boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on 5-stage architecture and component boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q31: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q31: 5-stage trace + repo map complete"
```

### Q32. How do you handle 5-stage architecture and component boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on 5-stage architecture and component boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q32: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q32: 5-stage trace + repo map complete"
```

### Q33. How do you handle 5-stage architecture and component boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on 5-stage architecture and component boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q33: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q33: 5-stage trace + repo map complete"
```

### Q34. How do you handle 5-stage architecture and component boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on 5-stage architecture and component boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q34: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q34: 5-stage trace + repo map complete"
```

### Q35. How do you handle 5-stage architecture and component boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on 5-stage architecture and component boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q35: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q35: 5-stage trace + repo map complete"
```

### Q36. How do you handle 5-stage architecture and component boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on 5-stage architecture and component boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q36: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q36: 5-stage trace + repo map complete"
```

### Q37. How do you handle 5-stage architecture and component boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on 5-stage architecture and component boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q37: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q37: 5-stage trace + repo map complete"
```

### Q38. How do you handle 5-stage architecture and component boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on 5-stage architecture and component boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q38: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q38: 5-stage trace + repo map complete"
```

### Q39. How do you handle 5-stage architecture and component boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on 5-stage architecture and component boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q39: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q39: 5-stage trace + repo map complete"
```

### Q40. How do you handle 5-stage architecture and component boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on 5-stage architecture and component boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q40: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q40: 5-stage trace + repo map complete"
```

### Q41. How do you handle 5-stage architecture and component boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on 5-stage architecture and component boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q41: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q41: 5-stage trace + repo map complete"
```

### Q42. How do you handle 5-stage architecture and component boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on 5-stage architecture and component boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q42: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q42: 5-stage trace + repo map complete"
```

### Q43. How do you handle 5-stage architecture and component boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on 5-stage architecture and component boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q43: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q43: 5-stage trace + repo map complete"
```

### Q44. How do you handle 5-stage architecture and component boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on 5-stage architecture and component boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q44: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q44: 5-stage trace + repo map complete"
```

### Q45. How do you handle 5-stage architecture and component boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on 5-stage architecture and component boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q45: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q45: 5-stage trace + repo map complete"
```


## Section D: Data Engineering & Databricks

### Q46. How does bronze ingestion work for Facets claims?

**Answer:** Manifest-triggered Databricks workflows load encrypted JSON into 44+ bronze tables using AIR library SCD Type 2. Key tables: CMC_CLCL_CLAIM, CMC_CDML_CL_LINE (medical), CMC_CDDL_CL_LINE (dental), CMC_CLST_STATUS, CMC_MEME_MEMBER, CMC_SBSB_SUBSC.

**Example:** 420 Facets bronze tables released in prod (TechOps Jun 2024); incremental tracked via table_changes and manifest batch IDs.

**How to Check:**
- SELECT COUNT(*) FROM bronze.cmc_clcl_claim WHERE _is_current = true

**How to Fix:**
- Verify manifest schema before bronze job; fail closed if encryption key or AIR version mismatch.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q46: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q47. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q47: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q48. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q48: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q49. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q49: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q50. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q50: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q51. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q51: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q52. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q52: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q53. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q53: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q54. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q54: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q55. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q55: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q56. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q56: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q57. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q57: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q58. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q58: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q59. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q59: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q60. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q60: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q61. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q61: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q62. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q62: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q63. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q63: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q64. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q64: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q65. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q65: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q66. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q66: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q67. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q67: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q68. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q68: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q69. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q69: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q70. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q70: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q71. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q71: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q72. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q72: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q73. How do you handle Databricks bronze/silver/gold and SCD2 patterns in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Databricks bronze/silver/gold and SCD2 patterns: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q73: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```


## Section E: FHIR & Downstream Interop

### Q74. How do gold Facets tables feed SAM and FHIR?

**Answer:** Interop path: gold.fm_claim + gold.fm_claim_item filtered for CMS-9115 SAM (75 groups, Medicare patients, dental excluded). Onyx ng-pipelines-onyx runs DM 2.0 → FHIR Claim, ClaimCoverage, ClaimDiagnosis, etc. Workflow: cambia02-claims-dataingestion-workflow.

**Example:** Dental claims exist in bronze/silver but filtered out of Interop fm_claim before SAM load; CDP gold retains all.

**How to Check:**
- FHIR ingestion workflow job run history in Onyx; validate Claim resources against US Core

**How to Fix:**
- Confirm group filter list matches current attribution before SAM extract.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q74: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q74: Interop vs CDP row counts and dental filter verified
```

### Q75. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q75: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q75: Interop vs CDP row counts and dental filter verified
```

### Q76. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q76: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q76: Interop vs CDP row counts and dental filter verified
```

### Q77. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q77: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q77: Interop vs CDP row counts and dental filter verified
```

### Q78. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q78: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q78: Interop vs CDP row counts and dental filter verified
```

### Q79. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q79: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q79: Interop vs CDP row counts and dental filter verified
```

### Q80. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q80: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q80: Interop vs CDP row counts and dental filter verified
```

### Q81. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q81: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q81: Interop vs CDP row counts and dental filter verified
```

### Q82. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q82: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q82: Interop vs CDP row counts and dental filter verified
```

### Q83. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q83: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q83: Interop vs CDP row counts and dental filter verified
```

### Q84. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q84: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q84: Interop vs CDP row counts and dental filter verified
```

### Q85. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q85: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q85: Interop vs CDP row counts and dental filter verified
```

### Q86. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q86: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q86: Interop vs CDP row counts and dental filter verified
```

### Q87. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q87: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q87: Interop vs CDP row counts and dental filter verified
```

### Q88. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q88: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q88: Interop vs CDP row counts and dental filter verified
```

### Q89. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q89: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q89: Interop vs CDP row counts and dental filter verified
```

### Q90. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q90: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q90: Interop vs CDP row counts and dental filter verified
```

### Q91. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q91: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q91: Interop vs CDP row counts and dental filter verified
```

### Q92. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q92: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q92: Interop vs CDP row counts and dental filter verified
```

### Q93. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q93: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q93: Interop vs CDP row counts and dental filter verified
```

### Q94. How do you handle SAM/FHIR downstream from gold FM tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SAM/FHIR downstream from gold FM tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q94: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q94: Interop vs CDP row counts and dental filter verified
```


## Section F: Security, Auth & Compliance

### Q95. How do you handle VPN, encryption, HIPAA, and HITRUST boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on VPN, encryption, HIPAA, and HITRUST boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q95: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q95: 5-stage trace + repo map complete"
```

### Q96. How do you handle VPN, encryption, HIPAA, and HITRUST boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on VPN, encryption, HIPAA, and HITRUST boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q96: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q96: 5-stage trace + repo map complete"
```

### Q97. How do you handle VPN, encryption, HIPAA, and HITRUST boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on VPN, encryption, HIPAA, and HITRUST boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q97: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q97: 5-stage trace + repo map complete"
```

### Q98. How do you handle VPN, encryption, HIPAA, and HITRUST boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on VPN, encryption, HIPAA, and HITRUST boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q98: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q98: 5-stage trace + repo map complete"
```

### Q99. How do you handle VPN, encryption, HIPAA, and HITRUST boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on VPN, encryption, HIPAA, and HITRUST boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q99: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q99: 5-stage trace + repo map complete"
```

### Q100. How do you handle VPN, encryption, HIPAA, and HITRUST boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on VPN, encryption, HIPAA, and HITRUST boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q100: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q100: 5-stage trace + repo map complete"
```

### Q101. How do you handle VPN, encryption, HIPAA, and HITRUST boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on VPN, encryption, HIPAA, and HITRUST boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q101: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q101: 5-stage trace + repo map complete"
```

### Q102. How do you handle VPN, encryption, HIPAA, and HITRUST boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on VPN, encryption, HIPAA, and HITRUST boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q102: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q102: 5-stage trace + repo map complete"
```

### Q103. How do you handle VPN, encryption, HIPAA, and HITRUST boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on VPN, encryption, HIPAA, and HITRUST boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q103: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q103: 5-stage trace + repo map complete"
```

### Q104. How do you handle VPN, encryption, HIPAA, and HITRUST boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on VPN, encryption, HIPAA, and HITRUST boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q104: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q104: 5-stage trace + repo map complete"
```

### Q105. How do you handle VPN, encryption, HIPAA, and HITRUST boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on VPN, encryption, HIPAA, and HITRUST boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q105: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q105: 5-stage trace + repo map complete"
```

### Q106. How do you handle VPN, encryption, HIPAA, and HITRUST boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on VPN, encryption, HIPAA, and HITRUST boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q106: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q106: 5-stage trace + repo map complete"
```

### Q107. How do you handle VPN, encryption, HIPAA, and HITRUST boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on VPN, encryption, HIPAA, and HITRUST boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q107: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q107: 5-stage trace + repo map complete"
```

### Q108. How do you handle VPN, encryption, HIPAA, and HITRUST boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on VPN, encryption, HIPAA, and HITRUST boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q108: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q108: 5-stage trace + repo map complete"
```

### Q109. How do you handle VPN, encryption, HIPAA, and HITRUST boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on VPN, encryption, HIPAA, and HITRUST boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q109: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q109: 5-stage trace + repo map complete"
```

### Q110. How do you handle VPN, encryption, HIPAA, and HITRUST boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on VPN, encryption, HIPAA, and HITRUST boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q110: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q110: 5-stage trace + repo map complete"
```

### Q111. How do you handle VPN, encryption, HIPAA, and HITRUST boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on VPN, encryption, HIPAA, and HITRUST boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q111: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q111: 5-stage trace + repo map complete"
```

### Q112. How do you handle VPN, encryption, HIPAA, and HITRUST boundaries in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on VPN, encryption, HIPAA, and HITRUST boundaries: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q112: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q112: 5-stage trace + repo map complete"
```


## Section G: CDC Extraction & facets-core

### Q113. How does Facets CDC extraction work?

**Answer:** SQL Server CDC → unique change IDs → partitioned JSON files → encryption → manifest.json. Orchestration: Step Functions + Lambda (light) + AWS Batch (heavy SQL). Intermediate S3: abacus-facets-intermediate-<env>/claims-incremental/, claims-historical/.

**Example:** ~25 JSON files per batch: header, medical/dental line items, diagnosis, PPL, delete files + manifest.

**How to Check:**
- DynamoDB CdcGlobals lock — one CDC job per domain; overlapping runs dropped

**How to Fix:**
- Check Step Functions execution history; verify nightly trigger Facets_BatchJobComplete_<OrderNumber>_<timestamp>.txt

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q113: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q113: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q114. How do you handle facets-core CDC, Step Functions, and Batch jobs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on facets-core CDC, Step Functions, and Batch jobs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q114: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q114: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q115. How do you handle facets-core CDC, Step Functions, and Batch jobs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on facets-core CDC, Step Functions, and Batch jobs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q115: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q115: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q116. How do you handle facets-core CDC, Step Functions, and Batch jobs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on facets-core CDC, Step Functions, and Batch jobs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q116: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q116: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q117. How do you handle facets-core CDC, Step Functions, and Batch jobs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on facets-core CDC, Step Functions, and Batch jobs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q117: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q117: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q118. How do you handle facets-core CDC, Step Functions, and Batch jobs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on facets-core CDC, Step Functions, and Batch jobs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q118: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q118: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q119. How do you handle facets-core CDC, Step Functions, and Batch jobs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on facets-core CDC, Step Functions, and Batch jobs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q119: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q119: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q120. How do you handle facets-core CDC, Step Functions, and Batch jobs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on facets-core CDC, Step Functions, and Batch jobs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q120: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q120: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q121. How do you handle facets-core CDC, Step Functions, and Batch jobs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on facets-core CDC, Step Functions, and Batch jobs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q121: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q121: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q122. How do you handle facets-core CDC, Step Functions, and Batch jobs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on facets-core CDC, Step Functions, and Batch jobs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q122: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q122: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q123. How do you handle facets-core CDC, Step Functions, and Batch jobs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on facets-core CDC, Step Functions, and Batch jobs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q123: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q123: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q124. How do you handle facets-core CDC, Step Functions, and Batch jobs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on facets-core CDC, Step Functions, and Batch jobs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q124: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q124: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```


## Section H: Dual Gold Paths — Interop vs CDP

### Q125. Explain the dual gold path: Interop vs CDP.

**Answer:** Interop: gold.fm_claim, gold.fm_claim_item — filtered for CMS-9115 SAM/FHIR (75 groups, Medicare, no dental). CDP: gold.fm_claim_cambia, gold.fm_claim_item_cambia — full 1:1 silver mapping + data signature bitmap for customer data platform.

**Example:** silver.claim_facets (Interop filtered) vs silver.claim_facets_cambia (CDP unfiltered)

**How to Check:**
- Row count ratio CDP/Interop > 1 due to dental + non-Medicare claims retained in CDP only

**How to Fix:**
- Never merge Interop and CDP paths; separate pipespecs and downstream consumers.

**Script:** *(builds proficiency: FHIR Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q125: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q125: Interop vs CDP row counts and dental filter verified
```

### Q126. How do you handle Interop vs CDP dual gold filtering in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Interop vs CDP dual gold filtering: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q126: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q126: Interop vs CDP row counts and dental filter verified
```

### Q127. How do you handle Interop vs CDP dual gold filtering in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Interop vs CDP dual gold filtering: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q127: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q127: Interop vs CDP row counts and dental filter verified
```

### Q128. How do you handle Interop vs CDP dual gold filtering in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Interop vs CDP dual gold filtering: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q128: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q128: Interop vs CDP row counts and dental filter verified
```

### Q129. How do you handle Interop vs CDP dual gold filtering in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Interop vs CDP dual gold filtering: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q129: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q129: Interop vs CDP row counts and dental filter verified
```

### Q130. How do you handle Interop vs CDP dual gold filtering in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Interop vs CDP dual gold filtering: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q130: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q130: Interop vs CDP row counts and dental filter verified
```

### Q131. How do you handle Interop vs CDP dual gold filtering in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Interop vs CDP dual gold filtering: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q131: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q131: Interop vs CDP row counts and dental filter verified
```

### Q132. How do you handle Interop vs CDP dual gold filtering in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Interop vs CDP dual gold filtering: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q132: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q132: Interop vs CDP row counts and dental filter verified
```

### Q133. How do you handle Interop vs CDP dual gold filtering in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Interop vs CDP dual gold filtering: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q133: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q133: Interop vs CDP row counts and dental filter verified
```

### Q134. How do you handle Interop vs CDP dual gold filtering in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Interop vs CDP dual gold filtering: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q134: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q134: Interop vs CDP row counts and dental filter verified
```

### Q135. How do you handle Interop vs CDP dual gold filtering in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Interop vs CDP dual gold filtering: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q135: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q135: Interop vs CDP row counts and dental filter verified
```

### Q136. How do you handle Interop vs CDP dual gold filtering in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Interop vs CDP dual gold filtering: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q136: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q136: Interop vs CDP row counts and dental filter verified
```

### Q137. How do you handle Interop vs CDP dual gold filtering in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Interop vs CDP dual gold filtering: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q137: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q137: Interop vs CDP row counts and dental filter verified
```

### Q138. How do you handle Interop vs CDP dual gold filtering in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Interop vs CDP dual gold filtering: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q138: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q138: Interop vs CDP row counts and dental filter verified
```

### Q139. How do you handle Interop vs CDP dual gold filtering in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Interop vs CDP dual gold filtering: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q139: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q139: Interop vs CDP row counts and dental filter verified
```

### Q140. How do you handle Interop vs CDP dual gold filtering in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Interop vs CDP dual gold filtering: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q140: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q140: Interop vs CDP row counts and dental filter verified
```

### Q141. How do you handle Interop vs CDP dual gold filtering in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Interop vs CDP dual gold filtering: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: FHIR Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q141: Dual gold / FHIR path check
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q141: Interop vs CDP row counts and dental filter verified
```


## Section I: Deployment, Operations & Troubleshooting

### Q142. How do you handle deploy, monitor, and restore Facets pipelines in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on deploy, monitor, and restore Facets pipelines: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q142: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q142: 5-stage trace + repo map complete"
```

### Q143. How do you handle deploy, monitor, and restore Facets pipelines in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on deploy, monitor, and restore Facets pipelines: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q143: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q143: 5-stage trace + repo map complete"
```

### Q144. How do you handle deploy, monitor, and restore Facets pipelines in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on deploy, monitor, and restore Facets pipelines: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q144: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q144: 5-stage trace + repo map complete"
```

### Q145. How do you handle deploy, monitor, and restore Facets pipelines in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on deploy, monitor, and restore Facets pipelines: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q145: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q145: 5-stage trace + repo map complete"
```

### Q146. How do you handle deploy, monitor, and restore Facets pipelines in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on deploy, monitor, and restore Facets pipelines: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q146: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q146: 5-stage trace + repo map complete"
```

### Q147. How do you handle deploy, monitor, and restore Facets pipelines in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on deploy, monitor, and restore Facets pipelines: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q147: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q147: 5-stage trace + repo map complete"
```

### Q148. How do you handle deploy, monitor, and restore Facets pipelines in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on deploy, monitor, and restore Facets pipelines: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q148: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q148: 5-stage trace + repo map complete"
```

### Q149. How do you handle deploy, monitor, and restore Facets pipelines in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on deploy, monitor, and restore Facets pipelines: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q149: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q149: 5-stage trace + repo map complete"
```

### Q150. How do you handle deploy, monitor, and restore Facets pipelines in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on deploy, monitor, and restore Facets pipelines: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q150: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q150: 5-stage trace + repo map complete"
```

### Q151. How do you handle deploy, monitor, and restore Facets pipelines in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on deploy, monitor, and restore Facets pipelines: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q151: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q151: 5-stage trace + repo map complete"
```

### Q152. How do you handle deploy, monitor, and restore Facets pipelines in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on deploy, monitor, and restore Facets pipelines: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q152: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q152: 5-stage trace + repo map complete"
```

### Q153. How do you handle deploy, monitor, and restore Facets pipelines in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on deploy, monitor, and restore Facets pipelines: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q153: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q153: 5-stage trace + repo map complete"
```

### Q154. How do you handle deploy, monitor, and restore Facets pipelines in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on deploy, monitor, and restore Facets pipelines: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q154: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q154: 5-stage trace + repo map complete"
```


## Section J: Reporting, Analytics & KPIs

### Q155. How do you handle pipeline KPIs, lag, and batch SLAs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on pipeline KPIs, lag, and batch SLAs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q155: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q155: 5-stage trace + repo map complete"
```

### Q156. How do you handle pipeline KPIs, lag, and batch SLAs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on pipeline KPIs, lag, and batch SLAs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q156: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q156: 5-stage trace + repo map complete"
```

### Q157. How do you handle pipeline KPIs, lag, and batch SLAs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on pipeline KPIs, lag, and batch SLAs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q157: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q157: 5-stage trace + repo map complete"
```

### Q158. How do you handle pipeline KPIs, lag, and batch SLAs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on pipeline KPIs, lag, and batch SLAs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q158: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q158: 5-stage trace + repo map complete"
```

### Q159. How do you handle pipeline KPIs, lag, and batch SLAs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on pipeline KPIs, lag, and batch SLAs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q159: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q159: 5-stage trace + repo map complete"
```

### Q160. How do you handle pipeline KPIs, lag, and batch SLAs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on pipeline KPIs, lag, and batch SLAs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q160: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q160: 5-stage trace + repo map complete"
```

### Q161. How do you handle pipeline KPIs, lag, and batch SLAs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on pipeline KPIs, lag, and batch SLAs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q161: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q161: 5-stage trace + repo map complete"
```

### Q162. How do you handle pipeline KPIs, lag, and batch SLAs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on pipeline KPIs, lag, and batch SLAs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q162: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q162: 5-stage trace + repo map complete"
```


## Section K: Claims & RCM Bridge

### Q163. How do you handle claims lifecycle and RCM handoff from Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on claims lifecycle and RCM handoff from Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q163: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q163: 5-stage trace + repo map complete"
```

### Q164. How do you handle claims lifecycle and RCM handoff from Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on claims lifecycle and RCM handoff from Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q164: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q164: 5-stage trace + repo map complete"
```

### Q165. How do you handle claims lifecycle and RCM handoff from Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on claims lifecycle and RCM handoff from Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q165: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q165: 5-stage trace + repo map complete"
```

### Q166. How do you handle claims lifecycle and RCM handoff from Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on claims lifecycle and RCM handoff from Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q166: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q166: 5-stage trace + repo map complete"
```

### Q167. How do you handle claims lifecycle and RCM handoff from Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on claims lifecycle and RCM handoff from Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q167: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q167: 5-stage trace + repo map complete"
```

### Q168. How do you handle claims lifecycle and RCM handoff from Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on claims lifecycle and RCM handoff from Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q168: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q168: 5-stage trace + repo map complete"
```

### Q169. How do you handle claims lifecycle and RCM handoff from Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on claims lifecycle and RCM handoff from Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q169: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q169: 5-stage trace + repo map complete"
```

### Q170. How do you handle claims lifecycle and RCM handoff from Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on claims lifecycle and RCM handoff from Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q170: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q170: 5-stage trace + repo map complete"
```

### Q171. How do you handle claims lifecycle and RCM handoff from Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on claims lifecycle and RCM handoff from Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q171: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q171: 5-stage trace + repo map complete"
```

### Q172. How do you handle claims lifecycle and RCM handoff from Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on claims lifecycle and RCM handoff from Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q172: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q172: 5-stage trace + repo map complete"
```


## Section L: Leadership & Program Management

### Q173. How do you handle program management across Cambia and Abacus teams in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on program management across Cambia and Abacus teams: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q173: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q173: 5-stage trace + repo map complete"
```

### Q174. How do you handle program management across Cambia and Abacus teams in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on program management across Cambia and Abacus teams: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q174: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q174: 5-stage trace + repo map complete"
```

### Q175. How do you handle program management across Cambia and Abacus teams in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on program management across Cambia and Abacus teams: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q175: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q175: 5-stage trace + repo map complete"
```

### Q176. How do you handle program management across Cambia and Abacus teams in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on program management across Cambia and Abacus teams: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q176: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q176: 5-stage trace + repo map complete"
```

### Q177. How do you handle program management across Cambia and Abacus teams in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on program management across Cambia and Abacus teams: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q177: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q177: 5-stage trace + repo map complete"
```

### Q178. How do you handle program management across Cambia and Abacus teams in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on program management across Cambia and Abacus teams: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q178: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q178: 5-stage trace + repo map complete"
```

### Q179. How do you handle program management across Cambia and Abacus teams in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on program management across Cambia and Abacus teams: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q179: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q179: 5-stage trace + repo map complete"
```

### Q180. How do you handle program management across Cambia and Abacus teams in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on program management across Cambia and Abacus teams: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q180: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q180: 5-stage trace + repo map complete"
```

### Q181. How do you handle program management across Cambia and Abacus teams in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on program management across Cambia and Abacus teams: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q181: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q181: 5-stage trace + repo map complete"
```

### Q182. How do you handle program management across Cambia and Abacus teams in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on program management across Cambia and Abacus teams: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q182: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q182: 5-stage trace + repo map complete"
```

### Q183. How do you handle program management across Cambia and Abacus teams in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on program management across Cambia and Abacus teams: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q183: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q183: 5-stage trace + repo map complete"
```

### Q184. How do you handle program management across Cambia and Abacus teams in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on program management across Cambia and Abacus teams: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q184: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q184: 5-stage trace + repo map complete"
```

### Q185. How do you handle program management across Cambia and Abacus teams in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on program management across Cambia and Abacus teams: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q185: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q185: 5-stage trace + repo map complete"
```


## Section M: Scenario Troubleshooting

### Q186. How do you handle incident scenarios: missed batch, lock contention, manifest mismatch in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on incident scenarios: missed batch, lock contention, manifest mismatch: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q186: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q186: 5-stage trace + repo map complete"
```

### Q187. How do you handle incident scenarios: missed batch, lock contention, manifest mismatch in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on incident scenarios: missed batch, lock contention, manifest mismatch: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q187: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q187: 5-stage trace + repo map complete"
```

### Q188. How do you handle incident scenarios: missed batch, lock contention, manifest mismatch in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on incident scenarios: missed batch, lock contention, manifest mismatch: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q188: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q188: 5-stage trace + repo map complete"
```

### Q189. How do you handle incident scenarios: missed batch, lock contention, manifest mismatch in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on incident scenarios: missed batch, lock contention, manifest mismatch: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q189: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q189: 5-stage trace + repo map complete"
```

### Q190. How do you handle incident scenarios: missed batch, lock contention, manifest mismatch in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on incident scenarios: missed batch, lock contention, manifest mismatch: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q190: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q190: 5-stage trace + repo map complete"
```

### Q191. How do you handle incident scenarios: missed batch, lock contention, manifest mismatch in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on incident scenarios: missed batch, lock contention, manifest mismatch: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q191: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q191: 5-stage trace + repo map complete"
```

### Q192. How do you handle incident scenarios: missed batch, lock contention, manifest mismatch in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on incident scenarios: missed batch, lock contention, manifest mismatch: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q192: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q192: 5-stage trace + repo map complete"
```

### Q193. How do you handle incident scenarios: missed batch, lock contention, manifest mismatch in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on incident scenarios: missed batch, lock contention, manifest mismatch: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q193: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q193: 5-stage trace + repo map complete"
```

### Q194. How do you handle incident scenarios: missed batch, lock contention, manifest mismatch in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on incident scenarios: missed batch, lock contention, manifest mismatch: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q194: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q194: 5-stage trace + repo map complete"
```

### Q195. How do you handle incident scenarios: missed batch, lock contention, manifest mismatch in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on incident scenarios: missed batch, lock contention, manifest mismatch: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q195: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q195: 5-stage trace + repo map complete"
```


## Section N: Snowflake Egress

### Q196. How do you handle Snowflake egress and chunked history loads in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Snowflake egress and chunked history loads: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q196: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q197. How do you handle Snowflake egress and chunked history loads in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Snowflake egress and chunked history loads: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q197: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q198. How do you handle Snowflake egress and chunked history loads in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Snowflake egress and chunked history loads: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q198: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q199. How do you handle Snowflake egress and chunked history loads in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Snowflake egress and chunked history loads: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q199: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q200. How do you handle Snowflake egress and chunked history loads in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Snowflake egress and chunked history loads: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q200: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q201. How do you handle Snowflake egress and chunked history loads in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Snowflake egress and chunked history loads: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q201: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q202. How do you handle Snowflake egress and chunked history loads in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Snowflake egress and chunked history loads: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q202: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q203. How do you handle Snowflake egress and chunked history loads in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Snowflake egress and chunked history loads: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q203: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q204. How do you handle Snowflake egress and chunked history loads in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Snowflake egress and chunked history loads: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q204: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q205. How do you handle Snowflake egress and chunked history loads in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Snowflake egress and chunked history loads: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q205: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```


## Section O: Orchestration & ng-orchestration-service

### Q206. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q206: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q206: 5-stage trace + repo map complete"
```

### Q207. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q207: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q207: 5-stage trace + repo map complete"
```

### Q208. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q208: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q208: 5-stage trace + repo map complete"
```

### Q209. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q209: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q209: 5-stage trace + repo map complete"
```

### Q210. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q210: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q210: 5-stage trace + repo map complete"
```

### Q211. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q211: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q211: 5-stage trace + repo map complete"
```

### Q212. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q212: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q212: 5-stage trace + repo map complete"
```

### Q213. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q213: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q213: 5-stage trace + repo map complete"
```

### Q214. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q214: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q214: 5-stage trace + repo map complete"
```

### Q215. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q215: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q215: 5-stage trace + repo map complete"
```

### Q216. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q216: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q216: 5-stage trace + repo map complete"
```

### Q217. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q217: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q217: 5-stage trace + repo map complete"
```

### Q218. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q218: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q218: 5-stage trace + repo map complete"
```

### Q219. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q219: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q219: 5-stage trace + repo map complete"
```

### Q220. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q220: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q220: 5-stage trace + repo map complete"
```

### Q221. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q221: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q221: 5-stage trace + repo map complete"
```

### Q222. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q222: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q222: 5-stage trace + repo map complete"
```

### Q223. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q223: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q223: 5-stage trace + repo map complete"
```

### Q224. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q224: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q224: 5-stage trace + repo map complete"
```

### Q225. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q225: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q225: 5-stage trace + repo map complete"
```

### Q226. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q226: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q226: 5-stage trace + repo map complete"
```

### Q227. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q227: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q227: 5-stage trace + repo map complete"
```

### Q228. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q228: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q228: 5-stage trace + repo map complete"
```

### Q229. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q229: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q229: 5-stage trace + repo map complete"
```

### Q230. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q230: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q230: 5-stage trace + repo map complete"
```

### Q231. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q231: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q231: 5-stage trace + repo map complete"
```

### Q232. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q232: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q232: 5-stage trace + repo map complete"
```

### Q233. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q233: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q233: 5-stage trace + repo map complete"
```

### Q234. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q234: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q234: 5-stage trace + repo map complete"
```

### Q235. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q235: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q235: 5-stage trace + repo map complete"
```

### Q236. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q236: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q236: 5-stage trace + repo map complete"
```

### Q237. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q237: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q237: 5-stage trace + repo map complete"
```

### Q238. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q238: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q238: 5-stage trace + repo map complete"
```

### Q239. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q239: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q239: 5-stage trace + repo map complete"
```

### Q240. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q240: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q240: 5-stage trace + repo map complete"
```

### Q241. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q241: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q241: 5-stage trace + repo map complete"
```

### Q242. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q242: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q242: 5-stage trace + repo map complete"
```

### Q243. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q243: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q243: 5-stage trace + repo map complete"
```

### Q244. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q244: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q244: 5-stage trace + repo map complete"
```

### Q245. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q245: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q245: 5-stage trace + repo map complete"
```

### Q246. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q246: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q246: 5-stage trace + repo map complete"
```

### Q247. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q247: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q247: 5-stage trace + repo map complete"
```

### Q248. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q248: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q248: 5-stage trace + repo map complete"
```

### Q249. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q249: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q249: 5-stage trace + repo map complete"
```

### Q250. How do you handle ng-orchestration-service manifest triggers in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-orchestration-service manifest triggers: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q250: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q250: 5-stage trace + repo map complete"
```


## Section P: SFTP/Inbound & Landing Zone

### Q251. How does SFTP landing and inbound transfer work?

**Answer:** Encrypted files + manifest → Abacus SFTP / connector landing zone → NextGen raw S3 (cambia02). Catalog: ng-abacus-inbound-infra, config/repo-rules/transporters/sftp.yaml. Nightly batch trigger file dropped to SFTP kicks CDC immediately after Cambia batch.

**Example:** Manifest path: cambia/facets/cambia/claims/extension/incremental/*/*manifest.json

**How to Check:**
- SFTP connector logs; S3 object listing under cambia02 raw prefix

**How to Fix:**
- Validate file count matches manifest (~25 files per batch) before orchestration trigger.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q251: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q251: 5-stage trace + repo map complete"
```

### Q252. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q252: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q252: 5-stage trace + repo map complete"
```

### Q253. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q253: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q253: 5-stage trace + repo map complete"
```

### Q254. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q254: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q254: 5-stage trace + repo map complete"
```

### Q255. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q255: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q255: 5-stage trace + repo map complete"
```

### Q256. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q256: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q256: 5-stage trace + repo map complete"
```

### Q257. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q257: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q257: 5-stage trace + repo map complete"
```

### Q258. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q258: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q258: 5-stage trace + repo map complete"
```

### Q259. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q259: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q259: 5-stage trace + repo map complete"
```

### Q260. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q260: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q260: 5-stage trace + repo map complete"
```

### Q261. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q261: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q261: 5-stage trace + repo map complete"
```

### Q262. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q262: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q262: 5-stage trace + repo map complete"
```

### Q263. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q263: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q263: 5-stage trace + repo map complete"
```

### Q264. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q264: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q264: 5-stage trace + repo map complete"
```

### Q265. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q265: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q265: 5-stage trace + repo map complete"
```

### Q266. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q266: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q266: 5-stage trace + repo map complete"
```

### Q267. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q267: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q267: 5-stage trace + repo map complete"
```

### Q268. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q268: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q268: 5-stage trace + repo map complete"
```

### Q269. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q269: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q269: 5-stage trace + repo map complete"
```

### Q270. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q270: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q270: 5-stage trace + repo map complete"
```

### Q271. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q271: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q271: 5-stage trace + repo map complete"
```

### Q272. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q272: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q272: 5-stage trace + repo map complete"
```

### Q273. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q273: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q273: 5-stage trace + repo map complete"
```

### Q274. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q274: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q274: 5-stage trace + repo map complete"
```

### Q275. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q275: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q275: 5-stage trace + repo map complete"
```

### Q276. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q276: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q276: 5-stage trace + repo map complete"
```

### Q277. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q277: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q277: 5-stage trace + repo map complete"
```

### Q278. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q278: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q278: 5-stage trace + repo map complete"
```

### Q279. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q279: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q279: 5-stage trace + repo map complete"
```

### Q280. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q280: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q280: 5-stage trace + repo map complete"
```

### Q281. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q281: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q281: 5-stage trace + repo map complete"
```

### Q282. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q282: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q282: 5-stage trace + repo map complete"
```

### Q283. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q283: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q283: 5-stage trace + repo map complete"
```

### Q284. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q284: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q284: 5-stage trace + repo map complete"
```

### Q285. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q285: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q285: 5-stage trace + repo map complete"
```

### Q286. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q286: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q286: 5-stage trace + repo map complete"
```

### Q287. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q287: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q287: 5-stage trace + repo map complete"
```

### Q288. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q288: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q288: 5-stage trace + repo map complete"
```

### Q289. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q289: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q289: 5-stage trace + repo map complete"
```

### Q290. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q290: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q290: 5-stage trace + repo map complete"
```

### Q291. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q291: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q291: 5-stage trace + repo map complete"
```

### Q292. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q292: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q292: 5-stage trace + repo map complete"
```

### Q293. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q293: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q293: 5-stage trace + repo map complete"
```

### Q294. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q294: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q294: 5-stage trace + repo map complete"
```

### Q295. How do you handle SFTP inbound, landing zone, and file validation in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SFTP inbound, landing zone, and file validation: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q295: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q295: 5-stage trace + repo map complete"
```


## Section Q: Databricks Engineering — Facets Claims

### Q296. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q296: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q297. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q297: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q298. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q298: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q299. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q299: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q300. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q300: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q301. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q301: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q302. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q302: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q303. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q303: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q304. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q304: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q305. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q305: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q306. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q306: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q307. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q307: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q308. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q308: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q309. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q309: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q310. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q310: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q311. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q311: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q312. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q312: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q313. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q313: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q314. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q314: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q315. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q315: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q316. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q316: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q317. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q317: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q318. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q318: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q319. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q319: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q320. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q320: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q321. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q321: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q322. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q322: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q323. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q323: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q324. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q324: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q325. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q325: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q326. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q326: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q327. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q327: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q328. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q328: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q329. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q329: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```

### Q330. How do you handle ng-pipelines-cambia notebooks and pipespecs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on ng-pipelines-cambia notebooks and pipespecs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```sql
-- Q330: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;
```


## Section R: MDM & Reltio Integration

### Q331. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q331: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q331: 5-stage trace + repo map complete"
```

### Q332. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q332: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q332: 5-stage trace + repo map complete"
```

### Q333. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q333: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q333: 5-stage trace + repo map complete"
```

### Q334. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q334: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q334: 5-stage trace + repo map complete"
```

### Q335. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q335: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q335: 5-stage trace + repo map complete"
```

### Q336. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q336: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q336: 5-stage trace + repo map complete"
```

### Q337. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q337: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q337: 5-stage trace + repo map complete"
```

### Q338. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q338: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q338: 5-stage trace + repo map complete"
```

### Q339. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q339: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q339: 5-stage trace + repo map complete"
```

### Q340. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q340: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q340: 5-stage trace + repo map complete"
```

### Q341. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q341: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q341: 5-stage trace + repo map complete"
```

### Q342. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q342: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q342: 5-stage trace + repo map complete"
```

### Q343. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q343: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q343: 5-stage trace + repo map complete"
```

### Q344. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q344: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q344: 5-stage trace + repo map complete"
```

### Q345. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q345: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q345: 5-stage trace + repo map complete"
```

### Q346. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q346: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q346: 5-stage trace + repo map complete"
```

### Q347. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q347: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q347: 5-stage trace + repo map complete"
```

### Q348. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q348: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q348: 5-stage trace + repo map complete"
```

### Q349. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q349: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q349: 5-stage trace + repo map complete"
```

### Q350. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q350: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q350: 5-stage trace + repo map complete"
```

### Q351. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q351: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q351: 5-stage trace + repo map complete"
```

### Q352. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q352: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q352: 5-stage trace + repo map complete"
```

### Q353. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q353: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q353: 5-stage trace + repo map complete"
```

### Q354. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q354: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q354: 5-stage trace + repo map complete"
```

### Q355. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q355: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q355: 5-stage trace + repo map complete"
```

### Q356. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q356: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q356: 5-stage trace + repo map complete"
```

### Q357. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q357: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q357: 5-stage trace + repo map complete"
```

### Q358. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q358: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q358: 5-stage trace + repo map complete"
```

### Q359. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q359: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q359: 5-stage trace + repo map complete"
```

### Q360. How do you handle Reltio MDM feed from silver Facets in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Reltio MDM feed from silver Facets: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q360: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q360: 5-stage trace + repo map complete"
```


## Section S: AWS Networking & VPN

### Q361. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q361: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q361: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q362. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q362: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q362: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q363. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q363: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q363: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q364. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q364: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q364: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q365. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q365: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q365: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q366. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q366: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q366: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q367. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q367: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q367: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q368. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q368: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q368: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q369. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q369: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q369: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q370. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q370: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q370: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q371. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q371: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q371: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q372. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q372: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q372: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q373. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q373: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q373: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q374. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q374: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q374: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q375. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q375: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q375: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q376. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q376: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q376: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q377. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q377: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q377: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q378. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q378: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q378: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q379. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q379: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q379: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q380. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q380: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q380: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q381. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q381: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q381: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q382. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q382: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q382: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q383. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q383: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q383: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q384. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q384: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q384: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q385. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q385: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q385: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q386. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q386: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q386: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q387. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q387: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q387: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q388. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q388: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q388: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q389. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q389: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q389: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q390. How do you handle cambia-facets-networking VPN and Palo Alto in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on cambia-facets-networking VPN and Palo Alto: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q390: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q390: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```


## Section T: SQL Server CDC & Facets Source

### Q391. How does SQL Server CDC work on the Facets read replica?

**Answer:** Cambia on-prem Facets SQL Server 2016 CDC-enabled read replica. CDC captures inserts/updates/deletes; facets-core converts to unique change IDs for idempotent JSON partitions.

**Example:** Claim types: M/H medical, D dental. Status codes: 11=pended, 15=error, 01=pre-final, 02=final, 91=adjusted.

**How to Check:**
- Verify CDC latency on replica; compare LSN watermark in CdcGlobals

**How to Fix:**
- Never run heavy queries on primary; read replica only for CDC extraction.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q391: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q391: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q392. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q392: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q392: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q393. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q393: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q393: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q394. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q394: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q394: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q395. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q395: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q395: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q396. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q396: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q396: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q397. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q397: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q397: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q398. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q398: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q398: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q399. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q399: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q399: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q400. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q400: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q400: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q401. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q401: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q401: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q402. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q402: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q402: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q403. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q403: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q403: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q404. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q404: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q404: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q405. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q405: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q405: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q406. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q406: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q406: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q407. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q407: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q407: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q408. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q408: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q408: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q409. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q409: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q409: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q410. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q410: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q410: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q411. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q411: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q411: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q412. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q412: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q412: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q413. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q413: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q413: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q414. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q414: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q414: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```

### Q415. How do you handle SQL Server CDC and Facets source tables in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on SQL Server CDC and Facets source tables: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Intermediate Associate Programmer)*

```bash
#!/usr/bin/env bash
# Q415: Facets CDC / source proficiency drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q415: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock
```


## Section U: Operations at Scale & Volumes

### Q416. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q416: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q416: 5-stage trace + repo map complete"
```

### Q417. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q417: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q417: 5-stage trace + repo map complete"
```

### Q418. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q418: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q418: 5-stage trace + repo map complete"
```

### Q419. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q419: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q419: 5-stage trace + repo map complete"
```

### Q420. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q420: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q420: 5-stage trace + repo map complete"
```

### Q421. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q421: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q421: 5-stage trace + repo map complete"
```

### Q422. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q422: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q422: 5-stage trace + repo map complete"
```

### Q423. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q423: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q423: 5-stage trace + repo map complete"
```

### Q424. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q424: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q424: 5-stage trace + repo map complete"
```

### Q425. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q425: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q425: 5-stage trace + repo map complete"
```

### Q426. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q426: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q426: 5-stage trace + repo map complete"
```

### Q427. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q427: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q427: 5-stage trace + repo map complete"
```

### Q428. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q428: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q428: 5-stage trace + repo map complete"
```

### Q429. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q429: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q429: 5-stage trace + repo map complete"
```

### Q430. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q430: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q430: 5-stage trace + repo map complete"
```

### Q431. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q431: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q431: 5-stage trace + repo map complete"
```

### Q432. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q432: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q432: 5-stage trace + repo map complete"
```

### Q433. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q433: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q433: 5-stage trace + repo map complete"
```

### Q434. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q434: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q434: 5-stage trace + repo map complete"
```

### Q435. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q435: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q435: 5-stage trace + repo map complete"
```

### Q436. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q436: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q436: 5-stage trace + repo map complete"
```

### Q437. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q437: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q437: 5-stage trace + repo map complete"
```

### Q438. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q438: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q438: 5-stage trace + repo map complete"
```

### Q439. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q439: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q439: 5-stage trace + repo map complete"
```

### Q440. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q440: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q440: 5-stage trace + repo map complete"
```

### Q441. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q441: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q441: 5-stage trace + repo map complete"
```

### Q442. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q442: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q442: 5-stage trace + repo map complete"
```

### Q443. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q443: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q443: 5-stage trace + repo map complete"
```

### Q444. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q444: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q444: 5-stage trace + repo map complete"
```

### Q445. How do you handle volume profiles and performance at scale in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on volume profiles and performance at scale: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q445: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q445: 5-stage trace + repo map complete"
```


## Section V: De-Identification & Safe Harbor

### Q446. How do you handle de-identification for analytics paths in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on de-identification for analytics paths: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q446: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q446: 5-stage trace + repo map complete"
```

### Q447. How do you handle de-identification for analytics paths in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on de-identification for analytics paths: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q447: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q447: 5-stage trace + repo map complete"
```

### Q448. How do you handle de-identification for analytics paths in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on de-identification for analytics paths: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q448: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q448: 5-stage trace + repo map complete"
```

### Q449. How do you handle de-identification for analytics paths in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on de-identification for analytics paths: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q449: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q449: 5-stage trace + repo map complete"
```

### Q450. How do you handle de-identification for analytics paths in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on de-identification for analytics paths: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q450: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q450: 5-stage trace + repo map complete"
```

### Q451. How do you handle de-identification for analytics paths in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on de-identification for analytics paths: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q451: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q451: 5-stage trace + repo map complete"
```

### Q452. How do you handle de-identification for analytics paths in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on de-identification for analytics paths: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q452: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q452: 5-stage trace + repo map complete"
```

### Q453. How do you handle de-identification for analytics paths in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on de-identification for analytics paths: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q453: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q453: 5-stage trace + repo map complete"
```

### Q454. How do you handle de-identification for analytics paths in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on de-identification for analytics paths: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q454: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q454: 5-stage trace + repo map complete"
```

### Q455. How do you handle de-identification for analytics paths in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on de-identification for analytics paths: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q455: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q455: 5-stage trace + repo map complete"
```


## Section W: Master Data Management

### Q456. How do you handle MDM golden records from Facets member/provider in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on MDM golden records from Facets member/provider: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q456: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q456: 5-stage trace + repo map complete"
```

### Q457. How do you handle MDM golden records from Facets member/provider in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on MDM golden records from Facets member/provider: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q457: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q457: 5-stage trace + repo map complete"
```

### Q458. How do you handle MDM golden records from Facets member/provider in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on MDM golden records from Facets member/provider: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q458: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q458: 5-stage trace + repo map complete"
```

### Q459. How do you handle MDM golden records from Facets member/provider in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on MDM golden records from Facets member/provider: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q459: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q459: 5-stage trace + repo map complete"
```

### Q460. How do you handle MDM golden records from Facets member/provider in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on MDM golden records from Facets member/provider: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q460: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q460: 5-stage trace + repo map complete"
```

### Q461. How do you handle MDM golden records from Facets member/provider in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on MDM golden records from Facets member/provider: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q461: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q461: 5-stage trace + repo map complete"
```

### Q462. How do you handle MDM golden records from Facets member/provider in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on MDM golden records from Facets member/provider: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q462: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q462: 5-stage trace + repo map complete"
```

### Q463. How do you handle MDM golden records from Facets member/provider in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on MDM golden records from Facets member/provider: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q463: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q463: 5-stage trace + repo map complete"
```

### Q464. How do you handle MDM golden records from Facets member/provider in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on MDM golden records from Facets member/provider: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q464: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q464: 5-stage trace + repo map complete"
```

### Q465. How do you handle MDM golden records from Facets member/provider in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on MDM golden records from Facets member/provider: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | Associate Solution Architect)*

```bash
#!/usr/bin/env bash
# Q465: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q465: 5-stage trace + repo map complete"
```


## Section X: Interop vs CDP Path Comparison

### Q466. How do you handle when to use Interop vs CDP gold outputs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on when to use Interop vs CDP gold outputs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q466: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q466: 5-stage trace + repo map complete"
```

### Q467. How do you handle when to use Interop vs CDP gold outputs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on when to use Interop vs CDP gold outputs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q467: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q467: 5-stage trace + repo map complete"
```

### Q468. How do you handle when to use Interop vs CDP gold outputs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on when to use Interop vs CDP gold outputs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q468: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q468: 5-stage trace + repo map complete"
```

### Q469. How do you handle when to use Interop vs CDP gold outputs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on when to use Interop vs CDP gold outputs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q469: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q469: 5-stage trace + repo map complete"
```

### Q470. How do you handle when to use Interop vs CDP gold outputs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on when to use Interop vs CDP gold outputs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q470: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q470: 5-stage trace + repo map complete"
```

### Q471. How do you handle when to use Interop vs CDP gold outputs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on when to use Interop vs CDP gold outputs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q471: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q471: 5-stage trace + repo map complete"
```

### Q472. How do you handle when to use Interop vs CDP gold outputs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on when to use Interop vs CDP gold outputs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q472: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q472: 5-stage trace + repo map complete"
```

### Q473. How do you handle when to use Interop vs CDP gold outputs in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on when to use Interop vs CDP gold outputs: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Data Engineer | FHIR Engineer)*

```bash
#!/usr/bin/env bash
# Q473: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q473: 5-stage trace + repo map complete"
```


## Section Y: Observability & Monitoring

### Q474. How do you handle CloudWatch, Databricks alerts, delivery monitoring in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on CloudWatch, Databricks alerts, delivery monitoring: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q474: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q474: 5-stage trace + repo map complete"
```

### Q475. How do you handle CloudWatch, Databricks alerts, delivery monitoring in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on CloudWatch, Databricks alerts, delivery monitoring: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q475: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q475: 5-stage trace + repo map complete"
```

### Q476. How do you handle CloudWatch, Databricks alerts, delivery monitoring in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on CloudWatch, Databricks alerts, delivery monitoring: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q476: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q476: 5-stage trace + repo map complete"
```

### Q477. How do you handle CloudWatch, Databricks alerts, delivery monitoring in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on CloudWatch, Databricks alerts, delivery monitoring: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q477: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q477: 5-stage trace + repo map complete"
```

### Q478. How do you handle CloudWatch, Databricks alerts, delivery monitoring in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on CloudWatch, Databricks alerts, delivery monitoring: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q478: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q478: 5-stage trace + repo map complete"
```

### Q479. How do you handle CloudWatch, Databricks alerts, delivery monitoring in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on CloudWatch, Databricks alerts, delivery monitoring: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q479: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q479: 5-stage trace + repo map complete"
```

### Q480. How do you handle CloudWatch, Databricks alerts, delivery monitoring in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on CloudWatch, Databricks alerts, delivery monitoring: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q480: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q480: 5-stage trace + repo map complete"
```

### Q481. How do you handle CloudWatch, Databricks alerts, delivery monitoring in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on CloudWatch, Databricks alerts, delivery monitoring: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q481: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q481: 5-stage trace + repo map complete"
```

### Q482. How do you handle CloudWatch, Databricks alerts, delivery monitoring in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on CloudWatch, Databricks alerts, delivery monitoring: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q482: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q482: 5-stage trace + repo map complete"
```

### Q483. How do you handle CloudWatch, Databricks alerts, delivery monitoring in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on CloudWatch, Databricks alerts, delivery monitoring: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q483: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q483: 5-stage trace + repo map complete"
```

### Q484. How do you handle CloudWatch, Databricks alerts, delivery monitoring in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on CloudWatch, Databricks alerts, delivery monitoring: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q484: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q484: 5-stage trace + repo map complete"
```

### Q485. How do you handle CloudWatch, Databricks alerts, delivery monitoring in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on CloudWatch, Databricks alerts, delivery monitoring: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Forward Deployed Engineer | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q485: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q485: 5-stage trace + repo map complete"
```


## Section Z: DevOps & CI/CD

### Q486. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q486: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q486: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q487. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q487: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q487: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q488. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q488: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q488: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q489. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q489: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q489: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q490. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q490: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q490: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q491. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q491: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q491: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q492. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q492: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q492: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q493. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q493: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q493: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q494. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q494: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q494: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q495. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q495: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q495: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q496. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q496: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q496: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q497. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q497: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q497: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q498. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q498: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q498: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q499. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q499: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q499: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q500. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q500: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q500: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q501. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q501: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q501: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q502. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q502: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q502: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q503. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q503: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q503: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q504. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q504: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q504: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q505. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q505: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q505: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q506. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q506: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q506: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q507. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q507: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q507: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q508. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q508: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q508: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q509. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q509: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q509: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q510. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q510: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q510: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q511. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q511: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q511: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q512. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q512: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q512: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q513. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q513: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q513: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q514. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q514: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q514: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```

### Q515. How do you handle GitLab CI, facets-infrastructure Terraform in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on GitLab CI, facets-infrastructure Terraform: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: DevOps Engineer | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q515: Facets DevOps gate
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/ci/run_ci_local.sh
echo "Q515: local CI green before facets-infrastructure or ng-pipelines-cambia MR
```


## Section AA: Governance & Compliance

### Q516. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q516: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q516: 5-stage trace + repo map complete"
```

### Q517. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q517: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q517: 5-stage trace + repo map complete"
```

### Q518. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q518: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q518: 5-stage trace + repo map complete"
```

### Q519. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q519: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q519: 5-stage trace + repo map complete"
```

### Q520. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q520: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q520: 5-stage trace + repo map complete"
```

### Q521. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q521: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q521: 5-stage trace + repo map complete"
```

### Q522. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q522: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q522: 5-stage trace + repo map complete"
```

### Q523. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q523: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q523: 5-stage trace + repo map complete"
```

### Q524. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q524: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q524: 5-stage trace + repo map complete"
```

### Q525. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q525: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q525: 5-stage trace + repo map complete"
```

### Q526. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q526: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q526: 5-stage trace + repo map complete"
```

### Q527. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q527: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q527: 5-stage trace + repo map complete"
```

### Q528. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q528: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q528: 5-stage trace + repo map complete"
```

### Q529. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q529: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q529: 5-stage trace + repo map complete"
```

### Q530. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q530: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q530: 5-stage trace + repo map complete"
```

### Q531. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q531: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q531: 5-stage trace + repo map complete"
```

### Q532. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q532: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q532: 5-stage trace + repo map complete"
```

### Q533. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q533: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q533: 5-stage trace + repo map complete"
```

### Q534. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q534: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q534: 5-stage trace + repo map complete"
```

### Q535. How do you handle governance, audit, and compliance for PHI in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on governance, audit, and compliance for PHI: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Forward Deployed Engineer)*

```bash
#!/usr/bin/env bash
# Q535: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q535: 5-stage trace + repo map complete"
```


## Section AB: Cambia-Specific Integrations & Cutover

### Q536. What is the cambia02 tenant and cutover state?

**Answer:** NextGen tenant label cambia02. Pipeline spans facets-core (bespoke, outside HITRUST) through ng-pipelines-cambia medallion. Confirm live schedule and 1.0 vs NextGen cutover with #xform-xport for your env.

**Example:** Historical volume: ~99M claims, ~250M lines from 1/1/2017. Nightly: 70k–120k claims; incremental: 500–1000 tx per 15-min window.

**How to Check:**
- Snowflake egress: bronze → silver → gold chunked history (XFORM-3515)

**How to Fix:**
- Document environment-specific workflow IDs before prod changes.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q536: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q536: 5-stage trace + repo map complete"
```

### Q537. How do you handle Cambia cutover, env-specific configs, xform coordination in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Cambia cutover, env-specific configs, xform coordination: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q537: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q537: 5-stage trace + repo map complete"
```

### Q538. How do you handle Cambia cutover, env-specific configs, xform coordination in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Cambia cutover, env-specific configs, xform coordination: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q538: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q538: 5-stage trace + repo map complete"
```

### Q539. How do you handle Cambia cutover, env-specific configs, xform coordination in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Cambia cutover, env-specific configs, xform coordination: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q539: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q539: 5-stage trace + repo map complete"
```

### Q540. How do you handle Cambia cutover, env-specific configs, xform coordination in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Cambia cutover, env-specific configs, xform coordination: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q540: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q540: 5-stage trace + repo map complete"
```

### Q541. How do you handle Cambia cutover, env-specific configs, xform coordination in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Cambia cutover, env-specific configs, xform coordination: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q541: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q541: 5-stage trace + repo map complete"
```

### Q542. How do you handle Cambia cutover, env-specific configs, xform coordination in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Cambia cutover, env-specific configs, xform coordination: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q542: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q542: 5-stage trace + repo map complete"
```

### Q543. How do you handle Cambia cutover, env-specific configs, xform coordination in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Cambia cutover, env-specific configs, xform coordination: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q543: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q543: 5-stage trace + repo map complete"
```

### Q544. How do you handle Cambia cutover, env-specific configs, xform coordination in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Cambia cutover, env-specific configs, xform coordination: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q544: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q544: 5-stage trace + repo map complete"
```

### Q545. How do you handle Cambia cutover, env-specific configs, xform coordination in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Cambia cutover, env-specific configs, xform coordination: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q545: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q545: 5-stage trace + repo map complete"
```

### Q546. How do you handle Cambia cutover, env-specific configs, xform coordination in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Cambia cutover, env-specific configs, xform coordination: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q546: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q546: 5-stage trace + repo map complete"
```

### Q547. How do you handle Cambia cutover, env-specific configs, xform coordination in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Cambia cutover, env-specific configs, xform coordination: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q547: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q547: 5-stage trace + repo map complete"
```

### Q548. How do you handle Cambia cutover, env-specific configs, xform coordination in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Cambia cutover, env-specific configs, xform coordination: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q548: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q548: 5-stage trace + repo map complete"
```

### Q549. How do you handle Cambia cutover, env-specific configs, xform coordination in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Cambia cutover, env-specific configs, xform coordination: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q549: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q549: 5-stage trace + repo map complete"
```

### Q550. How do you handle Cambia cutover, env-specific configs, xform coordination in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Cambia cutover, env-specific configs, xform coordination: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q550: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q550: 5-stage trace + repo map complete"
```

### Q551. How do you handle Cambia cutover, env-specific configs, xform coordination in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Cambia cutover, env-specific configs, xform coordination: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q551: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q551: 5-stage trace + repo map complete"
```

### Q552. How do you handle Cambia cutover, env-specific configs, xform coordination in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Cambia cutover, env-specific configs, xform coordination: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q552: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q552: 5-stage trace + repo map complete"
```

### Q553. How do you handle Cambia cutover, env-specific configs, xform coordination in the Cambia Facets Claims pipeline?

**Answer:** I apply first-principles ownership on Cambia cutover, env-specific configs, xform coordination: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.

**Example:** cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).

**How to Check:**
- Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.

**How to Fix:**
- Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.

**Script:** *(builds proficiency: Associate Solution Architect | Data Engineer)*

```bash
#!/usr/bin/env bash
# Q553: Facets Claims architecture drill
set -euo pipefail
cd /Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q553: 5-stage trace + repo map complete"
```


## Glossary

> Key terms for Cambia Facets Claims — organized with description and example.

| Term | Category | Description | Example |
|------|----------|-------------|---------|
| **cambia02** | Platform | NextGen tenant label for Cambia Facets data lake | All bronze/silver/gold tables scoped to cambia02 catalog |
| **Facets** | Source | TriZetto Facets claims admin on-prem SQL Server 2016 | CMC_CLCL_CLAIM header table in CDC replica |
| **facets-core** | CDC | Bespoke CDC extraction repo (GitLab abacusinsights/facets-integration) | Step Functions + Batch SQL → JSON partitions |
| **facets-infrastructure** | CDC | Terraform/IaC for Facets CDC AWS resources | Intermediate S3, DynamoDB CdcGlobals, VPN endpoints |
| **CdcGlobals** | CDC | DynamoDB lock table — one CDC job per domain | Overlapping incremental runs dropped when lock held |
| **Claims Incremental** | CDC | Micro-batch CDC ~every 4 hours daytime | 500–1000 tx per 15-min window; spikes during nightly batch |
| **Claims Historical** | CDC | Backfill CDC from 1/1/2017 | ~99M claims, ~250M lines historical volume |
| **PPL** | CDC | Provider Performance List appended separately | PPL Incremental/Historical process types |
| **manifest.json** | Landing | Batch metadata listing encrypted JSON files + checksums | Path: cambia/facets/cambia/claims/extension/incremental/*/*manifest.json |
| **AIR library** | Runtime | ng-abacus-insights-runtime — encryption, manifest, SCD2 sinks | Shared generic logic; pipelines import, never duplicate |
| **ng-orchestration-service** | Orchestration | Manifest-triggered bronze/silver/gold workflow orchestration | Monitors Facets CDC delivery; catalog orchestration.yaml |
| **ng-pipelines-cambia** | Pipelines | Bronze/silver/gold notebooks + pipespecs for Cambia | silver.unified_timeline_claim, gold.fm_claim* tables |
| **ng-abacus-inbound-infra** | Landing | SFTP/connector landing zone infrastructure | Catalog: transporters/sftp.yaml |
| **CMC_CLCL_CLAIM** | Bronze | Facets claim header bronze SCD2 table | Primary claim grain for unified timeline |
| **CMC_CDML_CL_LINE** | Bronze | Medical claim line bronze table | M/H claim types |
| **CMC_CDDL_CL_LINE** | Bronze | Dental claim line bronze table | D claim type; filtered from Interop gold |
| **SCD Type 2** | Bronze | Slowly changing dimension history in bronze | AIR library sink pattern; _is_current flag |
| **silver.unified_timeline_claim** | Silver | SCD2 unified incremental claims timeline | Tracks claim versions across batches |
| **silver.claim_facets** | Silver | Interop/SAM domain table — group + date filtered | Feeds gold.fm_claim Interop path |
| **silver.claim_facets_cambia** | Silver | CDP domain table — no filtering | Feeds gold.fm_claim_cambia |
| **gold.fm_claim** | Gold | Interop FM — CMS-9115 SAM/FHIR (75 groups, Medicare) | Dental excluded before SAM load |
| **gold.fm_claim_cambia** | Gold | CDP FM — full 1:1 silver + data signature bitmap | All claim types retained |
| **ng-pipelines-onyx** | Downstream | DM 2.0 → FHIR workflows for SAM load | Claim, ClaimCoverage, ClaimDiagnosis resources |
| **cambia02-claims-dataingestion-workflow** | Downstream | Onyx FHIR ingestion workflow name | CMS-9115 SAM → FHIR → Firely path |
| **Snowflake egress** | Downstream | bronze → silver → gold → Snowflake chunked loads | XFORM-3515 history migration pattern |
| **Reltio** | MDM | Silver Facets feeds Reltio tenant | Migration from 1.0 connector in progress |
| **cambia-facets-networking** | Network | Dedicated AWS account 697410135799 for VPN | Palo Alto site-to-site to on-prem Facets |
| **Facets_BatchJobComplete** | Trigger | Nightly trigger file after Cambia batch | Facets_BatchJobComplete_<OrderNumber>_<timestamp>.txt on SFTP |
| **HITRUST boundary** | Security | facets-core CDC runs outside HITRUST boundary | Encryption before landing in NextGen zone |
| **Claim status 02** | Domain | Facets CLCL status final | 11=pended, 15=error, 01=pre-final, 91=adjusted |
| **DevOps Engineer** | Role | CI/CD, facets-infrastructure, deployment gates | run_ci_local.sh before MR |
| **Data Engineer** | Role | Medallion pipelines, SCD2, unified timeline | ng-pipelines-cambia owner |

### Glossary Category Index

| Category | Terms Count | Key Terms |
|----------|-------------|-----------|
| CDC & Source | 8 | facets-core, CdcGlobals, Claims Incremental, PPL |
| Landing & Orchestration | 5 | manifest.json, AIR, ng-orchestration-service, SFTP |
| Medallion | 10 | bronze CMC_*, silver unified timeline, dual gold FM |
| Downstream | 5 | Onyx FHIR, Snowflake, Reltio |
| Network & Security | 3 | cambia-facets-networking, HITRUST, encryption |
| Domain | 4 | claim statuses, medical/dental, volumes |

---
