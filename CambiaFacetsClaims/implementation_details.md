# Cambia Facets Claims — Implementation Details

> Scope: Cambia on-prem TriZetto Facets → Abacus NextGen (tenant **cambia02**).  
> **Aligned to 4 pillars:** P1 E2E Implementation · P2 Facets/TriZetto SME · P3 On-Prem→Cloud Migration · P4 Postman API Role

---

## Pillar Map

| Pillar | This document sections | Exit proof |
|--------|------------------------|------------|
| **P1 E2E** | Stages 2–5, dual gold, downstream | Databricks chain + run_ci_local.sh |
| **P2 SME** | Claim domain reference, CMC tables | CLCL lifecycle + table joins |
| **P3 Migration** | Stage 1, HITRUST, VPN, SFTP handoff | migration_cutover_checklist.sh |
| **P4 Postman** | Downstream API validation | newman smoke on orchestration + FHIR |

---

## System Overview

Facets Claims spans five stages from on-prem SQL Server through dual gold FM outputs. Unlike catalog transporter services, it combines bespoke CDC (facets-core), VPN networking, SFTP trigger files, orchestration, and XFORM medallion pipelines.

```
On-Prem Facets CDC Replica
        │
        ▼ (Site-to-Site VPN — Palo Alto)
cambia-facets-networking AWS Account
        │
        ▼ (Step Functions + Lambda + Batch)
Encrypted JSON + manifest.json → Intermediate S3
        │
        ▼ (SFTP / Connector Landing)
NextGen Raw S3 (cambia02)
        │
        ▼ (Databricks + AIR SCD2)
Bronze (44+ tables) → Silver (unified timeline) → Gold (Interop ║ CDP)
        │
        ├──► Onyx SAM/FHIR (CMS-9115)
        ├──► Snowflake egress
        └──► Reltio MDM
```

---

## Stage 1 — Source & Network

| Item | Detail |
|------|--------|
| Source | Cambia on-prem Facets SQL Server 2016, CDC-enabled read replica |
| Network | Site-to-site VPN via Palo Alto in AWS account `cambia-facets-networking` (697410135799) |
| Scope | Core Facets claims (all statuses); PPL appended separately |
| Repos | `facets-core`, `facets-infrastructure` (GitLab: abacusinsights/facets-integration) |

**Failure modes:** VPN flap → CDC stall; replica lag → stale incremental; primary query → performance incident on source.

---

## Stage 2 — CDC Extraction

| Item | Detail |
|------|--------|
| Orchestration | AWS Step Functions + Lambda (light) + AWS Batch (heavy SQL/file) |
| Process types | Claims Incremental (~4 hr), Claims Historical, Claims PPL Incremental/Historical |
| Logic | SQL Server CDC → unique change IDs → partitioned JSON → encryption → manifest.json |
| Intermediate S3 | `abacus-facets-intermediate-<env>/claims-incremental/`, `claims-historical/` |
| Manifest pattern | `cambia/facets/cambia/claims/extension/incremental/*/*manifest.json` |
| Concurrency | One CDC job per domain — lock in DynamoDB `CdcGlobals`; overlaps dropped |
| Output | ~25 JSON files/batch (header, medical/dental lines, diagnosis, PPL, deletes) + manifest |

**Triggers:**
- CloudWatch schedule (~every 4 hours)
- Nightly: `Facets_BatchJobComplete_<OrderNumber>_<timestamp>.txt` on SFTP/S3 after Cambia batch

**HITRUST note:** facets-core runs **outside** HITRUST boundary; encryption before NextGen landing.

---

## Stage 3 — Landing & Bronze

| Item | Detail |
|------|--------|
| Transfer | Encrypted files + manifest → Abacus SFTP / connector landing → NextGen raw S3 |
| Bronze load | Databricks workflows (manifest / ng-orchestration-service) → 44+ bronze SCD2 tables |
| Runtime | AIR library from ng-abacus-insights-runtime |
| Key tables | `CMC_CLCL_CLAIM`, `CMC_CDML_CL_LINE`, `CMC_CDDL_CL_LINE`, `CMC_CLST_STATUS`, `CMC_MEME_MEMBER`, `CMC_SBSB_SUBSC` + ~35 reference tables |

All 420 Facets bronze tables released in prod (TechOps, Jun 2024).

---

## Stage 4 — Silver & Gold

### Silver

| Table | Purpose |
|-------|---------|
| `silver.unified_timeline_claim` | SCD2 unified incremental claims timeline |
| `silver.unified_claims` | Consolidated claim grain |
| `silver.claim_facets` | Interop/SAM — group + date filtered |
| `silver.claim_facets_cambia` | CDP — no filtering |
| `silver.claim_item_medical_facets` | Medical line items |
| `silver.claim_item_dental_facets` | Dental line items |
| `silver.claim_item_facets` | Combined line grain |

### Gold (dual FM)

| Path | Tables | Filtering |
|------|--------|-----------|
| Interop | `gold.fm_claim`, `gold.fm_claim_item` | 75 groups, Medicare patients; dental excluded |
| CDP | `gold.fm_claim_cambia`, `gold.fm_claim_item_cambia` | Full 1:1 silver + data signature bitmap |

**Dental note:** Dental exists in bronze/silver (`CMC_CDDL_CL_LINE`) but filtered from Interop `fm_claim` before SAM; CDP retains all.

---

## Stage 5 — Downstream

| Consumer | Path |
|----------|------|
| SAM → FHIR (CMS-9115) | ng-pipelines-onyx: Claim, ClaimCoverage, ClaimDiagnosis, ClaimOrganization, ClaimPractitioner, Patient |
| FHIR workflow | `cambia02-claims-dataingestion-workflow` |
| Snowflake | bronze → silver → gold → Snowflake (chunked history, XFORM-3515) |
| MDM | Silver Facets → Reltio tenant (1.0 connector migration in progress) |

---

## Claim Domain Reference

| Code | Meaning |
|------|---------|
| M / H | Medical claim type |
| D | Dental claim type |
| 11 | Pended |
| 15 | Error |
| 01 | Pre-final |
| 02 | Final |
| 91 | Adjusted |

---

## Service Catalog

| Service | Catalog / Repo |
|---------|----------------|
| SFTP/Inbound | ng-abacus-inbound-infra — `config/repo-rules/transporters/sftp.yaml` |
| Orchestration | ng-orchestration-service — `config/repo-rules/transporters/orchestration.yaml` |
| Pipelines | ng-pipelines-cambia — `config/repo-rules/xform/pipelines.yaml` |
| Runtime | ng-abacus-insights-runtime (AIR library) |
| Onyx/FHIR | ng-pipelines-onyx, onyx-infrastructure |

---

## Confluence / Source References

- Facets-Claims-Implementation-Bronze-Silver-Gold
- Cambia CDC Phase I & II Architecture
- Facets Medical & Dental Claims
- Facets Cambia Networking
- Claims CDC SFTP Trigger
- Reltio NextGen Migration
- Lucid: Facets Claims Overall Flow Chart

**Confidence:** High for architecture and layer/table names. Medium on live schedules and 1.0 vs NextGen cutover — confirm with #xform-xport for cambia02 dev/stg/prd.
