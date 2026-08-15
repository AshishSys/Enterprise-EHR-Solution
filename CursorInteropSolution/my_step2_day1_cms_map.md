# CMS API → Component Map

## Phase 1 — CMS-9115

| API | FHIR resources | Abacus (data) | Onyx (runtime) |
|-----|----------------|---------------|----------------|
| **Patient Access** | Patient, EOB, Observation, Condition, Encounter, MedicationRequest, Procedure, AllergyIntolerance | Claims + Clinical workflow families → SAM → Extract → NDJSON/bundles | SLAP (auth) → FITE (gateway) → Firely |
| **Provider Directory** | Practitioner, Organization, PractitionerRole, Location (Plan-Net) | PVD workflow → `pvd_sam` → Extract | FITE public endpoints (no member auth) |
| **Formulary** | MedicationKnowledge, InsurancePlan (Da Vinci Formulary) | Formulary workflow → `formulary_sam` → Extract | FITE public endpoints |

**Deadlines:** Patient Access operational; CMS metrics reporting Jan 2026.

## Phase 2 — CMS-0057 (Jan 2027)

| API | Pattern | Component |
|-----|---------|-----------|
| **Provider Access** | Backend Services auth + `$export` (bulk NDJSON) | SLAP + FITE + attribution SAM (Group resources) |
| **P2P** | `$bulk-member-match` + consent + NDJSON export | `p2p_member_match.py` :9004 |
| **ePA** | CRD → DTR → PAS (`$submit`) | `epa_burden_reduction_service.py` :9005 |

## IG registry (from MDP `ig_registry.json`)

| IG | Version | APIs |
|----|---------|------|
| US Core | 6.1.0 | patient_access, provider_access, payer_to_payer |
| CARIN BB | 2.0.0 | patient_access, provider_access, payer_to_payer |
| Da Vinci Plan-Net | 1.2.0 | provider_directory |
| Da Vinci Formulary | 2.0.1 | formulary |
| Da Vinci PDex | (continues in file) | payer_to_payer, provider_access |

## One-sentence summary

**CMS-9115** = member-facing SMART APIs (clinical + EOB + public directory/formulary); **CMS-0057** = attributed provider bulk access, payer-to-payer exchange, and ePA by **Jan 2027**.

## Interview checkpoint

- Apps never call Firely directly → always **FITE** after **SLAP** token
- EOB for Patient Access comes from **Claims SAM** (CARIN BB profile)
- PVD must complete before Claims (practitioner/org refs on EOB)
