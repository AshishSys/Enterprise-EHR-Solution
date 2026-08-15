[← 05](05-resource-planning.md) · [Index](../WISCONSIN_EHR_SOLUTION_BLUEPRINT.md) · [Next →](07-cost-planning.md)

---

## 6. Cloud-Native Services

### Google Cloud Platform

| Service | Use |
|---------|-----|
| GKE Autopilot | Microservices, HL7 adapters, bundle exporters |
| Cloud Healthcare API | FHIR R4 store |
| Apigee X | External API management, OAuth |
| Cloud Identity / IAP | SSO, zero-trust access |
| AlloyDB / Cloud SQL | Transactional index, MPI |
| Cloud Storage | Landing zones, bundle archives (CMEK) |
| Pub/Sub | Event streaming |
| Cloud Run / Functions | Webhooks, lightweight transforms |
| BigQuery | Operational analytics |
| Vertex AI | Training, prediction, Model Registry |
| Secret Manager + Cloud KMS | Credentials, CMEK |
| Cloud Logging / Monitoring | Observability (no PHI in logs) |
| Cloud Armor + CDN | WAF, portal edge |
| Assured Workloads | HIPAA-aligned controls |

### Microsoft Fabric

| Component | Use |
|-----------|-----|
| OneLake / Lakehouse | Bronze (raw CCLF, HL7, FHIR JSON) |
| Data Factory pipelines | Orchestration, PMS batch loads |
| Spark notebooks | CCLF normalization, SCD2 |
| Dataflows Gen2 | Lightweight transforms |

### Snowflake

| Object | Use |
|--------|-----|
| Bronze/Silver/Gold | Medallion architecture |
| Dynamic tables / streams | Incremental reporting views |
| Secure views | Row/column masking |
| Snowpipe | Continuous load from OneLake/GCS |

### Power BI

| Component | Use |
|-----------|-----|
| Datasets | Snowflake semantic layer |
| Dashboards | Gap closure, utilization, outcomes |
| Row-level security | Region/program scoping |
| Embedded analytics | Clinician GUI widgets (aggregates only) |

---
