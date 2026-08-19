# Postman API Role — Cambia Facets Claims

> **Pillar P4:** Validate orchestration and FHIR contracts before every migration gate and prod promotion.

---

## Your Role

As Postman/API engineer on Facets Claims you:

1. **Define API contracts** at each E2E handoff (orchestration, FHIR gateway)
2. **Build collections** scoped to cambia02 dev/stg/prd environments
3. **Run newman smoke** in CI and cutover gates — fail closed on red
4. **Never store PHI** in collection bodies, examples, or committed env files

---

## Collections

| File | Purpose | Run when |
|------|---------|----------|
| `postman/cambia-facets-claims-smoke.json` | Orchestration manifest-received + job status | Every batch |
| `postman/fhir-claims-interop.json` | GET Claim/Coverage/Diagnosis — Interop path | After gold.fm_claim load |
| `postman/fhir-claims-cdp.json` | GET Claim — CDP full set | After gold.fm_claim_cambia load |
| `postman/cambia-facets-cutover-gate.json` | All folders — pre-prod promotion | stg→prd gate only |

---

## Environment Variables

Store in `postman/env/<env>.json` (gitignored secrets) or Postman cloud:

| Variable | Example | Notes |
|----------|---------|-------|
| `base_url_orchestration` | `https://orchestration-dev.internal` | ng-orchestration-service |
| `base_url_fhir` | `https://fhir-dev.internal/fhir` | FITE/gateway |
| `tenant` | `cambia02` | Always |
| `test_claim_id` | synthetic UUID | Rotate per env; no real claim IDs |
| `auth_token` | secret | Postman secret type; never commit |

---

## Newman Commands

```bash
# Dev smoke (orchestration only)
newman run postman/cambia-facets-claims-smoke.json \
  -e postman/env/dev.json --bail

# Stg FHIR Interop after gold load
newman run postman/fhir-claims-interop.json \
  -e postman/env/stg.json --folder "Claim Read" --bail

# Cutover gate (all collections)
newman run postman/cambia-facets-cutover-gate.json \
  -e postman/env/stg.json --bail
```

---

## Assertions Checklist

### Orchestration
- [ ] `POST /manifest-received` returns 202
- [ ] Job status poll reaches `SUCCESS` within SLA
- [ ] Delivery monitor shows batch ID match

### FHIR Interop
- [ ] `GET /Claim/{id}` returns 200
- [ ] `meta.profile` contains US Core Claim URL
- [ ] Dental claim IDs return 404 or empty on Interop path

### FHIR CDP
- [ ] Dental + medical claims both readable
- [ ] Row count spot-check vs gold.fm_claim_cambia sample

---

## Cutover Gate (P3 + P4)

Before stg→prd promotion **all** must pass:

1. `migration_cutover_checklist.sh` exit 0
2. `newman run postman/cambia-facets-cutover-gate.json --bail` exit 0
3. Parallel-run row-count parity signed by Facets SME (P2)
4. #xform-xport approval on workflow IDs

---

## Security

- No member IDs, claim numbers, or names in collection JSON
- Use synthetic test resources provisioned in dev/stg
- Tokens via Postman secrets or CI vault injection
- Log newman output — scrub before sharing

---

## Cheat Sheet Sections

- **E** (Q74–94): FHIR/SAM API implementation + Postman validation
- **O** (Q206–250): Orchestration APIs
- **AB** (Q536–553): Collections + Cambia cutover
