# AI Governance & CCA Alignment

> Maps **AI Governance MVP** (May 2026) and **CCA Dev Milestones** (June 2026) discussions to this Healthcare Interop Solution.  
> Primary scope remains **CMS-9115/0057**; CCA patterns are captured as **adjacent product requirements** that share the same AI platform.

---

## Executive Summary

| Source | Core directive | Status in this solution |
|--------|----------------|-------------------------|
| AI Governance session | MLflow tracing + 3 core metrics (hallucination, bias, trustworthiness) via **daily batch** | **Added** — Component 13, `governance_metrics.yaml`, Phase 4E |
| AI Governance session | Deprioritize standalone PHI screening, governance-only de-ID, duplicate RBAC, version snapshots | **Aligned** — Unity AI Gateway, UC, GitLab CI |
| CCA working session | Define **metrics early** to reduce hallucinations | **Added** — golden eval + governance batch job before agent go-live |
| CCA working session | **Data before AI**; claims + medical records minimum | **Already in plan** — Phase 1 SAM before Phase 4 agents |
| CCA working session | UI/application ownership gap, Replit, SecOps for customer UI | **Documented** — RACI + leadership decision log (CCA adjacency) |
| CCA working session | Implementation/delivery early involvement | **Added** — Forward Deployed + Mahesh team in Phase 3 gate |
| CCA working session | Demo vs POC vs production-deployable ambiguity | **Added** — readiness levels per phase |

**Operating principle (Nav):** *"Start simple, prove the construct with core metrics, then scale sophistication."*

---

## Part 1 — AI Governance MVP Alignment

### 1.1 Core metrics (phased)

| Metric | Phase | Mechanism in solution | Artifact |
|--------|-------|----------------------|----------|
| **Hallucination rate** | 1 (now) | Semantic similarity + LLM-as-judge + behavioral signals (invalid MCP tool, bad FHIR path) | `pipeline/ai/governance_metrics.py` |
| **Bias** | 2 | Slice eval on de-identified Synthea/PulseEHR cohorts | `governance_metrics.yaml` phase_2 |
| **Trustworthiness** | 2 | Citation coverage + gateway policy pass + SME feedback | Same |

**Production path:** MLflow traces → Delta `onyx_ai.governance.interaction_traces` → Databricks job (daily) → Delta `onyx_ai.governance.metric_results` → notebook/CSV report.

### 1.2 Technical flow (agreed architecture)

```
User/agent interaction
    → Unity AI Gateway (trace + policy)
    → MLflow log (inputs, outputs, tools, latency)
    → Delta audit tables
    → Daily batch: governance_metrics job
    → Delta metric_results + weekly notebook report
```

Local mirror:

```bash
cd Training/onyx-interop
python3 pipeline/ai/governance_metrics.py --traces data/governance/sample_traces.json
```

### 1.3 Deprioritized items (explicitly NOT duplicated here)

| Backlog item (governance session) | Why deprioritized | How interop solution handles it |
|-----------------------------------|-------------------|--------------------------------|
| Standalone PHI screening | HIPAA-compliant perimeter | Unity AI Gateway `block_external_phi`; de-ID gate for analytics |
| De-ID **for governance eval** | Limits product improvement signal | De-ID **remains** for analytics/Fabric; governance eval uses **controlled golden set** on de-id summaries |
| Custom RBAC | Platform handles it | Unity Catalog + SLAP scopes + MCP OBO |
| System version snapshot | GitLab/process | `.gitlab-ci.yml` artifact retention, DAB deploy SHA |

### 1.4 Ontology anti-hallucination (Ali / Nav)

FHIR IGs + MDP registry + MCP read-only tools **reduce invalid queries** — same principle as ontology in Genie:

- Agents call `onyx.mcp.fhir_read` with allowlisted tools, not free-text SQL
- RAG indexes cite `cms_compliance` and SAM schema docs
- Invalid tool names flagged as **behavioral hallucination signal**

### 1.5 Evaluation dataset

| Governance PDF | Interop equivalent |
|----------------|-------------------|
| Purple Labs baseline | Synthea 10-patient local + PulseEHR 1K subset |
| 50–1000 controlled questions | Cheat Sheet golden eval (target 200 questions) |
| SME feedback | Weekly sample review in Phase 4D checklist |

### 1.6 Phase 3 future (not MVP)

- Real-time embedded metrics in user response
- AI/BI dashboards for governance KPIs
- Drift + lineage correlation into trust scores

---

## Part 2 — CCA Working Session Alignment

CCA (Complex Claim Audit) is a **separate product** but shares platform concerns. This solution **does not implement DRG audit UI**; it **does** adopt cross-cutting engineering patterns.

### 2.1 Concerns mapped

| CCA concern | Considered in interop solution? | Where |
|-------------|--------------------------------|-------|
| MVP scope too broad — narrow to "aha moment" | Yes — phased plan; AI Phase 4 after CMS path | Plan Phases 0–4 |
| Medical record summarization + DRG evidence | **Adjacent** — not CMS interop scope | Section 2.3 below |
| Product content vs engineering mechanisms | Yes — Luisa/SME content vs pipeline/agents | RACI in plan |
| Rules engine build-vs-buy (Coverself) | CCA-specific | Leadership decision log |
| UI/application architecture unowned | Partial — Developer Portal + decision required for CCA UI | RACI + 2.4 |
| Replit PDLC not ready | Documented as assumption/risk | 2.4 |
| SecOps + pen test for customer UI | Yes | `security_checklist_interop.md`, DevOps Wiz gate |
| Data before AI | Yes | Phase 1 exit before Phase 4 |
| Synthetic medical records realism | Yes — Synthea labeled demo; PulseEHR for scale path | Step 4 LEARN |
| Clinical SME required for audit content | CCA-specific | Not in interop team scope |
| Generic LLM insufficient for clinical coding | Yes — RAG + IG-grounded agents, no diagnosis | Agent prompts + gateway |
| **Metrics defined early** | **Added** | Component 13, Step 8 |
| Implementation team not involved early | **Added** | Phase 3 Forward Deployed gate |
| Named individual owners vs team-only | **Added** | Leadership decision log template |
| Demo vs POC vs production-deployable | **Added** | Readiness levels 2.5 |
| Everything inside Abacus perimeter | Yes | No external LLM without gateway |
| Profiling / filtering / scoring for audit queue | CCA-specific | Reuse `ai_events` + SAM patterns |

### 2.2 CCA "aha moment" (reference only)

If leadership selects **DRG validation + medical record evidence** as CCA MVP:

- **Engineering mechanisms** this platform already provides: de-id SAM, RAG over policies, MCP read of clinical SAM, governance metrics, Unity AI Gateway
- **Still requires:** audit rules content (Luisa), UI owner, real client data or approved client dev environment, implementation team (Mahesh)

### 2.3 Adjacent product track (optional Phase 5)

Not blocking CMS Jan 2027. Document for portfolio planning:

| Workstream | Owner (TBD by Nav) | Depends on interop |
|------------|-------------------|-------------------|
| CCA rules + profiling | Product + Data Eng / partner | Claims SAM, MDM |
| MR summarization agent | AI Engineering | Rail C clinical SAM, gateway, governance metrics |
| Auditor UI | **Unresolved** — Replit / Deepa / Product Eng | SLAP auth, API layer |
| SecOps client UI | Shared SecOps | Pen test gate in DevOps checklist |

### 2.4 Leadership decision log (from CCA session)

| Decision | Options | Impact |
|----------|---------|--------|
| MVP readiness level | demo / POC / production-client | Scope, SecOps, implementation hours |
| CCA content area | DRG vs other (Lisa/Luisa) | AI eval set, rules complexity |
| UI path | Replit vs internal K8s vs partner | 60-day feasibility |
| UI owner | AI Eng vs Product Eng vs Deepa | Staffing |
| Rules engine | Build vs Coverself vs hybrid | Data eng capacity |
| Implementation involvement | Mahesh team from Phase 3 vs Phase 5 | Client data access |
| Named milestone owners | Individual vs team RACI | Execution risk |

### 2.5 Readiness levels (explicit)

| Level | Definition | Interop phase example |
|-------|------------|----------------------|
| **Demo** | Local/Synthea, no client deploy | Phase 0–1 local stack |
| **POC** | Dev/stage with subset data, internal users | Phase 2–3 stage soak |
| **Production-client** | SecOps sign-off, pen test, implementation runbook | Phase 3–4 CMS go-live |

John's "production-ready for client" expectation maps to **Production-client** — requires Phase 3 DevOps + SecOps gates, not Phase 4 AI alone.

---

## Part 3 — Implementation Checklist

### Phase 4E — AI Governance (new)

- [ ] MLflow tracing enabled on all agent/gateway calls
- [ ] Delta tables: `interaction_traces`, `metric_results`
- [ ] Daily batch job: hallucination rate (alpha)
- [ ] Controlled query set ≥ 50 questions documented
- [ ] Weekly governance notebook / CSV report
- [ ] Phase 2 backlog: bias + trustworthiness pipelines
- [ ] SME review slot for flagged traces

### Cross-cutting (CCA + Governance)

- [ ] Metrics defined **before** agent UAT (not after)
- [ ] Implementation team in Phase 3 deploy tabletop
- [ ] Leadership decision log reviewed quarterly
- [ ] Synthetic vs real data labeled on all demos

---

## References

- `configs/ai/governance_metrics.yaml`
- `pipeline/ai/governance_metrics.py`
- `implementation_details.md` — Component 13
- Plan v3.1 — Phase 4E
- Source PDFs: `Interview/AI+Governance+-+review+and+prioritization+of+MVP+features.pdf`, `Interview/CCA+Working+Session+-+Dev+Milestones+and+Estimates+-+AI+Engineering.pdf`
