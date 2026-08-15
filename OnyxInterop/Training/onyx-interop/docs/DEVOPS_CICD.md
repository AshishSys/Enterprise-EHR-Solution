# DevOps & CI/CD — Healthcare Interop Solution

> **Owner:** Platform / DevOps (shared with Forward Deployed Engineering)  
> **Goal:** Every merge to `main` is validated, tested, and deployable via gated pipelines — no manual-only releases for CMS-critical paths.

---

## CI/CD Architecture

```
Developer PR
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│  GitLab CI (.gitlab-ci.yml)                              │
│  validate → test → security → build → deploy-stage → prod│
└─────────┬───────────────────────────────────────────────┘
          │
    ┌─────┴─────┬─────────────┬──────────────┐
    ▼           ▼             ▼              ▼
 pytest    FHIR validate  terraform/helm  DAB deploy
           baseline       lint            (stage/prod)
    │
    ▼
 Seiji canary (EKS) — Firely / FITE / SLAP helm charts
    │
    ▼
 CMS smoke: SLAP token → FITE $everything → metrics reporter
```

---

## Pipeline Stages

| Stage | Jobs | Blocks merge if fail? |
|-------|------|------------------------|
| **validate** | lint, configs, terraform, helm, DAB validate | Yes (except TF/DAB if tooling absent) |
| **test** | pytest, FHIR baseline pipeline | Yes |
| **security** | PHI literal scan, secrets grep | Yes on main |
| **build** | FSI Docker image | Manual |
| **deploy-stage** | DAB stage, Seiji stage | Manual gate |
| **deploy-prod** | DAB prod, Seiji prod | Manual + approval |

---

## Local CI (before every push)

```bash
cd Training/onyx-interop
chmod +x scripts/ci/run_ci_local.sh
./scripts/ci/run_ci_local.sh
```

---

## Required GitLab CI/CD Variables

| Variable | Scope | Purpose |
|----------|-------|---------|
| `DATABRICKS_HOST` | stage/prod deploy | Workspace URL |
| `DATABRICKS_CLIENT_ID` | stage/prod deploy | SP for bundle deploy |
| `DATABRICKS_CLIENT_SECRET` | stage/prod deploy | SP secret (masked) |
| `AWS_ACCESS_KEY_ID` | Seiji/terraform | EKS deploy |
| `AWS_SECRET_ACCESS_KEY` | Seiji/terraform | EKS deploy |
| `SEIJI_MANIFEST` | deploy jobs | Target environment manifest |

Never commit secrets — use GitLab masked variables only.

---

## Databricks Asset Bundles (DAB)

```bash
databricks bundle validate -t dev
databricks bundle deploy -t stage    # after MR merge + CI green
databricks bundle deploy -t prod     # manual job + change ticket
```

Workflow families in `databricks.yml`: Claims, Clinical, Rail C Autoloader, SAM maintenance.

---

## Seiji Deploy Integration

1. CI `test` stage green on `main`
2. Manual trigger `deploy:stage:seiji`
3. Canary 10% → health check → 100%
4. CMS smoke test job (post-deploy hook)
5. Prod deploy only after stage soak 24h

Reference: [seiji_deploy_rollback_runbook.md](../../../seiji_deploy_rollback_runbook.md)

---

## Branch Strategy

| Branch | CI | Deploy |
|--------|-----|--------|
| `feature/*` | MR pipeline (validate + test) | None |
| `release/*` | Full pipeline | stage (manual) |
| `main` | Full + security | stage/prod (manual) |

---

## CMS Go-Live Gate

Production deploy blocked unless:

- [ ] pytest + FHIR baseline green on commit SHA
- [ ] `validate_fhir_output.py --strict` pass on staging FHIR export
- [ ] Helm lint + terraform validate pass
- [ ] Wiz scan clean on FSI image (build stage)
- [ ] CMS metrics reporter smoke on stage
- [ ] Change ticket approved

---

## Troubleshooting

| Failure | Fix |
|---------|-----|
| FHIR baseline count 0 | Check `source_data/` present in repo |
| pytest import error | `pip install -r requirements.txt` |
| terraform validate | `cd terraform && terraform init -backend=false` |
| bundle validate auth | Export `DATABRICKS_HOST` + configure SP OAuth |
| Seiji deploy fail | Check EKS kubeconfig + helm values diff |
