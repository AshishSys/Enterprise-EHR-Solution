# Onyx Component Ownership Matrix

## Artifact #2 — Interoperability Platform Component Ownership & Responsibility Mapping

**Document Version:** 2.0
**Last Updated:** 2026-07-07
**Classification:** Internal — Engineering & Operations
**Scope:** Full component inventory across Abacus and Onyx teams for CMS Interoperability Platform

---

## 1. Full Component Inventory

### 1.1 Platform Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        INTEROPERABILITY PLATFORM                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌──────────────┐  │
│  │   INGEST    │   │  TRANSFORM  │   │    SERVE    │   │   MONITOR    │  │
│  ├─────────────┤   ├─────────────┤   ├─────────────┤   ├──────────────┤  │
│  │ SLAP        │   │ Databricks  │   │ Firely      │   │ Onyx Insights│  │
│  │ FITE        │   │ FM Pipeline │   │ HealthLake  │   │ CloudWatch   │  │
│  │ Extract     │   │ SAM Pipeline│   │ Dev Portal  │   │ PagerDuty    │  │
│  │ MongoDB     │   │ MDP         │   │ IAM/Auth    │   │ Dashboards   │  │
│  └─────────────┘   └─────────────┘   └─────────────┘   └──────────────┘  │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    SHARED INFRASTRUCTURE                             │   │
│  │  Config/SSM │ CI/CD (Seiji) │ IAM │ Networking │ Secrets Mgmt      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Component Registry

| # | Component | Category | Environment(s) | Technology Stack | Criticality |
|---|-----------|----------|----------------|-----------------|-------------|
| 1 | SLAP (Standardized Lakehouse Acceleration Platform) | Ingestion | Dev, Stage, Prod | Databricks, Spark, Delta Lake | P1 — Critical |
| 2 | FITE (FHIR Interoperability Transform Engine) | Transformation | Dev, Stage, Prod | Databricks, Python, Spark | P1 — Critical |
| 3 | Firely Server | FHIR Store/API | Dev, Stage, Prod | .NET, FHIR R4, SQL Server | P1 — Critical |
| 4 | AWS HealthLake | FHIR Store (Backup/Secondary) | Dev, Stage, Prod | AWS Managed, FHIR R4 | P2 — High |
| 5 | MongoDB | Operational Data Store | Dev, Stage, Prod | MongoDB Atlas / DocumentDB | P1 — Critical |
| 6 | Onyx Insights | Analytics & Monitoring | Dev, Stage, Prod | Custom Python, React, Grafana | P2 — High |
| 7 | MDP (Master Data Platform) | Reference Data | Dev, Stage, Prod | Databricks, Delta Lake | P1 — Critical |
| 8 | Databricks Workflows | Orchestration | Dev, Stage, Prod | Databricks Jobs, Airflow | P1 — Critical |
| 9 | FM Pipelines (FHIR Mapping) | Transformation | Dev, Stage, Prod | Python, Spark, Liquid Templates | P1 — Critical |
| 10 | SAM Pipelines (Standardized Analytical Models) | Analytics | Dev, Stage, Prod | Databricks, SQL, Python | P2 — High |
| 11 | Extract Tasks | Data Extraction | Dev, Stage, Prod | Python, JDBC, APIs, SFTP | P1 — Critical |
| 12 | FHIR Load/Upsert | Data Loading | Dev, Stage, Prod | Python, FHIR Client, Bulk API | P1 — Critical |
| 13 | Developer Portal | API Management | Dev, Stage, Prod | React, Node.js, API Gateway | P2 — High |
| 14 | Config/SSM (Parameter Store) | Configuration | All | AWS SSM, Secrets Manager | P1 — Critical |
| 15 | IAM/Auth Layer | Security | All | OAuth 2.0, SMART on FHIR, Cognito | P1 — Critical |
| 16 | Monitoring/Alerting | Observability | All | CloudWatch, Datadog, PagerDuty | P2 — High |
| 17 | CI/CD (Seiji) | Deployment | All | Seiji, GitHub Actions, Terraform | P2 — High |

---

## 2. Ownership Matrix Table

### 2.1 Primary Ownership Matrix

| Component | Owner | Primary Responsibility | Key Dependencies | Upstream Interfaces | Downstream Interfaces | Deployment Method | On-Call Team |
|-----------|-------|----------------------|------------------|--------------------|-----------------------|-------------------|--------------|
| **SLAP** | Abacus | Raw data ingestion, schema validation, Bronze layer creation | Extract Tasks, Config/SSM, Databricks Workflows | Source systems (claims, eligibility, provider files) | FITE, MDP, Bronze Delta tables | Seiji → Databricks Deploy | Abacus Data Engineering |
| **FITE** | Abacus | FHIR resource transformation, Silver/Gold layer mapping | SLAP (Bronze), MDP (reference), FM Pipelines | Bronze/Silver Delta tables, MDP lookups | FHIR Load/Upsert, SAM Pipelines | Seiji → Databricks Deploy | Abacus Data Engineering |
| **Firely Server** | Onyx | FHIR R4 API serving, resource storage, search, validation | FHIR Load/Upsert, IAM/Auth, HealthLake (failover) | FHIR Load/Upsert (Bundle POST), Bulk Import | Developer Portal, Patient/Provider Apps, Payer Partners | Seiji → ECS/EKS Deploy | Onyx Platform Engineering |
| **AWS HealthLake** | Onyx | Secondary FHIR store, analytics queries, backup | Firely (sync), IAM/Auth | Firely sync replication, Direct FHIR Load | Analytics queries, Compliance reporting | Terraform (IaC) | Onyx Platform Engineering |
| **MongoDB** | Shared | Operational metadata, job state, config cache, audit logs | SLAP, FITE, Extract Tasks, Onyx Insights | All pipeline components (write metadata) | Onyx Insights (read), Alerting (triggers) | Seiji → Atlas/DocumentDB | Abacus (schema), Onyx (infra) |
| **Onyx Insights** | Onyx | Platform analytics, SLA dashboards, data quality scoring | MongoDB, Firely, Databricks, CloudWatch | All platform telemetry, FHIR store metrics | Dashboards, Alert triggers, Compliance reports | Seiji → ECS Deploy | Onyx Analytics |
| **MDP** | Abacus | Reference/master data: code sets, provider directory, member crosswalks | External reference sources, Config/SSM | NPI Registry, CMS code sets, Payer enrollment | FITE (lookups), FM Pipelines, SAM Pipelines | Seiji → Databricks Deploy | Abacus Data Engineering |
| **Databricks Workflows** | Shared | Job orchestration, scheduling, dependency management, retries | All pipeline components, Config/SSM | Triggers (schedule, event, API), Config/SSM | SLAP, FITE, FM, SAM, Extract, Load tasks | Seiji → Databricks API | Abacus (job logic), Onyx (platform) |
| **FM Pipelines** | Abacus | FHIR resource mapping logic, Liquid templates, conformance | FITE (transformed data), MDP (code mappings) | Silver/Gold Delta tables | FHIR Load/Upsert (FHIR Bundles) | Seiji → Databricks Deploy | Abacus Clinical Engineering |
| **SAM Pipelines** | Abacus | Analytical model execution, quality measures, risk scores | FITE (Gold layer), MDP, Databricks Workflows | Gold Delta tables, MDP reference | Onyx Insights, Reporting, downstream analytics | Seiji → Databricks Deploy | Abacus Analytics |
| **Extract Tasks** | Abacus | Source system connectivity, data extraction, file processing | Source systems, Config/SSM (credentials), SFTP | Source DBs, APIs, SFTP servers, S3 drops | SLAP (raw files/tables to Bronze) | Seiji → Lambda/ECS Deploy | Abacus Data Engineering |
| **FHIR Load/Upsert** | Shared | FHIR Bundle creation, conditional upserts, bulk operations | FM Pipelines (output), Firely (target), IAM/Auth | FM Pipeline output (FHIR JSON/Bundles) | Firely Server, HealthLake | Seiji → ECS/Lambda Deploy | Abacus (logic), Onyx (connectivity) |
| **Developer Portal** | Onyx | API documentation, sandbox, key management, rate limiting | Firely, IAM/Auth, API Gateway | Firely (proxied APIs), Auth tokens | External developers, Partner payers, Providers | Seiji → S3/CloudFront + ECS | Onyx Platform Engineering |
| **Config/SSM** | Shared | Centralized configuration, secrets, feature flags | AWS SSM, Secrets Manager | All components (read config) | All components (provide config) | Terraform (IaC) | Onyx (infra), Abacus (app config) |
| **IAM/Auth Layer** | Onyx | OAuth 2.0 flows, SMART on FHIR, token validation, scopes | Cognito, Firely, Developer Portal | User/app auth requests | All API-serving components (token validation) | Seiji → Cognito/Lambda Deploy | Onyx Security Engineering |
| **Monitoring/Alerting** | Shared | Metrics collection, log aggregation, alerting, dashboards | CloudWatch, Datadog, PagerDuty, all components | All components (emit metrics/logs) | PagerDuty (alerts), Onyx Insights (feeds) | Terraform + Seiji | Onyx (infra), Abacus (app alerts) |
| **CI/CD (Seiji)** | Shared | Build, test, deploy automation; environment promotion | GitHub, Terraform, Databricks API, ECS/EKS | Developer commits, PR merges | All deployment targets | Self-managed (bootstrap) | Onyx DevOps |

### 2.2 Ownership Summary by Team

| Team | Components Owned (Primary) | Components Shared |
|------|---------------------------|-------------------|
| **Abacus** | SLAP, FITE, MDP, FM Pipelines, SAM Pipelines, Extract Tasks | MongoDB (schema), Databricks Workflows (job logic), FHIR Load/Upsert (logic), Config/SSM (app config), Monitoring (app alerts) |
| **Onyx** | Firely, HealthLake, Onyx Insights, Developer Portal, IAM/Auth Layer | MongoDB (infra), Databricks Workflows (platform), FHIR Load/Upsert (connectivity), Config/SSM (infra), Monitoring (infra), CI/CD (Seiji) |

### 2.3 RACI by Component

| Component | Abacus | Onyx | Notes |
|-----------|--------|------|-------|
| SLAP | R, A | C, I | Abacus owns all ingestion logic |
| FITE | R, A | C, I | Abacus owns transformation; Onyx consulted on FHIR conformance |
| Firely | C, I | R, A | Onyx owns; Abacus consulted on resource requirements |
| HealthLake | I | R, A | Fully Onyx managed |
| MongoDB | R (schema) | R (infra), A | Shared — split by domain |
| Onyx Insights | C | R, A | Onyx owns; Abacus provides pipeline telemetry |
| MDP | R, A | I | Abacus owns all reference data |
| Databricks Workflows | R (jobs) | R (platform), A | Shared orchestration |
| FM Pipelines | R, A | C | Abacus owns mapping logic |
| SAM Pipelines | R, A | I | Abacus owns analytical models |
| Extract Tasks | R, A | I | Abacus owns source connectivity |
| FHIR Load/Upsert | R (logic), A | R (infra) | Shared — Abacus writes bundles, Onyx manages connectivity |
| Developer Portal | I | R, A | Onyx owns external API experience |
| Config/SSM | R (app) | R (infra), A | Shared — Onyx manages platform, Abacus manages app params |
| IAM/Auth | C | R, A | Onyx owns; Abacus defines scope requirements |
| Monitoring/Alerting | R (app) | R (infra), A | Shared — each team owns their alert definitions |
| CI/CD (Seiji) | C | R, A | Onyx owns pipeline; both teams define deploy specs |

*R = Responsible, A = Accountable, C = Consulted, I = Informed*

---

## 3. Data Flow Ownership

### 3.1 End-to-End Data Flow Ownership Map

```
Source Systems → [Extract] → Raw → [SLAP] → Bronze → [FITE] → Silver → [FITE] → Gold → [FM] → FHIR Bundles → [Load] → FHIR Store → [API] → Response
     │              │         │       │         │        │         │       │        │         │          │         │        │         │
     ▼              ▼         ▼       ▼         ▼        ▼         ▼       ▼        ▼         ▼          ▼         ▼        ▼         ▼
  External       Abacus    Abacus  Abacus    Abacus   Abacus    Abacus  Abacus   Abacus    Shared      Onyx      Onyx     Onyx      Onyx
```

### 3.2 Detailed Stage Ownership

| Stage | Layer | Owner | Responsibility | Quality Gate | SLA |
|-------|-------|-------|----------------|--------------|-----|
| **Source Extraction** | Raw (Landing) | Abacus | Connect to source, extract, land in S3/Delta | File integrity checks, row counts | Extract completes within 2hr window |
| **Raw → Bronze** | Bronze | Abacus (SLAP) | Schema inference, dedup, type casting, partitioning | Schema validation, null checks, freshness | < 30 min after extract |
| **Bronze → Silver** | Silver | Abacus (FITE) | Business rules, cleansing, conformance, joins | Data quality scores ≥ 95%, referential integrity | < 1 hr after Bronze |
| **Silver → Gold** | Gold | Abacus (FITE) | Aggregation, enrichment, analytics-ready views | Completeness checks, business rule validation | < 1 hr after Silver |
| **Gold → FM (FHIR Mapping)** | FHIR Resources | Abacus (FM Pipeline) | Map Gold records to FHIR R4 resources, apply Liquid templates | FHIR validation (structure/terminology), conformance % ≥ 99% | < 2 hr after Gold |
| **SAM Execution** | Analytical | Abacus (SAM Pipeline) | Run analytical models, quality measures, risk stratification | Model accuracy thresholds, drift detection | Per schedule (daily/weekly) |
| **FHIR Load/Upsert** | Load | Shared (Abacus logic, Onyx infra) | Bundle POST, conditional upserts, conflict resolution | Load success rate ≥ 99.5%, zero data loss | < 1 hr after FM completion |
| **FHIR Store** | Serve | Onyx (Firely/HealthLake) | Persist resources, index for search, maintain versioning | Storage integrity, version consistency | 99.9% availability |
| **API Response** | Serve | Onyx (Firely + Dev Portal) | Serve FHIR API requests, enforce auth, rate limiting | Response time p95 < 500ms, error rate < 0.1% | 99.9% uptime, < 500ms p95 |

### 3.3 Data Quality Ownership

| Quality Dimension | Primary Owner | Secondary Owner | Measurement |
|-------------------|---------------|-----------------|-------------|
| Completeness (source) | Abacus | — | % of expected records received |
| Accuracy (transformation) | Abacus | — | Validation rule pass rate |
| Conformance (FHIR) | Abacus (FM) | Onyx (validation) | FHIR validator error count |
| Timeliness (end-to-end) | Shared | — | Time from source to API availability |
| Availability (API) | Onyx | — | Uptime %, error rate |
| Consistency (cross-resource) | Abacus | Onyx | Referential integrity checks |

### 3.4 Handoff Points & Contracts

| Handoff | From | To | Contract | Validation |
|---------|------|----|----------|------------|
| Extract → SLAP | Abacus (Extract) | Abacus (SLAP) | Files in agreed S3 prefix, manifest file present | Manifest row count matches file count |
| SLAP → FITE | Abacus (SLAP) | Abacus (FITE) | Bronze tables in Delta Lake, schema registered | Schema registry validation |
| FITE → FM | Abacus (FITE) | Abacus (FM) | Gold tables available, quality score ≥ threshold | Quality gate check before FM trigger |
| FM → FHIR Load | Abacus (FM) | Shared (Load) | Valid FHIR Bundles in output path | FHIR validation pre-load |
| FHIR Load → Firely | Shared (Load) | Onyx (Firely) | Bundle POST via FHIR API, auth token | HTTP 2xx response, OperationOutcome check |
| Firely → Developer Portal | Onyx (Firely) | Onyx (Dev Portal) | FHIR R4 API endpoints available | Health check, search parameter availability |

---

## 4. API Ownership by CMS Mandate

### 4.1 CMS Interoperability Rule Coverage

| CMS Mandate | Rule Reference | Compliance Deadline | Overall Owner | Status |
|-------------|---------------|--------------------:|---------------|--------|
| Patient Access API | CMS-9115-F, §2 | Active (enforced) | Onyx (API) + Abacus (Data) | ✅ Live |
| Provider Access API | CMS-0057-F, §3 | 2026-01-01 | Onyx (API) + Abacus (Data) | ✅ Live |
| Payer-to-Payer (P2P) | CMS-0057-F, §4 | 2026-01-01 | Shared | 🟡 Phase 2 |
| Prior Authorization (ePA) | CMS-0057-F, §5 | 2026-01-01 | Onyx (API) + Abacus (Workflow) | ✅ Live |
| Provider Directory | CMS-9115-F, §4 | Active (enforced) | Abacus (Data) + Onyx (API) | ✅ Live |

### 4.2 Detailed API Ownership Breakdown

#### Patient Access API

| Layer | Component | Owner | Responsibility |
|-------|-----------|-------|----------------|
| Data Sourcing | Claims, Encounters, Clinical Data | Abacus | Extract from adjudication/clinical systems |
| Transformation | FHIR mapping (ExplanationOfBenefit, Condition, Procedure, etc.) | Abacus (FM Pipeline) | Map to US Core / CARIN profiles |
| FHIR Store | Resource persistence & indexing | Onyx (Firely) | Store, version, index resources |
| Authentication | OAuth 2.0 / SMART on FHIR | Onyx (IAM/Auth) | Member-facing auth flows |
| API Serving | RESTful FHIR endpoints | Onyx (Firely + Dev Portal) | Serve /Patient, /ExplanationOfBenefit, /Coverage, etc. |
| Third-Party App Registration | Developer onboarding | Onyx (Developer Portal) | App registration, sandbox, prod access |
| Consent Management | Member consent tracking | Onyx (IAM/Auth) | Consent enforcement on API responses |

#### Provider Access API

| Layer | Component | Owner | Responsibility |
|-------|-----------|-------|----------------|
| Data Sourcing | Claims, Prior Auth, Encounters | Abacus | Extract and prepare provider-attributed data |
| Transformation | FHIR mapping (all resource types) | Abacus (FM Pipeline) | Map to Da Vinci PDex profiles |
| Attribution Logic | Provider-patient attribution | Abacus (SAM Pipeline) | Determine which data to surface per provider |
| FHIR Store | Resource persistence | Onyx (Firely) | Store with provider-scoped access |
| Authentication | OAuth 2.0 / SMART Backend Services | Onyx (IAM/Auth) | Provider system auth (client credentials) |
| API Serving | Bulk FHIR export, RESTful endpoints | Onyx (Firely + Dev Portal) | Serve $export, individual reads |
| Access Control | Scope enforcement | Onyx (IAM/Auth) | Ensure providers see only attributed patients |

#### Payer-to-Payer (P2P)

| Layer | Component | Owner | Responsibility |
|-------|-----------|-------|----------------|
| Outbound Data Assembly | Member history compilation | Abacus (FITE + FM) | Compile 5-year claims history per member |
| Outbound API | FHIR Bulk Export to requesting payer | Onyx (Firely) | Serve P2P export endpoints |
| Inbound Receipt | Receive data from prior payer | Onyx (Firely) | Accept inbound FHIR bundles |
| Inbound Processing | Validate, transform, store inbound data | Abacus (SLAP + FITE) | Process received payer data into pipeline |
| Consent/Opt-Out | Member opt-out tracking | Shared | Abacus (data), Onyx (enforcement) |
| Partner Connectivity | mTLS, endpoint registration | Onyx | Network/security for payer connections |
| Reconciliation | Match members across payers | Abacus (MDP) | Member matching/crosswalk logic |

#### Prior Authorization (ePA)

| Layer | Component | Owner | Responsibility |
|-------|-----------|-------|----------------|
| PA Data Sourcing | Prior auth decisions, status | Abacus | Extract from UM systems |
| Workflow Engine | PA request/response processing | Abacus | CRD, DTR, PAS workflow logic |
| FHIR Mapping | ClaimResponse, Task resources | Abacus (FM Pipeline) | Map PA data to Da Vinci PAS profiles |
| API Serving | $submit, Task polling endpoints | Onyx (Firely) | Serve ePA FHIR operations |
| CDS Hooks | Decision support integration | Abacus | CRD hook implementation |
| Document Exchange | Questionnaire/QuestionnaireResponse | Shared | Abacus (content), Onyx (delivery) |

#### Provider Directory

| Layer | Component | Owner | Responsibility |
|-------|-----------|-------|----------------|
| Data Sourcing | Provider enrollment, NPI, specialties | Abacus (MDP) | Maintain provider master data |
| Transformation | FHIR mapping (Practitioner, Organization, Location, etc.) | Abacus (FM Pipeline) | Map to DaVinci PDex Plan-Net profiles |
| FHIR Store | Resource persistence & search | Onyx (Firely) | Store directory resources, enable search |
| API Serving | Public-facing directory endpoints | Onyx (Dev Portal) | Serve /Practitioner, /Organization, /Location |
| Data Currency | Regular refresh cycles | Abacus | Ensure directory data is ≤ 30 days stale |
| Public Access | No-auth access (CMS requirement) | Onyx (IAM/Auth) | Configure open access per CMS mandate |

### 4.3 CMS Mandate Compliance Ownership Summary

| Compliance Area | Abacus Owns | Onyx Owns | Shared |
|-----------------|-------------|-----------|--------|
| Data completeness | ✅ | — | — |
| FHIR conformance (profiles) | ✅ (mapping) | ✅ (validation) | — |
| API availability | — | ✅ | — |
| Authentication/Authorization | — | ✅ | — |
| Response time SLAs | — | ✅ | — |
| Data freshness | ✅ | — | — |
| Consent enforcement | — | ✅ | — |
| Audit logging | — | — | ✅ |
| CMS attestation | — | — | ✅ (joint) |

---

## 5. Incident Routing Matrix

### 5.1 First-Responder Routing

| Symptom / Alert Area | First Response Team | Escalation Path | SLA (Acknowledge) | SLA (Resolve) |
|---------------------|--------------------|-----------------|--------------------|---------------|
| API 5xx errors spike | Onyx Platform Engineering | → Onyx Security → Abacus Data (if data issue) | 5 min | 30 min (P1), 2 hr (P2) |
| API latency degradation (p95 > 500ms) | Onyx Platform Engineering | → Onyx DevOps → Firely vendor | 5 min | 1 hr |
| FHIR validation errors in load | Abacus Clinical Engineering | → Abacus Data Engineering → Onyx (if Firely issue) | 15 min | 2 hr |
| Pipeline job failure (Databricks) | Abacus Data Engineering | → Abacus Lead → Onyx DevOps (if platform) | 15 min | 1 hr (P1), 4 hr (P2) |
| Data freshness SLA breach | Abacus Data Engineering | → Abacus Lead → Shared Incident Bridge | 15 min | 2 hr |
| Extract task failure | Abacus Data Engineering | → Source system team → Abacus Lead | 15 min | 2 hr |
| Authentication/token failures | Onyx Security Engineering | → Onyx Platform → Cognito support | 5 min | 30 min |
| Developer Portal down | Onyx Platform Engineering | → Onyx DevOps | 5 min | 1 hr |
| MongoDB connectivity issues | Onyx Platform Engineering | → Onyx DevOps → Atlas/AWS support | 5 min | 30 min |
| HealthLake degradation | Onyx Platform Engineering | → AWS support ticket | 15 min | Per AWS SLA |
| Data quality score drop (< 95%) | Abacus Data Engineering | → Abacus Clinical → Business stakeholders | 30 min | 4 hr |
| Deployment failure (Seiji) | Onyx DevOps | → Component-owning team | 15 min | 1 hr |
| Config/SSM access errors | Onyx DevOps | → Affected component team | 5 min | 30 min |
| Monitoring gaps / alerting failure | Onyx DevOps | → Both teams | 15 min | 2 hr |
| CMS audit finding | Shared (Compliance) | → Both teams depending on finding | 1 hr | Per finding severity |
| Member data mismatch (complaint) | Abacus Data Engineering | → Abacus Clinical → Onyx (if API-layer issue) | 1 hr | 24 hr |
| Bulk export timeout | Onyx Platform Engineering | → Abacus (if data volume) → Firely vendor | 15 min | 2 hr |
| Rate limiting triggering falsely | Onyx Platform Engineering | → Onyx DevOps | 15 min | 1 hr |
| Payer-to-Payer connectivity failure | Onyx Platform Engineering | → Onyx Security (mTLS) → Partner payer | 15 min | 4 hr |
| SAM model drift / accuracy alert | Abacus Analytics | → Abacus Data Science Lead | 1 hr | 1 week |

### 5.2 Severity Definitions

| Severity | Definition | Response Time | Escalation Trigger |
|----------|-----------|---------------|-------------------|
| **P1 — Critical** | Production API down, data loss, CMS compliance breach | Immediate (5 min) | Auto-page on-call; bridge call within 15 min |
| **P2 — High** | Degraded performance, partial outage, SLA at risk | 15 min | Escalate after 30 min without progress |
| **P3 — Medium** | Non-critical feature impacted, workaround available | 1 hr | Escalate after 4 hr without progress |
| **P4 — Low** | Cosmetic, non-urgent improvement, monitoring noise | Next business day | Standard sprint process |

### 5.3 Escalation Matrix

```
Level 1: On-Call Engineer (owning team)
    │
    ├── No resolution in 30 min (P1) / 2 hr (P2)
    ▼
Level 2: Engineering Lead (owning team)
    │
    ├── Cross-team dependency identified OR no resolution in 1 hr (P1)
    ▼
Level 3: Shared Incident Bridge (both teams + leads)
    │
    ├── No resolution in 2 hr (P1) OR CMS compliance risk
    ▼
Level 4: VP Engineering + Compliance Officer
    │
    ├── Vendor engagement needed OR regulatory notification required
    ▼
Level 5: Executive Escalation + CMS liaison
```

### 5.4 War Room / Bridge Call Triggers

| Condition | Action | Participants |
|-----------|--------|--------------|
| P1 unresolved > 15 min | Open bridge call | On-call from both teams, Engineering Leads |
| Any CMS-facing API down > 5 min | Open bridge call | Onyx Platform, Abacus Data, Compliance |
| Data pipeline halted > 1 extraction cycle | Notify bridge | Abacus Data Engineering, Onyx DevOps |
| Security incident (any severity) | Mandatory bridge | Both Security, Engineering Leads, Legal |

---

## 6. Change Management

### 6.1 Change Classification

| Change Type | Definition | Approval Required | Lead Time | Examples |
|-------------|-----------|-------------------|-----------|----------|
| **Standard** | Pre-approved, low-risk, repeatable | Auto-approved via CI/CD | 0 (automated) | Config param update, feature flag toggle |
| **Normal** | Moderate risk, tested, scheduled | Team Lead + Peer Review | 3 business days | New pipeline, API version, schema change |
| **Major** | High risk, cross-team impact, CMS-facing | Both Team Leads + Compliance + Architecture | 10 business days | New CMS mandate implementation, Firely upgrade, auth model change |
| **Emergency** | Production fix for active P1/P2 | Verbal approval → retroactive documentation | Immediate | Hotfix for API outage, data corruption fix |

### 6.2 Approval Authority

| Component | Standard Change | Normal Change | Major Change | Emergency Change |
|-----------|----------------|---------------|--------------|-----------------|
| SLAP | Abacus DE Lead | Abacus DE Lead + PR Review | Abacus Arch + Onyx Arch | Abacus DE Lead (verbal) |
| FITE | Abacus DE Lead | Abacus DE Lead + PR Review | Abacus Arch + Onyx Arch | Abacus DE Lead (verbal) |
| FM Pipelines | Abacus Clinical Lead | Abacus Clinical Lead + Conformance Review | Both Arch + Compliance | Abacus Clinical Lead (verbal) |
| SAM Pipelines | Abacus Analytics Lead | Abacus Analytics Lead + PR Review | Abacus Arch | Abacus Analytics Lead (verbal) |
| Extract Tasks | Abacus DE Lead | Abacus DE Lead + PR Review | Abacus Arch | Abacus DE Lead (verbal) |
| MDP | Abacus DE Lead | Abacus DE Lead + Data Steward | Both Arch + Compliance | Abacus DE Lead (verbal) |
| Firely Server | Onyx Platform Lead | Onyx Platform Lead + Vendor Review | Both Arch + Compliance + Vendor | Onyx Platform Lead (verbal) |
| HealthLake | Onyx Platform Lead | Onyx Platform Lead | Both Arch | Onyx Platform Lead (verbal) |
| FHIR Load/Upsert | Abacus DE Lead | Both DE Leads + PR Review | Both Arch | Both DE Leads (verbal) |
| Developer Portal | Onyx Platform Lead | Onyx Platform Lead + UX Review | Both Arch + Business | Onyx Platform Lead (verbal) |
| IAM/Auth | Onyx Security Lead | Onyx Security Lead + Security Review | Both Arch + Compliance + Security | Onyx Security Lead (verbal) |
| Config/SSM | Component Owner | Component Owner + Platform Review | Both Arch | Component Owner (verbal) |
| CI/CD (Seiji) | Onyx DevOps Lead | Onyx DevOps Lead + Both Team Leads | Both Arch + Both Leads | Onyx DevOps Lead (verbal) |
| MongoDB | Schema: Abacus, Infra: Onyx | Both respective leads | Both Arch | Respective Lead (verbal) |
| Monitoring | Alert Owner | Alert Owner + Platform Review | Both Leads | Alert Owner (verbal) |
| Databricks Workflows | Job Owner | Job Owner + Platform Review | Both Arch | Job Owner (verbal) |

### 6.3 Testing Requirements by Change Type

| Change Type | Unit Tests | Integration Tests | E2E Tests | Performance Tests | Conformance Tests | Canary/Blue-Green |
|-------------|-----------|------------------|-----------|-------------------|-------------------|-------------------|
| Standard | ✅ (automated) | — | — | — | — | — |
| Normal | ✅ | ✅ | ✅ (affected flows) | If API-facing | If FHIR-affecting | ✅ (recommended) |
| Major | ✅ | ✅ | ✅ (full regression) | ✅ (mandatory) | ✅ (mandatory) | ✅ (mandatory) |
| Emergency | Best effort | Post-deploy validation | ✅ (within 24 hr) | Post-deploy | If FHIR-affecting | Rollback plan required |

### 6.4 Deployment Windows

| Component Category | Standard Window | Maintenance Window | Blackout Periods |
|-------------------|----------------|-------------------|-----------------|
| Pipeline (SLAP, FITE, FM, SAM, Extract) | Mon–Thu, 6 AM–10 AM ET (between runs) | Sat, 2 AM–6 AM ET | CMS submission periods, Open Enrollment |
| API-Facing (Firely, Dev Portal, IAM) | Tue–Thu, 2 AM–5 AM ET | Sat, 12 AM–6 AM ET | CMS audit windows, Open Enrollment |
| Infrastructure (Databricks, MongoDB, Config) | Mon–Thu, 2 AM–5 AM ET | Sat, 12 AM–6 AM ET | Never during active pipeline runs |
| CI/CD (Seiji) | Mon–Fri, 10 AM–4 PM ET (non-deploy hours) | Sat, anytime | During active deployments |

### 6.5 Rollback Procedures

| Component | Rollback Strategy | Rollback Time Target | Owner |
|-----------|-------------------|---------------------|-------|
| SLAP / FITE / FM / SAM | Revert Databricks job to prior version | < 5 min | Abacus DE |
| Firely Server | Blue-green swap to prior version | < 2 min | Onyx Platform |
| Developer Portal | CloudFront invalidation + ECS rollback | < 5 min | Onyx Platform |
| IAM/Auth | Cognito config restore + Lambda rollback | < 5 min | Onyx Security |
| FHIR Load/Upsert | Halt load, revert to prior bundle version | < 10 min | Shared |
| Config/SSM | SSM parameter version restore | < 1 min | Component owner |
| Databricks Workflows | Restore prior job JSON definition | < 5 min | Job owner |
| MongoDB | Point-in-time restore (last 24 hr) | < 30 min | Onyx Platform |

---

## 7. Shared Components & SLAs

### 7.1 Inter-Team Service Level Agreements

#### 7.1.1 Abacus → Onyx SLAs (Data Pipeline to API Layer)

| Metric | SLA Target | Measurement | Penalty/Escalation |
|--------|-----------|-------------|-------------------|
| Data freshness (Extract → Load complete) | ≤ 6 hours from source availability | Timestamp delta: source available → Firely resource updated | Escalation to Abacus Lead if breached 2x in 7 days |
| FHIR conformance rate | ≥ 99.0% of resources pass validation | FHIR validator error count / total resources loaded | Block load if < 98%, auto-escalate |
| Load success rate | ≥ 99.5% of bundle POSTs succeed | HTTP 2xx responses / total POST attempts | P2 incident if < 99% for > 1 hour |
| Data completeness | ≥ 99% of expected resources present | Expected resource count vs. actual in Firely | Weekly review, escalate if < 97% |
| Pipeline notification | ≤ 5 min after pipeline completion/failure | Event timestamp to Onyx notification receipt | Required for Onyx SLA tracking |
| Schema change notice | ≥ 5 business days before breaking changes | Calendar days from notification to deployment | Mandatory; violating blocks deployment |

#### 7.1.2 Onyx → Abacus SLAs (Platform Services to Pipelines)

| Metric | SLA Target | Measurement | Penalty/Escalation |
|--------|-----------|-------------|-------------------|
| Firely API availability | ≥ 99.9% uptime (monthly) | Successful health checks / total checks | P1 if < 99.5% for any 1-hour window |
| FHIR Load endpoint response time | p95 < 2 seconds for Bundle POST | Server-side latency measurement | Investigate if p95 > 3s for > 15 min |
| Databricks workspace availability | ≥ 99.9% uptime | Job start success rate | P2 if workspace unreachable > 5 min |
| Config/SSM read availability | ≥ 99.99% | Successful reads / total attempts | P1 if config unavailable (pipeline halt) |
| CI/CD (Seiji) deployment success | ≥ 99% of triggered deploys succeed | Successful deploys / total triggered | Investigate if < 95% in any week |
| MongoDB availability | ≥ 99.95% uptime | Connection success rate | P1 if unreachable > 2 min |
| Incident notification to Abacus | ≤ 5 min for P1/P2 affecting pipelines | Time from detection to Abacus notification | Required; violating triggers process review |
| Platform change notice | ≥ 10 business days for breaking changes | Calendar days from notification | Mandatory; violating blocks deployment |

#### 7.1.3 Shared Component SLAs

| Shared Component | SLA Metric | Target | Abacus Responsibility | Onyx Responsibility |
|------------------|-----------|--------|----------------------|---------------------|
| MongoDB | Availability | 99.95% | Schema migrations tested, backward-compatible | Infrastructure, backups, scaling |
| MongoDB | Query performance | p95 < 100ms | Efficient queries, proper indexing requests | Index creation, query optimization |
| Databricks Workflows | Job scheduling accuracy | 99.9% on-time start | Job definitions correct, dependencies declared | Platform availability, cluster management |
| Databricks Workflows | Cluster spin-up time | < 3 min | Appropriately-sized cluster configs | Capacity planning, instance availability |
| FHIR Load/Upsert | End-to-end load time | < 1 hr for standard batch | Valid, well-formed bundles; batch size ≤ limits | Endpoint availability, throughput capacity |
| Config/SSM | Config propagation | < 30 sec after update | Correct parameter values, namespacing | Platform availability, access control |
| Monitoring | Alert delivery | < 1 min from threshold breach | Correct alert definitions, thresholds | Platform delivery, PagerDuty integration |
| CI/CD (Seiji) | Deploy time (standard) | < 15 min | Deployable artifacts, passing tests | Pipeline performance, infra provisioning |

### 7.2 Shared Responsibility Boundaries

#### 7.2.1 MongoDB Ownership Split

| Aspect | Owner | Details |
|--------|-------|---------|
| Database provisioning | Onyx | Atlas/DocumentDB setup, sizing, networking |
| Cluster management | Onyx | Scaling, patching, backup/restore |
| Schema design | Abacus | Collection schemas, document structure |
| Index strategy | Shared | Abacus requests, Onyx implements/reviews |
| Application connectivity | Abacus | Connection strings, retry logic |
| Infrastructure connectivity | Onyx | VPC peering, security groups, DNS |
| Monitoring (DB-level) | Onyx | Disk, CPU, connections, replication lag |
| Monitoring (app-level) | Abacus | Query patterns, slow queries, app errors |

#### 7.2.2 Databricks Workflows Ownership Split

| Aspect | Owner | Details |
|--------|-------|---------|
| Workspace provisioning | Onyx | Account setup, Unity Catalog, networking |
| Cluster policies | Onyx | Instance types, auto-scaling rules, cost controls |
| Job definitions | Abacus | DAGs, task dependencies, parameters, schedules |
| Job execution | Shared | Abacus triggers/monitors; Onyx ensures platform health |
| Secrets management | Onyx | Databricks secrets scope, rotation |
| Library management | Abacus | Python packages, JARs, wheel files |
| Cost monitoring | Shared | Onyx (infrastructure); Abacus (job efficiency) |
| Performance tuning | Shared | Abacus (Spark code); Onyx (cluster config) |

#### 7.2.3 FHIR Load/Upsert Ownership Split

| Aspect | Owner | Details |
|--------|-------|---------|
| Bundle construction logic | Abacus | Resource assembly, references, identifiers |
| Conditional upsert logic | Abacus | Match criteria, conflict resolution rules |
| Load service deployment | Onyx | ECS/Lambda infra, scaling, networking |
| Auth token management | Onyx | Service-to-service auth for Firely access |
| Error handling & retry | Shared | Abacus (logic); Onyx (infrastructure retries) |
| Throughput tuning | Shared | Abacus (batch sizes); Onyx (concurrency, rate limits) |
| Load monitoring | Shared | Abacus (data completeness); Onyx (infra health) |

### 7.3 Communication Protocols

| Communication Type | Channel | Frequency | Participants |
|-------------------|---------|-----------|--------------|
| **Daily Standup (Shared)** | Slack + Video | Daily, 9:15 AM ET | Leads from both teams |
| **Pipeline Health Review** | Dashboard + Slack | Daily (automated) | Both DE teams |
| **Cross-Team Architecture Review** | Video | Bi-weekly, Wed 2 PM ET | Architects from both teams |
| **Incident Retrospective** | Video + Doc | Within 5 days of P1/P2 | All involved + Leads |
| **SLA Review** | Video + Report | Monthly, 1st Thursday | Leads + Management |
| **Change Advisory Board** | Video | Weekly, Tue 11 AM ET | Both Leads + Compliance |
| **CMS Compliance Sync** | Video + Doc | Bi-weekly, Mon 3 PM ET | Compliance + Both Leads |
| **Production Readiness Review** | Video | Before every Major change | Both Arch + Leads |

### 7.4 Dispute Resolution

| Level | Trigger | Process | Timeline |
|-------|---------|---------|----------|
| 1 — Working Level | Disagreement on implementation | Discuss in architecture sync, document options | 1 week |
| 2 — Lead Escalation | No resolution at working level | Both leads meet, review options, decide | 3 days |
| 3 — Management | Leads cannot agree | VP Engineering arbitrates | 2 days |
| 4 — Executive | Business/compliance implications | CTO + Compliance Officer decide | 1 day |

### 7.5 Dependency Risk Register

| Dependency | Risk | Likelihood | Impact | Mitigation | Owner |
|-----------|------|-----------|--------|------------|-------|
| Firely vendor support | Delayed patches, breaking upgrades | Medium | High | Maintain N-1 version support, vendor escalation path | Onyx |
| Databricks platform changes | API deprecation, pricing changes | Low | High | Version pinning, multi-cloud readiness | Onyx |
| Source system availability | Unplanned downtime, schema drift | High | Medium | Retry logic, schema evolution handling, SLA with sources | Abacus |
| AWS HealthLake | Service limitations, regional issues | Low | Medium | Firely as primary, HealthLake as secondary | Onyx |
| CMS rule changes | New mandates, timeline changes | Medium | High | Compliance monitoring, architecture flexibility | Shared |
| MongoDB Atlas | Connection limits, performance degradation | Low | High | Connection pooling, read replicas, failover | Onyx |
| Cross-team knowledge silos | Key person dependency | Medium | Medium | Documentation, cross-training, pair rotations | Shared |

---

## Appendix A: Contact & Escalation Directory

| Role | Team | Contact Method | Escalation Authority |
|------|------|---------------|---------------------|
| Abacus DE Lead | Abacus | Slack: @abacus-de-lead, PagerDuty | Pipeline decisions, Extract/SLAP/FITE/FM/SAM |
| Abacus Clinical Lead | Abacus | Slack: @abacus-clinical-lead, PagerDuty | FHIR conformance, FM mapping decisions |
| Abacus Analytics Lead | Abacus | Slack: @abacus-analytics-lead | SAM pipeline, quality measures |
| Abacus Architect | Abacus | Slack: @abacus-arch | Cross-cutting data architecture |
| Onyx Platform Lead | Onyx | Slack: @onyx-platform-lead, PagerDuty | Firely, HealthLake, Dev Portal, FHIR Load |
| Onyx Security Lead | Onyx | Slack: @onyx-security-lead, PagerDuty | IAM, Auth, mTLS, security incidents |
| Onyx DevOps Lead | Onyx | Slack: @onyx-devops-lead, PagerDuty | CI/CD, infrastructure, Databricks platform |
| Onyx Architect | Onyx | Slack: @onyx-arch | Cross-cutting platform architecture |
| Compliance Officer | Shared | Slack: @compliance, Email | CMS mandate decisions |

## Appendix B: Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-05-01 | Platform Architecture | Initial creation |
| 1.5 | 2026-06-15 | Both Teams | Added P2P, ePA ownership details |
| 2.0 | 2026-07-07 | Platform Architecture | Full revision — added incident routing, change management, SLAs |

---

*This document is the authoritative source for component ownership and inter-team responsibilities. Updates require approval from both team leads and must be reflected within 5 business days of any organizational or architectural change.*
