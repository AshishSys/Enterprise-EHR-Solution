
## Glossary

> All key terms from the Abacus/Onyx CMS interoperability solution — organized by category with description and practical example.

| Term | Category | Description | Example |
|------|----------|-------------|---------|
| **Abacus** | Platform & Architecture | Data plane owned by Abacus Insights — ingestion, FM/SAM marts, extract/transform, FHIR bundle generation | Databricks Claims workflow writes `claims_sam.eob_records` before Firely load |
| **Onyx** | Platform & Architecture | API/runtime plane — SLAP auth, FITE gateway, Developer Portal, Onyx Insights, MDP | Consumer apps call FITE :8080 after SLAP token, never Firely directly |
| **FM (Foundational Mart)** | Data Engineering | Canonical normalized layer — NOT FHIR-shaped; validates, dedupes, stable keys for incremental updates | `claims_fm.claim_line` holds typed columns from raw CSV before SAM mapping |
| **SAM (Subject Area Mart)** | Data Engineering | IG-aligned marts bridging FM to FHIR; each SAM maps to a CMS domain/workflow family | `clinical_sam.observations` → US Core Observation resources |
| **Extract Task** | Data Engineering | Reads SAM Delta tables, writes NDJSON/bundles to S3 staging for transform/FSI | Extract pulls changed rows via `table_changes` since last watermark |
| **FHIR Generation** | FHIR Engineering | Converts SAM rows to FHIR R4 JSON per US Core / CARIN BB / Da Vinci profiles | `claims_transformer.py` maps EOB SAM row → `ExplanationOfBenefit` resource |
| **Bundle Packaging** | FHIR Engineering | Wraps resources in transaction bundles (Firely) or NDJSON files (HealthLake `$import`) | `bundle_Alberto639_Berge125.json` with 793 entries for bulk upsert |
| **interop_pipeline.py** | Data Engineering | Local reference pipeline: CSV → FM → SAM → FHIR (5 layers) | `python interop_pipeline.py --input ./source_data --output ./fhir_output` → 9,997 resources |
| **SLAP** | Runtime & Security | SMART Launch Authentication Proxy — OAuth2 tokens, PKCE, scopes, consent (:9000) | Patient app exchanges auth code + PKCE verifier at `/auth/token` |
| **FITE** | Runtime & Security | FHIR Integration & Transformation Engine — API gateway proxying to Firely (:8080) | `GET /Patient/{id}/$everything` after SLAP Bearer token validation |
| **MDP** | Platform & Architecture | Metadata & Discovery Platform — service registry, IG packages, workflow configs (:9002) | `configs/mdp/ig_registry.json` pins US Core 6.1.0 |
| **Onyx Insights** | Observability | Monitoring, CMS metrics, alerts, audit trail (:9001) | CMS Patient Access uptime reporter feeds compliance dashboard |
| **Developer Portal** | Runtime & Security | App registration, SMART client configs, API documentation for third-party developers | Register `patient-app-001` with `patient/*.read` scopes |
| **Firely Server** | FHIR Store | Production FHIR R4 store on EKS; serves resources after FSI bulk/incremental load | `kubectl get pods -n firely` — Patient Access queries hit Firely via FITE |
| **HealthLake** | FHIR Store | AWS managed FHIR store; accepts NDJSON via `$import` for bulk historical loads | `Patient.ndjson` (10 resources) imported via HealthLake bulk API |
| **FSI (Firely Server Ingest)** | FHIR Store | Bulk/incremental upload job converting staging NDJSON → Firely resources | Step Functions triggers FSI Docker job after Extract completes |
| **Seiji** | Deployment | Internal deployment tool for Helm/Terraform rollouts with canary support | Canary deploy Firely helm chart 10% → 100% after health check |
| **onyx_job_state** | Data Engineering | DynamoDB table storing workflow watermarks, run status, error messages | Watermark `updated_at=2025-07-18T06:00:00Z` for incremental Extract |
| **metadata_v1** | Data Engineering | Maps business IDs (member_id, claim_id) to FHIR resource IDs for idempotent upserts | `member_id=M123` → `Patient/abc-fhir-id` |
| **CMS-9115** | CMS & Regulatory | Interoperability and Patient Access Final Rule — mandates Patient Access, Provider Directory, Formulary APIs | Phase 1 delivers SMART Patient Access + public Plan-Net directory |
| **CMS-0057** | CMS & Regulatory | Interoperability and Prior Authorization Final Rule — Provider Access, P2P, ePA by Jan 2027 | Phase 2 adds `$export`, `$bulk-member-match`, CRD/DTR/PAS |
| **Patient Access API** | CMS & Regulatory | SMART-authenticated FHIR API giving members access to their claims/clinical/PA data | Member app calls `$everything` on their Patient resource |
| **Provider Directory API** | CMS & Regulatory | Public FHIR API exposing practitioner/org directory (Plan-Net) — no auth required | `GET /Practitioner?address-state=MA` returns Plan-Net profiles |
| **Formulary API** | CMS & Regulatory | Public API for drug formulary, tiers, PA requirements | `GET /MedicationKnowledge?code=NDC123` |
| **Provider Access API** | CMS & Regulatory | Backend Services API for attributed provider access to member data via `$export` | Provider EHR triggers bulk export with attribution Group resources |
| **P2P (Payer-to-Payer)** | CMS & Regulatory | CMS-0057 workflow for member data exchange between payers with consent | `$bulk-member-match` + opt-in consent + NDJSON export |
| **ePA (Electronic Prior Authorization)** | CMS & Regulatory | Da Vinci CRD/DTR/PAS workflows for prior auth burden reduction | CRD checks if PA needed; PAS `$submit` for authorization request |
| **HTI-1** | CMS & Regulatory | Health IT certification rule updating USCDI standards and FHIR requirements | Track USCDI version bumps in IG registry quarterly |
| **USCDI** | CMS & Regulatory | US Core Data for Interoperability — minimum data classes payers must exchange | USCDI v3 adds health insurance information elements |
| **FHIR R4** | FHIR Standards | Fast Healthcare Interoperability Resources Release 4 — JSON/XML healthcare data standard | All API resources use `"resourceType": "Patient"` etc. |
| **US Core** | FHIR Standards | HL7 FHIR IG defining US baseline profiles for Patient, Observation, Condition, etc. | Patient resource declares `meta.profile` US Core Patient URL |
| **CARIN Blue Button (CARIN BB)** | FHIR Standards | FHIR IG for consumer-directed claims/EOB/COB data | `ExplanationOfBenefit` with CARIN BB profile for Patient Access |
| **Da Vinci IGs** | FHIR Standards | HL7 implementation guides: PDex, Plan-Net, Formulary, CRD, DTR, PAS | Plan-Net `PractitionerRole` for Provider Directory |
| **PDex** | FHIR Standards | Da Vinci Payer Data Exchange — member clinical/claims export patterns | PDex `$member-everything` operation for P2P export |
| **Plan-Net** | FHIR Standards | Da Vinci Provider Directory IG for Practitioner/Organization/PractitionerRole | PVD workflow produces Plan-Net compliant directory resources |
| **CRD** | FHIR Standards | Da Vinci Coverage Requirements Discovery — checks if PA/docs needed at point of care | `POST /CoverageRequirements/$discovery` before ordering procedure |
| **DTR** | FHIR Standards | Da Vinci Documentation Templates & Rules — adaptive PA questionnaire forms | CRD response links DTR questionnaire for clinical documentation |
| **PAS** | FHIR Standards | Da Vinci Prior Authorization Support — `$submit` PA requests/responses as FHIR | `ClaimResponse` resource carries PA decision/outcome |
| **SMART on FHIR** | Runtime & Security | OAuth2-based app launch framework for healthcare APIs | `.well-known/smart-configuration` discovery document on SLAP |
| **PKCE** | Runtime & Security | Proof Key for Code Exchange — S256 challenge prevents auth code interception | Mobile app sends `code_challenge` at authorize, `code_verifier` at token |
| **Backend Services Auth** | Runtime & Security | OAuth2 client_credentials or JWT assertion for system-level API access | Payer bulk `$export` uses `system/*.read` scope |
| **CapabilityStatement** | FHIR Standards | FHIR metadata resource describing server capabilities (`/metadata`) | FITE `/metadata` lists supported resources and search params |
| **$everything** | FHIR Operations | FHIR operation returning all resources for a patient compartment | `GET /Patient/123/$everything` for member app full record |
| **$export** | FHIR Operations | Bulk data export operation — async NDJSON dump with manifest | Provider Access triggers `$export` → poll `_status` → download NDJSON |
| **$bulk-member-match** | FHIR Operations | CMS-0057 P2P operation matching members across payers | POST member identifiers → receive matched Patient references |
| **NDJSON** | FHIR Standards | Newline-delimited JSON — one FHIR resource per line for bulk import/export | `Observation.ndjson` with 6,868 lines for HealthLake `$import` |
| **Transaction Bundle** | FHIR Standards | FHIR bundle type `transaction` with POST/PUT entries for atomic upsert | Per-patient bundle uploaded to Firely via FSI |
| **Must Support** | FHIR Standards | US Core elements required if data exists — validation failure if missing | Patient `name.family` Must Support — quarantine if null |
| **StructureDefinition** | FHIR Standards | FHIR profile definition constraining resource elements | US Core Patient SD stored in UC Volume `fhir_igs/` |
| **Rail A** | Multi-Channel Ingestion | CSV/batch ingestion path — existing Synthea/payer flat-file pipeline (unchanged) | `Patients.csv` → FM → SAM → FHIR via `interop_pipeline.py` |
| **Rail B** | Multi-Channel Ingestion | Serverless webhook transport — API Gateway → Lambda → Kafka/SQS → S3 Bronze | NASCO claim adjudication webhook lands in `bronze.nasco_events` |
| **Rail C** | Multi-Channel Ingestion | Native FHIR JSON from EHR exports (PulseEHR) via medallion Autoloader | 129K patients, 8.9M resources → Bronze → Silver → SAM convergence |
| **Medallion Architecture** | Data Engineering | Bronze (raw) → Silver (validated) → Gold (SAM/business) Delta Lake layers | Autoloader ingests FHIR NDJSON to Bronze; LDP validates Silver |
| **Autoloader** | Data Engineering | Databricks streaming ingest from cloud files with schema evolution | `cloudFiles.schemaEvolutionMode=addNewColumns` for PulseEHR schema changes |
| **Delta Lake** | Data Engineering | ACID table format on S3 — time travel, MERGE, change data feed | `RESTORE TABLE clinical_sam.conditions TO VERSION AS OF 842` rollback |
| **Liquid Clustering** | Data Engineering | Auto-reclustering on write for high-churn SAM tables | Cluster on `(member_id, service_date)` for claims SAM |
| **Unity Catalog** | Data Engineering | Databricks governance — permissions, masking, lineage, model registry | `prod_interop.sam.clinical.conditions` with PII column masks |
| **Databricks Asset Bundles (DABs)** | Data Engineering | IaC for Databricks jobs, pipelines, schemas — deploy via `databricks bundle` | `claims_workflow` DAB deploys to dev/stage/prod targets |
| **LDP (Lakeflow Declarative Pipelines)** | Data Engineering | Declarative Spark pipelines with `@dp.expect_or_drop` data quality | Invalid Observation (missing `code`) dropped to quarantine table |
| **Quarantine Table** | Data Engineering | Holds records failing validation — not silently dropped, not blocking batch | `fhir_silver.quarantine` with `violation_type` for partner escalation |
| **PulseEHR** | Multi-Channel Ingestion | Reference EHR export — 129,218 patients, ~8.9M FHIR R4 JSON resources | Rail C ingests Observation (53%), Encounter (13%) distribution |
| **ng-nasco-event-api** | Multi-Channel Ingestion | Reference serverless pattern for partner webhook ingestion | API Gateway + Lambda + Firehose → S3 landing zone |
| **MSK (Amazon MSK)** | Kafka & Events | Managed Kafka for Rail B event streaming between webhook and Bronze | Topic `interop.claim.adjudicated.v1` consumed by Autoloader |
| **SQS DLQ** | Kafka & Events | Dead-letter queue for failed webhook/Lambda processing | Messages after 3 retries → DLQ → Payer Ops Agent alert |
| **Schema Contract** | Kafka & Events | JSON Schema per event type validated at Lambda before landing | `claim_adjudicated` v1.2 requires `member_id`, `claim_id` |
| **Kafka Engineer** | Role Proficiency | Designs event transport, topic retention, replay, schema evolution | Producer/consumer scripts for NASCO adjudication events |
| **Unity AI Gateway** | AI Layer | Databricks governance for all LLM + MCP traffic — caps, PII guardrails, audit | Patient Agent calls route through gateway with spend cap |
| **RAG** | AI Layer | Retrieval-Augmented Generation — Vector Search indexes ground LLM responses | Formulary policy chunks retrieved before answering "PA required for Humira?" |
| **Vector Search** | AI Layer | Databricks embedding index for semantic retrieval over SAM/docs | `formulary_policy_idx` synced daily from `formulary_sam` |
| **MCP (Model Context Protocol)** | AI Layer | Tool servers exposing read-only APIs to AI agents (FHIR, metrics, notify) | `onyx.mcp.fhir_read` tool: `get_observations`, `get_eob` |
| **ai_events** | AI Layer | SAM mart + event queue for due dates, care gaps, pipeline failures | `PA_DECISION_DUE` CRITICAL event triggers Provider Agent Slack |
| **Patient Agent** | AI Layer | Member-facing agent — RAG + MCP fhir_read + notify; no diagnosis | "Am I due for screenings?" → RAG gap + MCP confirm → push notification |
| **Provider Agent** | AI Layer | Attributed provider agent — panel gaps, PA deadlines, ePA docs | PA overdue alert with deep link to provider portal |
| **Payer Ops Agent** | AI Layer | Internal ops agent — ingest lag, DLQ depth, workflow failures | Bronze lag 4h → Slack alert with Databricks job run URL |
| **MLflow** | AI Layer | Model lifecycle — logging, registry, serving endpoints | PAS denial model v3 logged with AUC 0.87 to UC registry |
| **Feature Store** | AI Layer | Offline/online feature tables for ML and real-time CRD lookups | `member_cr_features_online` lookup by `member_id` at CRD request |
| **OBO (On Behalf Of)** | AI Layer | MCP executes with user's SLAP token scopes — not elevated service account | Patient Agent cannot fetch another member's EOB |
| **Inference Audit Table** | AI Layer | Logs model/agent requests without PHI — retention for HIPAA | `ml.pas_inference_log` with hashed member_id |
| **Microsoft Fabric** | Analytics | Enterprise analytics platform — Lakehouse, pipelines, Power BI semantic models | OneLake shortcut to Databricks CMS metrics export |
| **OneLake Shortcut** | Analytics | Fabric reads ADLS export in place without data duplication | Shortcut to `abfss://exports@datalake/metrics/cms/` |
| **V-Order** | Analytics | Fabric parquet optimization for faster Power BI DirectLake scans | Enable on `formulary_dim` — dashboard load 4.2s → 1.1s |
| **Type 2 SCD** | Analytics | Slowly Changing Dimension — track eligibility history with `is_current` flag | Member PPO→HMO switch closes old row, opens new current row |
| **RLS (Row-Level Security)** | Analytics & SQL | Filters rows by payer/user context at query time | Power BI role `PayerA` filters `payer_id = 'A'` |
| **DDM (Dynamic Data Masking)** | Analytics & SQL | Masks PHI columns (SSN, DOB) for non-privileged roles | Analyst sees `XXX-XX-6789` for SSN |
| **BigQuery** | Hybrid Cloud | GCP analytics for de-identified benchmarks — not primary PHI store | CMS monthly rollup scheduled query on aggregated metrics |
| **Dataplex** | Hybrid Cloud | GCP data governance — policy tags, quality rules, curated zones | `PHI` policy tag masks member_id in sandbox |
| **Terraform** | Deployment | IaC for AWS infra — S3, EKS, DocumentDB, DynamoDB, API Gateway | `terraform/modules/s3/main.tf` provisions Bronze buckets |
| **Helm** | Deployment | Kubernetes package manager for Firely, FITE, SLAP on EKS | `helm/firely-server/values.yaml` configures replicas |
| **EKS** | Deployment | AWS Kubernetes cluster hosting Firely and runtime services | `kubectl rollout status deployment/firely-server -n firely` |
| **DocumentDB** | Deployment | MongoDB-compatible store for SLAP sessions/metadata | SLAP token store with TTL index |
| **Canary Deploy** | Deployment | Gradual rollout — small traffic slice before full promotion | 10% FITE pods on new version → promote if error rate OK |
| **RCM (Revenue Cycle Management)** | Healthcare Domain | Claims adjudication, denial management — downstream of CMS interop | FHIR EOB for Patient Access; X12 835 tables for RCM reconciliation |
| **VBC (Value-Based Care)** | Healthcare Domain | Quality measures, attribution, gap closure — consumes SAM marts | HEDIS gap logic on `clinical_sam.observations` vitals/labs |
| **HEDIS** | Healthcare Domain | Healthcare Effectiveness Data and Information Set — quality measure standards | Diabetes A1c measure uses LOINC 4548-4 Observations |
| **Attribution** | Healthcare Domain | Assigning members to providers/panels for VBC and Provider Access | Group resource links Patient → Practitioner attribution |
| **EOB (Explanation of Benefits)** | Healthcare Domain | Claim adjudication summary shown to members | CARIN BB `ExplanationOfBenefit` from `claims_sam.eob_records` |
| **NPI** | Healthcare Domain | National Provider Identifier — 10-digit provider ID | Plan-Net Practitioner.identifier NPI system |
| **NDC** | Healthcare Domain | National Drug Code — unique drug identifier for formulary | Formulary SAM `ndc` column → MedicationKnowledge |
| **PA (Prior Authorization)** | Healthcare Domain | Payer approval required before certain procedures/drugs | Da Vinci PAS `$submit` returns ClaimResponse with decision |
| **PHI** | Security & Compliance | Protected Health Information — HIPAA-regulated identifiable health data | Never in LLM prompts, external LLM, or unmasked analytics |
| **BAA** | Security & Compliance | Business Associate Agreement — required per data source/partner | BAA indexed per Rail B webhook partner in compliance folder |
| **HIPAA** | Security & Compliance | Health Insurance Portability and Accountability Act — privacy/security rules | Audit logs retained 6 years; encryption at rest/transit |
| **Wiz** | Security & Compliance | Cloud security scanner for container/IaC vulnerabilities | Scan Lambda images before prod Rail B deploy |
| **CMS Metrics Reporter** | Observability | Reports Patient Access API uptime/call volume for CMS compliance | `monitoring/cms_metrics_reporter.py` → monthly filing data |
| **Workflow Family** | Data Engineering | Databricks job group for a CMS domain: Claims, Clinical, Formulary, PVD, ePA, P2P | Claims family: ingest → FM → SAM → Extract → FSI |
| **Extract Config YAML** | Data Engineering | Declarative mapping of SAM tables to FHIR resource types | `configs/workflows/claims/extract_config.yaml` |
| **Incremental Watermark** | Data Engineering | High-water mark (`updated_at` or change version) for delta processing | Only rows changed since watermark enter Extract |
| **Change Data Feed** | Data Engineering | Delta feature emitting row changes for incremental downstream | `table_changes('clinical_sam.conditions', v1, v2)` |
| **Synthea** | Data Engineering | Synthetic patient data generator — 10 patients, 9,997 FHIR resources in baseline | `./source_data/Patients.csv` local baseline validation |
| **GitLab CI** | Deployment | CI/CD pipeline for DAB deploy, pytest, bundle validate | `databricks bundle deploy -t stage` on release branch |
| **Forward Deployed Engineer** | Role Proficiency | Deploys, troubleshoots, onboards customers at payer sites | Solo Phase 0 checklist + customer incident runbook execution |
| **FHIR Engineer** | Role Proficiency | IG validation, resource mapping, Firely/FSI operations, CMS API compliance | Zero IG errors on `validate_fhir_output.py --strict` |
| **Data Engineer** | Role Proficiency | Pipelines, Delta, Autoloader, SAM merges, multi-rail convergence | Three rails land Bronze, merge at SAM, Extract to Firely |
| **AI Engineer** | Role Proficiency | RAG, agents, MLflow, Unity AI Gateway, MCP governance | Golden eval >85%; gateway blocks PHI in prompts |
| **Associate Solution Architect** | Role Proficiency | Phase planning, CMS traceability, ownership split, hybrid ADRs | Whiteboard 3-rail ingestion + AI layer for CMS deadline |
| **Intermediate Associate Programmer** | Role Proficiency | Python transformers, bash automation, SQL, unit tests | Patch `claims_transformer.py` + pytest green independently |
| **Safe Harbor** | Security & Compliance | HIPAA 45 CFR 164.514(b)(2) — remove/generalize 18 identifiers | ZIP → 3 digits; DOB → year; names/SSN suppressed |
| **Expert Determination** | Security & Compliance | HIPAA 45 CFR 164.514(b)(1) — statistician certifies very small re-id risk | Used when Safe Harbor would break clinical utility |
| **De-ID Gate** | Security & Compliance | First pipeline layer; splits identified CMS path from de-id analytics path | `pipeline/deid_engine.py` + `configs/deid/safe_harbor.yaml` |
| **Tokenization** | Security & Compliance | HMAC surrogate for MRN/member_id; irreversible from analytics side | `tok_member_id_<hmac24>` stored in de-id Gold |
| **Golden Record** | MDM | Survivorship-resolved master entity after deterministic/probabilistic match | EHR beats claims on demographics; recency wins coverage status |
| **Survivorship** | MDM | Attribute-level win rules (source priority, recency, completeness) | `source_priority: [ehr_fhir, claims, pvd]` |
| **ISO 8000** | MDM | Data quality / master data standard used with AHIMA IG | Crosswalk never stores raw PHI |
| **AHIMA IG** | MDM | AHIMA Information Governance principles for healthcare MDM | Steward per entity: member, provider, coverage |
| **Fabric Capacity Unit (CU)** | Analytics | Microsoft Fabric compute billing unit vs Databricks DBU | `run_engine_benchmark.sh` compares CU-hour vs DBU cost |
| **Dual-Engine Bake-off** | Analytics | Same de-id SAM job on Databricks and Fabric for cost/speed | Winner_speed vs winner_cost recorded in `observability.engine_benchmark` |
| **AI Observability** | Observability | LLM RCA + anomaly explanation on de-id traces/metrics only | Claude/GPT via Unity AI Gateway; `block_external_phi` |

### Glossary Category Index

| Category | Terms Count | Key Terms |
|----------|-------------|-----------|
| Platform & Architecture | 6 | Abacus, Onyx, MDP, Developer Portal |
| Data Engineering | 22 | FM, SAM, Autoloader, Delta, DABs, Medallion, Watermark |
| FHIR Standards | 18 | US Core, CARIN BB, Da Vinci, Bundle, NDJSON, Must Support |
| CMS & Regulatory | 10 | CMS-9115, CMS-0057, Patient Access, P2P, ePA, HTI-1 |
| Runtime & Security | 8 | SLAP, FITE, SMART, PKCE, Backend Services |
| Multi-Channel Ingestion | 7 | Rail A/B/C, PulseEHR, ng-nasco-event-api |
| Kafka & Events | 3 | MSK, SQS DLQ, Schema Contract |
| AI Layer | 12 | RAG, MCP, Unity AI Gateway, ai_events, Agents |
| Analytics | 6 | Fabric, OneLake, V-Order, SCD, RLS, DDM |
| Hybrid Cloud | 2 | BigQuery, Dataplex |
| Deployment | 8 | Terraform, Helm, EKS, Seiji, Canary |
| Healthcare Domain | 8 | RCM, VBC, HEDIS, EOB, NPI, NDC, PA, Attribution |
| Security & Compliance | 4 | PHI, HIPAA, BAA, Wiz |
| Observability | 2 | Onyx Insights, CMS Metrics Reporter |
| Role Proficiency | 7 | FHIR Engineer, Data Engineer, Kafka Engineer, AI Engineer, etc. |

---
