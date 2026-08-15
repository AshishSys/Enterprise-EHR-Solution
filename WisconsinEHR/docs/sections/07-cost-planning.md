[← 06](06-cloud-native-services.md) · [Index](../WISCONSIN_EHR_SOLUTION_BLUEPRINT.md) · [Next →](08-source-files-cclf.md)

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
