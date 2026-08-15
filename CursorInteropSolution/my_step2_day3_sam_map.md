# SAM → FHIR resource map (Step 2 Day 3)

| Workflow | SAM table | FHIR resources | IG profiles | CMS API |
|----------|-----------|----------------|-------------|---------|
| **Claims** | `claims_sam.eob_records` | ExplanationOfBenefit, Coverage | CARIN BB C4BB-EOB, C4BB-Coverage | Patient Access |
| **PVD** | `pvd_sam.provider_directory` | Practitioner, PractitionerRole, Organization, Location | Da Vinci **Plan-Net** | Provider Directory (public) |
| **Formulary** | `formulary_sam.formulary_items` | MedicationKnowledge, InsurancePlan | Da Vinci **Formulary** (usdf-*) | Formulary API (public) |
| **Clinical** | `clinical_sam.*` | Patient, Observation, Condition, Encounter, ... | **US Core** | Patient Access |

## Critical dependency (from `claims/extract_config.yaml`)

```yaml
depends_on:
  - pvd
```

**Why PVD before Claims:** EOB and Coverage reference Practitioner/Organization NPIs. Provider Directory must be in Firely first so references resolve.

## Trace — Claims EOB (one row)

| Stage | Name | Example |
|-------|------|---------|
| CSV | Claims.csv | `Id`, `PATIENTID`, `SERVICEDATE` |
| FM | `claims_fm.medical_claims` | typed, deduped claim lines |
| SAM | `claims_sam.eob_records` | `MEMBER_ID`, `SERVICE_DATE`, `PAID_AMOUNT` |
| FHIR | ExplanationOfBenefit | CARIN BB profile + `billablePeriod`, `patient` |
| Load | FSI bulk / Firely REST | NDJSON or transaction bundle |

## Trace — PVD (Plan-Net)

| SAM column | FHIR element |
|------------|--------------|
| `NPI` | Practitioner.identifier |
| `SPECIALTY` | PractitionerRole.specialty |
| `ORG_NAME` | Organization.name |
| `ADDRESS` | Location.address |

**Cadence:** PVD extract `update_cadence_days: 30` (directory refreshes monthly).

## Trace — Formulary

| SAM column | FHIR element |
|------------|--------------|
| `NDC` | MedicationKnowledge.code |
| `TIER` | formulary tier extension |
| `PA_REQUIRED` | prior auth flag |

## Config locations

```
configs/workflows/claims/extract_config.yaml   ← depends_on: pvd
configs/workflows/pvd/extract_config.yaml      ← Plan-Net profiles
configs/workflows/formulary/extract_config.yaml
configs/workflows/clinical/extract_config.yaml
```

## Interview line

> Extract configs are the contract between SAM and FHIR: they declare source tables, target profiles, bundle size, and load method (incremental REST vs historical FSI).
