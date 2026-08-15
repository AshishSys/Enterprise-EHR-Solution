# InterOperability with Onyx — Implementation Plan

## Project Overview — ✅ All Artifacts Complete (Jul 7, 2026)

**Goal:** Build deep engineering expertise across CMS interoperability, Onyx architecture, Databricks workflows, FHIR stores, deployment, security, and production troubleshooting.

**Core Architecture (from PDF):**
- **Data Pipeline (Abacus-led):** Client Data → Raw Ingestion → FM (Foundational Marts) → SAM (Subject Area Marts, IG-aligned) → FHIR Bundles → FHIR Store (Firely/HealthLake)
- **Runtime API Access (Onyx-led):** App → SLAP (auth/OAuth2/SMART) → FITE (FHIR gateway) → FHIR Store → Response

**Ownership Split:**
| Layer | Owner | Responsibility |
|-------|-------|----------------|
| Data pipelines, FM, SAM, DQ rules | Abacus | Data correctness, scale, CMS-0057 data accuracy |
| SLAP, FITE, Developer Portal, IGs | Onyx | Security, IG correctness, runtime interoperability |
| FHIR Store (Firely/HealthLake) | Shared | Hidden behind SLAP/FITE, no direct access |

---

## Module Execution Plan

### Module 1: Interoperability & CMS Foundation
**Duration:** 1–2 weeks | **Output:** 30-min teach-back per engineer

| Topic | Key Areas to Cover |
|-------|--------------------|
| FHIR R4 Basics | Resources, references, validation, search parameters, bundles |
| CMS-9115 vs CMS-0057 | Scope differences, timeline, enforcement, API mandates |
| Mandated APIs | Patient Access, Provider Access, Payer-to-Payer, ePA, Provider Directory |
| Security/Compliance | Consent (SMART scopes), OAuth2 auth, audit logging, reporting |

**Study Resources:**
- HL7 FHIR R4 spec (hl7.org/fhir)
- CMS Interoperability Final Rules (cms.gov)
- CARIN Blue Button IG, Da Vinci Plan-Net IG, Da Vinci Formulary IG
- US Core IG

**Artifacts to produce:**
- ✅ Artifact #3: FHIR/IG Quick Reference Guide
- ✅ Artifact #4: CMS-9115 vs CMS-0057 Implementation Map

---

### Module 2: End-to-End Onyx Architecture
**Duration:** 1–2 weeks | **Output:** Architecture diagram + failure-point map

| Topic | Key Areas to Cover |
|-------|--------------------|
| Data Flow | Raw → Bronze → Silver → Gold → SAM → FHIR |
| Components | SLAP, FITE, Firely, MongoDB, HealthLake, Onyx Insights, MDP |
| Workflows | Incremental vs historical |
| Ownership | Abacus vs Onyx boundary (as per PDF) |

**Key understanding from PDF:**
- FM = canonical, stable, NOT FHIR-shaped (optimized for reuse, correctness, incremental updates)
- SAM = IG-aligned staging layer (bridge between FM and FHIR)
- Extract task = configurable step to export SAM → CSV → FHIR bundles
- Users interact with SLAP/FITE only, never directly with Firely

**Artifacts to produce:**
- ✅ Artifact #1: Interop Architecture Overview Deck
- ✅ Artifact #2: Onyx Component Ownership Matrix

---

### Module 3: Onyx Databricks Workflows
**Duration:** 2 weeks | **Output:** Troubleshooting guide by workflow family

| Topic | Key Areas to Cover |
|-------|--------------------|
| Workflow Structure | Naming conventions, extract configs, job state table, task sequencing |
| Pipeline Steps | Transform, upload, upsert, preprocessing, extraction, termination |
| Infrastructure | Runtime image, wheel files, config INIs, Terraform definitions |
| Failure Modes | Config mismatch, validation errors, duplicates, runtime/package drift |

**Workflow Families:**
1. Claims
2. Clinical
3. Formulary
4. PVD (Provider Directory)
5. CMS-0057
6. CMS-9115

**Artifacts to produce:**
- ✅ Artifact #5: Databricks Workflow Troubleshooting Handbook

---

### Module 4: Firely & HealthLake Engineering
**Duration:** 1–2 weeks | **Output:** Decision matrix

| Topic | Key Areas to Cover |
|-------|--------------------|
| Firely | Architecture, MongoDB behavior, FSI, bulk/incremental load |
| HealthLake | Ingestion model, API limitations, validation differences |
| Migration | Coexistence constraints, unified workflows |
| Diagnosis | When problem is Firely-specific vs HealthLake-specific vs integration |

**Artifacts to produce:**
- ✅ Artifact #7: Firely vs HealthLake Support Matrix

---

### Module 5: Seiji & Deployment Engineering
**Duration:** 1–2 weeks | **Output:** Deployment runbook

| Topic | Key Areas to Cover |
|-------|--------------------|
| Deploys | Targeted deploys, manifests, components, logs |
| Config | SSM/config secrets, helm charts |
| Failures | Version mismatch, secret resolution, credentials, lock/reset, repo-shims |
| Recovery | Safe rollback, refresh-deployed behavior, validation |

**Artifacts to produce:**
- ✅ Artifact #6: Seiji Deploy and Rollback Runbook

---

### Module 6: Security, Scalability & Performance
**Duration:** 1–2 weeks | **Output:** Non-functional review checklist

| Topic | Key Areas to Cover |
|-------|--------------------|
| Security | IAM roles vs static keys, Databricks secret scopes, WAF, VPC isolation |
| Scalability | Cluster sizing, bundle sizing, retry/shred logic, parallelism |
| Performance | HealthLake + Firely tuning, workload profiling |
| Observability | Audit trails, monitoring, alerting |

**Artifacts to produce:**
- ✅ Artifact #9: Performance Tuning Checklist
- ✅ Artifact #10: Security Checklist for Interop

---

### Module 7: Production Defect Troubleshooting & RCA
**Duration:** 2 weeks | **Output:** Defect pattern library

| Topic | Key Areas to Cover |
|-------|--------------------|
| Triggers | File arrival issues, workflow schedules |
| Context | State-specific schedules, data-volume expectations |
| Classification | Expected failures vs true defects |
| Defect Classes | Data quality, mapping, workflow config, deployment, auth/network, Firely/HealthLake, performance, operational sequencing |

**Artifacts to produce:**
- ✅ Artifact #8: Production Issue Taxonomy & RCA Library

---

### Module 8: DevOps & CI/CD Engineering
**Duration:** 1–2 weeks | **Output:** GitLab CI pipeline + local CI script + deploy gates

| Topic | Key Areas to Cover |
|-------|--------------------|
| CI/CD | GitLab stages: validate → test → security → build → deploy |
| DAB | `databricks bundle validate/deploy` per environment |
| Deploy | Seiji canary, Helm lint, Terraform validate |
| Gates | CMS go-live checklist, stage soak, secret management |

**Artifacts to produce:**
- ✅ `.gitlab-ci.yml` + `databricks.yml` (Training/onyx-interop)
- ✅ `scripts/ci/run_ci_local.sh` + `docs/DEVOPS_CICD.md`
- ✅ Cheat Sheet Section Z (Q486–515)

---

## Artifact Tracker

| # | Artifact | Module | Status |
|---|----------|--------|--------|
| 1 | Interop Architecture Overview Deck | M2 | ✅ Complete |
| 2 | Onyx Component Ownership Matrix | M2 | ✅ Complete |
| 3 | FHIR/IG Quick Reference Guide | M1 | ✅ Complete |
| 4 | CMS-9115 vs CMS-0057 Implementation Map | M1 | ✅ Complete |
| 5 | Databricks Workflow Troubleshooting Handbook | M3 | ✅ Complete |
| 6 | Seiji Deploy and Rollback Runbook | M5 | ✅ Complete |
| 7 | Firely vs HealthLake Support Matrix | M4 | ✅ Complete |
| 8 | Production Issue Taxonomy & RCA Library | M7 | ✅ Complete |
| 9 | Performance Tuning Checklist | M6 | ✅ Complete |
| 10 | Security Checklist for Interop | M6 | ✅ Complete |

---

## Suggested Timeline (10–12 weeks)

```
Week 1-2:   Module 1 — CMS Foundation & FHIR basics
Week 3-4:   Module 2 — E2E Architecture
Week 5-6:   Module 3 — Databricks Workflows
Week 7:     Module 4 — Firely & HealthLake
Week 8:     Module 5 — Seiji & Deployment
Week 9-10:  Module 6 — Security & Performance
Week 11-12: Module 7 — Production Troubleshooting & RCA
```

---

## Next Steps

1. **Start with Module 1** — foundational knowledge that everything else builds on
2. **Set up a shared repo/wiki** for artifact collaboration
3. **Schedule teach-back sessions** (30 min per engineer per module)
4. **Identify internal SMEs** for each module area (Abacus team, Onyx team)
5. **Gather access** to Databricks, Seiji, HealthLake console, Firely admin for hands-on work
