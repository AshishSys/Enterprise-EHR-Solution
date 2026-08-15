[← 07](07-cost-planning.md) · [Index](../WISCONSIN_EHR_SOLUTION_BLUEPRINT.md) · [Next →](09-implementation-guide.md)

---

## 8. Source Files Inventory (CMS CCLF)

CMS Claims and Claims Line Feed (CCLF) public use files support sandbox analytics without PHI.

| File | Description | Platform Use |
|------|-------------|----------------|
| CCLF1 | Part A header (institutional) | Inpatient events, DRG |
| CCLF2 | Part A revenue center lines | Procedure timing |
| CCLF3 | Part A procedure codes | Surgical history |
| CCLF4 | Part A diagnosis codes | Condition inference |
| CCLF5 | Part B header | Professional encounters |
| CCLF6 | Part B line items | E&M, labs, imaging |
| CCLF7 | Part D header | Pharmacy events |
| CCLF8 | Part D line items | NDC, adherence |
| CCLF9 | Beneficiary demographics | Synthetic MPI |
| CCLF-A/B/C | SNF, HHA, hospice | Post-acute pathways |
| CCLF0 | Summary / cross-reference | Join keys |

### CCLF → Canonical Mapping

| CCLF Element | Target |
|--------------|--------|
| BENE_MBI_ID (de-id) | Patient.identifier |
| CLM_FROM/THRU_DT | Encounter.period |
| PRNCPL_DGNS_CD | Condition (ICD-10) |
| HCPCS/CDM | Procedure / ServiceRequest |
| NDC | MedicationStatement |
| PRVDR_NPI | PractitionerRole |

### Fabric Landing Structure

```
/onlake/bronze/cms_cclf/{year}/{month}/cclf1/ ... cclf9/
/onlake/silver/clinical_events/
/onlake/gold/care_gaps/, population_health/
```

---
