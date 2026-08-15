[← 12](12-data-models.md) · [Index](../WISCONSIN_EHR_SOLUTION_BLUEPRINT.md) · [Next →](14-go-live.md)

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
