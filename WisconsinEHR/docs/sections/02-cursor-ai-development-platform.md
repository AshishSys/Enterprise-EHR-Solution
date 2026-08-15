[← 01](01-pre-sales-rfp.md) · [Index](../WISCONSIN_EHR_SOLUTION_BLUEPRINT.md) · [Next →](03-discovery-session.md)

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
