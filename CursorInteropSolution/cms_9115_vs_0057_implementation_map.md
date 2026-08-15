# CMS-9115 vs CMS-0057: Comprehensive Implementation Map

## Executive Summary

This document provides a detailed comparison of the two CMS interoperability final rules — **CMS-9115-F** (2020) and **CMS-0057-F** (2024) — and maps their requirements to the **Abacus/Onyx** technical architecture. CMS-9115-F established the foundation for FHIR-based patient data access; CMS-0057-F expands that foundation significantly with Provider Access, Payer-to-Payer, and Prior Authorization APIs while imposing operational improvements to prior authorization processes.

---

## 1. Rule Scope and Timeline

| Dimension | CMS-9115-F (Interoperability & Patient Access) | CMS-0057-F (Prior Authorization & Payer Data Exchange) |
|-----------|-----------------------------------------------|-------------------------------------------------------|
| **Published** | May 1, 2020 (85 FR 25510) | February 8, 2024 (89 FR 8758) |
| **Short Name** | Interoperability and Patient Access Final Rule | Interoperability and Prior Authorization Final Rule |
| **Legislative Authority** | 21st Century Cures Act; ACA §1311(e)(3) | 21st Century Cures Act; ACA; Medicare Prescription Drug, Improvement & Modernization Act |
| **Primary Goal** | Liberate patient data; establish FHIR API foundation for payer data access | Streamline prior authorization; expand data exchange to providers and between payers |
| **Scope** | Patient-facing data access + Provider Directory | All of CMS-9115 scope + Provider Access, Payer-to-Payer, Prior Auth APIs + PA operational reforms |
| **Estimated Savings** | Not formally quantified at rule level | ~$15 billion over 10 years |
| **Relationship** | Foundational rule | Builds on and enhances CMS-9115-F |

### Impacted Payers (Both Rules)

| Payer Type | CMS-9115-F | CMS-0057-F |
|-----------|:----------:|:----------:|
| Medicare Advantage (MA) organizations | ✅ | ✅ |
| Medicaid Fee-for-Service (FFS) programs | ✅ | ✅ |
| Medicaid managed care plans | ✅ | ✅ |
| CHIP FFS programs | ✅ | ✅ |
| CHIP managed care entities | ✅ | ✅ |
| QHP issuers on FFEs | ✅ | ✅ |
| Stand-alone Dental Plans (SADPs) | ❌ Excluded | ❌ Excluded |

---

## 2. Mandated APIs — Detailed Comparison

### 2.1 Patient Access API

| Attribute | CMS-9115-F | CMS-0057-F Enhancement |
|-----------|-----------|----------------------|
| **Status** | Required (original mandate) | Enhanced with PA data |
| **Data Scope** | Claims & encounter data (incl. cost); USCDI v1 clinical data subset | Adds: Prior authorization requests & decisions (excl. drugs) |
| **User** | Patient / member via third-party apps | Same |
| **Auth Model** | SMART on FHIR (patient-facing, standalone launch) | Same |
| **Bulk Data** | Not applicable | Not applicable |
| **Compliance Date (9115)** | Jan 1, 2021 (QHP: plan years beginning ≥ Jan 1, 2021) | — |
| **Compliance Date (0057 enhancement)** | — | Jan 1, 2027 (PA data addition) |
| **Metrics Reporting** | Not required | Required annually beginning Jan 1, 2026 |

### 2.2 Provider Directory API

| Attribute | CMS-9115-F | CMS-0057-F |
|-----------|-----------|-----------|
| **Status** | Required (original mandate) | Maintained; extended to Medicaid/CHIP FFS |
| **Data Scope** | Provider names, addresses, phone numbers, specialties | Same + pharmacy directory for MA-PD plans |
| **User** | Public (no authentication required) | Same |
| **Auth Model** | None — publicly accessible, no user auth | Same |
| **Bulk Data** | Not applicable | Not applicable |
| **Compliance Date** | Jan 1, 2021 | Ongoing compliance; Medicaid/CHIP FFS added |
| **Update Cadence** | Within 30 calendar days of receiving update | Same |
| **QHP Issuers** | Already required machine-readable format; API not mandated | Same |

### 2.3 Payer-to-Payer Data Exchange

| Attribute | CMS-9115-F (Original) | CMS-0057-F (Replaced/Enhanced) |
|-----------|----------------------|-------------------------------|
| **Status** | Originally mandated as process-based exchange | Replaced with FHIR API requirement |
| **Data Scope (9115)** | USCDI v1 clinical data only | — |
| **Data Scope (0057)** | — | Claims & encounter data (excl. provider remittances & cost-sharing); USCDI; PA info (excl. drugs & denied PAs) |
| **Data Timeframe** | Not specified | Only data with date of service within 5 years of request |
| **User** | Payer (new) on behalf of member | Same — payer-to-payer (B2B) |
| **Auth Model** | Not specified (process-based) | SMART Backend Services (OAuth 2.0 client credentials) |
| **Bulk Data** | Not applicable | Required — FHIR Bulk Data Access |
| **Member Matching** | Not defined | $member-match operation required |
| **Consent Model** | Patient request-based | Patient opt-in with plain-language education |
| **Compliance Date (9115)** | Jan 1, 2022 | Superseded |
| **Compliance Date (0057)** | — | Jan 1, 2027 |

### 2.4 Provider Access API

| Attribute | CMS-0057-F (New) |
|-----------|-----------------|
| **Status** | New — not in CMS-9115-F |
| **Data Scope** | Claims & encounter data (excl. provider remittances & cost-sharing); USCDI; PA information (excl. drugs) |
| **User** | In-network providers with treatment relationship |
| **Auth Model** | SMART on FHIR + Backend Services for bulk |
| **Bulk Data** | Required — FHIR Bulk Data Access |
| **Attribution** | Payer must maintain attribution lists associating patients with providers |
| **Opt-Out** | Patient opt-out with plain-language education |
| **Compliance Date** | Jan 1, 2027 |

### 2.5 Prior Authorization API (ePA)

| Attribute | CMS-0057-F (New) |
|-----------|-----------------|
| **Status** | New — not in CMS-9115-F |
| **Capabilities** | (1) Identify if PA required for item/service; (2) Identify documentation requirements; (3) Submit PA request; (4) Receive PA response (approve/deny/pend) |
| **Scope Exclusion** | Drugs excluded |
| **User** | Providers via EHR/practice management systems |
| **Auth Model** | SMART on FHIR (EHR Launch + Standalone) |
| **Bulk Data** | Not applicable |
| **HIPAA X12 278** | Enforcement discretion — FHIR-only implementation permitted |
| **Decision Timeframes** | 72 hours (urgent); 7 calendar days (standard) |
| **Denial Requirements** | Must include specific reason |
| **Compliance Date** | Jan 1, 2027 (API); Jan 1, 2026 (operational PA reforms) |
| **MIPS/PI Measure** | "Electronic Prior Authorization" attestation starting CY 2027 |

### 2.6 API Summary Matrix

| API | Introduced In | Data Direction | Auth Pattern | Bulk Data | Compliance |
|-----|:------------:|:--------------:|:------------:|:---------:|:----------:|
| Patient Access | CMS-9115 | Payer → Patient | SMART Patient | ❌ | 2021 (base) / 2027 (PA data) |
| Provider Directory | CMS-9115 | Payer → Public | None (public) | ❌ | 2021 |
| Payer-to-Payer | CMS-9115* → CMS-0057 | Payer → Payer | SMART Backend Services | ✅ | 2027 |
| Provider Access | CMS-0057 | Payer → Provider | SMART Backend Services | ✅ | 2027 |
| Prior Authorization | CMS-0057 | Provider ↔ Payer | SMART EHR/Standalone | ❌ | 2027 |

*CMS-9115 established a non-API exchange process; CMS-0057 superseded it with a FHIR API requirement.*

---

## 3. Technical Requirements

### 3.1 Required Standards

| Standard | CMS-9115-F | CMS-0057-F | Notes |
|----------|:----------:|:----------:|-------|
| HL7 FHIR Release 4.0.1 | ✅ Required | ✅ Required | Foundational data model for all APIs |
| USCDI Version 1 | ✅ Required | ✅ (transitioning) | Expiring Jan 1, 2026 per 89 FR 1192 |
| USCDI Version 3 | — | ✅ Required | Successor content standard |
| US Core IG STU 3.1.1 | ✅ Required | ✅ (transitioning) | Expiring Jan 1, 2026 |
| US Core IG STU 6.1.0 | — | ✅ Required | Updated profiles |
| SMART App Launch 1.0.0 | ✅ Required | ✅ (transitioning) | Expiring Jan 1, 2026 |
| SMART App Launch 2.0.0 | — | ✅ Required | Adds Backend Services, PKCE |
| FHIR Bulk Data Access v1.0.0 (STU1) | — | ✅ Required | Provider Access & P2P |
| OpenID Connect Core 1.0 | — | ✅ Required | Identity layer |

### 3.2 Recommended Implementation Guides (CMS-0057-F)

| Implementation Guide | Patient Access | Provider Access | Provider Directory | Payer-to-Payer | Prior Auth |
|---------------------|:--------------:|:---------------:|:------------------:|:--------------:|:----------:|
| CARIN Blue Button IG STU 2.0.0 / 2.1.0 | ✅ | ✅ | — | ✅ | — |
| Da Vinci PDex IG STU 2.0.0 / 2.1.0 | ✅ | ✅ | — | ✅ | — |
| Da Vinci PDex US Drug Formulary STU 2.0.1 | ✅ | — | — | — | — |
| Da Vinci PDex Plan-Net STU 1.1.0 / 1.2.0 | — | — | ✅ | — | — |
| Da Vinci CRD STU 2.0.1 | — | — | — | — | ✅ |
| Da Vinci DTR STU 2.0.0 | — | — | — | — | ✅ |
| Da Vinci PAS STU 2.0.1 | — | — | — | — | ✅ |
| SMART App Launch 2.0.0 (Backend Services) | — | ✅ | — | ✅ | — |

### 3.3 Authentication & Authorization Patterns

| API | Auth Flow | Token Type | Scopes Pattern | Consent |
|-----|-----------|-----------|----------------|---------|
| **Patient Access** | SMART Standalone Launch | Access token (patient context) | `patient/*.read` | Implicit (patient grants access) |
| **Provider Directory** | None | N/A | Public access | None required |
| **Provider Access** | SMART Backend Services (client credentials) | System-level access token | `system/*.read` | Attribution list + patient opt-out |
| **Payer-to-Payer** | SMART Backend Services (client credentials) | System-level access token | `system/*.read` | Patient opt-in |
| **Prior Authorization** | SMART EHR Launch or Standalone | Access token (provider + patient context) | `user/Claim.write`, `user/ClaimResponse.read` | Implicit (provider on behalf of patient) |

### 3.4 Bulk Data Requirements

| Capability | Provider Access API | Payer-to-Payer API |
|-----------|:------------------:|:-----------------:|
| $export (Group-level) | ✅ Required | ✅ Required |
| $member-match | Not required | ✅ Required |
| $bulk-member-match | Recommended | ✅ Recommended |
| NDJSON output format | ✅ | ✅ |
| _since parameter | ✅ Recommended | ✅ Recommended |
| Async request/poll pattern | ✅ | ✅ |
| Kick-off → Status → Download | ✅ | ✅ |

### 3.5 Key FHIR Resources by API

| API | Primary FHIR Resources |
|-----|----------------------|
| Patient Access | Patient, ExplanationOfBenefit, Coverage, Condition, Encounter, Observation, MedicationRequest, Immunization, AllergyIntolerance, Procedure, ClaimResponse |
| Provider Directory | Organization, Practitioner, PractitionerRole, Location, HealthcareService, Endpoint, Network, InsurancePlan |
| Provider Access | Same as Patient Access + Group (attribution) |
| Payer-to-Payer | Same as Patient Access + Group (matched members) |
| Prior Authorization (ePA) | Claim (PA request), ClaimResponse (PA decision), Coverage, Questionnaire, QuestionnaireResponse, CoverageEligibilityRequest/Response |

---

## 4. Compliance Deadlines

### 4.1 CMS-9115-F Timeline (Completed)

| Milestone | Deadline | Status |
|-----------|----------|--------|
| Patient Access API live | January 1, 2021 | ✅ Passed |
| Provider Directory API live | January 1, 2021 | ✅ Passed |
| Payer-to-Payer data exchange (process-based) | January 1, 2022 | ✅ Passed (superseded by CMS-0057) |
| Daily dual-eligible data exchange (MMA files) | April 1, 2022 | ✅ Passed |
| ADT notifications (CoP modification) | May 1, 2021 | ✅ Passed |
| Public reporting of info blocking attestations | Late 2020 | ✅ Passed |

### 4.2 CMS-0057-F Timeline

| Milestone | Deadline | Applies To |
|-----------|----------|-----------|
| **PA operational reforms** (decision timeframes, denial reasons) | **January 1, 2026** | All impacted payers (excl. QHP for timeframes) |
| **Patient Access API metrics reporting** | **January 1, 2026** | All impacted payers |
| **PA metrics public reporting** (initial) | **March 31, 2026** | All impacted payers |
| **Patient Access API** (PA data addition) | **January 1, 2027** | All impacted payers |
| **Provider Access API** | **January 1, 2027** | All impacted payers |
| **Payer-to-Payer API** | **January 1, 2027** | All impacted payers |
| **Prior Authorization API** | **January 1, 2027** | All impacted payers |
| **Electronic PA MIPS measure** | **CY 2027 performance period** | MIPS eligible clinicians |
| **Electronic PA hospital measure** | **CY 2027 EHR reporting period** | Eligible hospitals & CAHs |
| USCDI v1 / US Core 3.1.1 / SMART 1.0.0 expiration | January 1, 2026 | Transitional standards |

### 4.3 Compliance Deadline Summary Visual

```
2020  2021         2022         2023  2024         2025         2026         2027
 |     |            |            |     |            |            |            |
 |     ├─ Patient Access API     |     |            |            |            |
 |     ├─ Provider Directory API |     |            |            |            |
 |     |            ├─ P2P Exchange (process)       |            |            |
 |     |            |            |     |            |            |            |
 |     |            |            |     ├─ CMS-0057 Published    |            |
 |     |            |            |     |            |            |            |
 |     |            |            |     |            |     ├──── PA Ops Reform |
 |     |            |            |     |            |     ├──── API Metrics   |
 |     |            |            |     |            |     |     ├──── ALL APIs |
 |     |            |            |     |            |     |     |   (Jan 2027)|
```

---

## 5. Mapping to Abacus/Onyx System Components

### 5.1 Architecture Overview

The Abacus/Onyx interoperability platform implements CMS rules through two distinct flows:

1. **Data Pipeline (Abacus-led):** Raw Data → Ingestion → FM (Foundational Marts) → SAM (Subject Area Marts) → FHIR Bundles → FHIR Store
2. **Runtime API Access (Onyx-led):** Consumer App → SLAP (auth) → FITE (gateway) → FHIR Store → Response

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        DATA PIPELINE (Abacus-Led)                                │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  Payer Systems ──► Raw Ingestion ──► Foundational    ──► Subject Area ──► FHIR  │
│  (Claims, PVD,     (Validate,        Marts (FM)         Marts (SAM)     Store   │
│   Clinical,         Normalize,       (Canonical,        (IG-aligned)    (Firely │
│   Formulary,        DQ Rules)         Non-FHIR)                         or HL)  │
│   Prior Auth)                                                                    │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│                      RUNTIME API ACCESS (Onyx-Led)                                │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  Consumer App ──► SLAP ──► FITE ──► FHIR Store ──► Response                     │
│  (Member App,    (Auth/    (FHIR    (Firely or     (FHIR Bundle /                │
│   Provider App,   OAuth2/   Gate-    HealthLake)    OperationOutcome)             │
│   Payer System)   SMART)    way)                                                 │
│                                                                                  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Component Responsibilities

| Component | Owner | Role | CMS Relevance |
|-----------|-------|------|---------------|
| **SLAP** (SMART Launch Authentication Proxy) | Onyx | OAuth 2.0 / SMART on FHIR authentication; token issuance; scope validation; patient/provider context binding | Enforces CMS auth requirements; consent; SMART scopes |
| **FITE** (FHIR Integration & Transformation Engine) | Onyx | FHIR gateway/proxy; IG-specific endpoint enforcement; request routing; response shaping | Ensures API responses are IG-compliant; exposes CMS-mandated endpoints |
| **Firely Server** | Shared (Abacus operates, Onyx configures) | FHIR R4 data store; resource persistence; search; validation; SMART auth support | Primary FHIR repository for clients using on-premise/self-managed deployment |
| **AWS HealthLake** | Shared (Abacus operates) | Managed FHIR R4 data store; CMS interoperability endpoints; CloudWatch metrics; $bulk-member-match | Managed FHIR repository with built-in CMS compliance tracking |
| **FM (Foundational Marts)** | Abacus | Canonical data model; validated & normalized payer data; NOT FHIR-shaped | Upstream source of truth; optimized for correctness & incremental updates |
| **SAM (Subject Area Marts)** | Abacus (with Onyx IG guidance) | IG-aligned staging tables; bridge between FM and FHIR; domain-specific naming (e.g., `cms0057_claim_eob_outpatient`) | Directly maps to CMS-0057 API data requirements per IG |
| **Databricks Workflows** | Abacus | ETL orchestration; FM→SAM transform; SAM→CSV extract; FHIR bundle generation; load to FHIR store | Powers the data pipeline; workflow families per domain |
| **Developer Portal** | Onyx | API documentation; app registration; sandbox access | Payer obligation to provide developer resources |

### 5.3 CMS API → Component Mapping

#### Patient Access API

| Layer | Component | Function |
|-------|-----------|----------|
| Data Ingestion | Abacus Ingestion → FM | Ingest claims, clinical, formulary data |
| Data Transformation | FM → SAM | Transform to CARIN BB, US Core, Formulary, PDex profiles |
| FHIR Loading | SAM → FHIR Store | Generate FHIR Bundles; upsert to Firely/HealthLake |
| Authentication | **SLAP** | SMART Standalone Launch; patient OAuth2 flow; token with patient scopes |
| API Gateway | **FITE** | Route patient requests; enforce read-only; filter by patient context |
| Data Store | **Firely** or **HealthLake** | Persist & serve Patient, EOB, Coverage, Condition, Observation, etc. |
| CMS Tracking | HealthLake `/patientaccess/v2/r4` | Automatic CloudWatch metrics for compliance reporting |
| SAM Tables | `cms0057_claim_eob_*`, `cms0057_clinical_*`, `cms0057_formulary_*` | Claims, clinical, formulary data aligned to CARIN/US Core/Formulary IGs |

#### Provider Directory API

| Layer | Component | Function |
|-------|-----------|----------|
| Data Ingestion | Abacus Ingestion → Provider FM | Ingest provider network data |
| Data Transformation | Provider FM → SAM | Transform to Da Vinci Plan-Net profiles |
| FHIR Loading | SAM → FHIR Store | Generate Organization, Practitioner, Location, etc. |
| Authentication | **None** | Public-facing, no auth required |
| API Gateway | **FITE** (public instance) | Public endpoint; no security protocols |
| Data Store | **Firely** (unsecured instance) or **HealthLake** | Serve provider directory resources |
| Update Cadence | Databricks workflow | Must update within 30 days of source change |
| SAM Tables | `cms0057_provider_location`, `cms0057_provider_*` | Plan-Net IG aligned |

#### Provider Access API

| Layer | Component | Function |
|-------|-----------|----------|
| Data Ingestion | Same as Patient Access | Claims, clinical, PA data |
| Data Transformation | FM → SAM | Same profiles as Patient Access + Group/attribution |
| FHIR Loading | SAM → FHIR Store | Same as Patient Access |
| Authentication | **SLAP** | SMART Backend Services (client credentials); provider org identity |
| Authorization | **SLAP** + FITE | Attribution list validation; opt-out enforcement; TIN/NPI-based access policies |
| API Gateway | **FITE** | Bulk Data $export; Group-level export; individual resource access |
| Data Store | **Firely** or **HealthLake** | Serve bulk NDJSON + individual resources |
| CMS Tracking | HealthLake `/provideraccess/v2/r4` | Automatic metrics |
| SAM Tables | Same as Patient Access + attribution tables | Plus member-provider attribution |

#### Payer-to-Payer API

| Layer | Component | Function |
|-------|-----------|----------|
| Data Ingestion | Same as Patient Access | Claims, clinical, PA data |
| Data Transformation | FM → SAM | Same profiles; 5-year data window filter |
| FHIR Loading | SAM → FHIR Store | Same as Patient Access |
| Authentication | **SLAP** | SMART Backend Services; payer org-to-org trust |
| Member Matching | **FITE** + **HealthLake** | $member-match / $bulk-member-match operation |
| Consent | **SLAP** | Patient opt-in verification |
| API Gateway | **FITE** | Bulk Data $export for matched members; dynamic access policies |
| Data Store | **Firely** or **HealthLake** | Serve matched member data |
| CMS Tracking | HealthLake `/payertopayerdx/v2/r4` | Automatic metrics |
| Update Cadence | Databricks workflow | Within 1 business day of data availability |
| SAM Tables | Same as Patient Access | Filtered by 5-year window |

#### Prior Authorization API (ePA)

| Layer | Component | Function |
|-------|-----------|----------|
| Coverage Requirements | Onyx (CQL rules engine) | CRD: Identify if PA required; documentation requirements |
| Documentation Gather | Onyx (DTR) | FHIR Questionnaire + CQL rules for documentation capture |
| PA Submission | **FITE** | PAS: Accept Claim resource (PA request) from provider EHR |
| PA Adjudication | Backend UM system (via FITE) | Process request; return ClaimResponse (approve/deny/pend) |
| Authentication | **SLAP** | SMART EHR Launch; provider + patient context |
| API Gateway | **FITE** | Route CRD hooks, DTR Questionnaires, PAS Claim/ClaimResponse |
| X12 Translation | Backend (Abacus/payer) | Optional: translate FHIR→X12 278 for legacy UM systems |
| CMS Tracking | HealthLake `/priorauthservice/v2/r4` | Automatic metrics |
| Data Store | **Firely** or **HealthLake** | Persist PA decisions as ClaimResponse |
| SAM Tables | `cms0057_prior_auth_*` | PA-specific data for exposure via other APIs |

### 5.4 Component × CMS Rule Matrix

| Component | CMS-9115-F Role | CMS-0057-F Role |
|-----------|----------------|-----------------|
| **SLAP** | Patient Access OAuth2; SMART scopes | + Backend Services for Provider Access & P2P; ePA EHR Launch; consent enforcement (opt-in/opt-out) |
| **FITE** | Patient Access gateway; Provider Directory (public) | + Provider Access bulk export; P2P bulk export; $member-match routing; ePA (CRD hooks, DTR, PAS) |
| **Firely Server** | FHIR R4 storage for Patient Access & Provider Directory | + All CMS-0057 APIs; bulk data export; member-match |
| **AWS HealthLake** | FHIR R4 storage (alternative to Firely) | + CMS interoperability endpoints with CloudWatch metrics; $bulk-member-match; compliance reporting |
| **FM (Foundational Marts)** | Source for claims, clinical, provider data | + Prior auth data; expanded clinical (USCDI v3) |
| **SAM Tables** | IG-aligned staging for CARIN BB, Plan-Net, US Core | + CMS-0057 specific tables (PA, attribution, expanded claims); versioned per IG update |
| **Databricks Workflows** | Workflow families: Claims, Clinical, PVD, Formulary, CMS-9115 | + CMS-0057 family; incremental PA data; attribution list management; 1-day P2P freshness |
| **Developer Portal** | API documentation for Patient Access & Provider Directory | + Provider Access, P2P, ePA documentation; sandbox for all 5 APIs |

### 5.5 Firely vs HealthLake — Decision Matrix for CMS Compliance

| Capability | Firely Server | AWS HealthLake |
|-----------|:-------------:|:--------------:|
| FHIR R4 native | ✅ | ✅ |
| SMART on FHIR support | ✅ (via Firely Auth) | ✅ (via SMART datastores) |
| US Core validation | ✅ | ✅ |
| Bulk Data $export | ✅ | ✅ |
| $member-match | Custom implementation | ✅ Native support |
| $bulk-member-match | Custom implementation | ✅ Native support |
| CMS interoperability endpoints (categorized tracking) | ❌ Custom needed | ✅ Built-in (/patientaccess, /provideraccess, /payertopayerdx, /priorauthservice) |
| CloudWatch metrics (URIType, Sub, ClientId) | ❌ | ✅ Automatic |
| CMS compliance reporting | Manual/custom | ✅ Native CloudWatch integration |
| Multi-tenant support | ✅ (self-managed) | ✅ (managed) |
| Self-hosted / on-premise | ✅ | ❌ (AWS only) |
| Managed service (no ops) | ❌ | ✅ |
| MongoDB backend | ✅ | ❌ |
| Custom validation plugins | ✅ (extensible) | Limited |

### 5.6 SAM Table Naming Convention & Domain Mapping

| SAM Domain | CMS Rule | API(s) Served | Example Table Names |
|-----------|----------|---------------|-------------------|
| Claims EOB | Both | Patient Access, Provider Access, P2P | `cms0057_claim_eob_inpatient`, `cms0057_claim_eob_outpatient`, `cms0057_claim_eob_pharmacy` |
| Clinical | Both | Patient Access, Provider Access, P2P | `cms0057_clinical_condition`, `cms0057_clinical_observation`, `cms0057_clinical_encounter` |
| Provider Directory | CMS-9115 | Provider Directory | `cms0057_provider_location`, `cms0057_provider_organization`, `cms0057_provider_practitioner` |
| Formulary | Both | Patient Access | `cms0057_formulary_item`, `cms0057_formulary_plan` |
| Prior Authorization | CMS-0057 | Patient Access, Provider Access, P2P, ePA | `cms0057_prior_auth_request`, `cms0057_prior_auth_decision` |
| Enrollment/Coverage | Both | Patient Access, P2P | `cms0057_enrollment_coverage` |
| Attribution | CMS-0057 | Provider Access | `cms0057_attribution_group`, `cms0057_attribution_member` |

---

## 6. Key Differences Summary

### 6.1 What CMS-9115-F Established (Foundation)

- ✅ Patient Access API (FHIR R4 + SMART on FHIR)
- ✅ Provider Directory API (public, no auth)
- ✅ Payer-to-Payer exchange (process-based, not API-based)
- ✅ FHIR R4.0.1 as foundational standard
- ✅ USCDI v1 as content standard
- ✅ ADT event notifications (hospital CoPs)
- ✅ Digital contact information in NPPES

### 6.2 What CMS-0057-F Added (Expansion)

- 🆕 Provider Access API (bulk + individual)
- 🆕 Payer-to-Payer API (FHIR-based, replaces process)
- 🆕 Prior Authorization API (CRD + DTR + PAS workflow)
- 🆕 PA operational reforms (72hr/7day decisions, denial reasons)
- 🆕 PA metrics public reporting
- 🆕 Patient Access API metrics reporting
- 🆕 MIPS/PI Electronic PA measure
- 🆕 USCDI v3 + US Core 6.1.0 + SMART 2.0.0 requirements
- 🆕 Bulk Data Access requirement
- 🆕 $member-match for P2P
- 🆕 HIPAA X12 278 enforcement discretion (FHIR-only permitted)
- 🆕 Backend Services authorization pattern

### 6.3 Implementation Complexity Comparison

| Dimension | CMS-9115-F | CMS-0057-F |
|-----------|:----------:|:----------:|
| Number of APIs | 2 (Patient Access + Provider Directory) | 5 (all APIs) |
| Auth patterns | 1 (SMART Patient) | 3 (Patient, Backend Services, EHR Launch) |
| Bulk data required | No | Yes (2 APIs) |
| New FHIR operations | None | $member-match, $export, CDS Hooks |
| IG complexity | Low (CARIN BB, Plan-Net) | High (+ PDex, CRD, DTR, PAS, Formulary) |
| B2B trust model | None | Required (P2P, Provider Access) |
| Consent models | Implicit | Opt-in (P2P) + Opt-out (Provider Access) |
| Real-time requirements | None | CRD hooks (synchronous), PAS (near-real-time) |
| Workflow integration | None | EHR workflow (CDS Hooks, SMART Launch) |

---

## 7. Implementation Roadmap Recommendations

### Phase 1: Foundation Compliance (Already Completed — CMS-9115-F)
- [x] Patient Access API with SMART on FHIR
- [x] Provider Directory API (public)
- [x] SLAP → FITE → Firely/HealthLake pipeline operational
- [x] FM → SAM → FHIR data pipeline for claims, clinical, provider, formulary

### Phase 2: CMS-0057-F Operational Reforms (Due Jan 1, 2026 ✅ PASSED)
- [x] PA decision timeframes (72hr/7day)
- [x] Denial reason specificity
- [x] Patient Access API metrics collection & reporting
- [x] PA metrics public reporting (March 31, 2026)

### Phase 3: CMS-0057-F API Delivery (Due Jan 1, 2027)
- [ ] **Provider Access API** — SLAP Backend Services + FITE bulk export + attribution management
- [ ] **Payer-to-Payer API** — $member-match + bulk export + opt-in consent + 5-year window + 1-day freshness
- [ ] **Prior Authorization API** — CRD hooks + DTR questionnaires + PAS submission/response
- [ ] **Patient Access API enhancement** — PA data via existing Patient Access endpoint
- [ ] Standards migration: USCDI v3, US Core 6.1.0, SMART 2.0.0

### Phase 4: Ongoing Compliance & Optimization
- [ ] Annual metrics reporting
- [ ] IG version management (track ONC-approved updates)
- [ ] Performance tuning for bulk data at scale
- [ ] CMS-0062-P readiness (2026 proposed rule — drugs)

---

## 8. References

| Resource | URL |
|----------|-----|
| CMS-9115-F Final Rule | https://www.cms.gov/interoperability/policies-and-regulations/cms-interoperability-and-patient-access-final-rule-cms-9115-f |
| CMS-0057-F Final Rule | https://www.cms.gov/initiatives/burden-reduction/overview/interoperability/policies-regulations/cms-interoperability-prior-authorization-final-rule-cms-0057-f |
| CMS-0057-F Fact Sheet | https://www.cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f |
| APIs & IGs Reference | https://www.cms.gov/priorities/burden-reduction/overview/interoperability/implementation-guides-standards/application-programming-interfaces-apis-relevant-standards-implementation-guides-igs |
| AWS HealthLake CMS Compliance | https://docs.aws.amazon.com/healthlake/latest/devguide/reference-compliance-cms.html |
| Firely Server CMS-0057 Compliance | https://docs.fire.ly/projects/Firely-Server/en/latest/compliance/cms.html |
| Federal Register (CMS-0057-F) | https://www.federalregister.gov/documents/2024/02/08/2024-00895 |
| Abacus Help Center — InterOperability with Onyx | https://abacusinsights.atlassian.net/servicedesk/customer/portal/7/article/5423071246 |

---

*Document generated: July 7, 2026*
*Artifact #4 of the InterOp with Onyx Engineering Implementation project*
