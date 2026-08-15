#!/usr/bin/env python3
"""Generate Section Z DevOps/CI/CD Q&A and append before Glossary."""

from pathlib import Path

CHEAT = Path("/Users/ashishsingh/Interview/Healthcare_Interop_Interview_Cheat_Sheet.md")
BASE = "/Users/ashishsingh/OnyxInterop/Training/onyx-interop"

QUESTIONS = [
    ("What is the CI/CD architecture for the healthcare interop platform?",
     "I use GitLab CI with stages validate → test → security → build → deploy-stage → deploy-prod. Every MR runs pytest + FHIR baseline; merges to main unlock manual Seiji and Databricks bundle deploys. No direct prod push without green CI on the commit SHA.",
     "MR #442: validate + test green → manual stage Seiji → CMS smoke → prod gate next day.",
     "`.gitlab-ci.yml` stage list; MR pipeline view; `deploy:prod:seiji` manual job history",
     "Add missing job to CI if new component (e.g. Rail B Lambda); wire post-deploy smoke",
     "bash", f"""#!/usr/bin/env bash
cd {BASE}
./scripts/ci/run_ci_local.sh
"""),
    ("What runs on every merge request in GitLab CI?",
     "MR pipeline runs: Python compile, config existence checks, pytest, full interop_pipeline + validate_fhir_output, terraform validate, helm lint. Security scans on main only. Deploy jobs never run on MR.",
     "Feature branch MR shows 6 validate/test jobs — all green before merge allowed.",
     "GitLab MR → Pipelines tab; job logs for test:unit and test:fhir-baseline",
     "Fix failing job locally with run_ci_local.sh before pushing",
     "bash", f"cd {BASE} && ./scripts/ci/run_ci_local.sh"),
    ("How do you run CI checks locally before push?",
     "I run `scripts/ci/run_ci_local.sh` — mirrors GitLab validate + test stages: compileall, pytest, FHIR pipeline, optional terraform/helm/bundle validate.",
     "Pre-push hook or habit: run_ci_local.sh — 2 min — catches 90% of CI failures.",
     "Script exit 0; same pytest count as CI artifact",
     "Install missing tools (helm, terraform) or accept SKIP lines; fix pytest first",
     "bash", f"chmod +x {BASE}/scripts/ci/run_ci_local.sh && {BASE}/scripts/ci/run_ci_local.sh"),
    ("How do Databricks Asset Bundles fit in CI/CD?",
     "databricks.yml defines workflow families per target (dev/stage/prod). CI job `databricks:bundle-validate` runs on MR; deploy-stage/prod jobs call `databricks bundle deploy -t {env}` manually after merge.",
     "Bundle validate catches YAML typo before stage deploy; prod deploy pinned to release tag SHA.",
     "`databricks bundle validate -t dev` locally; CI job log",
     "Fix bundle permissions block for SP; pin cluster policy ID in target",
     "bash", f"cd {BASE} && databricks bundle validate -t dev 2>/dev/null || echo 'Configure Databricks auth'"),
    ("What is the branch strategy for interop releases?",
     "feature/* → MR to main with CI gate; release/* for staged soak; main only for production manual deploys. Hotfix branch from main tag, CI full run, expedited prod approval with ticket.",
     "Hotfix CMS-9115 scope typo: release/2.4.1 from tag v2.4.0 — CI green — prod Seiji 2h.",
     "GitLab protected branches; main requires MR + pipeline success",
     "Unprotect main if emergency — restore protection after hotfix",
     "bash", "git branch -a | head -20 && git log -1 --oneline"),
    ("How do you gate production Seiji deploys on CI success?",
     "deploy:prod:seiji is manual, runs only on main, requires same commit SHA as last green test:fhir-baseline. Change ticket ID in job variable. Canary 10% before full promotion.",
     "Prod deploy job checks CI_COMMIT_SHA matches last green pipeline on main.",
     "GitLab environment production deploy history; canary pod ratio",
     "Rollback via Seiji previous manifest if canary error rate > 1%",
     "bash", f"cd {BASE} && test -x bin/seiji && bin/seiji --help 2>/dev/null || echo 'Seiji shim at bin/seiji'"),
    ("How do you CI-test the FHIR baseline pipeline?",
     "Job test:fhir-baseline runs interop_pipeline on source_data, validate_fhir_output, asserts JSON file count > 0. Artifact fhir_output/ retained 1 day for debugging.",
     "MR breaks Patient transform — baseline job fails — merge blocked.",
     "CI artifact download; resource count matches ~9997 locally",
     "Fix transformer; re-run pipeline locally; push fix",
     "bash", f"cd {BASE} && python interop_pipeline.py --input ./source_data --output ./fhir_output && python scripts/validate_fhir_output.py ./fhir_output"),
    ("What security jobs run in CI for HIPAA workloads?",
     "security:phi-scan greps for hardcoded PHI patterns in pipeline/configs; security:secrets-scan greps for AWS keys/password literals. Complement with Wiz on container build (manual build stage).",
     "Catches accidental member_ssn= in test fixture — MR blocked on main branch scan.",
     "CI security stage logs; zero matches on intentional test",
     "Move test data to fixtures/deidentified/; rotate leaked key immediately",
     "bash", f"cd {BASE} && grep -rEn 'AKIA[0-9A-Z]{{16}}' . --include='*.py' --include='*.yaml' 2>/dev/null | head -5 || echo 'No AWS keys found'"),
    ("How do you store CI secrets for Databricks and AWS?",
     "GitLab CI/CD variables: DATABRICKS_HOST, CLIENT_ID, CLIENT_SECRET (masked), AWS keys for Seiji. Never in repo. SP OAuth preferred over PAT. Rotate 90 days.",
     "Stage deploy uses masked variables — logs show [MASKED] only.",
     "GitLab Settings → CI/CD → Variables; audit masked + protected flags",
     "Revoke leaked secret; update variable; re-run failed deploy job",
     "bash", "echo 'Use GitLab UI for secrets — never echo in CI logs'"),
    ("How does Helm lint integrate into CI?",
     "Job helm:lint runs `helm lint helm/firely-server/` and template render on every MR. Catches invalid YAML and missing required values before EKS deploy.",
     "Typo in values.yaml replicas — helm lint fails MR.",
     "helm lint locally; match CI job output",
     "Fix chart values; helm template diff against stage cluster",
     "bash", f"cd {BASE} && helm lint helm/firely-server/ && helm template firely helm/firely-server/ | head -20"),
    ("How does Terraform validate integrate into CI?",
     "Job terraform:validate runs init -backend=false + validate on terraform/. Catches module syntax errors before infra MR merge.",
     "Bad output reference in modules/eks — validate fails.",
     "cd terraform && terraform validate",
     "Fix HCL; run plan in dev account before apply",
     "bash", f"cd {BASE}/terraform && terraform init -backend=false && terraform validate"),
    ("What is the FSI Docker build job in CI?",
     "build:fsi-image manual job on main — docker build docker/fsi-job/ tagged with CI_COMMIT_SHORT_SHA. Wiz scan before prod tag promotion.",
     "FSI image interop-fsi:abc1234 deployed to stage EKS job.",
     "GitLab container registry or ECR tag list",
     "Fix Dockerfile if build fails; pin base image digest",
     "bash", f"cd {BASE} && docker build -t interop-fsi:local docker/fsi-job/"),
    ("How do you add a new workflow family to CI/CD?",
     "1) Add notebook/tasks to databricks.yml 2) Add pytest for transformer 3) Extend test:fhir-baseline if new resource types 4) Update bundle validate 5) Document in DEVOPS_CICD.md",
     "Added ePA family — bundle job epa_workflow — CI validate passes — stage deploy.",
     "databricks.yml diff; pytest new test file; CI green",
     "Missing task dependency in bundle — fix depends_on chain",
     "bash", f"cd {BASE} && python -m pytest tests/ -v --co | wc -l"),
    ("What post-deploy smoke tests run after stage Seiji?",
     "CMS smoke: SLAP token → FITE /metadata → GET Patient → cms_metrics_reporter dry-run. Fail stage soak if any step non-200.",
     "Stage deploy Thursday — smoke script — uptime metric row inserted.",
     "curl stage FITE /metadata; Insights metrics endpoint",
     "Fix SLAP-FITE service mesh routing if 502",
     "bash", f"curl -sf http://localhost:8080/metadata | head -5 || echo 'Start local stack for smoke'"),
    ("How do you version interop releases in CI?",
     "Git tags v{major}.{minor}.{patch} on main after prod deploy. Bundle deploy uses tag SHA. Release notes link CI pipeline ID + FHIR resource count from baseline job.",
     "v2.5.0 tag — pipeline 88421 — 9997 baseline resources.",
     "git tag -l 'v*'; GitLab Releases page",
     "Never retag — new patch version for hotfix",
     "bash", "git describe --tags --always 2>/dev/null || echo 'no tags yet'"),
    ("How do you rollback a bad Databricks bundle deploy?",
     "databricks bundle deploy rollback or redeploy previous git tag bundle. Restore SAM tables via Delta RESTORE if bad merge coincided. Never rollback prod without incident ticket.",
     "Bad Claims extract config — redeploy v2.4.0 bundle — SAM RESTORE TO VERSION.",
     "Bundle deploy history; DESCRIBE HISTORY on affected SAM table",
     "Fix forward on new patch; document in RCA",
     "bash", "echo 'databricks bundle deploy -t prod --rollback  # when supported'"),
    ("How do CI/CD and Unity Catalog governance interact?",
     "Bundle deploy uses SP with UC grants per target catalog (dev/stage/prod_interop). CI validate fails if bundle references catalog SP cannot write. Prod catalog has no human write.",
     "Stage SP blocked on prod_interop — validate catches before deploy.",
     "UC grants audit; bundle permissions block in databricks.yml",
     "Add permissions block for SP on new schema before deploy",
     "python", "# UC grant check in notebook\n# SHOW GRANTS ON CATALOG stage_interop"),
    ("How do you CI-test Rail B Lambda before deploy?",
     "Unit test webhook handler JSON schema; optional integration test with LocalStack SQS. Separate repo ng-nasco-event-api has own pipeline — contract test against schema version.",
     "Lambda unit test 400 on missing claim_id — blocks Terraform apply MR.",
     "pytest tests/test_webhook*.py; JSON schema validator",
     "Add schema version bump + dual-topic overlap period",
     "python", "import json\nschema={'required':['member_id','claim_id']}\nprint(json.dumps(schema))"),
    ("What is GitOps vs CI/CD in this solution?",
     "GitLab CI is push-based CI/CD for builds/tests/deploy triggers. GitOps (Helm values in Git) is source of truth for K8s desired state — Seiji reconciles cluster to manifest. Both required: CI proves commit; GitOps proves cluster state.",
     "Helm values change in Git — Seiji sync — CI already validated chart at that SHA.",
     "Git helm values hash vs cluster live values diff",
     "Drift: cluster manual kubectl edit — re-sync from Git",
     "bash", f"cd {BASE} && helm template firely helm/firely-server/ -f helm/firely-server/values.yaml | grep -c 'kind:'"),
    ("How do you monitor CI pipeline health for the program?",
     "Track MR pipeline pass rate, median duration, test:fhir-baseline flake rate. Alert if main pipeline red > 2h. Payer Ops Agent optional ingest of GitLab webhook failures.",
     "Main red 3h — PagerDuty — broken pytest import after pandas bump.",
     "GitLab CI analytics; failed job notification email",
     "Pin dependency version; add retry for flaky network jobs only",
     "bash", "echo 'Configure GitLab pipeline failure notifications to #interop-oncall'"),
    ("How do environment promotion gates work?",
     "dev (auto on feature MR) → stage (manual on main) → prod (manual + ticket + 24h soak). FHIR strict validation required at stage; CMS metrics reporter must succeed before prod.",
     "Stage soak 24h green — change ticket CHG-8842 — prod deploy Friday 6pm UTC.",
     "GitLab environments timeline; change ticket link in deploy job",
     "Extend soak if CMS smoke flaky — do not skip gate",
     "bash", "echo 'Stage soak checklist in docs/DEVOPS_CICD.md'"),
    ("How do you parallelize CI for faster MR feedback?",
     "validate jobs parallel (lint, terraform, helm, bundle); test jobs after validate. Cache pip/.venv per branch slug. FHIR baseline only on MR to main-bound branches if needed for speed.",
     "MR feedback 8min → 4min after parallel validate.",
     "GitLab pipeline graph; job duration trends",
     "Do not skip FHIR baseline on main-target MRs",
     "bash", f"cd {BASE} && time python -m pytest tests/ -q"),
    ("What artifacts does CI retain for audit?",
     "JUnit report.xml, fhir_output/ 1 day, Docker image tags, deploy job logs, environment URL. CMS audit may request pipeline ID for prod deploy SHA.",
     "Auditor asks prod FHIR build — pipeline 88421 artifact fhir_output downloaded.",
     "GitLab job artifacts; retention policy settings",
     "Extend artifact retention for compliance hold tickets",
     "bash", "echo 'CI_COMMIT_SHA and pipeline ID logged in deploy job output'"),
    ("How do you integrate Wiz security scan in CI/CD?",
     "After build:fsi-image, Wiz CLI scan image — fail build if CRITICAL. Lambda images in ng-nasco-event-api separate pipeline. Block prod promote on unresolved CRITICAL.",
     "Wiz CRITICAL on fsi base image — prod promote blocked — base image bump.",
     "Wiz dashboard scan results; CI job wiz-scan log",
     "Fix CVE via base image update; re-run build job",
     "bash", "echo 'wizcli scan --image interop-fsi:$TAG  # in build pipeline'"),
    ("How do DevOps engineers learn this stack in Step 1?",
     "Day 1: run run_ci_local.sh. Week 7: read DEVOPS_CICD.md, trace .gitlab-ci.yml, manual stage deploy drill. Cheat Sheet Section Z Scripts.",
     "New hire green run_ci_local day 1; shadow stage deploy week 2.",
     "LEARN_FROM_STEP_1 Step 7; personal tracker DevOps items ticked",
     "Pair with Forward Deployed on first Seiji canary",
     "bash", f"cd {BASE} && ./scripts/ci/run_ci_local.sh"),
    ("Scenario: main pipeline red blocks prod CMS hotfix. What do you do?",
     "Identify failing job — if test:fhir-baseline, fix data/transformer; if infra flake, retry once; if urgent CMS scope fix only in runtime (not pipeline), expedite hotfix branch with narrowed test scope + leadership approval — never skip security on main.",
     "pytest fail on unrelated module — fix or quarantine test — hotfix proceeds in 90min.",
     "Failed job log; fix commit; re-run pipeline",
     "Document any gate bypass in incident + retro",
     "bash", f"cd {BASE} && python -m pytest tests/ -v --tb=short"),
    ("How does CI validate extract_config YAML changes?",
     "validate:configs job checks file existence; pytest integration tests load YAML and assert required keys. Add schema test when extract config structure changes.",
     "Renamed column in extract_config — pytest test_extract_config_keys fails MR.",
     "pytest tests/test_*config*; yaml.safe_load in CI",
     "Update test golden keys when intentional schema change",
     "python", f"import yaml\nfrom pathlib import Path\np=Path('{BASE}/configs/workflows/claims/extract_config.yaml')\nprint(list(yaml.safe_load(p.read_text()).keys()) if p.exists() else 'missing')"),
    ("What is the CMS go-live CI/CD checklist?",
     "pytest green, FHIR strict pass, helm+tf validate, Wiz clean, stage smoke 24h, metrics reporter, change ticket, prod manual deploy, post-prod smoke, tag release.",
     "Jan 2027 go-live — checklist 12/12 — tag v3.0.0.",
     "docs/DEVOPS_CICD.md CMS Go-Live Gate section",
     "Any unchecked item blocks prod — no exceptions without CISO sign-off",
     "bash", f"cat {BASE}/docs/DEVOPS_CICD.md | grep -A20 'CMS Go-Live Gate'"),
    ("How do you add GitLab CI for ng-nasco-event-api (Rail B)?",
     "Separate repo pipeline: validate Terraform, pytest Lambda handler, deploy dev/stage/prod API Gateway stages. Contract test publishes schema to MDP registry on prod.",
     "NASCO repo CI — Lambda test — Terraform plan — stage API GW deploy.",
     "ng-nasco-event-api repo .gitlab-ci.yml if present",
     "Share schema contract test artifact with Abacus Bronze ingest CI",
     "python", "# Lambda handler schema test pattern\nassert 'claim_id' in required_fields"),
    ("What DevOps skills does Section Z build for interviews?",
     "GitLab CI stage design, DAB deploy gates, Seiji canary, secret management, FHIR baseline as CI test, CMS go-live checklist, rollback discipline — maps to DevOps Engineer + Forward Deployed roles.",
     "Interview whiteboard: MR → CI → stage → smoke → prod with CMS gates labeled.",
     "Cheat Sheet Z Scripts all run green; can explain each CI job purpose",
     "Run Q486–Q515 Scripts before DevOps-focused interviews",
     "bash", f"cd {BASE} && ./scripts/ci/run_ci_local.sh && echo 'Section Z DevOps baseline OK'"),
]


def block(qnum: int, title: str, answer: str, example: str, check: str, fix: str, lang: str, script: str) -> str:
    checks = "\n".join(f"- {c.strip()}" for c in check.split(";"))
    fixes = "\n".join(f"- {c.strip()}" for c in fix.split(";"))
    roles = "DevOps Engineer | Forward Deployed Engineer"
    return f"""
### Q{qnum}. {title}

**Answer:** {answer}

**Example:** {example}

**How to Check:**
{checks}

**How to Fix:**
{fixes}

**Script:** *(builds proficiency: {roles})*

```{lang}
{script.strip()}
```

---
"""


def main() -> None:
    text = CHEAT.read_text(encoding="utf-8")
    if "## Section Z:" in text:
        print("Section Z already exists")
        return

    lines = ["\n## Section Z: DevOps & CI/CD (Q486–515)\n"]
    for i, (title, ans, ex, chk, fx, lang, scr) in enumerate(QUESTIONS, start=486):
        lines.append(block(i, title, ans, ex, chk, fx, lang, scr))

    section = "".join(lines)
    marker = "\n## Glossary"
    if marker not in text:
        raise SystemExit("Glossary marker not found")
    text = text.replace(marker, section + marker, 1)
    CHEAT.write_text(text, encoding="utf-8")
    print(f"Added Section Z Q486-Q{485 + len(QUESTIONS)}")


if __name__ == "__main__":
    main()
