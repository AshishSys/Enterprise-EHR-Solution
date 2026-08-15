[← 09](09-implementation-guide.md) · [Index](../WISCONSIN_EHR_SOLUTION_BLUEPRINT.md) · [Next →](11-brd.md)

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
