# ePA Option A vs Option B — Deployment Architecture

> Source: Interoperability Pipeline / ePA deployment diagram (Gainwell vs Wellmark patterns).

---

## Shared ingress (both options)

```
Provider EHR (HL7 / FHIR)
    → AWS ALB
    → APISIX Gateway
    → CDS Service (epa-appsvc) + dapr sidecar
```

- **ALB** — TLS termination, health checks
- **APISIX** — API gateway (routing, auth plugins, rate limits)
- **CDS Service** — hosts Da Vinci CRD CDS Hooks (`/cds-services/order-sign`)
- **dapr** — sidecar for service invocation, secrets, pub/sub between ePA microservices

---

## Option A — Gainwell (batch / SFTP path)

```
Routing-DIR → AWS Transfer Family (SFTP)
    → Gainwell/UM Vendor (PAS System)
    → ClaimResponse DG Batch (837 / 275 / CSV)
    → Databricks Workflows (Ingest, Transform, Load)
    → Firely FHIR Server
```

| Characteristic | Detail |
|----------------|--------|
| **Pattern** | Batch file exchange |
| **Transport** | SFTP via AWS Transfer Family |
| **Vendor** | Gainwell UM / external PAS |
| **Output** | ClaimResponse batches → Databricks → Firely |
| **When to use** | Legacy PAS integrations, high-volume batch PA responses |

**Abacus role:** Databricks ingest/transform; Firely load via FSI  
**Onyx role:** Routing-DIR config; APISIX routes to CDS for CRD only

---

## Option B — Wellmark (real-time rules path)

```
Auth Table + 13 Decision Tables (Member/Plan, Benefits, Clinical, Coverage)
    ├─ Jiva APIs (PAS Integration) — no SFTP for PAS
    └─ InterQual / Evicore (DTR) — clinical rules
         → Real-time Event A Notification (Determination, Status, Reason)
         → FHIR Subscription (Event A) → Provider EHR callback
```

| Characteristic | Detail |
|----------------|--------|
| **Pattern** | Real-time CRD + inline rules + PAS API |
| **Rules** | 13 decision tables + external clinical content (InterQual/Evicore) |
| **PAS** | Jiva APIs — synchronous, not batch SFTP |
| **Callback** | FHIR Subscription notifies Provider EHR of determination |
| **When to use** | Point-of-care CRD/DTR with immediate PA decision feedback |

**Abacus role:** Rules table data in SAM; event payloads to Bronze  
**Onyx role:** CDS + PAS endpoints; Subscription management

---

## Deploy order (mandatory sequence)

Each step must complete before the next:

| Step | Job | Owner |
|------|-----|-------|
| 1 | `onyx.provision` | Infrastructure — VPC, EKS, ALB |
| 2 | `onyx.epa` | Platform — APISIX, CDS namespace, dapr |
| 3 | `onyx.deploy` | Application — ePA services, Firely chart |
| 4 | `databricks.provision` | Databricks workspace + UC |
| 5 | `databricks_continuous_deployment` | CI/CD for workflows |
| 6 | `databricks.onyx` | Workflow families (Claims, ePA, etc.) |

**Rule:** Do not deploy Databricks workflows before ePA ingress is live — CRD hooks must resolve.

---

## Local reference

```bash
python3 epa_burden_reduction_service.py --port 9005
curl http://localhost:9005/cds-services
```

## Solution mapping

| Diagram component | Repo artifact |
|-------------------|---------------|
| CDS Service | `epa_burden_reduction_service.py` |
| Databricks | `configs/workflows/epa/extract_config.yaml` |
| APISIX/ALB | `terraform/modules/apigateway`, Helm ingress |
| Option A SFTP | Rail A batch + AWS Transfer (Phase 1) |
| Option B rules | `ai_events` + future rules engine integration |

## Cheat Sheet

Section AB Q541–Q545; Section H (ePA CRD/DTR/PAS).
