# Wisconsin Statewide EHR Platform — Solution Blueprint

Modular, cloud-native statewide EHR for Wisconsin supporting care coordination, gap closure, outcome improvement, and bidirectional Cerner (Oracle Health) migration via FHIR bundles.

---

## Table of Contents

1. [Pre-Sales & RFP](#1-pre-sales--rfp)
2. [Cursor AI Development Platform](#2-cursor-ai-development-platform)
3. [Discovery Session](#3-discovery-session)
4. [Technical Architecture](#4-technical-architecture)
5. [Resource Planning](#5-resource-planning)
6. [Cloud-Native Services](#6-cloud-native-services)
7. [Cost Planning](#7-cost-planning)
8. [Source Files Inventory (CMS CCLF)](#8-source-files-inventory-cms-cclf)
9. [Implementation Guide](#9-implementation-guide)
10. [DevOps](#10-devops)
11. [BRD](#11-brd)
12. [Data Models](#12-data-models)
13. [UAT Planning](#13-uat-planning)
14. [Go Live](#14-go-live)
15. [Interview Questions Guide](#15-interview-questions-guide)
16. [Lessons Learned](#16-lessons-learned)

---

## 1. Pre-Sales & RFP

### Value Proposition

- Single statewide longitudinal record across FQHCs, rural clinics, hospitals, and state programs (Medicaid, WIC, public health)
- Care gap closure via HEDIS/Stars-aligned analytics and closed-loop workflows
- Interoperability-first: FHIR R4, SMART on FHIR, bulk export, Cerner-compatible bundles
- Governed AI/ML for documentation assist, risk stratification, and gap prediction

### RFP Response Structure

| Section | Content |
|---------|---------|
| Executive summary | Vision, outcomes, 3-year roadmap |
| Solution overview | Clinician GUI, patient portal, PMS integrations, analytics |
| Technical architecture | GCP + Fabric + Snowflake + Power BI |
| Interoperability | FHIR, HL7 v2, X12, Cerner migration |
| Security & compliance | HIPAA, HITECH, SOC 2, Wisconsin Act 117 |
| AI/ML governance | Model registry, bias testing, human-in-the-loop |
| Implementation plan | Phased rollout by region/program |
| Staffing & timeline | Roles, FTEs, milestones |
| Pricing model | TCO by phase |
| SLAs | 99.9% uptime, RPO/RTO, support tiers |

### Wisconsin Differentiators

- CMS CCLF seed data for demo, UAT, and ML without PHI
- Modular export — any module emits Cerner-compatible FHIR bundles
- Fabric → Snowflake → Power BI aligned with Microsoft investments
- Rural/low-bandwidth clinician UX

---

## 2. Cursor AI Development Platform

Cursor is the AI-native IDE used to design, build, and govern the Wisconsin statewide EHR platform. This section defines how the delivery team uses Cursor end-to-end — from solution architecture through FHIR services, Fabric pipelines, and governed ML — while maintaining HIPAA-aligned engineering practices.

### 2.1 Platform Overview

| Capability | Description | EHR project use |
|------------|-------------|-----------------|
| **Cursor IDE** | VS Code–compatible editor with embedded AI | Primary dev environment for all engineers |
| **Agent** | Autonomous multi-file coding agent | FHIR services, Terraform modules, Fabric notebooks |
| **Chat / Ask** | Conversational Q&A; Ask mode is read-only | Architecture reviews, FHIR mapping questions |
| **Plan** | Collaborative planning before implementation | Cerner migration phasing, data model design |
| **Debug** | Systematic troubleshooting with runtime evidence | Integration failures, pipeline errors |
| **Tab** | Inline code completion | Boilerplate FHIR profiles, SQL, TypeScript |
| **Cloud Agents** | Background agents on isolated VM + git branch | Long-running refactors, doc generation |
| **Automations** | Scheduled/event-driven Cursor agents | Nightly gap-report drafts, CI triage loops |
| **Canvas** | Live React artifact beside chat | Architecture diagrams, cost models, gap analytics |
| **MCP** | Model Context Protocol tool integrations | GitHub, Databricks, Snowflake, Linear, Sentry |
| **Bugbot / Security Review** | Subagent code review on diffs | Pre-PR HIPAA and security gates |

**Repository:** [Enterprise-EHR-Solution](https://github.com/AshishSys/Enterprise-EHR-Solution.git)  
**Branch convention:** `cursor/<short-description>` for agent-generated feature work (e.g., `cursor/wisconsin-ehr-solution-blueprint`).

### 2.2 Workspace & Project Layout

```
Enterprise-EHR-Solution/
├── WisconsinEHR/
│   ├── README.md
│   ├── docs/
│   │   └── WISCONSIN_EHR_SOLUTION_BLUEPRINT.md
│   ├── .cursor/
│   │   ├── rules/              # Project rules (.mdc)
│   │   └── skills/             # Project-specific agent skills
│   ├── src/                    # Application services (GKE)
│   ├── terraform/              # GCP + Snowflake IaC
│   ├── fabric/                 # Microsoft Fabric pipelines
│   ├── fhir/                   # Profiles, bundles, Inferno tests
│   └── tests/
└── .github/workflows/          # CI/CD (Agent can triage via Automations)
```

**Workspace protection:** Temp artifacts go at repo root (`reports/`, `tmp/`) — never under `.cursor/` or agent workspaces.

### 2.3 Interaction Modes

| Mode | When to use | Example prompt |
|------|-------------|----------------|
| **Agent** | Implementation, multi-file changes | "Add FHIR Bundle exporter for Cerner migration" |
| **Plan** | Architecture trade-offs, phasing | "Compare AlloyDB vs Cloud SQL for MPI at 5M lives" |
| **Ask** | Read-only exploration | "How does CCLF4 join to CCLF1 in our lakehouse?" |
| **Debug** | Failures with logs/traces | "Snowpipe load failed — trace the MERGE idempotency bug" |

**Mode switching rule:** Start in Plan for cross-cutting decisions (Cerner coexistence, MPI strategy); move to Agent only after scope is clear.

### 2.4 Project Rules (`.cursor/rules/`)

Rules are `.mdc` files with YAML frontmatter that persist compliance and conventions for every agent session.

| Rule file | Scope | Purpose |
|-----------|-------|---------|
| `healthcare-compliance.mdc` | `alwaysApply: true` | HIPAA/HITECH — no PHI in logs, secrets via KMS |
| `fhir-interop.mdc` | `fhir/**`, `src/**` | US Core STU6, Wisconsin extensions, Cerner bundle format |
| `dry-principal.mdc` | `alwaysApply: true` | Reuse existing utilities before new functions |
| `terraform-secrets.mdc` | `**/*.tf` | CMEK, recovery_window_in_days = 0, air-cd decrypt |
| `spark-delta-compliance.mdc` | `fabric/**`, `**/*.py` | No collect() on PHI; Delta MERGE idempotency |
| `http-https-redirect.mdc` | `terraform/**`, `helm/**` | ALB/Ingress must redirect HTTP → HTTPS |
| `vpc-bridge-pattern.mdc` | `terraform/**` | Air-gapped Databricks via bridge VPC only |
| `terse-communication.mdc` | `alwaysApply: true` | Concise agent responses for clinical stakeholders |

**Example rule frontmatter:**

```yaml
---
description: FHIR and Cerner migration conventions
globs: fhir/**/*.json, src/**/fhir/**
alwaysApply: false
---
```

### 2.5 Agent Skills (`.cursor/skills/`)

Skills teach the agent domain workflows beyond generic coding.

| Skill | Location | Trigger |
|-------|----------|---------|
| `cclf-ingestion` | Project | Fabric pipeline work on CMS CCLF files |
| `cerner-fhir-bundle-export` | Project | Migration bundle generation |
| `hedis-gap-engine` | Project | Care gap measure logic |
| `fhir-inferno-validation` | Project | US Core conformance testing |
| `healthcare-security-review` | Personal | Pre-PR security review requests |
| `create-pull-request` | Personal | `gh pr create` workflow |
| `canvas-architecture` | Personal | Standalone architecture artifacts |

**Skill structure:**

```
.cursor/skills/cclf-ingestion/
├── SKILL.md           # Required — agent instructions
├── reference.md       # CCLF field dictionary
└── scripts/
    └── validate_joins.py
```

### 2.6 MCP Integrations

MCP servers extend the agent with live tool access. Configure in **Cursor Settings → MCP** or project `mcp.json`.

| MCP server | Tools | EHR use case |
|------------|-------|--------------|
| **GitHub** | Issues, PRs, checks | Branch/PR workflow, CI triage |
| **Databricks** | SQL, jobs, clusters | Feature engineering on CCLF (de-identified) |
| **Snowflake** | Queries, stages | Reporting view validation |
| **Linear / Jira** | Issues, sprints | BRD traceability, UAT defects |
| **Sentry** | Errors, traces | Clinician GUI production monitoring |
| **Slack** | Channels, threads | Hypercare war-room alerts (no PHI) |
| **Datadog** | Metrics, logs | SLO dashboards (redacted labels) |

**MCP auth gate:** Authenticate each server before use (`mcp_auth`). Never configure MCP tools that expose PHI to external SaaS without BAA.

**Automation eligibility:** Only dashboard-backed MCP servers (prefix `dashboard-`, `dashboard-team-`, `plugin-`) appear in Cursor Automations editor.

### 2.7 Cloud Agents

Cloud Agents run in an isolated VM with their own git branch and worktree — suited for long tasks.

| Use case | Cloud Agent task | Output |
|----------|------------------|--------|
| Canonical model v1 | Generate FHIR profiles + AlloyDB DDL | PR on `cursor/canonical-model-v1` |
| CCLF sandbox pipeline | Fabric notebooks + Snowflake views | PR + Canvas cost/gap demo |
| Cerner bundle mapper | Resource-by-resource mapping doc | PR in `fhir/cerner/` |
| Terraform foundation | GKE + Healthcare API modules | PR in `terraform/` |

**Workflow:**

1. Launch Cloud Agent with detailed prompt (include Full Repository Path + constraints).
2. Agent works on `cursor/<task>` branch in cloud worktree.
3. Review via **Review** link or checkout branch locally.
4. Merge via PR after Bugbot + Security Review pass.

### 2.8 Cursor Automations

Automations are scheduled or event-driven agents defined in the Automations editor.

| Automation | Trigger | Action |
|------------|---------|--------|
| `nightly-gap-report-draft` | Cron 06:00 CT | Query Snowflake gold views → draft Power BI summary (aggregates only) |
| `ci-triage-loop` | GitHub check failure on `main` | Investigate failing check, propose fix PR |
| `fhir-profile-drift` | Weekly | Compare deployed profiles vs repo; open Linear issue if drift |
| `dependency-cve-scan` | Daily | Scan container images; flag critical CVEs |

**PHI rule for Automations:** Prompts and tool outputs must use CCLF/synthetic data only unless running in prod-automation with explicit BAA and redaction middleware.

### 2.9 Canvas

Use Canvas for deliverables that benefit from visual layout:

- Statewide architecture diagram (GCP + Fabric + Snowflake)
- Care gap closure funnel by region
- Cerner migration wave timeline
- TCO sensitivity model (infra vs services)
- CCLF join explorer (interactive)

Invoke via the **canvas skill** when presenting quantitative or architectural artifacts instead of markdown tables.

### 2.10 Code Review Subagents

| Subagent | Invocation | Focus |
|----------|------------|-------|
| **Bugbot** | `@review` or skill | Logic bugs, edge cases, test gaps |
| **Security Review** | `@security-review` | PHI leakage, secrets, IAM, injection |

**Pre-PR checklist (agent-assisted):**

1. Run Bugbot on branch diff.
2. Run Security Review on FHIR/auth/logging changes.
3. Confirm no PHI in test fixtures or logs.
4. FHIR Inferno smoke pass on changed profiles.

### 2.11 Hooks (`.cursor/hooks.json`)

Hooks automate behavior on agent events.

| Hook event | Script | Purpose |
|------------|--------|---------|
| `beforeSubmitPrompt` | `scripts/scan_phi_in_prompt.sh` | Block prompts containing MRN/SSN patterns |
| `afterFileEdit` | `scripts/lint_fhir.sh` | Validate FHIR JSON on save |
| `stop` | `scripts/audit_agent_session.sh` | Structured audit log (no content, metadata only) |

### 2.12 Cursor SDK (Programmatic Agents)

Use `@cursor/sdk` (TypeScript) or `cursor-sdk` (Python) for CI/CD and backend orchestration outside the IDE.

| Scenario | SDK pattern |
|----------|-------------|
| PR opened → architecture review | `Agent.create()` → prompt with diff context |
| Nightly regression | Cloud runtime agent on `staging` branch |
| Migration dry-run | Agent generates bundle manifest; human approves upload |

**SDK agent config:** Attach MCP servers (GitHub, Snowflake) in agent definition; never pass PHI in `Agent.prompt()` — use resource IDs and aggregate stats only.

### 2.13 Git Workflow in Cursor

| Action | Cursor UI | Result |
|--------|-----------|--------|
| Create branch + commit | Diff tab → **Create branch and commit** | `cursor/<desc>` branch, local commit |
| Commit + push | Diff tab → **Commit and push** | Push to `origin` |
| Open PR | Agent + `gh pr create` skill | PR against `main` |

**Branch policy:**

- `main` — protected; merge via PR only
- `cursor/*` — agent/feature work; delete after merge
- `release/*` — regional go-live waves

### 2.14 Role-Based Cursor Usage

| Role | Primary Cursor surfaces | Typical tasks |
|------|-------------------------|---------------|
| **Solution Architect** | Plan, Canvas, Ask | Architecture decisions, NFR matrix, Cerner strategy |
| **Data Engineer** | Agent, MCP (Fabric/Snowflake) | CCLF pipelines, Snowflake gold views |
| **Product Engineer** | Agent, Tab, Debug | Clinician GUI, FHIR services on GKE |
| **AI Engineer** | Agent, Cloud Agent | Vertex models, feature store, governance metrics |
| **Delivery Manager** | Automations, Linear MCP | Sprint tracking, RAID, go-live checklists |
| **QA / UAT lead** | Agent, Ask | Test case generation from BRD FR IDs |

### 2.15 Security, Privacy & Compliance

| Requirement | Cursor control |
|-------------|----------------|
| No PHI in prompts | Rules + `beforeSubmitPrompt` hook; use CCLF IDs only |
| No PHI in agent logs | Structured logging rule; redaction middleware |
| Secrets never in code | Rules enforce Secrets Manager / SSM + KMS |
| Least privilege | MCP scoped to dev/staging workspaces |
| Human-in-the-loop for clinical AI | Plan mode sign-off before Agent deploys model code |
| BAA coverage | Cursor Business/Enterprise — confirm with legal before prod PHI adjacency |
| Audit trail | Git commits + agent session metadata hooks |

**Red flags to reject in agent output:**

- Hardcoded credentials or connection strings
- `console.log(patient)` or logging identifiers
- Training on CCLF without label-leakage guards
- Direct internet from air-gapped Databricks VPC

### 2.16 Licensing & Team Setup

| Tier | Seats | Recommended for |
|------|-------|-----------------|
| **Cursor Business** | Core engineering (12–22 FTE) | Agent, privacy mode, team rules |
| **Cursor Enterprise** | State IT + security reviewers | SSO, audit, advanced privacy |
| **Cloud Agent minutes** | Burst capacity | Large refactors, doc generation sprints |

**Onboarding checklist:**

1. Clone `Enterprise-EHR-Solution`; open `WisconsinEHR/` as workspace root.
2. Install recommended extensions (Terraform, FHIR, Python, ESLint).
3. Authenticate MCP: GitHub, Snowflake (dev), Linear.
4. Read project rules in `.cursor/rules/`.
5. Complete CCLF sandbox walkthrough (Section 9) before touching prod configs.

### 2.17 Cursor-Specific Interview Questions

| Role | Question |
|------|----------|
| All | How do Cursor rules enforce HIPAA in agent-generated code? |
| Architect | When do you use Plan vs Agent for a Cerner migration workstream? |
| Data Engineer | How would you wire Snowflake MCP without exposing row-level PHI? |
| Product Engineer | Describe SMART on FHIR auth flow implementation with Agent mode. |
| AI Engineer | How do Cloud Agents differ from local Agent for Vertex pipeline work? |
| Delivery Manager | Design a Cursor Automation for CI triage on gap-engine tests. |

### 2.18 Recommended Next Steps (Cursor)

1. Scaffold `.cursor/rules/` with healthcare-compliance and fhir-interop rules.
2. Create `cclf-ingestion` and `cerner-fhir-bundle-export` project skills.
3. Configure GitHub + Snowflake MCP for dev environment.
4. Launch Cloud Agent for Terraform foundation module (GKE + Healthcare API).
5. Enable Bugbot + Security Review on all `cursor/*` → `main` PRs.

---

## 3. Discovery Session

### Stakeholder Map

| Group | Key Questions |
|-------|---------------|
| State CIO / DHS | Governance, funding, Medicaid alignment |
| Clinicians | Workflow pain points, order sets, inbox |
| Nursing / care managers | Gap closure, care plans, outreach |
| HIM / compliance | Audit, release of information, consent |
| IT / security | IAM, network, BAA, incident response |
| Patients / advocates | Portal features, language access |
| PMS vendors | API availability, batch vs real-time |
| Cerner / Oracle Health | Current footprint, FHIR maturity |

### 5-Day Workshop Agenda

| Day | Focus |
|-----|-------|
| 1 | Vision, scope, success metrics |
| 2 | Clinical workflows (ambulatory, BH, public health) |
| 3 | Data & integrations (PMS, lab, pharmacy, registries) |
| 4 | Security, compliance, AI governance |
| 5 | Migration phasing, pilot regions, CCLF sandbox |

### Discovery Deliverables

- Current-state integration inventory
- Priority use-case backlog (MoSCoW)
- Non-functional requirements matrix
- Risk register
- High-level data domain model
- Cerner migration decision tree

---

## 4. Technical Architecture

### Principles

- Modular bounded contexts (Clinical, Patient, Integration, Analytics, AI)
- API-first — FHIR facade over canonical model
- Event-driven — Pub/Sub for clinical events, gap alerts, audit
- Zero-trust — IAP, workload identity, least privilege
- Export-ready — FHIR Bundle generation on demand per domain

### Layer Overview

| Layer | Components | Purpose |
|-------|------------|---------|
| Experience | Clinician SPA, patient portal, Power BI embed | User-facing |
| API & integration | Apigee, Cloud Healthcare API (FHIR R4), HL7 v2 adapters | Interop |
| Application | GKE microservices: Patient, Encounter, Meds, Gaps, Care Plan | Business logic |
| Canonical data | FHIR store + AlloyDB relational index | Source of truth |
| Event bus | Pub/Sub: `clinical.events`, `gap.detected`, `audit.trail` | Async workflows |
| ETL | Fabric → OneLake → Snowflake | Analytics pipeline |
| AI/ML | Vertex AI, Feature Store, Model Registry | Governed ML |
| Security | IAM, VPC-SC, CMEK, Assured Workloads | HIPAA alignment |

### Cerner Migration

**Export (Wisconsin EHR → Cerner)**

1. Canonical record → FHIR R4 Bundle builder
2. Bulk `$export` or scheduled jobs to encrypted Cloud Storage
3. Cerner ingestion via Oracle Health FHIR APIs

**Import (Cerner → Wisconsin EHR)**

1. Cerner FHIR bulk export → OneLake/GCS landing zone
2. Fabric transformation to canonical model
3. Idempotent upsert into FHIR store + relational index

**Coexistence**

- MPI with cross-reference IDs (Wisconsin ID ↔ Cerner ID ↔ PMS ID)
- Source-of-truth flags per domain until cutover

### PMS Integration Patterns

| Pattern | Use Case | Technology |
|---------|----------|------------|
| FHIR subscription | Real-time appointments, demographics | Pub/Sub + webhooks |
| HL7 v2 ADT/SIU | Legacy PMS | MLLP adapter on GKE |
| Batch SFTP | Nightly sync | Cloud Storage + Fabric |
| SMART on FHIR | Embedded apps | OAuth 2.0 / OIDC |

---

## 5. Resource Planning

### Team Structure (18–24 months)

| Role | Count | Responsibilities |
|------|-------|------------------|
| Solution Architect | 1 lead + 1 integration | Topology, FHIR/Cerner strategy, NFR, security |
| Data Engineer | 3–4 | Fabric pipelines, CCLF, Snowflake, data quality |
| Product Engineer | 4–6 | Clinician GUI, portal, GKE services, FHIR mapping |
| Delivery Manager | 1 + 1 SM | Roadmap, vendors, RAID, rollout |
| AI Engineer | 2 | Feature store, gap/risk models, MLOps |
| DevOps / SRE | 2–3 | IaC, CI/CD, observability, DR |
| Clinical informaticist | 2 | Workflows, order sets, gap definitions |
| QA / UAT lead | 2 | Test strategy, CCLF synthetic patients |
| Security / compliance | 1 shared | BAA, audit, pen test coordination |

### Phase Ramp

| Phase | Duration | FTE |
|-------|----------|-----|
| Foundation | Months 1–4 | ~12 |
| Pilot | Months 5–10 | ~18 |
| Expansion | Months 11–18 | ~22 |
| Cerner readiness | Months 16–24 | ~15 |

---

## 6. Cloud-Native Services

### Google Cloud Platform

| Service | Use |
|---------|-----|
| GKE Autopilot | Microservices, HL7 adapters, bundle exporters |
| Cloud Healthcare API | FHIR R4 store |
| Apigee X | External API management, OAuth |
| Cloud Identity / IAP | SSO, zero-trust access |
| AlloyDB / Cloud SQL | Transactional index, MPI |
| Cloud Storage | Landing zones, bundle archives (CMEK) |
| Pub/Sub | Event streaming |
| Cloud Run / Functions | Webhooks, lightweight transforms |
| BigQuery | Operational analytics |
| Vertex AI | Training, prediction, Model Registry |
| Secret Manager + Cloud KMS | Credentials, CMEK |
| Cloud Logging / Monitoring | Observability (no PHI in logs) |
| Cloud Armor + CDN | WAF, portal edge |
| Assured Workloads | HIPAA-aligned controls |

### Microsoft Fabric

| Component | Use |
|-----------|-----|
| OneLake / Lakehouse | Bronze (raw CCLF, HL7, FHIR JSON) |
| Data Factory pipelines | Orchestration, PMS batch loads |
| Spark notebooks | CCLF normalization, SCD2 |
| Dataflows Gen2 | Lightweight transforms |

### Snowflake

| Object | Use |
|--------|-----|
| Bronze/Silver/Gold | Medallion architecture |
| Dynamic tables / streams | Incremental reporting views |
| Secure views | Row/column masking |
| Snowpipe | Continuous load from OneLake/GCS |

### Power BI

| Component | Use |
|-----------|-----|
| Datasets | Snowflake semantic layer |
| Dashboards | Gap closure, utilization, outcomes |
| Row-level security | Region/program scoping |
| Embedded analytics | Clinician GUI widgets (aggregates only) |

---

## 7. Cost Planning

### Assumptions

- 5M attributed lives
- 8,000 clinical users, 500K patient portal MAU
- 50 TB analytics data year 1
- 3 environments: dev, staging, prod

### Annual TCO Bands (USD, illustrative)

| Category | Year 1 | Year 2–3 |
|----------|--------|----------|
| GCP compute & storage | $1.2M–$2.0M | $1.5M–$2.5M |
| Cloud Healthcare API | $300K–$600K | Scales with volume |
| Vertex AI | $150K–$400K | Model-dependent |
| Microsoft Fabric | $400K–$800K | $500K–$900K |
| Snowflake Enterprise | $350K–$700K | $500K–$1M |
| Apigee, networking, security | $200K–$400K | $200K–$400K |
| Professional services | $4M–$8M one-time | $1M–$2M/year |
| Licenses | $100K–$200K | $100K–$200K |

### Optimization Levers

- Committed use discounts (GKE, BigQuery)
- Snowflake resource monitors and auto-suspend
- Fabric capacity pause in non-prod
- Coldline for CCLF archives
- CCLF/public data in dev only

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

## 10. DevOps

### Environments

| Environment | Purpose | Data |
|-------------|---------|------|
| dev | Feature development | CCLF only |
| staging | Integration/UAT | Synthetic + CCLF subset |
| prod | Live statewide | PHI (encrypted, audited) |

### CI/CD

```
PR → lint/test → SAST → build → deploy dev (GKE)
  → FHIR contract tests → promote staging
  → UAT sign-off → change advisory → prod (blue/green)
```

| Tool | Function |
|------|----------|
| Cloud Build / GitHub Actions | CI |
| Argo CD / Flux | GitOps on GKE |
| Artifact Registry | Immutable images |
| Terraform | IaC for GCP + Snowflake |

### Observability & DR

- Structured logs with PHI redaction; correlation IDs only
- SLOs: API p99 < 500ms; 99.9% monthly uptime
- RPO 15 min; RTO 4 hours; quarterly DR drills
- CMEK for Storage, SQL, Healthcare API, BigQuery
- VPC Service Controls perimeter around PHI services

---

## 11. BRD

### Outline

1. Executive summary
2. Business objectives (gap closure %, coordination metrics)
3. Scope (in/out — billing vs clinical)
4. Stakeholders & RACI
5. User personas
6. Functional requirements (FR-CLIN, FR-GAP, FR-PORT, FR-MIG)
7. Non-functional requirements (security, performance, WCAG 2.1 AA)
8. Integration requirements
9. Reporting requirements (Power BI catalog)
10. AI/ML requirements (human review, bias thresholds)
11. Assumptions & constraints
12. Acceptance criteria linked to UAT

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

## 13. UAT Planning

### Principles

- CCLF-driven synthetic cohorts with known expected gaps
- Pilot clinicians from each region and specialty
- Traceability: BRD FR → test case → result

### Phases

| Phase | Focus | Duration |
|-------|-------|----------|
| UAT-0 | CCLF → Snowflake → Power BI | 2 weeks |
| UAT-1 | Clinician GUI core chart | 4 weeks |
| UAT-2 | Gap engine + care manager worklists | 3 weeks |
| UAT-3 | Patient portal + consent | 2 weeks |
| UAT-4 | PMS integration (pilot) | 4 weeks |
| UAT-5 | Cerner FHIR bundle export/import | 3 weeks |
| UAT-6 | AI recommendations (shadow mode) | 2 weeks |

### Exit Criteria

- ≥ 95% critical test cases pass
- No Sev-1/Sev-2 open
- Clinical and security sign-off

---

## 14. Go Live

### Strategy

- Regional wave rollout (not big-bang)
- Read-only coexistence with PMS/Cerner during stabilization
- Command center first 72 hours per wave

### Pre Go-Live Checklist

| Area | Items |
|------|-------|
| Technical | Prod smoke tests, DR verified, on-call roster |
| Data | MPI golden records, code sets loaded |
| Security | Pen test remediated, BAAs executed |
| Training | Super-users, help desk scripts |
| Clinical | Order sets, gap definitions signed off |
| Migration | Rollback plan tested |

### Hypercare KPIs

- P1 incident count
- Login success rate
- Gap list generation latency
- Daily user satisfaction pulse

### Rollback Triggers

- MPI corruption threshold exceeded
- Critical patient records unavailable > SLA
- Security incident

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

## 16. Lessons Learned

| Lesson | Mitigation |
|--------|------------|
| MPI failures destroy trust | Invest early; manual merge queue; no risky auto-merge |
| Clinicians reject another inbox | SMART embed in PMS; minimize clicks |
| Analytics without closed-loop fails | Gap list → care plan tasks |
| Big-bang go-live disasters | Regional waves; hypercare; rollback plan |
| HL7 variance underestimated | Adapter per site; message profiling sprint |
| AI hype backlash | Shadow mode; explainability; governance board |
| Cerner migration as afterthought | FHIR export from day 1; quarterly dry runs |
| PHI in non-prod | CCLF/synthetic only until UAT |
| Fabric/Snowflake duplication | Fabric = engineering; Snowflake = reporting gold |
| FHIR API cost overrun | Cache reads; bulk export; aggregate in Snowflake |

### Wisconsin-Specific

- Rural connectivity — optimize payloads; regional caching
- Tribal health sovereignty — data governance and consent models
- Medicaid MCO fragmentation — align gap measures across payers
- Seasonal workforce — scalable licensing

---

## Recommended Next Steps

1. Weeks 1–2: Discovery workshops + integration inventory
2. Weeks 3–4: BRD v0.9 + CCLF sandbox (Fabric → Snowflake → Power BI)
3. Month 2: Terraform foundation + FHIR store + canonical model v1
4. Month 3: Clinician GUI prototype on CCLF synthetic patients
