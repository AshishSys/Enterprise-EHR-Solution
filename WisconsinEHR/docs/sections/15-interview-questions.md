[← 14](14-go-live.md) · [Index](../WISCONSIN_EHR_SOLUTION_BLUEPRINT.md) · [Next →](16-lessons-learned.md)

---

## 15. Interview Questions Guide

### Solution Architect

- Design FHIR-based MPI across three MRN systems
- Cerner coexistence without dual documentation
- VPC-SC and CMEK for HIPAA on GCP
- FHIR profile versioning without breaking consumers

### Data Engineer

- CCLF1–CCLF9 joins to encounter fact table
- Idempotent MERGE for late-arriving claims in Snowflake
- Prevent PHI in Fabric/Spark driver logs
- Medallion vs data vault tradeoffs

### Product Engineer

- SMART on FHIR authorization flow
- Offline-first for rural clinics
- Break-glass access with full audit
- FHIR `$everything` vs granular reads

### Delivery Manager

- Phased statewide rollout with competing MCO priorities
- Change management for resistant clinicians
- Go-live success metrics beyond uptime

### AI Engineer

- Governed gap-propensity model — features, labels, bias checks
- When not to deploy ML in clinical workflow
- Vertex AI Feature Store vs batch features from Snowflake
- Model rollback after drift detection

### Red Flags

- PHI in logs for debugging
- No consent or minimum necessary access
- Cerner migration as one-time ETL vs modular export
- Training on CCLF without label leakage awareness

---
