# FHIR R4 & CMS Interoperability Implementation Guide — Quick Reference

> **Audience**: Engineers building CMS-compliant payer/provider interoperability systems  
> **FHIR Version**: R4 (4.0.1)  
> **Last Updated**: July 2026

---

## Table of Contents

1. [FHIR R4 Fundamentals](#1-fhir-r4-fundamentals)
2. [Key Implementation Guides](#2-key-implementation-guides)
3. [CARIN Blue Button (C4BB)](#3-carin-blue-button-c4bb)
4. [Da Vinci Plan-Net (Provider Directory)](#4-da-vinci-plan-net-provider-directory)
5. [Da Vinci Formulary (DaVinci Drug Formulary)](#5-da-vinci-formulary)
6. [US Core](#6-us-core)
7. [Da Vinci PDex (Payer Data Exchange)](#7-da-vinci-pdex-payer-data-exchange)
8. [Da Vinci PAS (Prior Authorization Support)](#8-da-vinci-pas-prior-authorization-support)
9. [Common FHIR Operations](#9-common-fhir-operations)
10. [Authentication: SMART on FHIR & OAuth2](#10-authentication-smart-on-fhir--oauth2)
11. [Resource Relationship Diagrams](#11-resource-relationship-diagrams)
12. [Validation Checklist](#12-validation-checklist)

---

## 1. FHIR R4 Fundamentals

### 1.1 Resources

Everything in FHIR is a **Resource**. Each resource has:

| Component | Description |
|-----------|-------------|
| `resourceType` | The type name (e.g., `"Patient"`) |
| `id` | Server-assigned logical ID |
| `meta` | Version, lastUpdated, profile, security, tag |
| `text` | Human-readable narrative (XHTML) |
| Elements | Structured data fields |

```json
{
  "resourceType": "Patient",
  "id": "example-1",
  "meta": {
    "versionId": "3",
    "lastUpdated": "2026-07-01T10:30:00Z",
    "profile": ["http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"]
  },
  "identifier": [{
    "system": "http://hl7.org/fhir/sid/us-medicare",
    "value": "1EG4-TE5-MK72"
  }],
  "name": [{"family": "Shaw", "given": ["Amy"]}],
  "gender": "female",
  "birthDate": "1960-01-01"
}
```

### 1.2 Data Types

| Category | Types | Notes |
|----------|-------|-------|
| **Primitive** | `string`, `boolean`, `integer`, `decimal`, `uri`, `url`, `code`, `dateTime`, `instant`, `date`, `time`, `id`, `oid`, `base64Binary` | Serialized as JSON primitives |
| **Complex General** | `Identifier`, `HumanName`, `Address`, `ContactPoint`, `CodeableConcept`, `Coding`, `Period`, `Quantity`, `Money`, `Attachment` | Reusable structures |
| **Special** | `Reference`, `Extension`, `Narrative`, `Meta` | Infrastructure types |

#### CodeableConcept (most common complex type)

```json
{
  "coding": [{
    "system": "http://snomed.info/sct",
    "code": "386661006",
    "display": "Fever"
  }],
  "text": "Fever"
}
```

#### Reference

```json
{
  "reference": "Patient/example-1",
  "display": "Amy Shaw"
}
```

Reference formats:
- **Relative**: `"Patient/123"` (same server)
- **Absolute**: `"https://fhir.example.com/Patient/123"`
- **Logical**: `{"identifier": {"system": "...", "value": "..."}}`
- **Contained**: `"#contained-id"` (resource embedded in parent)

### 1.3 Bundles

Bundles group resources for transactions, search results, or documents.

| Bundle Type | Use Case |
|-------------|----------|
| `searchset` | Search results from server |
| `transaction` | Atomic batch of operations |
| `batch` | Independent operations (no atomicity) |
| `collection` | Arbitrary grouping |
| `document` | Clinical document |
| `message` | Message exchange |

```json
{
  "resourceType": "Bundle",
  "type": "searchset",
  "total": 1,
  "link": [
    {"relation": "self", "url": "https://fhir.example.com/Patient?name=Shaw"},
    {"relation": "next", "url": "https://fhir.example.com/Patient?name=Shaw&_page=2"}
  ],
  "entry": [{
    "fullUrl": "https://fhir.example.com/Patient/example-1",
    "resource": { "resourceType": "Patient", "id": "example-1" },
    "search": { "mode": "match", "score": 1.0 }
  }]
}
```

#### Transaction Bundle

```json
{
  "resourceType": "Bundle",
  "type": "transaction",
  "entry": [
    {
      "fullUrl": "urn:uuid:61ebe359-bfdc-4613-8bf2-c5e300945f0a",
      "resource": { "resourceType": "Patient", "name": [{"family": "Smith"}] },
      "request": { "method": "POST", "url": "Patient" }
    },
    {
      "fullUrl": "urn:uuid:88f151c0-a954-468a-88bd-5ae15c08e059",
      "resource": {
        "resourceType": "Encounter",
        "subject": { "reference": "urn:uuid:61ebe359-bfdc-4613-8bf2-c5e300945f0a" }
      },
      "request": { "method": "POST", "url": "Encounter" }
    }
  ]
}
```

### 1.4 Search Parameters

Standard search syntax: `GET [base]/[ResourceType]?param=value`

| Prefix | Meaning | Example |
|--------|---------|---------|
| `eq` | Equal (default) | `date=eq2026-01-01` |
| `ne` | Not equal | `status=ne:cancelled` |
| `gt` | Greater than | `date=gt2025-01-01` |
| `lt` | Less than | `date=lt2026-12-31` |
| `ge` | Greater or equal | `_lastUpdated=ge2026-01-01` |
| `le` | Less or equal | `_count=le50` |

**Common modifiers:**

| Modifier | Usage | Example |
|----------|-------|---------|
| `:exact` | Exact string match | `name:exact=Shaw` |
| `:contains` | Substring | `name:contains=Sha` |
| `:not` | Negation | `status:not=cancelled` |
| `:missing` | Element absent | `email:missing=true` |
| `:of-type` | Token type filter | `identifier:of-type=MR|12345` |

**Special parameters:**

| Parameter | Purpose |
|-----------|---------|
| `_include` | Include referenced resources |
| `_revinclude` | Include resources that reference results |
| `_count` | Page size |
| `_sort` | Sort order (`-` prefix = descending) |
| `_total` | Request total count (`accurate`, `estimate`, `none`) |
| `_elements` | Sparse fieldset |
| `_summary` | Summary mode (`true`, `text`, `count`, `data`) |
| `_has` | Reverse chaining |

**Chained search:**
```
GET /Observation?patient.name=Shaw&code=http://loinc.org|8867-4
```

**Composite search:**
```
GET /Observation?component-code-value-quantity=http://loinc.org|8480-6$gt140||mmHg
```

### 1.5 Validation

FHIR validation layers:

1. **Structure** — JSON/XML schema compliance
2. **Cardinality** — min/max element counts  
3. **Terminology** — coded values from correct ValueSets
4. **Invariants** — FHIRPath constraints (e.g., `pat-1`: contact SHALL have details)
5. **Profile** — IG-specific constraints (must-support, slicing, fixed values)
6. **Business Rules** — Cross-resource referential integrity

**Validation tools:**
- HAPI FHIR Validator (`org.hl7.fhir.validation`)
- Inferno Test Suites (for IG conformance)
- HL7 Validator CLI: `java -jar validator_cli.jar resource.json -ig hl7.fhir.us.core`

**OperationOutcome (validation response):**
```json
{
  "resourceType": "OperationOutcome",
  "issue": [{
    "severity": "error",
    "code": "required",
    "details": {"text": "Patient.identifier: minimum required = 1, but only found 0"},
    "expression": ["Patient.identifier"]
  }]
}
```

---

## 2. Key Implementation Guides

| IG | Version | Primary Use | CMS Rule |
|----|---------|-------------|----------|
| **CARIN Blue Button (C4BB)** | 2.0+ | Claims/EOB data to patients | CMS-9115-F (Patient Access) |
| **Da Vinci Plan-Net** | 1.1+ | Provider directory | CMS-9115-F |
| **Da Vinci Formulary** | 2.0+ | Drug formulary access | CMS-9115-F |
| **US Core** | 6.1+ | Clinical data foundation | Underpins all IGs |
| **Da Vinci PDex** | 2.0+ | Payer-to-payer/provider exchange | CMS-0057-F |
| **Da Vinci PAS** | 2.0+ | Prior authorization | CMS-0057-F |

---

## 3. CARIN Blue Button (C4BB)

### Purpose
Enables health plan members to access their claims and encounter data via a FHIR API. Mandated by CMS Patient Access API rule.

### Key Profiles

| Profile | Base Resource | Description |
|---------|--------------|-------------|
| `C4BB-ExplanationOfBenefit-Inpatient-Institutional` | ExplanationOfBenefit | Inpatient facility claims |
| `C4BB-ExplanationOfBenefit-Outpatient-Institutional` | ExplanationOfBenefit | Outpatient facility claims |
| `C4BB-ExplanationOfBenefit-Professional-NonClinician` | ExplanationOfBenefit | Professional/provider claims |
| `C4BB-ExplanationOfBenefit-Pharmacy` | ExplanationOfBenefit | Pharmacy claims |
| `C4BB-ExplanationOfBenefit-Oral` | ExplanationOfBenefit | Dental claims |
| `C4BB-Coverage` | Coverage | Insurance coverage |
| `C4BB-Patient` | Patient | Member demographics |
| `C4BB-Organization` | Organization | Payer/provider orgs |
| `C4BB-Practitioner` | Practitioner | Rendering providers |

### Required Search Parameters

```http
# Patient's EOBs
GET /ExplanationOfBenefit?patient=Patient/123

# By service date
GET /ExplanationOfBenefit?patient=Patient/123&service-date=ge2025-01-01&service-date=le2025-12-31

# By type
GET /ExplanationOfBenefit?patient=Patient/123&type=professional

# Include referenced resources
GET /ExplanationOfBenefit?patient=Patient/123&_include=ExplanationOfBenefit:provider&_include=ExplanationOfBenefit:care-team

# Last updated
GET /ExplanationOfBenefit?patient=Patient/123&_lastUpdated=ge2026-01-01
```

### Must-Support Elements (EOB)

```
ExplanationOfBenefit:
  ├── status (active | cancelled | draft | entered-in-error)
  ├── type (institutional | professional | pharmacy | oral | vision)
  ├── use (claim | preauthorization | predetermination)
  ├── patient → Patient
  ├── billablePeriod.start / .end
  ├── insurer → Organization
  ├── provider → Organization | Practitioner
  ├── outcome (queued | complete | error | partial)
  ├── insurance[].coverage → Coverage
  ├── item[]:
  │     ├── sequence
  │     ├── productOrService (CPT/HCPCS)
  │     ├── servicedDate / servicedPeriod
  │     ├── adjudication[]:
  │     │     ├── category (submitted | eligible | deductible | benefit | copay | coinsurance)
  │     │     └── amount
  │     └── revenue (Revenue Center Code)
  ├── total[]:
  │     ├── category
  │     └── amount
  ├── payment.amount
  └── careTeam[]:
        ├── provider → Practitioner
        └── role (primary | supervisor | referring)
```

### JSON Example: Professional EOB

```json
{
  "resourceType": "ExplanationOfBenefit",
  "id": "eob-prof-001",
  "meta": {
    "profile": ["http://hl7.org/fhir/us/carin-bb/StructureDefinition/C4BB-ExplanationOfBenefit-Professional-NonClinician"]
  },
  "status": "active",
  "type": {
    "coding": [{
      "system": "http://terminology.hl7.org/CodeSystem/claim-type",
      "code": "professional"
    }]
  },
  "use": "claim",
  "patient": { "reference": "Patient/mem-123" },
  "billablePeriod": {
    "start": "2026-03-15",
    "end": "2026-03-15"
  },
  "insurer": { "reference": "Organization/payer-xyz" },
  "provider": { "reference": "Practitioner/prov-456" },
  "outcome": "complete",
  "insurance": [{
    "focal": true,
    "coverage": { "reference": "Coverage/cov-789" }
  }],
  "careTeam": [{
    "sequence": 1,
    "provider": { "reference": "Practitioner/prov-456" },
    "role": {
      "coding": [{
        "system": "http://hl7.org/fhir/us/carin-bb/CodeSystem/C4BBClaimCareTeamRole",
        "code": "performing"
      }]
    }
  }],
  "item": [{
    "sequence": 1,
    "productOrService": {
      "coding": [{
        "system": "http://www.ama-assn.org/go/cpt",
        "code": "99213",
        "display": "Office visit, established patient"
      }]
    },
    "servicedDate": "2026-03-15",
    "adjudication": [
      {
        "category": {
          "coding": [{"system": "http://hl7.org/fhir/us/carin-bb/CodeSystem/C4BBAdjudicationDiscriminator", "code": "benefitpaymentstatus"}]
        }
      },
      {
        "category": {
          "coding": [{"system": "http://terminology.hl7.org/CodeSystem/adjudication", "code": "submitted"}]
        },
        "amount": { "value": 150.00, "currency": "USD" }
      },
      {
        "category": {
          "coding": [{"system": "http://terminology.hl7.org/CodeSystem/adjudication", "code": "benefit"}]
        },
        "amount": { "value": 120.00, "currency": "USD" }
      }
    ]
  }],
  "total": [
    {
      "category": {
        "coding": [{"system": "http://terminology.hl7.org/CodeSystem/adjudication", "code": "submitted"}]
      },
      "amount": { "value": 150.00, "currency": "USD" }
    },
    {
      "category": {
        "coding": [{"system": "http://terminology.hl7.org/CodeSystem/adjudication", "code": "benefit"}]
      },
      "amount": { "value": 120.00, "currency": "USD" }
    }
  ],
  "payment": {
    "amount": { "value": 120.00, "currency": "USD" }
  }
}
```

### Validation Rules
- `status` MUST be from `explanationofbenefit-status` ValueSet
- `type` MUST match the profile (e.g., `professional` for Professional profile)
- Each `item` MUST have at least one `adjudication`
- `insurance.focal` = `true` for at least one entry
- `billablePeriod` MUST be present for institutional claims
- `careTeam.role` MUST use C4BB-defined codes

---

## 4. Da Vinci Plan-Net (Provider Directory)

### Purpose
Standardized provider directory API for health plan provider networks. Supports CMS requirement for public-facing provider directory data.

### Key Profiles

| Profile | Base Resource | Description |
|---------|--------------|-------------|
| `PlanNet-Organization` | Organization | Healthcare organizations |
| `PlanNet-Practitioner` | Practitioner | Individual providers |
| `PlanNet-PractitionerRole` | PractitionerRole | Provider roles in networks |
| `PlanNet-HealthcareService` | HealthcareService | Services offered |
| `PlanNet-Location` | Location | Practice locations |
| `PlanNet-Network` | Organization | Insurance networks |
| `PlanNet-InsurancePlan` | InsurancePlan | Plan details |
| `PlanNet-Endpoint` | Endpoint | Technical endpoints |

### Required Search Parameters

```http
# Find practitioners by name
GET /Practitioner?name=Smith

# Find practitioners by specialty
GET /PractitionerRole?specialty=http://nucc.org/provider-taxonomy|207R00000X

# Find by location (within 25 miles)
GET /Location?near=42.35|-71.06|25|mi

# Find by network
GET /PractitionerRole?network=Organization/network-abc

# Find organizations offering a service
GET /HealthcareService?service-type=http://terminology.hl7.org/CodeSystem/service-type|124

# Include location details with practitioner roles
GET /PractitionerRole?specialty=207R00000X&_include=PractitionerRole:location&_include=PractitionerRole:practitioner

# Active providers only
GET /PractitionerRole?active=true
```

### Must-Support Elements

```
PractitionerRole:
  ├── active
  ├── practitioner → Practitioner
  ├── organization → Organization
  ├── code (provider role type)
  ├── specialty[] (NUCC taxonomy)
  ├── location[] → Location
  ├── network[] → Organization (network)
  ├── healthcareService[] → HealthcareService
  ├── telecom[] (phone, fax)
  └── availableTime[]

Location:
  ├── status (active | suspended | inactive)
  ├── name
  ├── type[] (facility type)
  ├── telecom[]
  ├── address (full street address)
  ├── position (lat/lng for geo search)
  └── hoursOfOperation[]

Practitioner:
  ├── identifier[] (NPI required)
  ├── active
  ├── name[]
  ├── qualification[] (board certifications)
  └── communication[] (languages)
```

### JSON Example: PractitionerRole

```json
{
  "resourceType": "PractitionerRole",
  "id": "pract-role-001",
  "meta": {
    "profile": ["http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-PractitionerRole"]
  },
  "active": true,
  "practitioner": { "reference": "Practitioner/pract-smith" },
  "organization": { "reference": "Organization/org-clinic-main" },
  "code": [{
    "coding": [{
      "system": "http://hl7.org/fhir/us/davinci-pdex-plan-net/CodeSystem/ProviderRoleCS",
      "code": "ph",
      "display": "Physician"
    }]
  }],
  "specialty": [{
    "coding": [{
      "system": "http://nucc.org/provider-taxonomy",
      "code": "207R00000X",
      "display": "Internal Medicine"
    }]
  }],
  "location": [
    { "reference": "Location/loc-main-office" }
  ],
  "network": [
    { "reference": "Organization/network-blue-ppo" }
  ],
  "telecom": [
    { "system": "phone", "value": "555-123-4567", "use": "work" }
  ],
  "availableTime": [{
    "daysOfWeek": ["mon", "tue", "wed", "thu", "fri"],
    "availableStartTime": "08:00:00",
    "availableEndTime": "17:00:00"
  }]
}
```

### Validation Rules
- `Practitioner.identifier` MUST include NPI (`http://hl7.org/fhir/sid/us-npi`)
- `Location.address` MUST include `line`, `city`, `state`, `postalCode`
- `PractitionerRole.specialty` MUST use NUCC taxonomy codes
- All resources MUST have `meta.lastUpdated`
- Network references MUST resolve to valid Organization resources with `type` = `ntwk`
- Endpoint resources must specify `connectionType` and `payloadType`

---

## 5. Da Vinci Formulary

### Purpose
Enables patients and providers to query a health plan's drug formulary — which drugs are covered, at what tier, with what restrictions.

### Key Profiles

| Profile | Base Resource | Description |
|---------|--------------|-------------|
| `Formulary` | InsurancePlan | The formulary coverage plan |
| `FormularyItem` | Basic | Drug's formulary status & tier |
| `FormularyDrug` | MedicationKnowledge | Drug details (RxNorm) |

### Required Search Parameters

```http
# List all formularies for a plan
GET /InsurancePlan?type=http://terminology.hl7.org/CodeSystem/v3-ActCode|DRUGPOL

# Search drugs by code (RxNorm)
GET /Basic?code=http://hl7.org/fhir/us/davinci-drug-formulary/CodeSystem/usdf-InsuranceItemTypeCS|formulary-item&formulary=InsurancePlan/formulary-123

# Search drugs by name
GET /MedicationKnowledge?code:text=metformin

# Get formulary items for a specific drug
GET /Basic?subject=MedicationKnowledge/drug-metformin

# Drugs by tier
GET /Basic?drugTier=http://hl7.org/fhir/us/davinci-drug-formulary/CodeSystem/usdf-DrugTierCS|generic
```

### Must-Support Elements

```
InsurancePlan (Formulary):
  ├── status (active | draft | retired)
  ├── type (DRUGPOL)
  ├── name
  ├── period (effective dates)
  ├── coverage[]:
  │     ├── type (drug coverage type)
  │     └── benefit[]:
  │           └── type (cost-sharing details)
  └── plan[]:
        └── specificCost[] (copay/coinsurance by tier)

Basic (FormularyItem):
  ├── code (formulary-item)
  ├── subject → MedicationKnowledge
  ├── extension[usdf-DrugTierID] (generic | preferred-brand | non-preferred-brand | specialty)
  ├── extension[usdf-PriorAuthorization] (boolean)
  ├── extension[usdf-StepTherapyLimit] (boolean)
  ├── extension[usdf-QuantityLimit] (boolean)
  └── extension[usdf-FormularyReference] → InsurancePlan

MedicationKnowledge (FormularyDrug):
  ├── code (RxNorm)
  ├── status (active | inactive)
  └── doseForm
```

### JSON Example: FormularyItem

```json
{
  "resourceType": "Basic",
  "id": "formulary-item-metformin",
  "meta": {
    "profile": ["http://hl7.org/fhir/us/davinci-drug-formulary/StructureDefinition/usdf-FormularyItem"]
  },
  "code": {
    "coding": [{
      "system": "http://hl7.org/fhir/us/davinci-drug-formulary/CodeSystem/usdf-InsuranceItemTypeCS",
      "code": "formulary-item"
    }]
  },
  "subject": { "reference": "MedicationKnowledge/drug-metformin-500" },
  "extension": [
    {
      "url": "http://hl7.org/fhir/us/davinci-drug-formulary/StructureDefinition/usdf-DrugTierID-extension",
      "valueCodeableConcept": {
        "coding": [{
          "system": "http://hl7.org/fhir/us/davinci-drug-formulary/CodeSystem/usdf-DrugTierCS",
          "code": "generic",
          "display": "Generic"
        }]
      }
    },
    {
      "url": "http://hl7.org/fhir/us/davinci-drug-formulary/StructureDefinition/usdf-PriorAuthorization-extension",
      "valueBoolean": false
    },
    {
      "url": "http://hl7.org/fhir/us/davinci-drug-formulary/StructureDefinition/usdf-StepTherapyLimit-extension",
      "valueBoolean": false
    },
    {
      "url": "http://hl7.org/fhir/us/davinci-drug-formulary/StructureDefinition/usdf-QuantityLimit-extension",
      "valueBoolean": true
    },
    {
      "url": "http://hl7.org/fhir/us/davinci-drug-formulary/StructureDefinition/usdf-FormularyReference-extension",
      "valueReference": { "reference": "InsurancePlan/formulary-gold-plan" }
    }
  ]
}
```

### Validation Rules
- `MedicationKnowledge.code` MUST use RxNorm (`http://www.nlm.nih.gov/research/umls/rxnorm`)
- Drug tier extension MUST be present on every FormularyItem
- FormularyReference extension is required (links item to formulary)
- `InsurancePlan.type` MUST include `DRUGPOL` coding
- API must be publicly accessible (no auth required per CMS rule)

---

## 6. US Core

### Purpose
Foundation IG defining minimum conformance expectations for US healthcare data exchange. All CMS-related IGs build on US Core profiles.

### Key Profiles (v6.1+)

| Profile | Base Resource | Common Use |
|---------|--------------|------------|
| `us-core-patient` | Patient | Member/patient demographics |
| `us-core-condition` | Condition | Diagnoses and problems |
| `us-core-encounter` | Encounter | Visits and admissions |
| `us-core-procedure` | Procedure | Procedures performed |
| `us-core-observation-lab` | Observation | Lab results |
| `us-core-observation-vitalsigns` | Observation | Vital signs |
| `us-core-allergyintolerance` | AllergyIntolerance | Allergies |
| `us-core-medication` | Medication | Medications |
| `us-core-medicationrequest` | MedicationRequest | Prescriptions |
| `us-core-immunization` | Immunization | Vaccines |
| `us-core-diagnosticreport` | DiagnosticReport | Lab/path reports |
| `us-core-documentreference` | DocumentReference | Clinical documents (C-CDA) |
| `us-core-careplan` | CarePlan | Care plans |
| `us-core-careteam` | CareTeam | Care teams |
| `us-core-goal` | Goal | Patient goals |
| `us-core-provenance` | Provenance | Data provenance |

### Required Search Parameters (Selected)

```http
# Patient by identifier (Medicare ID)
GET /Patient?identifier=http://hl7.org/fhir/sid/us-medicare|1EG4-TE5-MK72

# Patient by name + birthdate
GET /Patient?name=Shaw&birthdate=1960-01-01

# Conditions for a patient
GET /Condition?patient=Patient/123&category=problem-list-item
GET /Condition?patient=Patient/123&clinical-status=active

# Encounters
GET /Encounter?patient=Patient/123&date=ge2025-01-01

# Lab results
GET /Observation?patient=Patient/123&category=laboratory&date=ge2026-01-01

# Medications
GET /MedicationRequest?patient=Patient/123&status=active

# Allergies
GET /AllergyIntolerance?patient=Patient/123&clinical-status=active

# Document references (C-CDA)
GET /DocumentReference?patient=Patient/123&type=http://loinc.org|34133-9

# Provenance
GET /Provenance?_has:target=Patient/123
```

### Must-Support Elements (Patient)

```
Patient (us-core-patient):
  ├── identifier[] (at least one — MBI for Medicare)
  │     ├── system
  │     └── value
  ├── name[] (at least one)
  │     ├── family (REQUIRED)
  │     └── given[]
  ├── gender (REQUIRED)
  ├── birthDate (REQUIRED)
  ├── address[]
  │     ├── line[]
  │     ├── city
  │     ├── state (USPS 2-letter)
  │     └── postalCode
  ├── telecom[]
  ├── communication[].language
  ├── extension[us-core-race]
  ├── extension[us-core-ethnicity]
  └── extension[us-core-birthsex]
```

### JSON Example: US Core Patient

```json
{
  "resourceType": "Patient",
  "id": "patient-shaw",
  "meta": {
    "profile": ["http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"]
  },
  "extension": [
    {
      "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race",
      "extension": [
        { "url": "ombCategory", "valueCoding": {"system": "urn:oid:2.16.840.1.113883.6.238", "code": "2106-3", "display": "White"} },
        { "url": "text", "valueString": "White" }
      ]
    },
    {
      "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity",
      "extension": [
        { "url": "ombCategory", "valueCoding": {"system": "urn:oid:2.16.840.1.113883.6.238", "code": "2186-5", "display": "Not Hispanic or Latino"} },
        { "url": "text", "valueString": "Not Hispanic or Latino" }
      ]
    },
    {
      "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
      "valueCode": "F"
    }
  ],
  "identifier": [
    { "system": "http://hl7.org/fhir/sid/us-medicare", "value": "1EG4-TE5-MK72" }
  ],
  "name": [{
    "use": "official",
    "family": "Shaw",
    "given": ["Amy", "V."]
  }],
  "gender": "female",
  "birthDate": "1960-01-01",
  "address": [{
    "line": ["123 Main St"],
    "city": "Anytown",
    "state": "MA",
    "postalCode": "02101"
  }],
  "telecom": [
    { "system": "phone", "value": "555-555-5555", "use": "home" }
  ]
}
```

### Validation Rules
- **Must Support**: Sender MUST populate if data exists; receiver MUST be able to process
- `Patient.gender` uses `http://hl7.org/fhir/administrative-gender` (male | female | other | unknown)
- Race/ethnicity extensions use OMB categories
- `Observation.status` is required (final | preliminary | amended | corrected)
- Lab observations MUST have `category` = `laboratory`
- Vital signs MUST conform to FHIR core vital signs profiles
- `Provenance` SHOULD accompany data exchanges (who, when, how)

---

## 7. Da Vinci PDex (Payer Data Exchange)

### Purpose
Enables payer-to-payer and payer-to-provider clinical and claims data exchange. Implements CMS-0057-F requirements for health plan transitions.

### Key Profiles

| Profile | Base Resource | Description |
|---------|--------------|-------------|
| `PDex-MemberMatch` | Parameters | Patient matching across payers |
| Uses all US Core profiles | Various | Clinical data |
| Uses C4BB profiles | EOB | Claims data |
| `HRex-Provenance` | Provenance | Data origin tracking |
| `HRex-Consent` | Consent | Member authorization |

### Key Operations

```http
# Member Match — find patient across payers
POST /Patient/$member-match
Content-Type: application/fhir+json

{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "MemberPatient",
      "resource": {
        "resourceType": "Patient",
        "identifier": [{"system": "http://hl7.org/fhir/sid/us-medicare", "value": "1EG4-TE5-MK72"}],
        "name": [{"family": "Shaw", "given": ["Amy"]}],
        "gender": "female",
        "birthDate": "1960-01-01"
      }
    },
    {
      "name": "OldCoverage",
      "resource": {
        "resourceType": "Coverage",
        "status": "active",
        "beneficiary": { "reference": "Patient/temp" },
        "payor": [{ "reference": "Organization/old-payer" }],
        "identifier": [{"system": "http://old-payer.com/member-id", "value": "OLD-MEM-123"}]
      }
    },
    {
      "name": "NewCoverage",
      "resource": {
        "resourceType": "Coverage",
        "status": "active",
        "beneficiary": { "reference": "Patient/temp" },
        "payor": [{ "reference": "Organization/new-payer" }]
      }
    }
  ]
}
```

**Response:**
```json
{
  "resourceType": "Parameters",
  "parameter": [{
    "name": "MemberIdentifier",
    "valueIdentifier": {
      "system": "http://old-payer.com/fhir/memberid",
      "value": "matched-member-456"
    }
  }]
}
```

### Required Search Parameters

```http
# After $member-match, use standard US Core/C4BB searches:
GET /Patient/matched-member-456
GET /ExplanationOfBenefit?patient=Patient/matched-member-456
GET /Condition?patient=Patient/matched-member-456
GET /Encounter?patient=Patient/matched-member-456
GET /Observation?patient=Patient/matched-member-456&category=laboratory
GET /AllergyIntolerance?patient=Patient/matched-member-456

# Bulk export for payer-to-payer
GET /Group/[payer-group]/$export?_type=Patient,ExplanationOfBenefit,Condition,Encounter
```

### PDex Exchange Flows

```
┌──────────────────────────────────────────────────────────────────┐
│ Flow 1: Payer-to-Payer (Member transitions plans)               │
├──────────────────────────────────────────────────────────────────┤
│ New Payer ──$member-match──▶ Old Payer                          │
│ New Payer ──GET /Patient, /EOB, /Condition──▶ Old Payer         │
│   (or $export for bulk)                                         │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│ Flow 2: Payer-to-Provider (Clinical data at point of care)      │
├──────────────────────────────────────────────────────────────────┤
│ Provider EHR ──SMART launch──▶ Payer FHIR Server               │
│ Provider EHR ──GET /Patient/$everything──▶ Payer                │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│ Flow 3: Patient Access (Member-facing app)                      │
├──────────────────────────────────────────────────────────────────┤
│ Patient App ──SMART on FHIR──▶ Payer FHIR Server               │
│ Patient App ──GET resources──▶ Payer (scoped to patient)        │
└──────────────────────────────────────────────────────────────────┘
```

### Must-Support & Validation
- `$member-match` MUST return exactly one match or an error
- All exchanged resources MUST include `Provenance`
- `Consent` must be captured before payer-to-payer exchange
- Data MUST be exchanged within **1 business day** of member request (CMS-0057-F)
- Minimum 5 years of claims history required
- Clinical data includes: conditions, encounters, observations, medications, allergies, immunizations, procedures

---

## 8. Da Vinci PAS (Prior Authorization Support)

### Purpose
Automates prior authorization requests and responses between providers and payers using FHIR, replacing fax/phone workflows. Supports X12 278 mapping.

### Key Profiles

| Profile | Base Resource | Description |
|---------|--------------|-------------|
| `PAS-Claim` | Claim | Authorization request |
| `PAS-ClaimResponse` | ClaimResponse | Authorization response |
| `PAS-CommunicationRequest` | CommunicationRequest | Additional info request |
| `PAS-Coverage` | Coverage | Insurance coverage |
| `PAS-Encounter` | Encounter | Encounter details |
| `PAS-Organization` | Organization | Provider/payer org |
| `PAS-Patient` | Patient | Beneficiary |
| `PAS-Practitioner` | Practitioner | Requesting provider |
| `PAS-Subscriber` | Patient | Subscriber (if different) |
| `PAS-Task` | Task | Workflow tracking |

### Key Operations

```http
# Submit prior auth request
POST /Claim/$submit
Content-Type: application/fhir+json

# Check status of pending auth
POST /Claim/$inquire
Content-Type: application/fhir+json

# Subscribe to auth updates
POST /Subscription
```

### JSON Example: PAS Claim (Prior Auth Request)

```json
{
  "resourceType": "Bundle",
  "type": "collection",
  "entry": [
    {
      "fullUrl": "http://example.com/Claim/pas-claim-001",
      "resource": {
        "resourceType": "Claim",
        "id": "pas-claim-001",
        "meta": {
          "profile": ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-claim"]
        },
        "status": "active",
        "type": {
          "coding": [{
            "system": "http://terminology.hl7.org/CodeSystem/claim-type",
            "code": "professional"
          }]
        },
        "use": "preauthorization",
        "patient": { "reference": "Patient/pat-001" },
        "created": "2026-07-01",
        "insurer": { "reference": "Organization/payer-abc" },
        "provider": { "reference": "Organization/provider-group" },
        "priority": {
          "coding": [{"system": "http://terminology.hl7.org/CodeSystem/processpriority", "code": "normal"}]
        },
        "insurance": [{
          "sequence": 1,
          "focal": true,
          "coverage": { "reference": "Coverage/cov-001" }
        }],
        "item": [{
          "sequence": 1,
          "productOrService": {
            "coding": [{
              "system": "http://www.ama-assn.org/go/cpt",
              "code": "27447",
              "display": "Total knee replacement"
            }]
          },
          "servicedDate": "2026-08-15",
          "locationCodeableConcept": {
            "coding": [{
              "system": "https://www.cms.gov/Medicare/Coding/place-of-service-codes/Place_of_Service_Code_Set",
              "code": "21",
              "display": "Inpatient Hospital"
            }]
          },
          "extension": [{
            "url": "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-serviceItemRequestType",
            "valueCodeableConcept": {
              "coding": [{
                "system": "http://codesystem.x12.org/005010/1525",
                "code": "SC",
                "display": "Specialty Care Review"
              }]
            }
          }]
        }],
        "diagnosis": [{
          "sequence": 1,
          "diagnosisCodeableConcept": {
            "coding": [{
              "system": "http://hl7.org/fhir/sid/icd-10-cm",
              "code": "M17.11",
              "display": "Primary osteoarthritis, right knee"
            }]
          }
        }],
        "supportingInfo": [{
          "sequence": 1,
          "category": {
            "coding": [{
              "system": "http://hl7.org/fhir/us/davinci-pas/CodeSystem/PASSupportingInfoType",
              "code": "patientEvent"
            }]
          },
          "timingPeriod": {
            "start": "2026-08-15",
            "end": "2026-08-18"
          }
        }]
      }
    }
  ]
}
```

### JSON Example: ClaimResponse (Auth Decision)

```json
{
  "resourceType": "ClaimResponse",
  "id": "pas-response-001",
  "meta": {
    "profile": ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-claimresponse"]
  },
  "status": "active",
  "type": {
    "coding": [{"system": "http://terminology.hl7.org/CodeSystem/claim-type", "code": "professional"}]
  },
  "use": "preauthorization",
  "patient": { "reference": "Patient/pat-001" },
  "created": "2026-07-01T14:30:00Z",
  "insurer": { "reference": "Organization/payer-abc" },
  "outcome": "complete",
  "preAuthRef": "AUTH-2026-07-001234",
  "preAuthPeriod": {
    "start": "2026-08-01",
    "end": "2026-10-31"
  },
  "item": [{
    "itemSequence": 1,
    "extension": [{
      "url": "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-reviewAction",
      "extension": [
        { "url": "number", "valueString": "AUTH-2026-07-001234" },
        { "url": "reasonCode", "valueCodeableConcept": {
          "coding": [{"system": "http://codesystem.x12.org/005010/306", "code": "A1", "display": "Certified in total"}]
        }}
      ]
    }],
    "adjudication": [{
      "category": {
        "coding": [{"system": "http://terminology.hl7.org/CodeSystem/adjudication", "code": "submitted"}]
      },
      "extension": [{
        "url": "http://hl7.org/fhir/us/davinci-pas/StructureDefinition/extension-reviewAction",
        "extension": [
          { "url": "reasonCode", "valueCodeableConcept": {
            "coding": [{"system": "http://codesystem.x12.org/005010/306", "code": "A1"}]
          }}
        ]
      }]
    }]
  }]
}
```

### Must-Support Elements

```
Claim ($submit input):
  ├── status = "active"
  ├── type (professional | institutional | oral | pharmacy)
  ├── use = "preauthorization"
  ├── patient → Patient
  ├── created
  ├── insurer → Organization (payer)
  ├── provider → Organization | Practitioner
  ├── priority
  ├── insurance[].coverage → Coverage
  ├── diagnosis[]:
  │     ├── diagnosisCodeableConcept (ICD-10)
  │     └── sequence
  ├── item[]:
  │     ├── productOrService (CPT/HCPCS)
  │     ├── servicedDate | servicedPeriod
  │     ├── locationCodeableConcept (place of service)
  │     ├── quantity
  │     └── extension[serviceItemRequestType]
  └── supportingInfo[] (clinical attachments, dates)

ClaimResponse ($submit output):
  ├── outcome (complete | queued | error | partial)
  ├── preAuthRef (authorization number)
  ├── preAuthPeriod (validity window)
  ├── item[].extension[reviewAction]:
  │     ├── number (auth tracking number)
  │     └── reasonCode (A1=approved, A2=modified, A3=denied, A4=pended)
  └── communicationRequest[] (if additional info needed)
```

### Validation Rules
- `Claim.use` MUST be `"preauthorization"`
- At least one `item` is required
- `diagnosis` MUST use ICD-10-CM (`http://hl7.org/fhir/sid/icd-10-cm`)
- `item.productOrService` MUST use CPT or HCPCS
- `$submit` MUST return response within defined SLA (payer-dependent)
- If `outcome` = `"queued"`, client should poll via `$inquire`
- X12 278 mapping extensions are required for interop with clearinghouses

---

## 9. Common FHIR Operations

### 9.1 Read

```http
# Read single resource
GET /Patient/123
Accept: application/fhir+json

# Conditional read (ETag)
GET /Patient/123
If-None-Match: W/"3"
# Returns 304 Not Modified if unchanged

# Version read
GET /Patient/123/_history/2
```

### 9.2 Search

```http
# GET-based search
GET /ExplanationOfBenefit?patient=Patient/123&_count=20&_sort=-service-date

# POST-based search (for long query strings)
POST /ExplanationOfBenefit/_search
Content-Type: application/x-www-form-urlencoded

patient=Patient/123&_count=20&_sort=-service-date

# Pagination (follow Bundle.link "next")
GET /ExplanationOfBenefit?patient=Patient/123&_page=2&_count=20
```

### 9.3 Create

```http
# Create resource
POST /Patient
Content-Type: application/fhir+json

{ "resourceType": "Patient", "name": [{"family": "Smith"}] }

# Response: 201 Created
# Location: https://fhir.example.com/Patient/new-id-123/_history/1

# Conditional create (avoid duplicates)
POST /Patient
If-None-Exist: identifier=http://example.com/mrn|12345
Content-Type: application/fhir+json

{ "resourceType": "Patient", ... }
```

### 9.4 Update

```http
# Full update
PUT /Patient/123
Content-Type: application/fhir+json
If-Match: W/"3"

{ "resourceType": "Patient", "id": "123", ... }

# Conditional update
PUT /Patient?identifier=http://example.com/mrn|12345
Content-Type: application/fhir+json

{ "resourceType": "Patient", ... }

# Patch (JSON Patch)
PATCH /Patient/123
Content-Type: application/json-patch+json

[
  { "op": "replace", "path": "/birthDate", "value": "1960-01-02" },
  { "op": "add", "path": "/telecom/-", "value": {"system": "email", "value": "new@example.com"} }
]
```

### 9.5 $everything (Patient Compartment)

```http
# Get all data for a patient
GET /Patient/123/$everything

# With date range
GET /Patient/123/$everything?start=2025-01-01&end=2026-06-30

# With type filter
GET /Patient/123/$everything?_type=Condition,MedicationRequest,AllergyIntolerance
```

**Response:** Bundle of type `searchset` containing all patient-compartment resources.

### 9.6 $export (Bulk Data / NDJSON)

```http
# Kick-off (async)
GET /Group/payer-members/$export?_type=Patient,ExplanationOfBenefit,Coverage&_since=2026-01-01
Accept: application/fhir+json
Prefer: respond-async

# Response: 202 Accepted
# Content-Location: https://fhir.example.com/export-status/job-abc

# Poll status
GET /export-status/job-abc

# In-progress response: 202 Accepted + X-Progress header
# Complete response: 200 OK with manifest
```

**Completed Export Manifest:**
```json
{
  "transactionTime": "2026-07-01T10:00:00Z",
  "request": "https://fhir.example.com/Group/all/$export",
  "requiresAccessToken": true,
  "output": [
    { "type": "Patient", "url": "https://fhir.example.com/bulk/file1.ndjson", "count": 50000 },
    { "type": "ExplanationOfBenefit", "url": "https://fhir.example.com/bulk/file2.ndjson", "count": 250000 },
    { "type": "Coverage", "url": "https://fhir.example.com/bulk/file3.ndjson", "count": 50000 }
  ],
  "error": [
    { "type": "OperationOutcome", "url": "https://fhir.example.com/bulk/errors.ndjson", "count": 12 }
  ]
}
```

**NDJSON format** (one JSON resource per line):
```
{"resourceType":"Patient","id":"1","name":[{"family":"Smith"}],"gender":"male","birthDate":"1955-03-15"}
{"resourceType":"Patient","id":"2","name":[{"family":"Jones"}],"gender":"female","birthDate":"1972-08-22"}
```

### 9.7 Operation Summary Table

| Operation | Method | URL Pattern | Use Case |
|-----------|--------|-------------|----------|
| Read | GET | `/[type]/[id]` | Single resource |
| VRead | GET | `/[type]/[id]/_history/[vid]` | Specific version |
| Search | GET/POST | `/[type]?params` | Query resources |
| Create | POST | `/[type]` | New resource |
| Update | PUT | `/[type]/[id]` | Replace resource |
| Patch | PATCH | `/[type]/[id]` | Partial update |
| Delete | DELETE | `/[type]/[id]` | Remove resource |
| $everything | GET | `/Patient/[id]/$everything` | Patient compartment |
| $export | GET | `/Group/[id]/$export` | Bulk async export |
| $member-match | POST | `/Patient/$member-match` | Cross-payer matching |
| $submit | POST | `/Claim/$submit` | Prior auth request |
| $inquire | POST | `/Claim/$inquire` | Prior auth status |

---

## 10. Authentication: SMART on FHIR & OAuth2

### 10.1 SMART on FHIR Overview

SMART (Substitutable Medical Applications, Reusable Technologies) is the OAuth2-based framework for FHIR API authorization.

**Discovery (Well-Known Endpoint):**
```http
GET /.well-known/smart-configuration

{
  "authorization_endpoint": "https://auth.example.com/authorize",
  "token_endpoint": "https://auth.example.com/token",
  "registration_endpoint": "https://auth.example.com/register",
  "scopes_supported": ["openid", "fhirUser", "launch", "launch/patient", "patient/*.read", "user/*.read", "system/*.read"],
  "response_types_supported": ["code"],
  "capabilities": ["launch-ehr", "launch-standalone", "client-public", "client-confidential-symmetric", "sso-openid-connect", "permission-v2"]
}
```

### 10.2 Launch Flows

#### Standalone Launch (Patient App)

```
┌─────────────┐         ┌──────────────┐         ┌──────────────┐
│  Patient    │         │  Auth Server │         │  FHIR Server │
│  App        │         │              │         │              │
└──────┬──────┘         └──────┬───────┘         └──────┬───────┘
       │                       │                        │
       │──GET /authorize──────▶│                        │
       │  ?response_type=code  │                        │
       │  &client_id=app123    │                        │
       │  &redirect_uri=...    │                        │
       │  &scope=launch/patient│                        │
       │   patient/*.read      │                        │
       │  &state=xyz           │                        │
       │  &aud=https://fhir..  │                        │
       │                       │                        │
       │◀─Redirect w/ code─────│                        │
       │                       │                        │
       │──POST /token─────────▶│                        │
       │  grant_type=           │                        │
       │   authorization_code  │                        │
       │  &code=AUTH_CODE      │                        │
       │  &redirect_uri=...    │                        │
       │                       │                        │
       │◀─Token Response───────│                        │
       │  {access_token,       │                        │
       │   patient: "123",     │                        │
       │   scope: "..."}       │                        │
       │                       │                        │
       │──GET /Patient/123─────────────────────────────▶│
       │   Authorization:      │                        │
       │    Bearer <token>     │                        │
       │◀──────────────────────────────────────────────│
```

#### Backend Services (System-to-System / Bulk Data)

```
┌──────────────┐         ┌──────────────┐         ┌──────────────┐
│  Backend     │         │  Auth Server │         │  FHIR Server │
│  Service     │         │              │         │              │
└──────┬───────┘         └──────┬───────┘         └──────┬───────┘
       │                        │                        │
       │──POST /token──────────▶│                        │
       │  grant_type=           │                        │
       │   client_credentials  │                        │
       │  &scope=system/*.read │                        │
       │  &client_assertion_   │                        │
       │   type=urn:ietf:...jwt│                        │
       │  &client_assertion=   │                        │
       │   <signed JWT>        │                        │
       │                        │                        │
       │◀─{access_token}───────│                        │
       │                        │                        │
       │──GET /Group/all/$export───────────────────────▶│
       │   Authorization: Bearer <token>                │
       │◀──202 Accepted────────────────────────────────│
```

### 10.3 OAuth2 Scopes

#### SMART v2 Scope Syntax

Format: `<context>/<resource>.<permission>?param=value`

| Scope Pattern | Meaning |
|---------------|---------|
| `patient/Patient.read` | Read the current patient's Patient resource |
| `patient/ExplanationOfBenefit.read` | Read the patient's EOBs |
| `patient/*.read` | Read all resource types for the patient |
| `user/Patient.read` | Read any Patient the user has access to |
| `user/*.cruds` | Full access scoped to user permissions |
| `system/Patient.read` | Backend service reads all Patients |
| `system/*.read` | Backend service full read access |
| `launch/patient` | App needs a patient context |
| `openid fhirUser` | Identity token with FHIR user reference |

#### CMS-Specific Scopes

```
# Patient Access API (member-facing)
patient/Patient.read
patient/ExplanationOfBenefit.read
patient/Coverage.read
patient/Condition.read
patient/Encounter.read
patient/Observation.read
patient/MedicationRequest.read
patient/AllergyIntolerance.read
patient/Procedure.read
patient/Immunization.read

# Provider Directory (public, no auth)
# (No scopes — unauthenticated access)

# Payer-to-Payer (backend services)
system/Patient.read
system/ExplanationOfBenefit.read
system/Coverage.read
system/Condition.read
system/Encounter.read
system/Observation.read
system/Group.read

# Prior Authorization (provider → payer)
user/Claim.write
user/ClaimResponse.read
system/Claim.write
system/ClaimResponse.read
```

### 10.4 Token Request Examples

**Standalone Patient Launch:**
```http
POST /token HTTP/1.1
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code
&code=SplxlOBeZQQYbYS6WxSbIA
&redirect_uri=https://myapp.example.com/callback
&client_id=my_app_id
&code_verifier=dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk
```

**Backend Services (JWT assertion):**
```http
POST /token HTTP/1.1
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
&scope=system/Patient.read system/ExplanationOfBenefit.read
&client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer
&client_assertion=eyJhbGciOiJSUzM4NCIsInR5cCI6IkpXVCIs...
```

**JWT Assertion Payload:**
```json
{
  "iss": "https://myapp.example.com",
  "sub": "my_client_id",
  "aud": "https://auth.fhir-server.com/token",
  "exp": 1720350000,
  "iat": 1720346400,
  "jti": "random-unique-id-abc123"
}
```

### 10.5 Access Token Response

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIs...",
  "token_type": "Bearer",
  "expires_in": 3600,
  "scope": "patient/Patient.read patient/ExplanationOfBenefit.read",
  "patient": "123",
  "id_token": "eyJhbGciOiJSUzI1NiIs..."
}
```

---

## 11. Resource Relationship Diagrams

### 11.1 CARIN Blue Button (Claims)

```
┌─────────────────────────────────────────────────────────────────┐
│                    ExplanationOfBenefit                          │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ .patient ──────────────────────▶ [Patient]                │  │
│  │ .insurer ──────────────────────▶ [Organization] (payer)   │  │
│  │ .provider ─────────────────────▶ [Organization | Pract.]  │  │
│  │ .insurance[].coverage ─────────▶ [Coverage]               │  │
│  │ .careTeam[].provider ──────────▶ [Practitioner]           │  │
│  │ .facility ─────────────────────▶ [Location]               │  │
│  │ .item[]:                                                   │  │
│  │   ├── .productOrService (CPT/HCPCS code)                 │  │
│  │   ├── .adjudication[] (allowed/paid amounts)              │  │
│  │   └── .revenue (UB-04 revenue code)                       │  │
│  │ .total[] (claim-level amounts)                            │  │
│  │ .payment.amount                                            │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
         │                    │                    │
         ▼                    ▼                    ▼
   ┌──────────┐      ┌──────────────┐     ┌──────────────┐
   │ Patient  │      │  Coverage    │     │ Organization │
   │          │◀─────│ .beneficiary │     │   (Payer)    │
   │ .name    │      │ .payor ─────────▶  │ .name        │
   │ .id (MBI)│      │ .class[]     │     │ .identifier  │
   └──────────┘      │ .period      │     └──────────────┘
                     └──────────────┘
```

### 11.2 Da Vinci Plan-Net (Provider Directory)

```
┌──────────────────────────────────────────────────────────────┐
│                     InsurancePlan                             │
│  .ownedBy ──────────────────────▶ [Organization] (Payer)     │
│  .administeredBy ───────────────▶ [Organization]             │
│  .network[] ────────────────────▶ [Organization] (Network)   │
│  .coverage[].benefit[]                                       │
└──────────────────────────────────────────────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │  Organization         │
              │  (Network)            │
              │  .type = "ntwk"       │
              └───────────┬───────────┘
                          │
              ┌───────────┼───────────────────────────┐
              ▼           ▼                           ▼
┌────────────────────┐ ┌────────────────────────┐ ┌──────────────────┐
│ PractitionerRole   │ │ HealthcareService      │ │ Organization     │
│ .network[] ────────┤ │ .providedBy ──────────▶│ │ (Provider Group) │
│ .practitioner ──▶  │ │ .location[] ──────────▶│ └──────────────────┘
│ .organization ──▶  │ │ .category              │
│ .location[] ───────┤ │ .type[]                │
│ .specialty[]       │ └────────────────────────┘
│ .healthcareService │
└──────┬─────────────┘
       │         │
       ▼         ▼
┌─────────────┐ ┌──────────┐
│Practitioner │ │ Location │
│ .name       │ │ .address │
│ .identifier │ │ .position│
│  (NPI)      │ │  (lat/lng│
│ .qualific.  │ │ .telecom │
└─────────────┘ └──────────┘
```

### 11.3 Da Vinci PAS (Prior Authorization)

```
                    ┌───────────────────────────────────┐
                    │        $submit (Bundle)           │
                    │                                   │
                    │  Claim (preauthorization)         │
                    │   ├── .patient ────▶ Patient      │
                    │   ├── .insurer ────▶ Organization │
                    │   ├── .provider ───▶ Practitioner │
                    │   ├── .insurance                  │
                    │   │     └── .coverage ─▶Coverage  │
                    │   ├── .item[]:                    │
                    │   │     ├── .productOrService     │
                    │   │     ├── .servicedDate         │
                    │   │     └── .location             │
                    │   ├── .diagnosis[]                │
                    │   └── .supportingInfo[]           │
                    └──────────────┬────────────────────┘
                                   │
                                   ▼ (Payer processes)
                    ┌───────────────────────────────────┐
                    │        Response (Bundle)          │
                    │                                   │
                    │  ClaimResponse                    │
                    │   ├── .outcome (complete|queued)  │
                    │   ├── .preAuthRef (AUTH #)        │
                    │   ├── .preAuthPeriod              │
                    │   ├── .item[].reviewAction        │
                    │   │     ├── reasonCode (approved/ │
                    │   │     │    denied/pended)       │
                    │   │     └── number                │
                    │   └── .communicationRequest[]     │
                    │         (if additional info       │
                    │          needed from provider)    │
                    └───────────────────────────────────┘
```

### 11.4 PDex Payer-to-Payer Exchange

```
┌───────────────┐                              ┌───────────────┐
│   New Payer   │                              │   Old Payer   │
│   (Receiver)  │                              │   (Sender)    │
└───────┬───────┘                              └───────┬───────┘
        │                                              │
        │──── $member-match ──────────────────────────▶│
        │     (Patient demographics + old coverage)    │
        │◀─── MemberIdentifier ────────────────────────│
        │                                              │
        │──── GET /Patient/{matched-id} ──────────────▶│
        │◀─── Patient resource ────────────────────────│
        │                                              │
        │──── GET /ExplanationOfBenefit?patient= ─────▶│
        │◀─── EOB Bundle ─────────────────────────────│
        │                                              │
        │──── GET /Condition?patient= ────────────────▶│
        │──── GET /Encounter?patient= ────────────────▶│
        │──── GET /Observation?patient= ──────────────▶│
        │──── GET /MedicationRequest?patient= ────────▶│
        │──── GET /AllergyIntolerance?patient= ───────▶│
        │◀─── Clinical data bundles ──────────────────│
        │                                              │
        │  (OR for bulk: GET /Group/{id}/$export)      │
        │                                              │
```

### 11.5 US Core Clinical Data Model

```
                            ┌──────────────┐
                            │   Patient    │
                            │  (us-core)   │
                            └──────┬───────┘
                                   │
          ┌────────────────────────┼────────────────────────────┐
          │              │         │         │                   │
          ▼              ▼         ▼         ▼                   ▼
┌──────────────┐ ┌────────────┐ ┌────────┐ ┌──────────────┐ ┌─────────┐
│  Condition   │ │MedicationRq│ │Observ. │ │AllergyIntoler│ │Encounter│
│ .code(ICD10) │ │ .medication│ │ .code  │ │ .code        │ │ .type   │
│ .category    │ │ .dosage    │ │ .value │ │ .reaction[]  │ │ .period │
│ .clinicalSta │ │ .status    │ │ .date  │ │ .clinicalSta │ │ .class  │
│ .verific.Sta │ │ .intent    │ │ .cat   │ │ .verific.Sta │ │ .reason │
└──────────────┘ └────────────┘ └────────┘ └──────────────┘ └────┬────┘
                       │                                          │
                       ▼                                          ▼
              ┌──────────────┐                          ┌──────────────┐
              │  Medication  │                          │  Procedure   │
              │ .code(RxNorm)│                          │ .code (CPT)  │
              └──────────────┘                          │ .performed   │
                                                        └──────────────┘

Additional linked resources:
  Patient ──▶ Immunization (.vaccineCode, .occurrenceDateTime)
  Patient ──▶ DiagnosticReport (.code, .result[] → Observation)
  Patient ──▶ DocumentReference (.type, .content[].attachment)
  Patient ──▶ CarePlan (.status, .category, .activity[])
  Patient ──▶ CareTeam (.participant[].member → Practitioner)
  Patient ──▶ Goal (.lifecycleStatus, .target[])
  Any    ──▶ Provenance (.target[], .agent[], .recorded)
```

---

## 12. Validation Checklist

### Pre-Production Validation

| # | Check | Tool/Method |
|---|-------|-------------|
| 1 | JSON schema validity | HAPI Validator / JSON Schema |
| 2 | Profile conformance | `meta.profile` declared & validated |
| 3 | Must-support populated | Check all MS elements when data exists |
| 4 | Terminology bindings | ValueSet membership for coded elements |
| 5 | Reference resolution | All `Reference` targets exist/resolvable |
| 6 | Search parameters work | Test each required search param |
| 7 | Pagination | `Bundle.link.next` returns valid pages |
| 8 | CapabilityStatement | Declares supported resources/operations |
| 9 | SMART endpoints | `.well-known/smart-configuration` valid |
| 10 | Bulk export flow | Kick-off → poll → download → parse NDJSON |
| 11 | Error handling | `OperationOutcome` for all error cases |
| 12 | Inferno test suite | Run applicable IG test suite to completion |

### CMS Compliance Dates (Key Milestones)

| Requirement | Rule | Deadline |
|-------------|------|----------|
| Patient Access API | CMS-9115-F | Jan 1, 2021 (in effect) |
| Provider Directory API | CMS-9115-F | Jan 1, 2021 (in effect) |
| Payer-to-Payer (FHIR) | CMS-0057-F | Jan 1, 2027 |
| Prior Auth API (FHIR) | CMS-0057-F | Jan 1, 2027 |
| Prior Auth decision in 72h (urgent) / 7 days (standard) | CMS-0057-F | Jan 1, 2026 |

### Common Pitfalls

| Issue | Resolution |
|-------|-----------|
| Missing `meta.profile` | Always declare the profile URL in `meta.profile[]` |
| Wrong code system URI | Use exact URIs: `http://www.ama-assn.org/go/cpt`, `http://hl7.org/fhir/sid/icd-10-cm` |
| Identifier without system | Every `identifier` needs both `system` and `value` |
| Reference format mismatch | Use relative references within same server, absolute across servers |
| Missing search `_include` support | Implement for all referenced resources listed in IG |
| Dates without timezone | Use `dateTime` with timezone for timestamps: `2026-07-01T10:00:00-04:00` |
| Bulk export timeout | Implement long-polling; exports can take hours for large populations |
| Scope mismatch | Match SMART scopes exactly to IG requirements |
| Bundle.total missing | Always include `total` in searchset bundles |
| Pagination not implemented | CMS requires working pagination for all search endpoints |

---

## Quick Command Reference

```bash
# Validate a resource against an IG
java -jar validator_cli.jar my-eob.json \
  -ig hl7.fhir.us.carin-bb#2.0.0 \
  -profile http://hl7.org/fhir/us/carin-bb/StructureDefinition/C4BB-ExplanationOfBenefit-Professional-NonClinician

# Run Inferno tests
# (via web UI at https://inferno.healthit.gov or CLI)
bundle exec inferno run --suite carin_for_blue_button \
  --inputs fhir_server=https://your-server.com/fhir

# Generate CapabilityStatement
GET /metadata
Accept: application/fhir+json

# Test SMART discovery
curl https://your-fhir-server.com/.well-known/smart-configuration | jq .

# Test bulk export
curl -H "Authorization: Bearer $TOKEN" \
     -H "Accept: application/fhir+json" \
     -H "Prefer: respond-async" \
     "https://your-fhir-server.com/Group/all/\$export?_type=Patient,ExplanationOfBenefit"
```

---

## Key Code Systems Reference

| System | URI | Used For |
|--------|-----|----------|
| ICD-10-CM | `http://hl7.org/fhir/sid/icd-10-cm` | Diagnoses |
| CPT | `http://www.ama-assn.org/go/cpt` | Procedures/services |
| HCPCS | `http://www.cms.gov/Medicare/Coding/HCPCSReleaseCodeSets` | CMS procedures |
| SNOMED CT | `http://snomed.info/sct` | Clinical terms |
| LOINC | `http://loinc.org` | Lab/observations |
| RxNorm | `http://www.nlm.nih.gov/research/umls/rxnorm` | Medications |
| NDC | `http://hl7.org/fhir/sid/ndc` | Drug products |
| NPI | `http://hl7.org/fhir/sid/us-npi` | Provider identifiers |
| Medicare (MBI) | `http://hl7.org/fhir/sid/us-medicare` | Beneficiary ID |
| NUCC | `http://nucc.org/provider-taxonomy` | Provider specialty |
| Place of Service | `https://www.cms.gov/Medicare/Coding/place-of-service-codes/Place_of_Service_Code_Set` | Service location type |
| Revenue Center | `http://www.nubc.org/RevenueCenterCode` | Facility billing |
| Claim Type | `http://terminology.hl7.org/CodeSystem/claim-type` | Claim categorization |

---

*This guide covers the most critical elements for CMS interoperability. For full specifications, consult the official IG pages at [build.fhir.org](https://build.fhir.org) and [hl7.org/fhir/us](http://hl7.org/fhir/us/).*
