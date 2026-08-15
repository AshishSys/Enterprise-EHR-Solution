[← 04](04-technical-architecture.md) · [Index](../WISCONSIN_EHR_SOLUTION_BLUEPRINT.md) · [Next →](06-cloud-native-services.md)

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
