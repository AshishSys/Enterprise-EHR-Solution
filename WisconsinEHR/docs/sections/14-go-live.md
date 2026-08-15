[← 13](13-uat-planning.md) · [Index](../WISCONSIN_EHR_SOLUTION_BLUEPRINT.md) · [Next →](15-interview-questions.md)

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
