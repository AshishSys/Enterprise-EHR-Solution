[← 15](15-interview-questions.md) · [Index](../WISCONSIN_EHR_SOLUTION_BLUEPRINT.md)

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
