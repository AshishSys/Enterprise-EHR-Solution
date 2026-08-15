# Step 2 Day 2 — Profiles (completed from terminal inspection)

## Resources inspected

| Resource | meta.profile | Key Must Support / required field |
|----------|--------------|-----------------------------------|
| **Patient** | `us-core-patient` | `name.family` = Berge125 ✅ |
| **Condition** | `us-core-condition-encounter-diagnosis` | clinicalStatus, code, subject ✅ |
| **Observation** | `us-core-observation-lab` | code, status, subject (US Core lab profile) ✅ |
| **EOB** | `C4BB-ExplanationOfBenefit-Inpatient-Institutional` | billablePeriod ✅, patient ⚠️ `Patient/unknown` |

## US Core vs CARIN BB (summary)

- **US Core** — baseline US clinical profiles (Patient, Condition, Observation, Encounter, etc.) for Patient Access clinical data.
- **CARIN Blue Button (C4BB)** — consumer-directed **claims/EOB** profiles; Patient Access EOB must use CARIN BB, not generic FHIR EOB.

## Why profile variants matter

- One FHIR resourceType can have **multiple valid profiles** (e.g. Condition vs encounter-diagnosis; EOB inpatient vs professional).
- Validators must accept the **variant the pipeline emits**, not only the generic profile URL.
- Wrong profile → IG validation failure → Firely quarantine → CMS API non-compliance.

## Data quality note (fix in Step 4)

EOB shows `patient: Patient/unknown` — profile and billablePeriod pass, but **reference join** from Claims CSV `PATIENT` column needs mapping fix in `interop_pipeline.py` (`PATIENT` vs `PATIENTID` column name). Good example of "validation passed ≠ production ready."

## Interview one-liner

> `meta.profile` declares which StructureDefinition applies; Must Support means if data exists the element must be present — we validate profiles and required fields locally before FSI/Firely load, and IG validation catches deeper Must Support gaps in prod.
