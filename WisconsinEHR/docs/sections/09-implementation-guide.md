[← 08](08-source-files-cclf.md) · [Index](../WISCONSIN_EHR_SOLUTION_BLUEPRINT.md) · [Next →](10-devops.md)

---

## 9. Implementation Guide

### Phase 0 — Foundation (Months 1–4)

1. GCP org setup — Assured Workloads, VPC, IAM
2. Terraform modules — GKE, Healthcare API, Pub/Sub, KMS
3. Fabric workspace — OneLake, CCLF ingest
4. Snowflake account — roles, masking policies
5. Canonical model v1 — Patient, Encounter, Condition, Medication
6. FHIR store — US Core + Wisconsin extensions
7. CCLF sandbox — pipeline to Power BI demo

### Phase 1 — Core Clinical (Months 5–10)

1. Clinician GUI: chart, problems, meds, allergies, results
2. MPI + identity matching
3. First PMS integration (pilot)
4. Care gap engine v1 (HEDIS-aligned)
5. Patient portal: results, messaging, consent
6. Audit logging and break-glass

### Phase 2 — Scale & AI (Months 11–18)

1. Additional PMS connectors
2. Care management module
3. Vertex AI: gap propensity, readmission risk
4. Statewide Power BI with RLS
5. HL7 v2 lab/imaging feeds

### Phase 3 — Cerner Readiness (Months 16–24)

1. FHIR Bundle export service
2. Cerner test environment import/export cycles
3. Cutover runbooks per facility
4. Decommission or read-only coexistence

### Definition of Done (per module)

- Unit + integration tests on critical paths
- Security scan clean (SAST/DAST)
- FHIR validation (Inferno / Touchstone)
- Runbook + on-call playbook
- Clinical sign-off

---
