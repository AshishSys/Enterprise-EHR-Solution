# Local vs Cloud Build — Healthcare Interop

> **Short answer:** You **learn locally** (Steps 1–2 ✅), then **build on AWS cloud** (Phase 0+).  
> Local is the lab; cloud is the product. Same architecture — different runtime.

---

## What runs where

| Layer | Local (your Mac) | Cloud (AWS + Databricks) |
|-------|------------------|---------------------------|
| **Learn / prove** | `interop_pipeline.py`, pytest, validation | — |
| **Raw landing** | `./source_data/` CSV | **S3** Bronze buckets |
| **Transform** | Python FM/SAM in memory | **Databricks** workflow families |
| **FHIR store** | In-memory / local NDJSON | **Firely on EKS** + HealthLake |
| **APIs** | SLAP/FITE `:9000/:8080` | **EKS** + ALB + Route53 |
| **Auth** | Local SLAP | SLAP on EKS + **DocumentDB** |
| **Config** | MDP `:9002` + JSON files | MDP + **DynamoDB** `onyx_job_state` |
| **Ingest Rail B** | — | **API Gateway → Lambda → S3/Kafka** |
| **Ingest Rail D** | — | **EKS CronJob + IRSA/WIF → BigQuery → S3** (Cambia) |
| **CMS-0057 machine auth** | Local SLAP client_credentials | **Apigee → SLAP → FITE** (`/atr-consumer`, `/pdexv2`) |
| **ePA ingress** | `epa_burden_reduction_service.py :9005` | **ALB → APISIX → CDS + dapr** on EKS |
| **CI/CD** | `run_ci_local.sh` | **GitLab CI → Seiji → EKS/DAB** |

---

## Learning path vs cloud path (same solution)

```
Steps 1–2 (DONE)     Steps 3–4           Phase 0 Cloud        Phase 1 Cloud
     │                    │                     │                    │
 Local baseline      Architecture          AWS foundation       Databricks + EKS
 CSV→FHIR proof      + data eng learn      S3/EKS/DocDB/API GW  Claims/PVD pipelines
```

| Milestone | Where | You are here |
|-----------|-------|--------------|
| Step 1 — local baseline | Mac | ✅ Done |
| Step 2 — CMS/FHIR vocab | Mac | ✅ Done (Day 3+) |
| **Phase 0 — AWS access + infra** | **Cloud** | **← Start here for cloud build** |
| Phase 1 — Databricks + Firely | Cloud | After Steps 3–4 learning |
| Phase 3 — prod hardening | Cloud | CI/CD, Wiz, go-live |

**Rule from LEARN guide:** Phase 0 cloud access can start after Step 1 ✅ (you qualify now).

---

## Phase 0 Cloud — terminal setup (AWS)

### 1. Configure AWS CLI on your Mac

```bash
export INTEROP_CODE="$HOME/OnyxInterop/Training/onyx-interop"
cd "$INTEROP_CODE"

# WHAT: Create access.env from template
# WHY:  Single file for AWS profile, region, Databricks, GitLab
cp configs/access/access.env.example configs/access/access.env

# Edit with your values (use Cursor or nano):
#   AWS_PROFILE=your-profile-name    # or use default
#   AWS_REGION=us-east-1           # or your preferred region
nano configs/access/access.env
```

**Option A — named profile (recommended):**

```bash
aws configure --profile onyx-dev
# Enter: Access Key, Secret Key, region (e.g. us-east-1), output json
```

**Option B — SSO (if your org uses IAM Identity Center):**

```bash
aws configure sso --profile onyx-dev
aws sso login --profile onyx-dev
```

**Verify:**

```bash
source configs/access/access.env
aws sts get-caller-identity
# Expect: Account, Arn, UserId
```

---

### 2. Run Phase 0 access checklist

```bash
cd "$INTEROP_CODE"
source .venv/bin/activate
./scripts/configure_access.sh
./scripts/phase0_access_checklist.sh
```

**Target:** `[PASS] AWS CLI configured` — other items can WARN until Databricks/GitLab added.

---

### 3. Provision AWS foundation (Terraform)

**WHAT:** S3, VPC, DynamoDB, DocumentDB, EKS, API Gateway (dev)  
**WHY:** Same modules as production Abacus/Onyx landing zone  
**COST WARNING:** EKS + DocumentDB incur charges — use `dev` only; destroy when not learning.

```bash
cd "$INTEROP_CODE/terraform"

# WHAT: Initialize Terraform providers
terraform init

# WHAT: Preview resources (no changes)
terraform plan -var="environment=dev" -var="aws_region=${AWS_REGION:-us-east-1}"

# WHAT: Apply (creates cloud infra — confirm account/region first!)
terraform apply -var="environment=dev" -var="aws_region=${AWS_REGION:-us-east-1}"

# WHAT: Save outputs (bucket names, cluster name, etc.)
terraform output
```

**After apply — verify from terminal:**

```bash
aws s3 ls | grep onyx-interop
aws eks list-clusters --region "${AWS_REGION:-us-east-1}"
aws dynamodb list-tables --region "${AWS_REGION:-us-east-1}"
```

---

### 4. Connect kubectl to EKS (runtime plane)

```bash
# WHAT: Merge EKS kubeconfig for Helm/Firely deploy later
aws eks update-kubeconfig \
  --name $(terraform -chdir="$INTEROP_CODE/terraform" output -raw eks_cluster_name) \
  --region "${AWS_REGION:-us-east-1}" \
  --profile "${AWS_PROFILE:-default}"

kubectl get nodes
# Expect: nodes Ready (may take 5–10 min after terraform apply)
```

---

### 5. Upload baseline FHIR to S3 (first cloud data)

```bash
# WHAT: Copy local NDJSON to Bronze/Silver prefix in S3
# WHY:  Proves Mac → cloud path before Databricks exists
BUCKET=$(terraform -chdir="$INTEROP_CODE/terraform" output -raw bronze_bucket 2>/dev/null || echo "YOUR-BUCKET-NAME")

aws s3 sync "$HOME/OnyxInterop/fhir_output/ndjson/" \
  "s3://${BUCKET}/baseline/ndjson/" \
  --region "${AWS_REGION:-us-east-1}"

aws s3 ls "s3://${BUCKET}/baseline/ndjson/"
```

---

## What stays local vs moves cloud next

| Keep local | Move to cloud next |
|------------|-------------------|
| Reading docs, cheat sheet, teach-backs | S3 landing zones |
| `run_ci_local.sh` before every commit | Terraform-managed infra |
| Debugging transformers with pytest | Databricks Claims/PVD workflows |
| `start_all_services.sh` for API concepts | Firely + SLAP on EKS |

---

## Recommended sequence for you (cloud objective)

| Week | Focus | Where |
|------|-------|-------|
| **Now** | Phase 0 AWS: CLI + Terraform dev stack | Cloud |
| **Parallel** | Finish Step 2 Day 4–5 teach-back | Local notes |
| **Next** | Step 3 architecture + Step 4 data eng learn | Local + read cloud configs |
| **Then** | Phase 1: Databricks bundle deploy + first workflow | Cloud |
| **Then** | Phase 1: Firely on EKS + SLAP/FITE Helm | Cloud |
| **Then** | Phase 1: Apigee auth paths (PVA/P2P) + ePA APISIX stack | Cloud |
| **Then** | Phase 1: Rail D Cambia BQ CronJob (IRSA + WIF) | Cloud |

---

## Attachment-aligned docs (read before cloud Phase 1)

| Doc | What it covers |
|-----|----------------|
| [CMS0057_AUTH_PATHS.md](../OnyxInterop/Training/onyx-interop/docs/CMS0057_AUTH_PATHS.md) | PAA vs PVA vs P2P auth models |
| [EPA_OPTION_A_B.md](../OnyxInterop/Training/onyx-interop/docs/EPA_OPTION_A_B.md) | ePA ingress + Gainwell/Wellmark + deploy order |
| [CAMBIA_BIGQUERY_INGESTION.md](../OnyxInterop/Training/onyx-interop/docs/CAMBIA_BIGQUERY_INGESTION.md) | Rail D cross-cloud ingest (XPORT-2596) |
| `configs/mdp/auth_paths.json` | Machine-readable auth path registry |

---

## Destroy dev stack (save cost)

```bash
cd "$INTEROP_CODE/terraform"
terraform destroy -var="environment=dev"
```

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `Unable to locate credentials` | `aws configure` or set `AWS_PROFILE` in access.env |
| `AccessDenied` on terraform apply | IAM needs EC2, EKS, S3, DynamoDB, IAM pass-role |
| EKS nodes not Ready | Wait 10 min; check `kubectl describe node` |
| Wrong account | `aws sts get-caller-identity` before every apply |

---

*Local learning guides: [STEP1_LEARN_AND_BUILD.md](./STEP1_LEARN_AND_BUILD.md) · [STEP2_LEARN_AND_BUILD.md](./STEP2_LEARN_AND_BUILD.md)*
