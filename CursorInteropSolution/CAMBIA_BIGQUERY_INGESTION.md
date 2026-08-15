# Cambia BigQuery Cross-Cloud Ingestion (Rail D)

> Source: *Cambia BigQuery Ingestion Design* (XPORT-2596, DRAFT).  
> **Pattern:** GCP BigQuery → EKS CronJob (WIF) → S3 NDJSON → Databricks Bronze (separate repo).

This is **Rail D — hybrid cloud ingest**: partner data stays in GCP BigQuery; Abacus pulls into AWS S3 without stored GCP keys.

---

## Boundary

| In scope (this service) | Out of scope |
|-------------------------|--------------|
| Query BigQuery, land NDJSON on S3 | Databricks Bronze load |
| Checkpoints, manifests (non-PHI) | Merge/dedup/delete in Delta |
| WIF auth, incremental windows | `ng-pipelines-cambia` pipespec |

**Handoff:** S3 prefix + manifest = contract for `ng-pipelines-cambia` Databricks workflow.

---

## Architecture

```
EKS CronJob (cambia02, PHI VPC)
    → IRSA (pod ServiceAccount → IAM role, no static keys)
    → Google STS (Workload Identity Federation)
    → iamcredentials (impersonate Cambia service account)
    → BigQuery query (bounded window)
    → S3 data-lake bucket (PHI, SSE-KMS) NDJSON parts
    → S3 metadata bucket (checkpoint + manifest, non-PHI only)
         ↓
Databricks Bronze (ng-pipelines-cambia) — separate ticket
```

**No inbound traffic.** No ALB/NLB. Egress allowlist: `bigquery`, `bigquerystorage`, `sts`, `oauth2`, `iamcredentials` `.googleapis.com` only.

---

## Auth (no stored credentials)

1. EKS OIDC → projected token  
2. AWS STS `AssumeRoleWithWebIdentity` (IRSA)  
3. Google STS — exchange AWS identity (external_account)  
4. `iamcredentials` — impersonate `svc-wif-cambia-aws-sso-poc@...`  
5. BigQuery access token — **1 hour TTL, memory only**

**Critical implementation notes (POC-learned):**

- Export IRSA creds to `AWS_*` env **before** Google auth lib init (else IMDS node role → Cambia trust fails)
- Pass GCP `project` explicitly (avoid `cloudresourcemanager.googleapis.com` — not on egress allowlist)

---

## Load modes

| Mode | CronJob | Purpose |
|------|---------|---------|
| **incremental** | scheduled daily | `watermark > window_start AND <= window_end` |
| **full** | suspended — manual trigger | Initial load; sets first checkpoint |
| **refresh** | monthly manual | Periodic full reload — **correctness requirement** |
| **replay** | operator window | Backfill to `replay/` prefix; does not advance checkpoint |

**Fail closed:** Missing checkpoint on incremental → **FAIL + alert**, never auto-switch to full load.

---

## S3 layout

```
s3://<data-lake>/raw/bigquery-claims/
  _staging/run_id=<id>/part-N.ndjson     ← in-flight, never read downstream
  full/run_id=<id>/part-N.ndjson
  incremental/date=<yyyy-mm-dd>/run_id=<id>/part-N.ndjson
  refresh/date=<yyyy-mm-dd>/run_id=<id>/part-N.ndjson
  replay/run_id=<id>/part-N.ndjson

s3://<metadata>/metadata/bigquery-claims/checkpoint/bigquery-claims-<ws>.json
```

**Atomic publish:** staging → server-side copy to final prefix only after full run succeeds.

---

## Why periodic full refresh is required

BigQuery **change history** and **time travel** are **not available** to Abacus on Cambia tables. Watermark-only incremental cannot detect restated rows whose watermark did not move. Monthly **refresh** is the recovery mechanism — not optional optimization.

---

## PHI / security

- Claims payload → PHI data-lake bucket (CMK, audit)
- Checkpoint/manifest → metadata bucket (**non-PHI only** — no claim IDs, member IDs, query predicates)
- Logs: run_id, counts, job id — **never** row values or tokens

---

## Reference values (cambia02 dev POC)

| Item | Value |
|------|-------|
| AWS account / region | 623353383501 / us-west-2 |
| EKS cluster | cambia02 |
| GCP project | dev-edap-cambia-poc |
| POC table | `CAMBIA_POC_CR.test_datashare_claims` |
| Default watermark | `received_at` (assumption A1 — open with Cambia) |

---

## Solution mapping

| Concept | Interop equivalent |
|---------|-------------------|
| Rail D hybrid ingest | New rail alongside A/B/C |
| S3 landing | Bronze Autoloader input (same as Rail B/C) |
| Checkpoint | `onyx_job_state` / DynamoDB watermark pattern |
| Connector split | Ingest service ≠ Databricks workflow (same as ng-nasco-event-api) |
| WIF cross-cloud | Extends hybrid cloud story (Section T BigQuery Qs) |

## Cheat Sheet

Section AB Q546–Q553; update Section T for production PHI cross-cloud ingest vs analytics-only BQ.
