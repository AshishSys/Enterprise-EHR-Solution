[← 11](11-brd.md) · [Index](../WISCONSIN_EHR_SOLUTION_BLUEPRINT.md) · [Next →](13-uat-planning.md)

---

## 12. Data Models

### Canonical Entities

- Patient, Practitioner, Organization
- Encounter (ambulatory, ED, inpatient, telehealth)
- Condition, MedicationStatement, MedicationRequest
- AllergyIntolerance, Observation, DiagnosticReport
- CarePlan, Goal, CareGap, DocumentReference

### MPI

```sql
MasterPatient (
  master_id UUID PK,
  match_score DECIMAL,
  match_status ENUM(verified, provisional, merged)
)

PatientIdentifier (
  master_id FK,
  system URI,  -- wisconsin-ehr, cerner, pms-athena
  value,
  verified BOOLEAN
)
```

### Snowflake Gold Views

| View | Grain | Consumers |
|------|-------|-----------|
| vw_patient_demographics | patient | Population health |
| vw_encounter_utilization | encounter | Utilization |
| vw_care_gaps_current | patient × measure | Care managers, Power BI |
| vw_med_adherence | patient × med | Pharmacy quality |
| vw_provider_panel | provider × patient | Panel management |

### FHIR Profiling

- US Core STU6 baseline
- Wisconsin extensions: program enrollment, consent directive
- Cerner alignment for migration bundles

---
