# CMS-0057 API Auth Paths — PAA, PVA, P2P

> Source: Onyx CMS-0057 APIs – Auth Paths architecture diagram.  
> **Shared runtime:** SLAP → FITE → FHIR Store. **Different:** IGs, scopes, auth models.

---

## Three paths (one platform)

| Path | API | Actor | Auth model | Gateway | SLAP | FITE route | IGs |
|------|-----|-------|------------|---------|------|------------|-----|
| **A — PAA** | Patient Access | Member via third-party app | **Member SAML** → OAuth/SMART (PKCE) | — | SAML federation from payer IdP | carin-bb / us-core | US Core + CARIN BB |
| **B — PVA** | Provider Access | External provider/payer system | **Machine auth** — `client_credentials` | Apigee/Gateway | Backend Services token | `/atr-consumer` | PDex / attribution |
| **C — P2P** | Payer-to-Payer | External payer | **Machine auth** — `client_credentials` + PDex token | Apigee/Gateway | `/pdex` scope | `/pdexv2` | PDex bulk export |

---

## Path A — Patient Access (member-facing)

```
Member → Third-party App → SLAP (SAML from Payer IdP) → OAuth/SMART token
    → FITE (carin-bb / us-core) → FHIR Store
```

- **Not** machine `client_credentials` — member login required
- Scopes: `patient/*.read`, PKCE for public clients
- Resources: Patient, EOB, Observation, etc. (Patient Access compartment)

**Local:** `slap_server.py :9000` + SMART standalone launch  
**Cloud:** SLAP on EKS + DocumentDB sessions + payer IdP SAML metadata

---

## Path B — Provider Access (attributed provider)

```
External Provider/Payer → Apigee/Gateway → SLAP (client_credentials)
    → FITE (/atr-consumer) → Provider Access APIs → FHIR Store
```

- **Machine auth** — no member SAML
- Attribution via Group / PractitionerRole resources
- Bulk `$export` for attributed panels

**Local:** `provider_access.py :9003`  
**Cloud:** Apigee + SLAP Backend Services + FITE attribution routes

---

## Path C — Payer-to-Payer (PDex)

```
External Payer → Apigee/Gateway → SLAP (client_credentials, PDex token)
    → FITE (/pdexv2) → Bulk Member Match + Data Export → FHIR Store
```

- Consent + opt-in before export
- `$bulk-member-match` then NDJSON export
- CMS-0057 deadline: Jan 2027

**Local:** `p2p_member_match.py :9004`  
**Cloud:** Same SLAP/FITE stack; PDex IG profiles on export bundles

---

## Design rules

1. **Never mix auth paths** — PAA tokens cannot call `/pdexv2`; machine tokens cannot call member `$everything` without attribution scope.
2. **FITE is the only FHIR edge** — apps and external payers never hit Firely directly.
3. **Apigee/Gateway** sits in front of PVA/P2P machine clients (rate limit, WAF, API keys).
4. **Audit** — Onyx Insights logs auth path + scope + endpoint for CMS compliance.

---

## Config reference

See `configs/mdp/auth_paths.json` for path → scope → FITE route mapping.

## Cheat Sheet

Section AB Q536–Q540; Section H (CMS-0057 APIs).
