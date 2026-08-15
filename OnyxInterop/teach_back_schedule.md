# InterOperability with Onyx — Teach-Back Schedule

## Overview

Each module culminates in a **30-minute teach-back session** where an engineer presents how the concepts map to Abacus/Onyx components. Sessions are scheduled weekly on **Thursdays** (allowing prep time after module study).

**Start date:** Thursday, July 16, 2026  
**End date:** Thursday, September 24, 2026  
**Duration:** 10 weeks (with 2 buffer weeks for catch-up/deep dives)

---

## Schedule

| Week | Date (Thursday) | Module | Teach-Back Topic | Presenter | Artifacts to Reference |
|------|-----------------|--------|------------------|-----------|------------------------|
| 1 | Jul 16, 2026 | M1 (Part A) | FHIR R4 Basics & IG Deep Dive | TBD | #3 FHIR/IG Quick Reference |
| 2 | Jul 23, 2026 | M1 (Part B) | CMS-9115 vs CMS-0057 & Mandated APIs | TBD | #4 CMS Implementation Map |
| 3 | Jul 30, 2026 | M2 | E2E Onyx Architecture & Ownership | TBD | #1 Architecture Deck, #2 Ownership Matrix |
| 4 | Aug 6, 2026 | M3 (Part A) | Databricks Workflows: Structure & Pipeline Steps | TBD | #5 Databricks Handbook |
| 5 | Aug 13, 2026 | M3 (Part B) | Databricks Workflows: Troubleshooting & Recovery | TBD | #5 Databricks Handbook |
| 6 | Aug 20, 2026 | M4 | Firely & HealthLake Engineering | TBD | #7 Firely vs HealthLake Matrix |
| 7 | Aug 27, 2026 | M5 | Seiji Deployment & Rollback | TBD | #6 Seiji Deploy Runbook |
| 8 | Sep 3, 2026 | M6 | Security, Scalability & Performance | TBD | #9 Performance Checklist, #10 Security Checklist |
| 9 | Sep 10, 2026 | M7 | Production Defect Troubleshooting & RCA | TBD | #8 Production Issue Taxonomy |
| 10 | Sep 17, 2026 | — | **Capstone:** Cross-module integration exercise | All | All artifacts |

**Buffer week:** Sep 24 — catch-up, retakes, or deep-dive on areas needing more coverage.

---

## Session Format (30 minutes each)

| Time | Activity |
|------|----------|
| 0–5 min | Context setting — what problem does this module solve? |
| 5–20 min | Technical deep dive — concepts mapped to Abacus/Onyx components |
| 20–25 min | Live demo or walkthrough (optional: show relevant artifact) |
| 25–30 min | Q&A and discussion |

---

## Presenter Assignment Guidelines

- Each engineer should present **at least 1 module** (ideally 2)
- Assign based on area of interest or growth area (not just comfort zone)
- Suggested pairings:

| Engineer Focus Area | Recommended Modules |
|--------------------|---------------------|
| Data Engineering / ETL | M3 (Databricks), M2 (Architecture) |
| Backend / API Development | M1 (FHIR/CMS), M4 (Firely/HealthLake) |
| DevOps / SRE | M5 (Seiji), **M8 (GitLab CI/DAB)**, M6 (Security/Performance) |
| AI Engineering / Governance | M9 (MLflow metrics), M6 (Security) |
| Product / CCA-adjacent | M9 (CCA decision log), M2 (Architecture) |
| Full-stack / Generalist | M2 (Architecture), M7 (Production Issues) |

---

## Preparation Checklist (per presenter)

- [ ] Read the assigned artifact(s) thoroughly
- [ ] Identify 3 key takeaways for the team
- [ ] Prepare at least 1 real-world scenario or example
- [ ] Create a brief slide deck OR whiteboard walkthrough
- [ ] Prepare 2–3 discussion questions for the team
- [ ] (Optional) Hands-on demo of a tool, config, or workflow
- [ ] Share materials with team 24 hours before session

---

## Study Plan (per week)

| Day | Activity |
|-----|----------|
| Monday | Read assigned artifact + any linked references |
| Tuesday | Hands-on exploration (access systems, try commands) |
| Wednesday | Prepare teach-back presentation |
| Thursday | **Deliver teach-back** (30 min) |
| Friday | Reflect, document learnings, update team wiki |

---

## Capstone Exercise (Week 10)

**Scenario:** A production incident occurs where:
- A Claims workflow fails in Databricks
- FHIR Load produces duplicate records in HealthLake
- Provider Directory API returns stale data through FITE
- The team needs to rollback a Seiji deployment

**Exercise format:**
1. Each engineer applies their module knowledge
2. Team collaborates to trace the issue end-to-end
3. Group produces a mock RCA using the template from Artifact #8
4. Review ownership boundaries and escalation paths

---

## Success Criteria

By the end of the 10-week program, each engineer should be able to:

- [ ] Explain the full data flow from Raw → FHIR Store → API Response
- [ ] Identify which team (Abacus/Onyx) owns each component
- [ ] Diagnose common production issues using the troubleshooting guides
- [ ] Execute a Seiji deployment and rollback safely
- [ ] Review changes against the security and performance checklists
- [ ] Write a proper RCA following the team template
- [ ] Navigate CMS-9115 and CMS-0057 compliance requirements
