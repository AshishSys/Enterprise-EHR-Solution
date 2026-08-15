[← 03](03-discovery-session.md) · [Index](../WISCONSIN_EHR_SOLUTION_BLUEPRINT.md) · [Next →](05-resource-planning.md)

---

## 4. Technical Architecture

### Principles

- Modular bounded contexts (Clinical, Patient, Integration, Analytics, AI)
- API-first — FHIR facade over canonical model
- Event-driven — Pub/Sub for clinical events, gap alerts, audit
- Zero-trust — IAP, workload identity, least privilege
- Export-ready — FHIR Bundle generation on demand per domain

### Layer Overview

| Layer | Components | Purpose |
|-------|------------|---------|
| Experience | Clinician SPA, patient portal, Power BI embed | User-facing |
| API & integration | Apigee, Cloud Healthcare API (FHIR R4), HL7 v2 adapters | Interop |
| Application | GKE microservices: Patient, Encounter, Meds, Gaps, Care Plan | Business logic |
| Canonical data | FHIR store + AlloyDB relational index | Source of truth |
| Event bus | Pub/Sub: `clinical.events`, `gap.detected`, `audit.trail` | Async workflows |
| ETL | Fabric → OneLake → Snowflake | Analytics pipeline |
| AI/ML | Vertex AI, Feature Store, Model Registry | Governed ML |
| Security | IAM, VPC-SC, CMEK, Assured Workloads | HIPAA alignment |

### Cerner Migration

**Export (Wisconsin EHR → Cerner)**

1. Canonical record → FHIR R4 Bundle builder
2. Bulk `$export` or scheduled jobs to encrypted Cloud Storage
3. Cerner ingestion via Oracle Health FHIR APIs

**Import (Cerner → Wisconsin EHR)**

1. Cerner FHIR bulk export → OneLake/GCS landing zone
2. Fabric transformation to canonical model
3. Idempotent upsert into FHIR store + relational index

**Coexistence**

- MPI with cross-reference IDs (Wisconsin ID ↔ Cerner ID ↔ PMS ID)
- Source-of-truth flags per domain until cutover

### PMS Integration Patterns

| Pattern | Use Case | Technology |
|---------|----------|------------|
| FHIR subscription | Real-time appointments, demographics | Pub/Sub + webhooks |
| HL7 v2 ADT/SIU | Legacy PMS | MLLP adapter on GKE |
| Batch SFTP | Nightly sync | Cloud Storage + Fabric |
| SMART on FHIR | Embedded apps | OAuth 2.0 / OIDC |

---
