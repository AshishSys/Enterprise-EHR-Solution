
## Section Q: Databricks Engineering — Healthcare Interop (Q296–330)

### Q296. How do you deploy Abacus interop pipelines using Databricks Asset Bundles (DABs)?

**Answer:** I package each workflow family (Claims, Clinical, Formulary, PVD, Rail C FHIR) as a DAB with environment targets (`dev`, `stage`, `prod`), bind Unity Catalog schemas per env, and deploy via `databricks bundle deploy -t prod`. Job schedules, cluster policies, and service principal permissions are declared in `databricks.yml`—not hand-configured in the UI.

**Example:** `claims_workflow` DAB deploys Extract → FHIR Gen → Bundle tasks to prod with `catalog=prod_interop`, cluster policy `phi_compute`, and GitLab CI gate on `bundle validate`.

**How to Check:**
- `databricks bundle validate` passes in CI
- Prod job IDs match bundle resource names after deploy
- No drift between UI job config and `databricks.yml`
- Service principal has USE CATALOG on prod_interop only

**How to Fix:**
- Re-deploy bundle after manual UI edit to reconcile drift
- Add missing `permissions` block for service principal in bundle
- Pin cluster policy ID in bundle target config
- Roll back: `databricks bundle deploy -t prod --rollback`

---

### Q297. How does Autoloader handle schema evolution for PulseEHR FHIR JSON (Rail C)?

**Answer:** I enable `cloudFiles.schemaEvolutionMode = addNewColumns` on Bronze Autoloader for FHIR NDJSON—new resource types or extensions add columns without failing the stream. Breaking changes (type change) route to `badRecordsPath` for quarantine review.

**Example:** PulseEHR adds `Observation.component` array in v2 export → Autoloader adds `component` column to Bronze; existing rows null; Silver validation unchanged until we promote field.

**How to Check:**
- Autoloader stream metrics: `numBytesOutstanding`, schema inference logs
- `cloudFiles.schemaLocation` S3 path has latest schema JSON
- Bad records count in `s3://.../fhir_bronze/_bad_records/`
- DESCRIBE TABLE shows new columns after evolution event

**How to Fix:**
- Set `rescuedDataColumn = _rescued_data` to capture overflow fields
- For breaking type change: pause stream, ALTER TABLE, restart with `schemaHints`
- Document schema version in MDP source registry per PulseEHR export batch

---

### Q298. How do you configure Unity Catalog column masking for member PHI in SAM tables?

**Answer:** I tag `member_ssn`, `member_dob`, `member_phone` with `PII` classification in Unity Catalog, then apply dynamic column mask functions—SSN shows last 4 only, DOB year-only for non-clinical roles. Mask applies at query time via UC grants, not copy-in-place.

**Example:** Analyst with `clinical_analyst` role sees full DOB; `payer_ops` role sees `****-**-15` for DOB via `mask_date_year_only()`.

**How to Check:**
- `DESCRIBE TABLE EXTENDED clinical_sam.members` shows tags and masks
- Test query as each role in SQL warehouse—verify mask output
- Audit log shows masked column access events
- No plaintext PHI in shared notebook outputs (export scan)

**How to Fix:**
- Apply tag: `ALTER TABLE ... ALTER COLUMN member_ssn SET TAGS ('PII' = 'SSN')`
- Create and attach mask function via `CREATE MASK ... ON COLUMN`
- Revoke SELECT on base column; grant via masked view if legacy tool lacks UC mask support

---

### Q299. When do you use Liquid Clustering vs Z-ORDER on interop Delta tables?

**Answer:** I use Liquid Clustering on high-churn SAM tables keyed by `member_id` + `service_date` (claims, conditions)—auto-reclusters on write without manual OPTIMIZE. Z-ORDER I reserve for static historical archives where partition + Z-ORDER on `payer_id, year` is one-time tuned.

**Example:** `claims_sam.claim_line` Liquid Cluster on `(member_id, service_date)`—Patient Access Extract filters by member_id hit fewer files than partition-only on `load_date`.

**How to Check:**
- `DESCRIBE DETAIL` shows `clusteringColumns`
- Query profile: fewer files read after clustering vs before
- `system.storage.predictive_optimization` recommendations
- File count per member_id slice in table history

**How to Fix:**
- `ALTER TABLE ... CLUSTER BY (member_id, service_date)` on existing table (one-time rewrite)
- Enable Predictive Optimization for auto-maintenance
- Avoid over-clustering low-cardinality columns alone

---

### Q300. What is your OPTIMIZE/VACUUM schedule for Gold SAM and FHIR staging tables?

**Answer:** I OPTIMIZE Gold SAM tables weekly (post-merge compaction) and VACUUM with 7-day retention on staging, 30-day on SAM. Never VACUUM within 24h of a rollback window. FHIR bundle staging OPTIMIZE daily before FSI bulk window.

**Example:** Sunday 02:00 UTC job: `OPTIMIZE clinical_sam.conditions ZORDER BY (member_id)` then `VACUUM RETAIN 168 HOURS` on `fhir_staging.bundles`.

**How to Check:**
- Job run history for `sam_maintenance` workflow
- `DESCRIBE HISTORY` shows OPTIMIZE commits
- Small file count trend (< 100MB avg file size target)
- Time travel versions still available within retention window

**How to Fix:**
- Increase OPTIMIZE frequency if small-file warning in query profile
- Extend VACUUM retention if rollback drill failed due to missing files
- Set `delta.deletedFileRetentionDuration` table property explicitly

---

### Q301. How do you use Lakeflow Spark Declarative Pipelines (LDP) for FHIR Silver validation?

**Answer:** I define Silver as an LDP pipeline with `@dp.expect_or_drop("valid_uscore", "profile_match = true")` on each resource type flow. Invalid resources drop to quarantine table via `@dp.expect_all_or_drop` with reason column. Event log table captures drop counts for Payer Ops Agent.

**Example:** LDP flow `fhir_observation_silver`: expect `code IS NOT NULL`, expect `status IN ('final','amended')`—drops logged to `fhir_silver.event_log`, quarantine rows in `fhir_silver.quarantine`.

**How to Check:**
- LDP pipeline UI: data quality tab shows expect pass/fail rates
- `event_log` table row count matches quarantine inserts
- Sample quarantine row has `violation_type` populated
- Pipeline update completes within SLA after Bronze landing

**How to Fix:**
- Relax expect to `@dp.expect` (warn) during partner onboarding—not drop
- Add `@dp.expect_or_fail` only for hard CMS blockers
- Reprocess quarantine after rule fix via `pipelines.reset`

---

### Q302. How do you configure Autoloader `badRecordsPath` for malformed FHIR NDJSON?

**Answer:** I set `cloudFiles.badRecordsPath = s3://.../fhir_bronze/_bad_records/` with JSON format—malformed lines (truncated JSON, wrong content-type) land there with error reason. Daily quarantine notebook summarizes by error class for partner escalation.

**Example:** PulseEHR batch includes 12 truncated Observation lines → Autoloader writes to bad records with `malformed_json` → quarantine report emailed to integration team.

**How to Check:**
- S3 `_bad_records/` prefix object count and sample content
- Autoloader metrics: `numFilesProcessed` vs Bronze row count delta
- Alert if bad record rate > 0.1% of batch volume
- Partner ticket opened for recurring error patterns

**How to Fix:**
- Re-ingest fixed files from partner after source correction
- Adjust `cloudFiles.maxFilesPerTrigger` if OOM caused truncation
- Enable `ignoreCorruptFiles` only in dev—never prod without audit

---

### Q303. How do you reduce shuffle on large eligibility-to-claims joins in Extract?

**Answer:** I broadcast the smaller eligibility snapshot (< 10M rows) when joining to claim lines, or pre-partition both sides on `member_id` with AQE enabled. For date-range joins I use `range_join_hint` with bucket size matching eligibility period granularity.

**Example:** `claims JOIN broadcast(eligibility)` on `member_id` where eligibility is 2M rows vs claims 400M—shuffle eliminated, Extract runtime 45min → 12min.

**How to Check:**
- Spark UI: Exchange node absent or significantly reduced
- Query profile: `BroadcastHashJoin` vs `SortMergeJoin`
- AQE coalesce and skew join metrics
- Extract task duration trend in workflow run

**How to Fix:**
- Increase `spark.sql.autoBroadcastJoinThreshold` if eligibility grew past default
- Repartition claims by `member_id` before join if broadcast too large
- Salting for skewed `member_id` hot keys

---

### Q304. How do you manage Delta deleted file retention for compliance audit?

**Answer:** I set table property `delta.deletedFileRetentionDuration = interval 30 days` on SAM Gold tables—supports rollback and audit reconstruction. Legal hold sources get 90-day retention. VACUUM never runs below retention without compliance sign-off.

**Example:** Erroneous merge on `formulary_sam.drug` day 5 → `RESTORE TO VERSION AS OF 4` succeeds because deleted files retained 30 days.

**How to Check:**
- `SHOW TBLPROPERTIES clinical_sam.claims` for retention interval
- Rollback drill in stage quarterly
- Storage cost report for deleted file accumulation
- Compliance ticket for retention policy exceptions

**How to Fix:**
- ALTER TABLE SET TBLPROPERTIES for retention increase before VACUUM
- If files already vacuumed: restore from S3 versioning on underlying bucket
- Document version number in incident ticket at time of bad merge

---

### Q305. How do you govern pipeline assets in Unity Catalog for multi-team interop?

**Answer:** I use three-level namespace `prod_interop.{bronze|silver|sam|fhir}.{domain}` with ownership per team: Abacus owns bronze/silver/sam, Onyx read-only on sam for Extract configs. External locations scoped per env S3 bucket with storage credentials via UC.

**Example:** `prod_interop.sam.clinical` owned by `abacus-sp`; `onyx-runtime-sp` has SELECT only; `payer_analytics-sp` has SELECT on masked views only.

**How to Check:**
- `SHOW GRANTS ON TABLE prod_interop.sam.clinical.conditions`
- No over-privileged ALL PRIVILEGES on prod for human users
- External location credential test from each cluster policy
- Catalog audit log for unauthorized access attempts

**How to Fix:**
- Revoke direct human prod access; route through service principals
- Create `sam_clinical_masked` view for analytics tier
- Migrate legacy hive_metastore tables via UC upgrade tool

---

### Q306. How do you handle incremental vs full refresh for Claims workflow?

**Answer:** I use incremental merge on `claim_id + line_number` with `load_timestamp` watermark—full refresh only on schema migration or source re-baseline. Extract reads SAM Delta change feed (`table_changes`) since last successful run.

**Example:** Daily Claims workflow merges 2M new lines; full refresh triggered only when payer sends historical correction file flagged `full_replace=true` in MDP.

**How to Check:**
- Workflow parameter `processing_mode=incremental|full`
- Merge metrics: inserted/updated/deleted row counts
- `table_changes` version range matches last run version + 1
- Full refresh runs logged and approved in change ticket

**How to Fix:**
- Reset watermark in workflow config after failed partial run
- Run full refresh in isolated clone before prod if data quality unknown
- Add idempotent merge keys to handle duplicate source files

---

### Q307. Scenario: Autoloader lag exceeds 4 hours on PulseEHR Rail C. What do you do?

**Answer:** I check Autoloader stream status, cluster capacity, and incoming file volume spike. Scale cluster, increase `maxFilesPerTrigger`, check for schema inference stall, verify S3 event notification queue depth. Notify Payer Ops Agent if SLA breach persists.

**Example:** PulseEHR drops 8.9M resource export overnight → lag 6h → scale to `Standard_E16s_v5` 8 workers, raise trigger to 2000 files, lag clears in 90min.

**How to Check:**
- Databricks job run: Autoloader `numBytesOutstanding`
- S3 landing prefix file count vs Bronze ingested count
- Cluster CPU/disk spill metrics during lag window
- `ai_events` INGESTION_LAG event fired

**How to Fix:**
- Increase max workers and shuffle partitions temporarily
- Split Autoloader into per-resource-type streams if single stream bottleneck
- Schedule large exports off-peak with partner coordination
- Add Autoloader lag alert > 2h WARN, > 4h CRITICAL

---

### Q308. How do you use Volumes for FHIR IG StructureDefinition artifacts in Databricks?

**Answer:** I store Firely StructureDefinitions and US Core packages in UC Volume `prod_interop.volumes.fhir_igs/`—versioned by IG release. Validation notebooks mount volume read-only; CI copies new IG version on Da Vinci update.

**Example:** PDex v2.0.0 StructureDefinitions in `/Volumes/prod_interop/fhir_igs/davinci-pdex/`—Silver validation references same path across dev/stage/prod volumes synced from Git.

**How to Check:**
- Volume listing shows version folders with README
- Validation notebook resolves profile URL to local SD file
- Hash match between Git tag and volume artifact
- No public internet fetch at runtime (air-gapped validation)

**How to Fix:**
- Upload missing SD: `databricks fs cp` or volume API
- Update validation config `ig_version` parameter on IG upgrade
- Archive old IG version; do not delete until CMS cert period ends

---

### Q309. How do you implement idempotent FHIR Extract task outputs?

**Answer:** Extract writes NDJSON to `fhir_staging/{resource_type}/run_id={uuid}/` with manifest JSON listing resource counts and source SAM version. Re-run with same `run_id` overwrites staging path idempotently; FSI reads manifest to skip unchanged types.

**Example:** Extract fails mid-Observation write → retry same `run_id` → manifest incomplete flag → FSI skips partial, Extract resumes from checkpoint.

**How to Check:**
- Staging manifest `status=complete` before FSI trigger
- Same run_id retry produces identical resource count
- FSI logs show skip for already-ingested run_id
- No duplicate resources in Firely after retry

**How to Fix:**
- Add Extract checkpoint table tracking resource_type completion
- FSI bulk loader uses conditional upsert on `resource_id`
- Purge incomplete staging paths older than 7 days

---

### Q310. How do you use Delta Live Tables expectations for CMS-required field completeness?

**Answer:** I map CMS Patient Access required fields to LDP expectations per resource type—Patient: name, identifier; Condition: code, subject; EOB: type, billablePeriod. `@dp.expect_or_drop` for hard failures; `@dp.expect` warns for optional US Core Must Support gaps.

**Example:** Claim EOB missing `billablePeriod` → dropped to quarantine → excluded from Patient Access bundle until fixed—prevents Firely 422 on API query.

**How to Check:**
- Expectation dashboard pass rate per resource type > 99.5%
- Quarantine reason distribution matches known source gaps
- Firely validation report zero CMS-required field errors post-Silver
- Patient Access API test member returns complete EOB

**How to Fix:**
- Add Silver enrichment join to fill billablePeriod from claim header
- Partner escalation for systematic missing fields
- Temporary `@dp.expect` downgrade with compliance approval ticket

---

### Q311. How do you configure cluster policies for PHI workloads?

**Answer:** I enforce: single-user clusters only, no DBR LTS below certified version, instance pool with encrypted local disks, `spark.databricks.privacy.enabled=true`, disable table access via passthrough except UC, auto-termination 30min, no public IP on workers.

**Example:** `phi_compute_policy` applied to all prod workflow jobs—attempt to launch all-purpose shared cluster blocked by policy.

**How to Check:**
- Policy compliance report in account console
- Cluster event log shows policy_id on every PHI job
- No all-purpose cluster runs against prod_interop catalog
- BAA-covered instance types only in allowlist

**How to Fix:**
- Attach policy to job cluster config in DAB
- Migrate non-compliant historical jobs flagged by audit
- Request policy exception via security review—time-boxed only

---

### Q312. How do you use `table_changes` for incremental FHIR bundle generation?

**Answer:** Extract task queries `SELECT * FROM table_changes('clinical_sam.conditions', {start_version}, {end_version})` to emit only changed Condition resources as FHIR updates. Bundle packager merges with unchanged resources from last full snapshot manifest.

**Example:** 50K condition updates overnight → incremental Extract emits 50K Observation/Condition NDJSON lines vs 12M full scan.

**How to Check:**
- Extract log: `changes_read` count matches SAM merge metrics
- End version stored in workflow checkpoint table
- Firely incremental upload job processes delta bundle only
- API returns updated condition within 4h SLA

**How to Fix:**
- Reset start_version to last known good after failed Extract
- Full snapshot fallback if version gap > 7 days
- Validate change feed enabled: `delta.enableChangeDataFeed=true`

---

### Q313. How do you handle multi-payer data isolation in a shared Databricks workspace?

**Answer:** I use UC row filters or separate schemas per payer (`sam_payer_a`, `sam_payer_b`) converging to unified SAM via controlled ETL—not commingled tables without filter. Service principals scoped per payer for API export paths.

**Example:** Payer A SP reads only `sam_payer_a.*`; unified Patient Access API uses payer context from SLAP token to filter Firely compartment.

**How to Check:**
- Row filter policy: `payer_id = current_user_payer()`
- Cross-payer query test returns zero rows
- SLAP token payer claim matches Firely compartment search
- Audit log per payer access pattern normal

**How to Fix:**
- Apply `CREATE ROW FILTER` on shared tables if schema split too costly
- Fix SLAP token mapping if wrong payer data exposed
- Separate S3 export prefixes per payer for FSI

---

### Q314. How do you monitor Databricks job SLA for CMS reporting deadlines?

**Answer:** I define SLA per workflow: Claims complete by 06:00 UTC, Extract by 08:00, FSI by 10:00 for same-day API freshness. Databricks job notifications to PagerDuty on failure/timeout; Onyx Insights dashboard shows end-to-end pipeline duration trend.

**Example:** Claims job exceeds 6h → PagerDuty alert → runbook: check source file delay vs cluster issue.

**How to Check:**
- Job run duration P50/P95 in last 30 days
- SLA breach count in Onyx Insights CMS metrics panel
- Alert fired within 5min of job failure
- Recovery time documented per incident

**How to Fix:**
- Pre-scale cluster before known large payer file drops
- Split long-running task into parallel resource-type tasks
- Negotiate earlier SFTP delivery with payer if source delay chronic

---

### Q315. How do you version control Databricks notebooks vs DABs for interop code?

**Answer:** Notebooks for exploratory/quarantine review stay in GitLab repo `abacus-interop/notebooks/`; production logic lives in DAB wheel tasks (`src/abacus_extract/`) deployed via CI. No prod job points to Repos HEAD—only released wheel version.

**Example:** `fhir_silver_validation.py` packaged in wheel v1.4.2 deployed by DAB; quarantine review notebook in repo for analysts—not in critical path.

**How to Check:**
- Prod job task shows wheel entry point + version pin
- Git tag matches deployed bundle version
- No `{repo}/main` reference in prod job config
- CI runs pytest before bundle deploy

**How to Fix:**
- Migrate notebook logic to wheel module with unit tests
- Pin wheel version in DAB; bump in CI on merge to main
- Archive orphaned notebooks referencing deprecated tables

---

### Q316. How do you use Photon for FHIR JSON parsing workloads?

**Answer:** I enable Photon on Autoloader and Silver transformation clusters—JSON parsing and filter-heavy transforms benefit most. Not used on small orchestration jobs (< 10 min runtime) where driver overhead dominates.

**Example:** Rail C Silver validation cluster `runtime_engine=PHOTON`—8.9M resource parse 3.2h → 1.8h vs standard.

**How to Check:**
- Cluster config shows Photon enabled
- Workload type JSON scan in query profile
- Cost vs duration tradeoff documented
- No Photon-incompatible UDF in pipeline (Java UDF fallback)

**How to Fix:**
- Switch cluster to PHOTON runtime engine in DAB
- Replace Python row UDF with Spark SQL/native expressions where Photon can't accelerate
- Benchmark before enabling on all workflow families

---

### Q317. How do you implement data quality contracts between Rail B webhook and Silver?

**Answer:** I publish JSON Schema contract per event type in MDP registry—Lambda validates before S3 write; Autoloader Silver applies same schema via `schemaHints`. Contract version in S3 object metadata; breaking change requires new `event_type_v2` topic.

**Example:** NASCO `claim_adjudicated` schema v1.2 requires `member_id`, `claim_id`, `adjudication_date`—Lambda 400 on missing field before landing.

**How to Check:**
- Contract JSON in MDP with version and effective date
- Lambda unit tests cover required fields
- Silver quarantine rate < 0.01% for schema violations
- Partner conformance test suite passes before prod enable

**How to Fix:**
- Reject at Lambda with descriptive 400—do not land bad events
- Add optional fields as schema evolution—not required until partner ready
- Deprecate v1 topic with 90-day overlap period

---

### Q318. How do you use Databricks SQL warehouse for CMS metrics reporting?

**Answer:** I create SQL warehouse `cms_reporting_wh` (Medium, serverless) with read-only access to `sam.metrics_*` tables and Onyx Insights export views. Scheduled SQL alert queries API uptime SLA; dashboard refreshed hourly for compliance team.

**Example:** Query: `SELECT payer_id, api_family, uptime_pct FROM sam.cms_patient_access_metrics WHERE metric_date = current_date()`—feeds Power BI via ODBC.

**How to Check:**
- Warehouse uptime and query history
- Dashboard refresh timestamp < 1h stale
- SQL alert triggers when uptime_pct < 99%
- No PHI columns in metrics views (aggregated only)

**How to Fix:**
- Add materialized view if dashboard query exceeds 30s
- Scale warehouse for month-end reporting spike
- Fix broken view if upstream SAM table renamed in DAB deploy

---

### Q319. How do you secure Databricks secrets for partner OAuth (Rail B)?

**Answer:** I store partner client secrets in Databricks secret scope backed by AWS Secrets Manager—not in notebooks or git. Lambda reads from Secrets Manager directly; Databricks scope used only for batch refresh jobs. Rotation every 90 days with dual-secret overlap.

**Example:** `nasco_oauth` scope key `client_secret` → Secrets Manager ARN reference; notebook `%run refresh_partner_token` uses `dbutils.secrets.get`.

**How to Check:**
- Secret scope ACL: only `abacus-sp` read access
- No secret values in notebook output or job logs
- Rotation calendar ticket open 30 days before expiry
- Lambda IAM role least-privilege on secret ARN

**How to Fix:**
- Redact leaked secret from logs; rotate immediately
- Migrate hardcoded secrets found in notebook to scope
- Enable secret scope audit logging

---

### Q320. How do you test DAB deployments in stage before prod?

**Answer:** Stage target uses `stage_interop` catalog clone of prod schema structure with synthetic/masked data. CI deploys on merge to `release/*`; smoke test runs Claims workflow on sample file; promotion to prod requires manual approval gate.

**Example:** Release 2.3.0 deploys to stage → smoke Extract produces 100 Patient resources → IG validation pass → prod deploy approved in GitLab environment.

**How to Check:**
- Stage job run green on release branch
- IG validation report attached to release ticket
- Prod deploy audit: approver + timestamp
- Rollback tag created pre-prod deploy

**How to Fix:**
- Fix stage failure before prod—never skip gate
- Refresh stage data monthly from prod snapshot (masked)
- Automate smoke test in CI post-`bundle deploy -t stage`

---

### Q321. How do you handle skew when merging PulseEHR Patient resources (129K patients, 8.9M total)?

**Answer:** I salt hot `patient_id` keys during Bronze→Silver dedup merge, or use MERGE with cluster on `patient_id` after repartitioning by hash. AQE skew join enabled; avoid single-partition collect on patient manifest.

**Example:** Top 1% patients with 500+ Observations caused 4h merge → salting factor 10 → 55min.

**How to Check:**
- Spark UI skew warning on merge stage
- Task duration before/after salting
- Patient resource count unchanged post-merge
- No duplicate Patient ids in Gold

**How to Fix:**
- `repartition(col("patient_id"))` before MERGE
- Split merge by resource type—not one mega-merge
- Pre-aggregate Observations per patient in Silver before Gold join

---

### Q322. How do you use job parameters for multi-tenant interop workflow runs?

**Answer:** Workflow accepts `payer_id`, `processing_mode`, `source_rail` as job parameters—same job definition serves Rail A CSV and Rail C FHIR with conditional task branches. Parameters logged to run metadata for audit.

**Example:** `claims_workflow` with `payer_id=UHC`, `source_rail=A` runs CSV path; `payer_id=PULSE`, `source_rail=C` triggers FHIR Autoloader branch.

**How to Check:**
- Job run UI shows parameter values
- Correct branch executed per parameter combination
- Parameter validation fails fast on invalid payer_id
- Audit log links run to payer and rail

**How to Fix:**
- Add parameter enum validation in first task notebook
- Document parameter matrix in runbook artifact
- Default safe values if parameter omitted (dev only)

---

### Q323. How do you implement lineage tracking from CSV source to FHIR API response?

**Answer:** Unity Catalog lineage captures CSV → Bronze → SAM → Extract → staging; Onyx MDP links API request to Firely resource version and upstream `pipeline_run_id` in resource meta.tag. Combined view in Onyx Insights for audit "show me source of this EOB."

**Example:** Member queries EOB → Firely meta.tag `pipeline_run_id=abc123` → UC lineage → `claims_sam.eob` → source file `payer_uhc_20250718.csv`.

**How to Check:**
- UC lineage graph complete for SAM tables
- Firely resource meta.tag populated on Extract
- Onyx Insights trace query returns end-to-end path
- Audit drill for CMS inquiry completes in < 15min

**How to Fix:**
- Add meta.tag in Extract if missing on resource type
- Register external tables in UC for S3 source files
- Fix broken lineage after table rename in DAB

---

### Q324. How do you configure auto-scaling for variable Rail B webhook volume?

**Answer:** Autoloader structured streaming cluster uses autoscale 2-16 workers with `targetWorkers` based on `numBytesOutstanding`. Scale-down delay 10min to avoid thrashing. Separate cluster from batch SAM jobs to isolate burst impact.

**Example:** NASCO open enrollment week 10x event rate → cluster scales 2→14 workers automatically; returns to 2 after 48h.

**How to Check:**
- Cluster timeline shows scale events correlated with ingest
- No job failure due to insufficient workers during burst
- Cost report: autoscale vs fixed cluster comparison
- Queue depth near zero during peak

**How to Fix:**
- Increase max workers cap if OOM at ceiling
- Decrease scale-down delay if cost overrun acceptable
- Dedicated instance pool for webhook Autoloader isolation

---

### Q325. How do you migrate hive_metastore tables to Unity Catalog for interop?

**Answer:** I use UC upgrade assistant `MIGRATE TABLE` per schema batch—bronze first, then silver, sam. Update all job references in DAB before cutover; dual-read validation period 1 week; deprecate hive paths after zero downstream refs.

**Example:** `hive_metastore.clinical_sam.conditions` → `prod_interop.sam.clinical.conditions`—148 downstream notebook refs updated in DAB v2.0.

**How to Check:**
- UC upgrade assistant completion report
- Zero queries hitting hive_metastore in audit 7 days post-cutover
- Row counts match pre/post migration
- All DAB jobs point to UC three-part names

**How to Fix:**
- Rollback: sync table back if row count mismatch
- Fix broken grants after migration
- Update external partner ODBC connections to UC endpoint

---

### Q326. How do you use Delta Sharing for payer analytics without copying PHI?

**Answer:** I share masked SAM views via Delta Sharing to payer recipient—column masks apply at share boundary. Share includes `formulary_sam`, `pvd_sam` only; no clinical PHI tables. Recipient gets read-only Databricks or Power BI connector token.

**Example:** Payer analytics team receives share `formulary_read_share`—sees NDC and tier, not member-level claim data.

**How to Check:**
- Share recipient access log
- Recipient query returns masked columns only
- Share certificate expiry monitored
- No clinical tables in share definition

**How to Fix:**
- Revoke share immediately if wrong table included
- Renew share token before expiry
- Add row filter on share if payer-specific slice needed

---

### Q327. How do you debug a failing Extract FHIR validation task?

**Answer:** I pull task run logs, sample failing resource from staging NDJSON, run standalone IG validator against US Core SD, compare to Silver source row. Common fixes: wrong profile declaration, missing Must Support element, invalid code system URI.

**Example:** Extract fails `Patient.name`—Silver had null family name → quarantine rule too permissive → tighten Silver expect → re-run Extract.

**How to Check:**
- Task stderr shows HAPI/Firely validator error line
- Sample resource JSON attached to incident ticket
- Validator reproduces error locally
- Fix verified on 10 sample resources before full re-run

**How to Fix:**
- Patch Silver enrichment to populate missing Must Support
- Map source null to `dataAbsentReason` extension in Extract
- Update IG version if profile URL outdated

---

### Q328. How do you implement cost controls on interop Databricks spend?

**Answer:** I tag all jobs with `cost_center=interop`, use job clusters not all-purpose, autoscale with caps, OPTIMIZE to reduce scan costs, serverless SQL for ad-hoc only, and monthly review of top 10 expensive runs. Spot instances for non-critical dev/stage.

**Example:** Rail C one-time 8.9M load used job cluster with 30-day cluster policy max workers 20—$4.2K run vs $9K projected on always-on cluster.

**How to Check:**
- Databricks billing dashboard by tag
- Cluster policy max workers enforced
- Idle cluster termination within 30min
- Monthly cost review meeting minutes

**How to Fix:**
- Right-size cluster for recurring job based on 30-day profile
- Cancel orphaned all-purpose clusters via scheduled audit script
- Use incremental processing to avoid full re-scan

---

### Q329. How do you use GitLab CI with Databricks bundles for interop releases?

**Answer:** Pipeline stages: lint → pytest → `bundle validate` → deploy stage → smoke test → manual prod gate → deploy prod. Service principal OAuth via GitLab CI variable; no PAT in repo.

**Example:** `.gitlab-ci.yml` job `deploy_stage` runs on `release/2.4.0` tag; prod requires `deploy_prod` manual by on-call lead.

**How to Check:**
- CI pipeline green on release tag
- Deploy job logs show bundle version
- Failed stage blocks prod gate
- Secret rotation does not break CI auth

**How to Fix:**
- Fix validate errors locally before push
- Refresh SP OAuth token in GitLab variables
- Rollback prod via tagged previous release redeploy

---

### Q330. Scenario: Silver quarantine spikes to 15% after PulseEHR schema change. Your response?

**Answer:** I pause Autoloader promotion to Gold, sample quarantine reasons, classify as schema evolution vs data defect, update Silver rules or partner contract, reprocess quarantine batch, resume only when pass rate > 99.5%. Communicate timeline to compliance if API freshness at risk.

**Example:** PulseEHR adds required `Observation.category` → 15% quarantine → Silver rule updated to default `category=unknown` with extension → reprocess → 0.2% quarantine.

**How to Check:**
- Quarantine reason pivot table by field name
- Partner changelog confirms schema update date
- Reprocess job row count matches original quarantine count
- Gold merge and Extract succeed post-fix

**How to Fix:**
- Coordinate schema change notice with partner 30 days ahead
- Version Silver rules per `source_schema_version` parameter
- Never auto-promote quarantine to Gold without review

---

## Section R: Databricks ML / MLOps — Healthcare AI (Q331–360)

### Q331. How do you log an ePA prior authorization prediction model in MLflow for the interop platform?

**Answer:** I use MLflow autolog with explicit params (`ig_version`, `training_payer_id`, `feature_store_version`) and log metrics (AUC, precision at CMS SLA threshold). Model artifact includes conda env and input schema matching Feature Store lookup keys `member_id + procedure_code`.

**Example:** PAS denial predictor v3 logged to `prod_interop.ml.pas_denial_model` with AUC 0.87, linked to training run `run_id=abc` and Feature Store snapshot version 12.

**How to Check:**
- MLflow UI shows params, metrics, artifacts
- Model registry stage = Staging with approval note
- Input schema matches online feature lookup
- Training data lineage tag references SAM table version

**How to Fix:**
- Re-log with correct schema if feature names drifted
- Add `registered_model_name` in log step for registry promotion
- Tag run with `cms_use_case=epa_pas` for audit filter

---

### Q332. How do you use Feature Store for member clinical features in CRD/DTR workflows?

**Answer:** I publish features (`active_conditions_count`, `recent_ed_visit_90d`, `formulary_tier`) to `prod_interop.ml.member_clinical_features` with primary keys `member_id`. Training and serving read same table—offline for batch CRD rules tuning, online table for real-time DTR questionnaire routing.

**Example:** CRD service queries online store: member with `recent_ed_visit_90d=2` triggers alternate evidence pathway in DTR.

**How to Check:**
- Feature table freshness < 24h from SAM merge
- Online store sync lag < 5min
- Point-in-time join test in training notebook passes
- Feature not null rate > 98% for production keys

**How to Fix:**
- Re-run feature pipeline after SAM delay
- Backfill online store from offline snapshot
- Add default feature values for cold-start members

---

### Q333. How do you deploy a model serving endpoint for formulary alternative recommendation?

**Answer:** I register model in Unity Catalog (`prod_interop.ml.formulary_alt_model`), create Mosaic AI serving endpoint with rate limit and scale-to-zero in dev. Endpoint wraps RAG retrieval + ranker—gateway routes via Unity AI Gateway policy `formulary_agent_policy`.

**Example:** Endpoint `/serving-endpoints/formulary-alt/invocations` accepts NDC + member formulary_id, returns top 3 alternatives with confidence scores.

**How to Check:**
- Endpoint status READY in serving UI
- Latency P95 < 500ms on load test
- Unity AI Gateway logs show policy allow
- Model version matches registry Production stage

**How to Fix:**
- Roll back endpoint to previous model version
- Scale up min replicas if cold-start latency breaches SLA
- Fix feature lookup 404 if online store out of sync

---

### Q334. How do you monitor model drift on PA denial prediction using Lakehouse Monitoring?

**Answer:** I create monitor on inference table `ml.pas_inference_log` with baseline from training distribution—track `prediction_score`, `procedure_code` slice, and label delay metrics when actual PA outcome arrives. Alert on PSI > 0.2 for top features.

**Example:** Cardiology PA volume spike changes feature distribution → PSI alert → retrain trigger ticket opened.

**How to Check:**
- Monitor dashboard shows drift status green/yellow/red
- Slice by `procedure_category` highlights specialty drift
- Inference log row count matches API call volume
- Retrain ticket linked to drift alert ID

**How to Fix:**
- Schedule retrain with recent 90-day SAM data
- Adjust decision threshold temporarily with clinical approval
- Investigate upstream SAM schema change if feature null spike

---

### Q335. How do you implement RAG for Provider Agent formulary policy Q&A?

**Answer:** I chunk payer formulary policy PDFs and SAM `formulary_sam.drug` rows, embed via Databricks Vector Search index `formulary_policy_idx`, retrieve top-k at query time, ground LLM response via Unity AI Gateway with citation requirement. MCP `formulary_lookup` tool wraps retrieval.

**Example:** Provider asks "PA required for Humira?" → RAG retrieves policy section + NDC row → Agent responds with tier, PA flag, doc link.

**How to Check:**
- Vector index sync lag < 24h post-formulary SAM merge
- Evaluation set 50 questions > 90% citation accuracy
- Gateway blocks response without source chunk (policy enforced)
- No raw PHI in indexed documents

**How to Fix:**
- Re-chunk after formulary schema change
- Increase k if recall low on eval set
- Filter index to active NDCs only

---

### Q336. How do you use MLflow nested runs for hyperparameter tuning on denial models?

**Answer:** Parent run logs experiment config; child runs per hyperparameter set via `hyperopt` or parallel foreach. Best child promoted by `mlflow.search_runs` on `metrics.auc` max—parent tags `best_child_run_id`.

**Example:** 20 child runs tuning `max_depth`, `learning_rate`—best AUC 0.89 child run_id=xyz promoted to registry.

**How to Check:**
- MLflow experiment shows parent-child hierarchy
- Best run metrics reproducible on re-train
- Parent run notes document search space
- No orphaned failed children without error logged

**How to Fix:**
- Increase max trials if convergence not reached
- Fix feature leakage if val AUC suspiciously high
- Prune bad runs with early stopping callback

---

### Q337. How do you implement blue-green deployment for a CMS-facing model endpoint?

**Answer:** I deploy new model version to green endpoint alias, run shadow traffic comparison for 48h against blue, promote alias to 100% traffic if error rate and latency within bounds. Unity AI Gateway routes canary percentage via policy weight.

**Example:** Formulary model v4 on green—10% shadow → mismatch rate 0.3% → full promote Friday off-peak.

**How to Check:**
- Shadow log comparison report attached to change ticket
- Latency P95 green ≤ blue + 10%
- Business metric (alt acceptance rate) stable
- Rollback alias switch tested

**How to Fix:**
- Instant rollback: point alias to blue version
- Fix training-serving skew if shadow mismatch high
- Extend shadow period if insufficient traffic

---

### Q338. How do you prevent PHI leakage in ML training notebooks?

**Answer:** I train on de-identified feature tables or aggregated slices—never copy raw `member_name` into notebooks. Use UC masked views, disable `display()` on raw SAM, scan notebook outputs in CI, and restrict notebook ACL to ML service principal + named users.

**Example:** PA model features: age_band, diagnosis_category—not member_name or exact DOB.

**How to Check:**
- Feature table column list has no direct identifiers
- Notebook ACL audit quarterly
- CI secret/PHI scanner clean on commit
- Model artifact explainability uses coded features only

**How to Fix:**
- Drop identifier columns from feature pipeline
- Revoke overly broad notebook access
- Rotate credentials if PHI pasted in cell output

---

### Q339. How do you use Pandas UDF for FHIR resource feature extraction in ML pipelines?

**Answer:** I apply Pandas UDF on Silver Observation batches to compute `bmi_latest`, `hba1c_latest` per member—vectorized per partition faster than row UDF. Output written to Feature Store offline table.

**Example:** `@pandas_udf` on Observation codes LOINC 39156-5 computes BMI from valueQuantity across 2M rows in 8min vs 45min row UDF.

**How to Check:**
- Spark UI shows Pandas UDF stage duration
- Sample member feature values match manual calculation
- Null rate for members without qualifying Observations
- Feature pipeline SLA within batch window

**How to Fix:**
- Replace row UDF with Pandas UDF or Spark SQL window
- Handle unit conversion edge cases in UDF
- Cache filtered Observation subset before UDF if reused

---

### Q340. How do you register and approve models in Unity Catalog model registry?

**Answer:** I register via `mlflow.register_model` to UC three-level name, request approval in registry UI with checklist (bias review, PHI scan, CMS use case doc), promote Staging → Production only after sign-off from clinical informatics + security.

**Example:** `prod_interop.ml.pas_denial_model` version 3 in Staging → approval ticket #4521 → Production alias updated.

**How to Check:**
- Registry shows version, stage, approver metadata
- Approval checklist attached in ticket
- Production alias points to approved version only
- Deprecated versions archived not deleted

**How to Fix:**
- Reject promotion if eval set not updated for new IG
- Archive compromised version; rotate endpoint
- Document rollback path in registry description

---

### Q341. How do you use Ray `map_in_batches` for large-scale FHIR embedding generation?

**Answer:** For RAG index rebuild over 8.9M resources, I use Ray on Databricks `map_in_batches` with batch_size 500 to call embedding API—parallelizes network-bound embedding vs single-thread driver loop.

**Example:** Observation text embed for vector index: Ray 32 workers, 500 batch → 8.9M embeddings in 2.1h vs 14h sequential.

**How to Check:**
- Ray dashboard shows worker utilization
- Embedding dimension consistent across batches
- Failed batch retry count < 0.1%
- Vector index document count matches source

**How to Fix:**
- Reduce batch size if API rate limit hit
- Checkpoint batch outputs to Delta for resume
- Validate embedding model version matches index config

---

### Q342. How do you evaluate RAG quality for Patient Agent FAQ before go-live?

**Answer:** I maintain golden Q&A set (50 member FAQ pairs) with expected citations from plan documents. Metrics: answer correctness, citation match, hallucination rate (human review sample 10%). Gate: > 85% correctness, 0 PHI in responses, 100% policy block on out-of-scope clinical advice.

**Example:** "When is my deductible reset?" → must cite `plan_summary_2025.pdf` section 3—not generic LLM guess.

**How to Check:**
- Eval notebook scores logged to MLflow each release
- Human review sample documented
- Gateway refusal rate for clinical diagnosis prompts = 100%
- Regression test in CI on golden set

**How to Fix:**
- Add missing plan doc chunks to index
- Tighten system prompt with scope limits
- Increase retrieval k for benefits questions

---

### Q343. How do you log inference requests for CMS audit without storing PHI?

**Answer:** Inference log table stores: `request_id`, `model_version`, `timestamp`, `payer_id`, hashed `member_id`, input feature hash, prediction, latency—no raw clinical text. Retention 90 days; UC row filter by payer.

**Example:** `ml.pas_inference_log` row: `member_hash=sha256(...)`, `procedure_code=27447`, `score=0.72`.

**How to Check:**
- Log schema has no PHI column names
- Sample rows pass PHI scanner
- Retention job deletes > 90 days
- Join to actual outcome table uses hash key only

**How to Fix:**
- Drop accidental raw text column from log pipeline
- Re-hash if salt rotation required
- Anonymize existing log if PHI found in incident

---

### Q344. How do you use MLflow autolog with Spark for feature pipeline tracking?

**Answer:** I enable `mlflow.spark.autolog()` in feature engineering notebook—logs Spark job metrics, params (`source_table_version`), and output dataset path. Links feature build to downstream training run via tag `feature_pipeline_run_id`.

**Example:** Feature pipeline run `fp_789` logged with 12M rows written; training run tags `feature_pipeline_run_id=fp_789` for reproducibility.

**How to Check:**
- MLflow shows Spark autolog metrics (duration, rows)
- Training run tag resolves to feature run
- Re-run feature pipeline reproduces row counts ±0.1%
- Data version matches SAM merge version

**How to Fix:**
- Disable autolog noise params if experiment cluttered
- Pin SAM version in feature run params explicitly
- Fix broken tag link in training notebook

---

### Q345. How do you implement MCP tools for AI agents accessing interop data?

**Answer:** I deploy MCP servers: `fhir_read` (read-only Firely search), `sam_lookup` (Databricks SQL for aggregated metrics), `notify` (Slack/email). Unity AI Gateway whitelists tools per agent policy—Patient Agent gets `notify` only; Payer Ops gets `sam_lookup` + `notify`.

**Example:** Payer Ops Agent calls MCP `sam_lookup` with query "Bronze lag by source" → returns structured JSON → Agent formats Slack alert.

**How to Check:**
- MCP server health endpoint green
- Gateway policy denies unauthorized tool for agent role
- Tool audit log per invocation
- No write/delete tools exposed to LLM agents

**How to Fix:**
- Restart MCP server on connection pool exhaustion
- Tighten SQL whitelist if agent generated broad query
- Add rate limit per agent on notify tool

---

### Q346. How do you handle label delay for PA outcome in model retraining?

**Answer:** PA decisions arrive 3–14 days after prediction—I store predictions immediately, join labels via nightly job on `claim_id + auth_id`, retrain monthly on matured labels only. Monitor provisional vs final metric separately.

**Example:** July predictions joined to August outcomes → September retrain uses labels with ≥14 day maturity filter.

**How to Check:**
- Label join job row match rate > 95%
- Maturity filter documented in training notebook
- Provisional AUC vs final AUC tracked in MLflow
- Unlabeled prediction backlog age histogram

**How to Fix:**
- Fix join keys if match rate drops
- Extend maturity window if payer decision delay increases
- Exclude immature labels from training set strictly

---

### Q347. How do you use Unity AI Gateway rate limits for agent cost control?

**Answer:** I set per-agent token limits (`patient_agent`: 4K req/day, `payer_ops_agent`: 10K), model allowlist (`databricks-meta-llama-3-70b-instruct` only), and block external model routes. Alert at 80% daily quota.

**Example:** Patient notification burst during open enrollment hits 80% → throttle non-critical FAQ queries; CRD real-time unaffected (separate endpoint).

**How to Check:**
- Gateway usage dashboard by agent policy
- 429 responses logged with agent id
- Monthly cost by agent within budget
- No bypass routes to unapproved models

**How to Fix:**
- Increase quota with finance approval
- Cache frequent RAG retrievals to reduce LLM calls
- Route batch summarization to smaller model

---

### Q348. How do you implement A/B test on formulary alternative ranking model?

**Answer:** MLflow model alias `Champion` vs `Challenger` with endpoint traffic split 90/10 via serving config. Track click-through on provider portal alternative selection as business metric—promote Challenger if +5% selection rate with p<0.05 over 2 weeks.

**Example:** Challenger v4 shows 7% higher alt selection → promoted to Champion after clinical review.

**How to Check:**
- Traffic split matches config
- Business metric dashboard by model version
- Statistical significance calculation documented
- No member harm signal (PA denial rate stable)

**How to Fix:**
- Stop test if Challenger increases inappropriate alt rate
- Balance split if insufficient Challenger traffic
- Fix tracking pixel if selection events missing

---

### Q349. How do you package ML dependencies for Databricks serving endpoints?

**Answer:** I log model with `mlflow.pyfunc` wrapper and `conda.yaml`/`requirements.txt` pinned to DBR-compatible versions. Integration test loads model in staging endpoint before prod. Avoid sklearn version mismatch between train and serve.

**Example:** `conda.yaml` pins `scikit-learn==1.3.0`, `pandas==2.0.3`—staging endpoint load test passes before prod promotion.

**How to Check:**
- Model artifact conda.yaml present in registry
- Staging load test notebook green
- Serving container logs no import errors
- Prediction parity train vs serve on 100 samples

**How to Fix:**
- Re-log model with corrected env file
- Use `mlflow.pyfunc.log_model` with `code_path` for custom preprocess
- Match DBR ML runtime for serving cluster

---

### Q350. Scenario: Patient Agent gives wrong deductible answer. How do you investigate?

**Answer:** I pull gateway trace: prompt, retrieved chunks, model response. Verify RAG retrieved correct plan doc for member's plan_id; check if formulary SAM stale; review if member switched plans mid-year. Fix index gap or prompt; add case to golden eval set.

**Example:** Wrong answer: retrieved 2024 plan doc—member on 2025 plan → index filter missing `plan_year` → fixed → re-eval pass.

**How to Check:**
- Gateway trace shows retrieval chunks and scores
- Member plan_id in session context matches SAM
- Index sync timestamp after plan update
- Golden eval includes this failure pattern post-fix

**How to Fix:**
- Add metadata filter `plan_year=2025` on retrieval
- Re-sync plan documents to vector index
- Patient Agent sends "verify with payer" fallback if confidence low

---

### Q351. How do you use Feature Store `write_online_table` for real-time CRD?

**Answer:** After SAM merge, feature pipeline publishes to offline table then `FeatureStoreClient.write_table` syncs to online table `member_cr_features_online`—CRD Onyx service performs single-row lookup by `member_id` at API request time.

**Example:** CRD request for member M123 → online lookup 12ms → returns `active_pa_count`, `formulary_id` → rule engine decides documentation requirement.

**How to Check:**
- Online table last sync timestamp < 1h
- Lookup latency P95 < 50ms in CRD service metrics
- Feature values match offline for sample audit
- Sync failure alert configured

**How to Fix:**
- Trigger manual sync after emergency SAM fix
- Scale online store throughput for enrollment spike
- Fallback to cached offline features if online unavailable (degraded mode)

---

### Q352. How do you document model risk for CMS-adjacent AI features?

**Answer:** I maintain model card per production model: intended use, limitations, training data description, bias analysis, human oversight requirement, rollback procedure. Stored in Git + linked from registry. Clinical informatics signs PA models; legal reviews Patient Agent.

**Example:** Model card for PAS denial model states "decision support only—not auto-denial"; override rate tracked monthly.

**How to Check:**
- Model card file in repo matches registry version
- Sign-off dates current (< 12 months)
- Override/appeal rate within expected bounds
- Audit request produces cards within 24h

**How to Fix:**
- Update card on any retrain with material data change
- Pause endpoint if card sign-off expired
- Add bias slice analysis if disparity flagged

---

### Q353. How do you chain MLflow runs from feature pipeline → train → deploy?

**Answer:** Orchestrator workflow: Task 1 feature pipeline logs run_id → Task 2 training reads param `feature_run_id` → Task 3 deploy reads `model_version` if metrics pass gate. Failed metric gate blocks deploy task.

**Example:** Databricks job `ml_pas_weekly`: feature run → train AUC 0.86 > 0.84 threshold → auto-register → staging endpoint update.

**How to Check:**
- Job task values pass run_ids correctly
- Deploy skipped when AUC below threshold
- End-to-end job duration within Sunday window
- Alert on any task failure

**How to Fix:**
- Fix param passing if train can't find feature snapshot
- Manual deploy override requires ticket approval
- Rollback endpoint if post-deploy smoke fails

---

### Q354. How do you use embedding model versioning for formulary RAG index?

**Answer:** I pin embedding model ID in index config (`databricks-bge-large-en` v1)—re-embed entire index on model upgrade, blue-green index swap, eval golden set before cutover. Never mix embeddings from two models in one index.

**Example:** Upgrade bge v1→v2: build `formulary_policy_idx_v2`, eval recall +3%, swap alias Sunday 2am.

**How to Check:**
- Index metadata shows embedding model version
- Eval recall/precision before alias swap
- Document count v1 == v2
- Query latency comparable post-swap

**How to Fix:**
- Full re-embed if mixed versions detected
- Rollback alias to v1 index
- Update MCP tool default index parameter

---

### Q355. How do you implement human-in-the-loop for Payer Ops Agent escalation?

**Answer:** Agent creates draft notification with severity and evidence links; CRITICAL events require human approve in Slack workflow before send. Audit log stores approver, original draft, final message. Auto-send only WARN and below per policy.

**Example:** INGESTION_LAG CRITICAL draft → on-call lead clicks Approve in Slack → message sent to payer integration channel.

**How to Check:**
- CRITICAL events have approve/reject audit row
- No CRITICAL auto-sent without approver in last 30 days
- Rejected drafts logged with reason
- Escalation timeout alerts if no approver in 30min

**How to Fix:**
- Fix Slack workflow webhook if approve stuck
- Fall back to PagerDuty if approver timeout
- Tune severity so CRITICAL reserved for true outages

---

### Q356. How do you validate ML model fairness across member demographics?

**Answer:** I slice evaluation metrics by age_band, sex, race (where available in de-identified SAM), and Medicaid vs commercial lines. Flag if denial prediction TPR difference > 10pp between slices. Document in model card; no auto-deploy if breach.

**Example:** PA model TPR gap 12pp commercial vs Medicaid → clinical review → retrain with balanced sampling → gap reduced to 6pp.

**How to Check:**
- Fairness report notebook output per release
- Slice sample sizes sufficient (> 100 per slice)
- Sign-off from compliance on acceptable thresholds
- Production monitoring continues slice metrics monthly

**How to Fix:**
- Adjust training sample weights
- Add slice-specific calibration
- Do not deploy if unresolved fairness breach

---

### Q357. How do you use MLflow model signatures for FHIR-adjacent serving inputs?

**Answer:** I define signature with `member_id` string, `procedure_code` string, feature vector schema—serving rejects malformed requests before inference. Signature logged with model artifact for contract testing.

**Example:** Signature missing `formulary_id` → serving 400 Bad Request → logged → client fixes request payload.

**How to Check:**
- `mlflow models validate` passes locally
- Serving logs show schema validation errors count
- Client SDK generated from signature if applicable
- Integration test sends invalid payload expects 400

**How to Fix:**
- Update signature on feature add; bump model version
- Coordinate client team on schema change notice
- Backward compatible: add optional fields only in minor version

---

### Q358. How do you isolate ML experimentation from production interop catalog?

**Answer:** Experiments use `dev_interop.ml` catalog; no prod SAM read except masked sample tables. Production models registered only from CI release branch. Experiment clusters cannot access prod_interop write.

**Example:** Data scientist runs hyperopt in `dev_interop.ml.experiments`—prod_interop read blocked by UC grant.

**How to Check:**
- UC grants: human users no write on prod_interop
- Experiment runs tagged `environment=dev`
- Prod registry versions only from CI SP
- No prod table names in dev experiment params accidentally

**How to Fix:**
- Revoke prod write from analyst groups
- Copy masked sample to dev for experimentation
- Delete accidental prod write from misconfigured notebook

---

### Q359. How do you monitor GPU utilization for embedding index rebuild jobs?

**Answer:** Ray/GPU cluster jobs log GPU utilization to Spark metrics; alert if avg < 30% (underutilized) or 100% with queue backlog. Right-size worker count for 8.9M resource embed window.

**Example:** 8x A10 cluster 45% avg GPU → reduce to 4x saves $800 with same 2.1h runtime.

**How to Check:**
- Cluster metrics GPU % during job
- Cost per million embeddings trend
- Job completes within maintenance window
- No OOM at reduced cluster size

**How to Fix:**
- Increase batch size to improve GPU fill
- Reduce workers if sustained low utilization
- Use inference optimized instance type for embed API

---

### Q360. Scenario: Unity AI Gateway blocks agent mid-incident. What do you do?

**Answer:** Check gateway policy (quota, model allowlist, content filter), verify MCP tool health, fail open to manual runbook for CRITICAL notifications only if gateway down > 15min—with leadership approval. Never bypass PHI policy.

**Example:** Gateway 503 during outage → Payer Ops uses manual Slack template from runbook → gateway restored → agent resumes with queued events replay.

**How to Check:**
- Gateway status page and error logs
- Policy change audit last 24h
- MCP server health checks
- Incident timeline documents manual fallback

**How to Fix:**
- Scale gateway capacity if rate limit false positive
- Fix misconfigured policy denying valid tool
- Queue events in `ai_events` for replay after restore

---

## Section S: Microsoft Fabric — Healthcare Analytics & Ingestion (Q361–390)

### Q361. How do you use Fabric Lakehouse for payer-facing CMS metrics analytics?

**Answer:** I mirror aggregated SAM metrics (no PHI) from Databricks via OneLake shortcut to ADLS export path—Fabric Lakehouse `cms_metrics_lh` holds `patient_access_uptime`, `api_call_volume` tables for Power BI semantic model. Refresh daily after Onyx Insights export lands.

**Example:** Shortcut `abfss://metrics@onyxexports/cms/` → Fabric table `cms_patient_access_daily` → Power BI dashboard for compliance officer.

**How to Check:**
- Shortcut connection status green in Fabric
- Row counts match Databricks export manifest
- Power BI refresh succeeds last 7 days
- No PHI columns in mirrored schema

**How to Fix:**
- Re-auth shortcut if ADLS credential expired
- Fix broken path if export prefix changed
- Update semantic model if column renamed

---

### Q362. How do you build a Fabric Data Factory pipeline for Rail B webhook landing monitoring?

**Answer:** Copy activity pulls S3/API landing file counts into Fabric Lakehouse staging; If Condition checks count delta vs expected; On failure triggers Teams notification activity and invokes `interop_escalation` pipeline. Schedule every 15min during business hours.

**Example:** NASCO webhook pipeline: Copy landing manifest → count < threshold → Teams alert to integration channel + ticket creation notebook.

**How to Check:**
- Pipeline run history success rate > 99%
- Failure branch fired on synthetic zero-file test
- Teams message received within 5min of failure
- Invoke pipeline parameter passes incident severity

**How to Fix:**
- Fix Copy activity connection to S3/API
- Adjust threshold if partner changes send schedule
- Add retry policy 3x exponential backoff on transient failures

---

### Q363. How do you implement Type 2 SCD for member eligibility in Fabric warehouse?

**Answer:** I hash compare `member_id + plan_id + effective_date + term_date + benefit_tier` in staging vs dimension—hash mismatch closes current row (`is_current=0`, `end_date=yesterday`) and inserts new row. Fabric notebook or Dataflow Gen2 with hash key column.

**Example:** Member switches PPO→HMO mid-year → old eligibility row end-dated; new row `is_current=1` with HMO plan_id.

**How to Check:**
- Only one `is_current=1` per member_id
- Hash function deterministic on same input
- Historical row count matches known plan change events
- Point-in-time query returns correct plan for service_date

**How to Fix:**
- Fix hash column list if missing benefit_tier caused missed change
- Backfill SCD from SAM eligibility history
- Reject staging rows with overlapping effective dates

---

### Q364. How do you apply Dynamic Data Masking (DDM) in Fabric SQL for analyst access?

**Answer:** I create Fabric Warehouse with DDM on `member_ssn` (partial), `member_dob` (year only), `member_email` (email mask)—analysts get read via `clinical_analyst` role; compliance gets unmask via separate elevated role with audit.

**Example:** Analyst query `SELECT member_dob FROM members` returns `xxxx-xx-15`—compliance role sees full date with justification logged.

**How to Check:**
- Test query as each Entra ID group
- DDM policy applied in Fabric warehouse settings
- Elevated unmask events in audit log
- Power BI DirectQuery respects RLS+DDM

**How to Fix:**
- Apply ALTER COLUMN MASK in Fabric warehouse DDL
- Fix RLS policy if cross-payer leak despite DDM
- Revoke elevated role from over-provisioned users

---

### Q365. How do you optimize Fabric Lakehouse tables with V-Order?

**Answer:** I enable V-Order on high-read CMS metrics and formulary dimension tables—improves Power BI DirectLake scan performance. Run after large load completes; trade-off is slower writes acceptable for daily batch tables.

**Example:** `formulary_dim` 2M rows V-Order enabled—Power BI visual load 4.2s → 1.1s.

**How to Check:**
- Table properties show V-Order enabled
- Power BI performance analyzer before/after
- Write duration acceptable post-enable
- Fabric capacity metrics within SKU limits

**How to Fix:**
- Disable V-Order on write-heavy staging tables
- OPTIMIZE/VACUUM equivalent in Fabric after bad compaction
- Scale Fabric capacity if CPU spike during refresh

---

### Q366. How do you use Semantic Link to push Fabric metrics to Power BI dataset?

**Answer:** I define semantic model in Fabric linking Lakehouse tables with relationships (`payer_id`, `metric_date`). Measures: `uptime_pct`, `api_calls_millions`. Incremental refresh on `metric_date` last 90 days—full history yearly.

**Example:** Semantic Link connects `cms_patient_access_daily` to Power BI dataset `CMS Compliance`—executive dashboard auto-refreshes 6am.

**How to Check:**
- Semantic model validation no orphan relationships
- Incremental refresh partition counts correct
- Measure values match Databricks source query
- Refresh failure email configured

**How to Fix:**
- Fix relationship cardinality if duplicate measure inflation
- Extend incremental window if late-arriving metrics
- Re-bind dataset if Lakehouse table renamed

---

### Q367. How do you configure incremental refresh with RangeStart/RangeEnd for claims analytics?

**Answer:** Power Query parameters `RangeStart`, `RangeEnd` filter `service_date` on Fabric Lakehouse claims summary (aggregated, de-identified). Gateway connection passes date window per refresh partition—90-day rolling incremental, 7-year archive full yearly.

**Example:** Incremental refresh loads service_date >= today-90 only—full partition 2018–2025 refreshed annually in January.

**How to Check:**
- Refresh history shows incremental vs full timing
- Partition row counts stable week-over-week
- Range parameters bound correctly in Power Query M
- No duplicate dates across partitions

**How to Fix:**
- Fix M query date filter if full scan each refresh
- Adjust partition count if refresh exceeds SLA
- Handle timezone on service_date boundary

---

### Q368. How do you use Eventstream for real-time claim adjudication monitoring (Rail B)?

**Answer:** Eventstream ingests webhook events from Azure Event Hub mirror of Kinesis fan-out—Aggregate by `payer_id` tumbling window 5min, count adjudications, sink to Lakehouse `realtime_adjudication_metrics`. Power BI real-time dashboard for ops.

**Example:** NASCO events → Eventstream 5min tumbling count → Lakehouse → dashboard shows adjudication rate drop alert.

**How to Check:**
- Eventstream throughput matches source rate ±5%
- Window aggregation timestamps aligned UTC
- Sink table row count increases during test burst
- Alert rule fires on 50% drop vs baseline

**How to Fix:**
- Scale Eventstream CU if lag detected
- Fix deserialization if JSON schema change
- Replay from Event Hub retention if pipeline down < 7 days

---

### Q369. How do you integrate Fabric Git with interop analytics notebooks?

**Answer:** I connect Fabric workspace to GitLab repo `fabric-interop-analytics`—notebooks for CMS reporting and SCD logic versioned on `main`, deploy to prod workspace via PR merge. No secrets in Git; connections reference Key Vault.

**Example:** Eligibility SCD notebook change PR #88 → merge → sync to prod Fabric workspace → pipeline uses updated logic next run.

**How to Check:**
- Git sync status clean in Fabric workspace
- Prod workspace synced to release tag not feature branch
- Connection references Key Vault not plaintext
- Diff review shows no accidental prod connection string

**How to Fix:**
- Resolve merge conflict in Fabric Git sync UI
- Rotate secret if accidentally committed—use BFG purge
- Re-bind connection after workspace migration

---

### Q370. How do you use OneLake shortcuts to Databricks export without data duplication?

**Answer:** Shortcut from Fabric Lakehouse to ADLS path where Databricks writes aggregated CMS metrics NDJSON/Parquet—Fabric reads in place, no copy cost, single source of truth remains Databricks SAM export job.

**Example:** Shortcut `Tables/cms_metrics` → `abfss://exports@datalake/metrics/cms/`—Power BI reads without second ETL copy.

**How to Check:**
- Shortcut metadata shows target path
- File format matches Fabric read expectations (Parquet)
- Latency: data visible within 15min of export job
- Storage billing shows no duplicate copy

**How to Fix:**
- Convert export to Parquet if CSV shortcut slow
- Fix ADLS RBAC if shortcut auth failure
- Update shortcut path on export job output change

---

### Q371. How do you implement pipeline failure dependency chain for interop SLA reporting?

**Answer:** Fabric pipeline: Activity 1 Copy metrics → Activity 2 Transform → Activity 3 Publish semantic model. Activity 2 `dependsOn` Activity 1 Success; Activity 3 On Failure sends email + skips publish. Failure path logs to Lakehouse `pipeline_errors`.

**Example:** Copy fails (ADLS timeout) → Transform skipped → email to on-call → error row in `pipeline_errors` with activity name and timestamp.

**How to Check:**
- Dependency graph in pipeline JSON correct
- Synthetic Copy failure triggers skip + email
- Error table populated with run_id
- Success path completes within 45min SLA

**How to Fix:**
- Fix dependency type (Success vs Completion) if race condition
- Increase Copy timeout for large export files
- Add retry on Copy before failure branch

---

### Q372. How do you use Dataflow Gen2 for payer roster cleansing before SAM?

**Answer:** Dataflow Gen2 ingests raw roster CSV from OneLake landing—Power Query steps: trim names, standardize NPI format, dedupe on `member_id`, flag invalid rows to quarantine table. Replace mode for full roster; append for delta roster files.

**Example:** Roster with duplicate member_ids → Dataflow keeps latest `effective_date` row → quarantine outputs 23 invalid NPI rows for payer correction.

**How to Check:**
- Dataflow refresh history success
- Output row count vs source ± quarantine
- NPI validation regex catches test values (0000000000)
- Downstream SAM merge accepts Dataflow output schema

**How to Fix:**
- Fix M step order if dedupe before normalize caused misses
- Change update method Append vs Replace per file type
- Add payer-specific mapping table for name suffix handling

---

### Q373. How do you secure Fabric workspace access for HIPAA analytics?

**Answer:** Entra ID groups map to Fabric roles: Viewer (Power BI consumers), Contributor (pipeline authors), Admin (platform team only). Conditional access requires MFA; no guest access to PHI workspaces; Private Link to OneLake where required.

**Example:** `fabric-interop-prod` workspace: only `interop-admins` Contributor; analysts Viewer on semantic model only—not raw Lakehouse.

**How to Check:**
- Workspace access audit quarterly
- Guest user count = 0 on prod workspace
- Conditional access policy applied
- Activity log shows no anonymous access

**How to Fix:**
- Remove direct user grants; use groups only
- Migrate users to correct group from over-privileged access
- Enable Private Link if compliance audit finding

---

### Q374. How do you compare Fabric vs Databricks for clinical SAM vs CMS reporting?

**Answer:** Databricks owns PHI clinical SAM, FHIR Extract, and IG validation—source of truth. Fabric owns de-identified aggregates, Power BI semantic models, and business user self-service. Never duplicate clinical transformation in both—Fabric consumes exports only.

**Example:** `clinical_sam.conditions` stays Databricks; Fabric gets `conditions_summary_by_payer_month` aggregate only.

**How to Check:**
- Architecture diagram shows single clinical transform path
- Fabric tables contain no member-level clinical identifiers
- Export job manifest lists allowed columns
- Data governance sign-off on boundary

**How to Fix:**
- Remove rogue PHI copy in Fabric if discovered
- Add export column allowlist validation in Databricks job
- Document boundary in onboarding for new analysts

---

### Q375. How do you handle Fabric capacity throttling during month-end CMS reporting?

**Answer:** I schedule heavy refreshes staggered (not all 6am), use incremental refresh, pre-warm V-Order tables off-peak, and temporarily scale Fabric capacity SKU F64→F128 for last 3 business days of month if budget approved.

**Example:** Month-end: move formulary refresh to 4am, CMS metrics 6am, eligibility SCD 8am—avoid concurrent full scans.

**How to Check:**
- Capacity metrics show throttling events
- Refresh completion before business hours deadline
- Cost report for temporary SKU bump
- User complaints on slow dashboard during window

**How to Fix:**
- Purchase burst capacity ahead of known peak
- Reduce model complexity (remove unused columns)
- Cache frequently used aggregates as materialized Lakehouse tables

---

### Q376. How do you implement row-level security in Power BI for multi-payer CMS dashboard?

**Answer:** RLS role `PayerA` filters `payer_id = 'A'` on all fact tables; embed reports pass `payer_id` from Entra ID UPN mapping table. Test with "View as role" before publish.

**Example:** Payer B user opens dashboard—sees only Payer B uptime metrics; cross-payer row count zero.

**How to Check:**
- View as each RLS role in Power BI Desktop
- Embed token test with sample users
- DAX filter uses `USERPRINCIPALNAME()` lookup table
- Security audit annually with sample account matrix

**How to Fix:**
- Fix mapping table if new payer not in RLS
- Add missing table to RLS filter if leak found
- Remove Admin publish rights from payer users

---

### Q377. How do you use Fabric notebook vs Data Factory for eligibility SCD orchestration?

**Answer:** SCD logic in Fabric notebook (complex hash/compare)—Data Factory orchestrates schedule, dependencies, failure alerts. Notebook returns status code; pipeline If Condition branches on notebook exit value.

**Example:** Pipeline 2am: notebook `eligibility_scd` → exit 0 success → refresh semantic model; exit 1 → Teams alert.

**How to Check:**
- Notebook exit value wired to pipeline condition
- Notebook run duration trend stable
- Failed notebook output logged to error table
- Idempotent re-run produces same current rows

**How to Fix:**
- Fix notebook exception handling to return proper exit code
- Split notebook if timeout exceeds pipeline limit
- Add checkpoint for long historical backfill

---

### Q378. Scenario: Fabric shortcut shows stale CMS metrics vs Databricks. Diagnosis?

**Answer:** Check Databricks export job completion time, ADLS file timestamps at shortcut path, Fabric shortcut sync status, Power BI cache vs DirectLake mode. Usually export delay or shortcut cache—not wrong data in SAM.

**Example:** Export job failed silently → ADLS files 26h old → shortcut stale → Power BI shows yesterday metrics.

**How to Check:**
- Export job run status in Databricks
- ADLS `lastModified` on latest Parquet file
- Fabric shortcut refresh/sync button
- Power BI dataset refresh log

**How to Fix:**
- Re-run export job; verify manifest complete
- Force shortcut refresh in Fabric
- Fix export job alert if failure undetected

---

### Q379. How do you document Fabric pipeline lineage for CMS audit?

**Answer:** I maintain data lineage diagram: Databricks export → ADLS → Fabric shortcut → semantic model → Power BI report. Fabric lineage view plus external doc in compliance folder with owner contacts and refresh SLA.

**Example:** Auditor asks "source of uptime_pct on March dashboard" → lineage doc traces to `sam.cms_patient_access_metrics` Databricks table and Onyx Insights API log aggregation.

**How to Check:**
- Fabric lineage graph populated for workspace
- External doc updated within 30 days of pipeline change
- Auditor drill completed in < 1 hour test
- Column definitions match between systems

**How to Fix:**
- Register manual lineage if shortcut not auto-detected
- Update doc on any export path or measure formula change
- Add column glossary to semantic model description

---

### Q380. How do you use Fabric Dataflow Replace vs Append for formulary updates?

**Answer:** Full formulary file from payer → Replace update method on `formulary_staging`—complete swap daily. Delta NDC updates only → Append with downstream merge dedupe on `ndc + effective_date` in notebook.

**Example:** Payer sends full formulary Monday (Replace); Wed delta file (Append) → notebook merges into `formulary_dim` Type 1 for tier changes.

**How to Check:**
- Dataflow settings match file type from MDP registry
- Row count Replace matches source file
- Append delta no duplicate NDC current rows
- Downstream Power BI shows new drug within SLA

**How to Fix:**
- Switch to Replace if Append duplicates caused tier conflicts
- Add pre-Append validation for required NDC columns
- Coordinate payer on file type per delivery schedule

---

### Q381. How do you mirror Rail A CSV ingestion status in Fabric for operations dashboard?

**Answer:** Databricks workflow writes CSV ingest status JSON to ADLS after each Rail A run—Fabric Copy ingests to `rail_a_ingest_status` Lakehouse table. Dashboard shows file name, row count, validation pass rate, last success timestamp per payer.

**Example:** UHC CSV failed schema validation → status row `status=FAILED`, `error=missing_claim_id` → ops dashboard red tile.

**How to Check:**
- Status file written every workflow run
- Fabric table lag < 30min behind Databricks
- Dashboard tile matches Databricks job outcome
- Historical status retained 90 days

**How to Fix:**
- Fix export task if status file missing
- Add pipeline trigger on file arrival vs schedule only
- Alert if no status row expected window elapsed

---

### Q382. How do you implement Invoke Pipeline for interop incident escalation in Fabric?

**Answer:** Parent pipeline on failure invokes child `escalation_pipeline` with parameters: `severity`, `pipeline_name`, `error_message`, `run_id`. Child sends Teams + emails compliance distribution list for CRITICAL CMS SLA breaches.

**Example:** CMS metrics pipeline fails 6am → escalation CRITICAL → Teams #interop-oncall + email compliance lead within 2min.

**How to Check:**
- Invoke activity parameter mapping correct
- Escalation received on synthetic failure test quarterly
- CRITICAL vs WARN routing per parameter
- Run_id in message links to Fabric run details

**How to Fix:**
- Fix Teams connector auth if messages stop
- Update distribution list in pipeline parameter
- Dedupe alerts if retry causes multiple invocations

---

### Q383. How do you use Fabric for VBC quality measure reporting alongside interop?

**Answer:** VBC measures computed from de-identified clinical aggregates exported from SAM—not duplicate clinical logic. Fabric Lakehouse holds HEDIS-like measure numerators/denominators by payer line of business; semantic model feeds VBC program dashboard separate from CMS API metrics.

**Example:** `measure_diabetes_a1c` numerator/denominator tables refreshed weekly from Databricks export—VBC team dashboard distinct from Patient Access uptime report.

**How to Check:**
- Measure definitions documented with SAM source SQL
- No double-counting members across measures
- Refresh aligns after clinical SAM merge completes
- VBC and CMS dashboards use separate workspaces if needed

**How to Fix:**
- Reconcile numerator drift if SAM logic changed
- Fix export filter if wrong population denominator
- Coordinate refresh order: SAM → export → Fabric

---

### Q384. How do you test Fabric pipeline changes without affecting prod CMS reports?

**Answer:** Dev Fabric workspace with shortcut to `dev` ADLS export path; clone pipeline and semantic model; run integration test with masked sample data; promote via Git sync to prod workspace only after UAT sign-off on dashboard diff.

**Example:** Change eligibility SCD hash in dev → UAT compares row counts vs prod snapshot → sign-off → merge Git → prod sync.

**How to Check:**
- Dev/prod workspace isolation verified
- UAT checklist signed before prod Git sync
- Prod dashboard bookmark comparison attached to ticket
- Rollback Git tag documented pre-merge

**How to Fix:**
- Revert Git commit and re-sync prod workspace
- Fix dev test data if not representative
- Never test directly in prod workspace

---

### Q385. How do you handle PHI accidentally landed in Fabric Lakehouse?

**Answer:** Immediate: stop pipeline, revoke workspace access, delete files, scan all dependent semantic models, notify privacy officer within 1h. Root cause: export allowlist breach. Prevent: column validation on export job rejects PHI columns.

**Example:** Export job bug included `member_name` → detected by column scanner → purge Lakehouse table + shortcut cache + incident ticket HIPAA-2025-042.

**How to Check:**
- Automated PHI column name scanner on every export
- Fabric table schema audit weekly
- Incident response drill annually
- Purge confirmation log from storage admin

**How to Fix:**
- Fix export SQL SELECT list
- Re-export clean aggregate only
- Mandatory code review on export job changes

---

### Q386. How do you optimize Power Query M for large roster files in Dataflow Gen2?

**Answer:** Filter early in M (`Table.SelectRows` on date window), remove unused columns before joins, avoid nested merges on full history—use incremental staging table for delta files. Native query pushdown where source supports it.

**Example:** 50M row roster history → M filters `effective_date >= #date(2024,1,1)` first → processing 8M rows → refresh 12min vs 2h.

**How to Check:**
- Query folding indicator on source steps
- Refresh duration trend after optimization
- Output row count matches expected filtered set
- Memory errors absent in Dataflow logs

**How to Fix:**
- Move heavy logic to Databricks export pre-aggregated
- Split Dataflow into staging + transform two-step
- Increase Dataflow capacity if legitimately large

---

### Q387. How do you align Fabric refresh schedule with Databricks SAM merge completion?

**Answer:** Fabric pipeline triggered by Databricks job completion webhook (via Azure Function) rather than fixed clock—ensures export exists before Copy activity. Fallback schedule 2h after expected SAM window if webhook missed.

**Example:** SAM merge completes 05:42 → webhook triggers Fabric Copy 05:43 → metrics available 06:00 vs stale 6am fixed schedule when merge ran late.

**How to Check:**
- Webhook firing logged in Azure Function metrics
- Fabric start time correlates with SAM completion
- Fallback schedule catches missed webhooks
- End-to-end freshness SLA met 95% days

**How to Fix:**
- Fix webhook auth if delivery failures
- Increase fallback delay if SAM often late
- Manual trigger runbook for webhook outage

---

### Q388. How do you use Fabric capacity metrics to right-size interop analytics SKU?

**Answer:** Review 30-day CU utilization, throttling minutes, and refresh queue delays. Target 60–75% peak CU—if sustained > 85% or throttling > 30min/day, upgrade SKU; if < 40%, downgrade with performance validation.

**Example:** F32 throttled 45min/day during month-end → upgrade F64 → throttling zero → cost +$800/mo justified by SLA.

**How to Check:**
- Fabric Admin Portal capacity utilization report
- Throttling event count per week
- Dashboard refresh SLA compliance
- Cost per refresh run trend

**How to Fix:**
- Schedule stagger before SKU upgrade if budget constrained
- Downgrade only after 30-day low utilization confirmed
- Document SKU decision in platform runbook

---

### Q389. How do you implement cross-workspace dataset sharing for CMS vs VBC teams?

**Answer:** Publish certified semantic model from prod workspace; grant Build permission to VBC workspace for subset measures via perspective or separate thin semantic model referencing shared dataset—avoid copying tables.

**Example:** CMS dataset certified in `interop-prod`; VBC workspace thin model references it with only quality measure fields exposed.

**How to Check:**
- Certified badge on source dataset
- VBC users cannot access CMS-only fields via drill
- Single refresh propagates to all dependent reports
- Lineage shows shared dataset not duplicate import

**How to Fix:**
- Create perspective if field leak in thin model
- Revoke direct Lakehouse access from VBC users
- Fix broken binding if source dataset renamed

---

### Q390. Scenario: Power BI CMS dashboard shows 100% uptime but Onyx Insights shows breach. Reconcile?

**Answer:** Compare aggregation windows (UTC vs local), definition of "successful" call (2xx vs excluding 429), data freshness lag, and RLS slice filtering wrong payer subset. Usually Fabric export uses daily avg while Onyx flags hourly dip below 99%.

**Example:** Onyx hourly 98.5% at 3am not visible in daily avg 99.2% → add hourly grain table to Fabric export for compliance alignment.

**How to Check:**
- Side-by-side query same payer/date range both systems
- Timezone on metric_date column
- SLA definition doc matches measure formula DAX
- Hourly vs daily grain documented

**How to Fix:**
- Align measure formula with Onyx SLA definition
- Add hourly export table for regulatory reporting
- Fix RLS if dashboard scoped to wrong payer

---

## Section T: Google Cloud — Hybrid & Reference Patterns (Q391–415)

### Q391. When would you use BigQuery in a hybrid interop architecture?

**Answer:** BigQuery suits payer analytics subsidiaries already on GCP, CMS public data benchmarking, or cross-payer research sandboxes—NOT primary PHI SAM (that stays Databricks). I federate aggregated exports from Databricks to BigQuery via scheduled Parquet load for GCP-native ML/BI tools.

**Example:** Research team runs BigQuery ML on de-identified national CMS benchmark joined to our aggregated formulary stats—no member PHI in BQ.

**How to Check:**
- Architecture decision record documents BQ scope boundary
- No PHI tables in BQ dataset inventory scan
- Export job allowlist enforced
- BQ IAM no public access

**How to Fix:**
- Drop PHI table immediately if migration mistake
- Use authorized views for aggregated access only
- Align with hybrid networking (Private Google Access)

---

### Q392. How do you use BigQuery partitioning and clustering for claims analytics?

**Answer:** Partition fact table by `service_date` (DAY or MONTH); cluster by `payer_id`, `procedure_code`—reduces scan cost for payer-specific quality reports. Partition expiration on sandbox tables only—not prod aggregates.

**Example:** `claims_summary` partitioned MONTH, clustered `(payer_id, hcpcs_code)`—query one payer one month scans 1/36 of table vs full scan.

**How to Check:**
- `INFORMATION_SCHEMA.PARTITIONS` row count per partition
- Query bytes processed in job history
- Clustering fields match common filter columns
- No full table scan on partitioned query explain plan

**How to Fix:**
- Re-cluster if query filters changed to new dimensions
- Fix queries missing partition filter (require partition filter option)
- Archive old partitions to cold storage if cost issue

---

### Q393. How do you implement Dataflow streaming for FHIR webhook validation (GCP reference)?

**Answer:** Reference pattern for GCP-native partners: Pub/Sub → Dataflow pipeline validates JSON schema, writes valid to BigQuery staging, invalid to dead-letter topic. Watermark handles late events up to 24h. Production Rail B uses AWS Lambda—this is hybrid reference for acquirers on GCP.

**Example:** Dataflow `FhirWebhookValidate` with 5min allowed lateness—late NASCO replay events still slotted in correct window.

**How to Check:**
- Dataflow job metrics: system lag, watermark
- Dead-letter topic message count
- BigQuery insert row count matches valid events
- Autoscaling worker count during burst

**How to Fix:**
- Increase allowed lateness if partner replay pattern longer
- Fix schema transform DoFn on new field type
- Scale max workers if persistent lag

---

### Q394. How do you use Dataplex for PHI policy tags on GCP analytics sandboxes?

**Answer:** Dataplex lake `interop_research` with raw zone (restricted) and curated zone (aggregated). Policy tags `PHI`, `PII` on columns—BigQuery column-level security masks tagged fields. Discovery scans document lineage for audit.

**Example:** Accidental load of member_id tagged PII—BigQuery query as analyst returns masked hash only.

**How to Check:**
- Dataplex asset inventory shows tagged columns
- Test query as restricted vs privileged role
- Discovery scan schedule weekly
- No untagged sensitive columns in curated zone

**How to Fix:**
- Apply policy tag taxonomy to new columns
- Move misclassified table to raw zone
- Revoke privileged access over-provisioned accounts

---

### Q395. How do you configure Cloud Storage retention for interop audit archives?

**Answer:** Audit log and CMS certification evidence buckets use retention policy (1 year minimum, 7 year for legal hold subset), versioning enabled, uniform bucket-level access, no public ACL. Cross-region dual-region for RPO requirements on certification artifacts.

**Example:** `onyx-cms-cert-evidence` bucket 7-year retention lock—object delete blocked even by admin until retention expires.

**How to Check:**
- Bucket retention policy and lock status
- Versioning enabled on audit buckets
- Public access prevention enforced
- Lifecycle rule transitions to Archive class after 90 days

**How to Fix:**
- Enable retention before objects landed (can't shorten after lock)
- Restore deleted object from versioning if accidental delete within retention
- Fix IAM if service account couldn't write evidence

---

### Q396. How do you use BigQuery scheduled queries for CMS monthly rollup?

**Answer:** Scheduled query aggregates hourly API metrics export into monthly compliance table 1st of month 06:00 UTC—writes to `cms.monthly_patient_access_sla`. Notification on failure to Cloud Monitoring alert channel.

**Example:** Jan 2025 rollup: `AVG(uptime_pct)`, `COUNT(breach_hours)` grouped by payer_id → table row per payer for regulatory filing export.

**How to Check:**
- Scheduled query run history success
- Row count equals active payer count
- Manual reconcile one payer vs Onyx source
- Alert fired on synthetic failure test

**How to Fix:**
- Fix SQL if new payer_id not in dimension
- Increase slot reservation if query timeout
- Re-run manual backfill for missed month

---

### Q397. How do you use Pub/Sub topic retention for webhook replay scenarios?

**Answer:** Configure 7-day message retention on `fhir-webhook-events` topic—if downstream Dataflow down 48h, replay from seek timestamp without partner resend. Dead-letter subscription for poison messages with 31-day retention for investigation.

**Example:** Dataflow outage 36h → seek subscription to timestamp before outage → reprocess 36h events → no data loss.

**How to Check:**
- Topic retention duration in console
- Seek operation logged with timestamp
- Reprocessed message count matches expected backlog
- Dead-letter depth near zero steady state

**How to Fix:**
- Extend retention if outage window exceeded (max 31 days)
- Fix poison message schema before replay
- Increase subscription ack deadline if processing slow

---

### Q398. How do you compare Vertex AI RAG vs Databricks Vector Search for formulary Q&A?

**Answer:** Databricks Vector Search wins when data already in SAM Delta—same governance, Unity AI Gateway integration, no cross-cloud PHI movement. Vertex AI RAG suits GCP-only subsidiaries with formulary docs in GCS—use aggregated/de-identified content only. Primary platform: Databricks RAG per our architecture.

**Example:** Enterprise chooses Databricks RAG indexed from `formulary_sam` Delta; GCP division uses Vertex on PDF bucket with no member data—both feed separate regional portals.

**How to Check:**
- Architecture ADR documents primary vs secondary RAG
- No PHI in Vertex corpus scan
- Eval metrics comparable if running parallel POC
- Cost comparison includes egress if cross-cloud

**How to Fix:**
- Consolidate to Databricks if duplicate indexes diverge
- Sync formulary updates to both if dual POC temporary
- Migrate Vertex to Databricks before single support model

---

### Q399. How do you use Cloud Workflows to orchestrate GCP-side export ingestion?

**Answer:** Workflow steps: check GCS landing file exists → trigger Dataproc/BQ load job → poll completion → call HTTP webhook to Databricks "ready for pick-up" if hybrid. Retry with backoff on transient failures; raise alert step on terminal failure.

**Example:** Partner drops file to GCS → Workflow loads BQ staging → POST Databricks external task trigger → Rail C pick-up starts.

**How to Check:**
- Workflow execution history success rate
- Retry count within limits on transient errors
- Databricks task triggered within 5min of load complete
- Alert email on terminal failure received

**How to Fix:**
- Fix GCS path condition if file naming changed
- Increase timeout on long BQ load step
- Manual workflow re-run from failed step

---

### Q400. How do you implement BigQuery row access policies for multi-payer sandbox?

**Answer:** `CREATE ROW ACCESS POLICY payer_filter ON claims_summary GRANT TO ('group:payer_a_analysts') FILTER USING (payer_id = 'A')`—each payer group sees own slice in shared table without table duplication.

**Example:** Payer B analyst `SELECT COUNT(*)` returns only Payer B rows—attempt join to expose Payer A blocked by policy.

**How to Check:**
- Test query impersonating each group
- Policy list in `INFORMATION_SCHEMA.ROW_ACCESS_POLICIES`
- No service account bypass unless documented break-glass
- Quarterly access review

**How to Fix:**
- Add policy for new payer before granting group access
- Fix OR filter mistake that widened access
- Revoke break-glass SA routine use

---

### Q401. How do you use BigQuery snapshots for pre-migration rollback?

**Answer:** Before major transform SQL change on `formulary_summary`, `CREATE SNAPSHOT TABLE formulary_summary_backup FOR SYSTEM_TIME AS OF CURRENT_TIMESTAMP()`—rollback by copying snapshot back if bad deploy.

**Example:** Bad SQL doubled row counts → restored from snapshot taken 10min pre-deploy → counts normalized.

**How to Check:**
- Snapshot table exists with expected row count
- Snapshot storage cost acceptable (7-day delete policy)
- Rollback drill in sandbox quarterly
- Change ticket references snapshot name

**How to Fix:**
- Restore: `CREATE OR REPLACE TABLE ... AS SELECT * FROM snapshot`
- Delete old snapshots per lifecycle policy
- Always snapshot before scheduled query deploy

---

### Q402. How do you configure Private Google Access for Dataflow PHI-adjacent pipelines?

**Answer:** Subnet enables Private Google Access—workers reach Google APIs without public IP. PHI never in BQ in our arch; if adjacent metadata pipelines, use VPC-SC perimeter around project. No 0.0.0.0/0 egress except approved NAT for partner allowlist.

**Example:** Dataflow workers in `us-central1` subnet PGA enabled—BigQuery and GCS access via private paths only.

**How to Check:**
- Subnet PGA setting true
- Worker has no external IP
- VPC-SC audit if perimeter enabled
- Egress firewall logs show no unexpected destinations

**How to Fix:**
- Enable PGA on subnet if API reachability failures
- Add VPC-SC ingress/egress rule for new service
- Remove public IP from worker template

---

### Q403. How do you use Bigtable for low-latency member session cache (SMART launch)?

**Answer:** Reference pattern: cache SMART launch context and short-lived member portal preferences keyed by `session_id`—sub-10ms read for SLAP adjacent services in multi-cloud DR scenario. Not primary auth store (DynamoDB in AWS prod).

**Example:** GCP DR site: Bigtable `smart_sessions` row `session_id` → launch context JSON TTL 15min—mirrors DynamoDB global table pattern.

**How to Check:**
- Read latency P99 < 20ms
- TTL garbage collection running
- Row count correlates with active sessions
- Failover drill reads correct context

**How to Fix:**
- Increase nodes if latency spike
- Fix column family GC if TTL not expiring
- Sync schema with DynamoDB for DR parity

---

### Q404. How do you use Analytics Hub for sharing de-identified quality benchmarks?

**Answer:** Publish `hedis_benchmark_aggregates` listing in Analytics Hub—subscriber payers receive read-only access to benchmark tables without copying data. Contract specifies no re-identification; IAM at listing level.

**Example:** Regional payer subscribes to benchmark listing—queries in their project—provider cannot see other subscribers' usage data.

**How to Check:**
- Listing documentation states de-identified only
- Subscriber count matches contracts
- No row-level member data in shared tables
- Revocation removes access within 24h

**How to Fix:**
- Unpublish listing if data quality issue found
- Update listing version with changelog
- Legal review before adding new columns

---

### Q405. How do you run inference in Dataflow with RunInference for document classification?

**Answer:** Reference for prior auth document routing: Dataflow `RunInference` with Vertex AI endpoint classifies uploaded PA PDF type (clinical note vs lab result)—routes to correct OCR pipeline. AWS prod uses different path; GCP pattern for hybrid docs.

**Example:** PA fax PDF → RunInference `doc_classifier` → label `lab_result` → route to lab extraction DoFn.

**How to Check:**
- Inference latency in Dataflow step metrics
- Classification accuracy sample audit 100 docs
- Misroute rate < 2%
- Endpoint scaling handles batch peak

**How to Fix:**
- Retrain classifier if new document template introduced
- Increase endpoint min replicas if cold start latency
- Fallback to manual queue if inference unavailable

---

### Q406. How do you use cross-region BigQuery copy for DR compliance reporting?

**Answer:** Scheduled cross-region copy job `us-east1` → `us-central1` for `cms.monthly_*` tables—RPO 24h for regulatory reporting continuity if primary region impaired. Copy not used for live queries—failover runbook promotes secondary.

**Example:** us-east1 regional outage → runbook query cms tables in us-central1 copy → monthly filing on time.

**How to Check:**
- Copy job success daily
- Row count primary vs secondary match
- Failover drill query secondary quarterly
- Copy cost in DR budget

**How to Fix:**
- Re-run copy job for missed day
- Fix IAM if copy service account lost access
- Update runbook if table list changed

---

### Q407. How do you design denormalized BigQuery schema for API call fact analytics?

**Answer:** Denormalize payer name, api_family label, http_status_category into fact table at load time—avoid star join on every dashboard query. Accept storage cost for scan speed on CMS compliance dashboards querying billions of API log rows.

**Example:** Fact row includes `payer_name`, `api_family=Patient Access`, `status_category=2xx`—dashboard query no joins, 3s on 2B rows.

**How to Check:**
- Query explain shows single table scan
- Storage cost vs query cost tradeoff documented
- Denormalized fields match dimension source on spot check
- Refresh job maintains consistency on payer rename

**How to Fix:**
- Rebuild fact if dimension drift caused wrong labels
- Partition prune if query still scans too much
- Materialized view alternative if storage excessive

---

### Q408. Scenario: Dataflow lag on GCP webhook pipeline exceeds SLA. Actions?

**Answer:** Check Dataflow system lag, worker count, hot keys in groupByKey, downstream BQ insert rate limits. Scale workers, increase max insert parallelism, fix skew with combiner pre-aggregate, temporarily raise BQ quota if insert bottleneck.

**Example:** Lag 45min → workers 5→20, fix skew on `payer_id` key salting → lag clears 20min.

**How to Check:**
- Dataflow monitoring: System lag, Watermark age
- Worker CPU and shuffle bytes
- BQ streaming insert errors in logs
- End-to-end event timestamp vs processing time delta

**How to Fix:**
- Increase maxNumWorkers cap in pipeline options
- Switch to load job instead of streaming inserts if batch acceptable
- Fix infinite loop or poison record blocking watermark

---

### Q409. How do you use external tables in BigQuery over S3 export (Omni/hybrid)?

**Answer:** BigQuery Omni external table over S3 Parquet export path—query federated without loading if hybrid analytics team needs SQL on Databricks export in place. Watch egress costs and latency; prefer scheduled load for heavy queries.

**Example:** External table `s3://exports/metrics/*.parquet`—ad-hoc analyst query 500GB scanned—decide load vs external per query pattern.

**How to Check:**
- External table definition points to current path
- Query bytes billed includes egress if cross-cloud
- Schema auto-detect matches Parquet evolution
- Performance acceptable for ad-hoc vs prod dashboard

**How to Fix:**
- Scheduled load to native BQ table if external too slow
- Fix S3 credentials/IAM for BQ connection
- Update path glob if export filename pattern changed

---

### Q410. How do you implement Cloud Monitoring alerts for interop GCP components?

**Answer:** Alert policies: Dataflow system lag > 15min, Pub/Sub oldest unacked age > 1h, BQ scheduled query failure, GCS landing bucket zero objects 4h. Notification channels: PagerDuty + email integration team—not same channel as AWS Onyx alerts unless unified ops.

**Example:** Pub/Sub unacked age alert fires → runbook links to seek/replay procedure → PagerDuty incident INC-4421.

**How to Check:**
- Alert policy test notification succeeds
- Runbook URL in alert annotation
- False positive rate < 1/week
- Coverage map: all GCP interop components listed

**How to Fix:**
- Tune threshold if chronic false positives
- Add missing alert for new pipeline component
- Fix notification channel auth expiry

---

### Q411. How do you use Dataplex data quality rules on curated CMS tables?

**Answer:** Dataplex rule: `uptime_pct BETWEEN 0 AND 100`, `NOT NULL payer_id`, row count anomaly vs 7-day median. Failures create incident in Dataplex quality dashboard → webhook to Teams.

**Example:** Bad load sets uptime_pct = 150 → quality rule fails → pipeline blocked from promoting to curated zone.

**How to Check:**
- Quality scan results in Dataplex UI
- Block promotion on critical rule failure enabled
- Historical false positive rate
- Sample failed row inspection procedure

**How to Fix:**
- Fix upstream SQL producing invalid values
- Adjust anomaly threshold if legitimate volume spike
- Quarantine bad batch before curated promotion

---

### Q412. How do you manage GCP IAM for hybrid interop service accounts?

**Answer:** One SA per pipeline function least privilege: `bq-load-sa` only `bigquery.dataEditor` on target dataset, `gcs-landing-sa` only objectCreator on landing prefix. No domain-wide SA keys—Workload Identity Federation from AWS if cross-cloud trigger. Key rotation 90 days if keys unavoidable.

**Example:** Dataflow SA cannot delete GCS audit bucket—only read landing write BQ.

**How to Check:**
- IAM policy analyzer over-privilege findings zero critical
- No SA user-managed keys on prod SAs
- SA last used audit—disable unused
- Cross-cloud federation test succeeds

**How to Fix:**
- Remove excess roles from SA
- Migrate key-based auth to WIF
- Disable compromised SA immediately; rotate downstream secrets

---

### Q413. How do you use BigQuery BI Engine for sub-second CMS dashboard?

**Answer:** BI Engine reservation 10GB on `cms` dataset—Power BI via BigQuery connector or Looker caches hot aggregates in memory. Valid when dashboard queries same monthly rollup tables repeatedly; not for ad-hoc full scan.

**Example:** BI Engine hit rate 85%—executive dashboard load 800ms vs 4s without reservation.

**How to Check:**
- BI Engine metrics: cache hit rate, evictions
- Dashboard load time trend
- Reservation size vs working set
- Cost vs latency benefit documented

**How to Fix:**
- Increase reservation if evictions high
- Pre-aggregate further if working set exceeds reservation
- Disable BI Engine on ad-hoc sandbox datasets

---

### Q414. How do you handle schema evolution in BigQuery load from FHIR export?

**Answer:** Use autodetect add new fields for Parquet load; nested RECORD for FHIR extensions; breaking changes versioned as new table `fhir_observation_v2` with view union during migration. Match Databricks Silver schema evolution policy.

**Example:** New `component` field in Observation export → BQ autodetect adds nullable column—downstream view handles NULL for legacy rows.

**How to Check:**
- New column appears after export schema change
- View `fhir_observation_all` row count unchanged
- Query jobs not failing on SELECT *
- Schema change logged in MDP registry

**How to Fix:**
- Explicit schema update if autodetect wrong type
- Backfill new column from re-export if needed
- Deprecate old table after migration window

---

### Q415. Scenario: Leadership wants full GCP migration from AWS interop stack. Your recommendation?

**Answer:** I recommend against full migration before Jan 2027 CMS deadline—Firely/SLAP/FITE AWS stack is certified path; GCP patterns useful for analytics subsidiaries only. Phased: keep runtime on AWS, federate aggregates to GCP if business requires—full migration post-certification with 18-month plan and dual-run period.

**Example:** Acquired payer on GCP gets BQ analytics on exports; Patient Access API stays AWS Firely—same member experience.

**How to Check:**
- Cost estimate AWS cert path vs full GCP rewrite
- CMS deadline risk assessment documented
- Executive sign-off if override migration timing
- Hybrid architecture ADR updated

**How to Fix:**
- Propose hybrid not rip-and-replace in roadmap
- Identify GCP-native components that add value without runtime move
- Set decision gate post-Jan 2027 certification

---

## Section U: SQL Server / Azure SQL / AI Developer — Healthcare Data (Q416–445)

### Q416. When do you use clustered columnstore vs rowstore for claims warehouse tables?

**Answer:** Clustered columnstore on large fact tables (`claim_line`, `eob_line`) for analytics scans—10x compression and batch mode. Rowstore clustered index on small dimensions (`procedure_code`, `payer`) and OLTP-adjacent staging tables needing singleton lookups and frequent updates.

**Example:** 400M row `claim_line` columnstore—monthly aggregate query 12min rowstore → 90sec columnstore. `payer_dim` 50 rows rowstore for FK lookups.

**How to Check:**
- `sys.column_store_row_groups` health—no delta store bloat > 10%
- Query uses batch mode in actual plan
- Dimension table seek performance < 5ms
- Rebuild columnstore if > 1M deleted rows in row groups

**How to Fix:**
- `ALTER INDEX ... REORGANIZE` on fragmented columnstore
- Move hot singleton-update table from columnstore to rowstore
- Add nonclustered rowstore index on columnstore if needed for point queries

---

### Q417. How do you implement Row-Level Security (RLS) for multi-payer SQL warehouse?

**Answer:** `CREATE SECURITY POLICY payer_isolation ADD FILTER PREDICATE dbo.fn_payerFilter(payer_id) ON dbo.claims_summary`—function returns `payer_id = CAST(SESSION_CONTEXT(N'payer_id') AS varchar)` set at connection from SLAP/API context. Block predicate optional for INSERT/UPDATE denial.

**Example:** Payer A service login sets `SESSION_CONTEXT` → `SELECT * FROM claims_summary` returns 2M rows not 50M.

**How to Check:**
- Test with each payer login—cross-payer count zero
- `sys.security_policies` enabled on correct tables
- Block predicate on write tables if required
- Application sets SESSION_CONTEXT on every connection pool checkout

**How to Fix:**
- Fix missing SESSION_CONTEXT set in app middleware
- Add FILTER to newly created tables—RLS doesn't auto-apply
- Audit bypass: only `dbo_admin` bypass role with logging

---

### Q418. How do you apply Dynamic Data Masking on member PHI in Azure SQL?

**Answer:** `ALTER TABLE members ALTER COLUMN ssn ADD MASKED WITH (FUNCTION = 'partial(0,"XXX-XX-",4)')`—analysts see masked; `UNMASK` permission only for break-glass compliance role with justification audit.

**Example:** Analyst `SELECT ssn FROM members` → `XXX-XX-6789`; compliance unmask logged in audit.

**How to Check:**
- Test masked output per role
- `sys.masked_columns` lists all PHI fields
- Unmask audit events reviewed monthly
- Power BI via SQL respects masking on DirectQuery

**How to Fix:**
- Add mask to new PHI column before granting SELECT
- Revoke UNMASK from over-provisioned users
- Fix app using elevated connection for routine queries

---

### Q419. How do you use VECTOR_DISTANCE for formulary therapeutic alternative search?

**Answer:** Store NDC description embeddings in `formulary_drug.embedding` vector column; query `ORDER BY VECTOR_DISTANCE('cosine', @query_embedding, embedding)` for semantic similar drugs when exact generic match unavailable—supports Provider Agent SQL MCP tool.

**Example:** Search "GLP-1 weight loss injectable" → top 5 NDCs by cosine distance despite brand name mismatch in query text.

**How to Check:**
- Vector index exists on embedding column
- Query latency P95 < 200ms on 100K NDC corpus
- Clinical pharmacist validates top results clinically appropriate
- Embedding model version pinned in table metadata

**How to Fix:**
- Rebuild vector index after bulk formulary reload
- Re-embed if embedding model upgraded
- Fallback to LIKE search if vector index offline

---

### Q420. How do you implement MERGE for idempotent claim line upserts from Rail A CSV?

**Answer:** Staging load CSV → `MERGE claim_line AS t USING staging AS s ON t.claim_id = s.claim_id AND t.line_number = s.line_number WHEN MATCHED AND CHECKSUM(t.*) <> CHECKSUM(s.*) THEN UPDATE ... WHEN NOT MATCHED THEN INSERT`. Transaction wrapped in TRY/CATCH with THROW on failure.

**Example:** Daily CSV 2M lines—MERGE updates 400K changed, inserts 1.6M new—rerun same file idempotent zero net change.

**How to Check:**
- MERGE output `$action` counts logged
- Rerun same file produces zero inserts/updates
- Transaction rollback test on mid-merge failure
- Duplicate key error absent on idempotent rerun

**How to Fix:**
- Fix merge keys if duplicate claim lines appearing
- Split large MERGE batch if log growth excessive
- Add HOLDLOCK hint if concurrent merge race

---

### Q421. How do you use Change Tracking for incremental sync to downstream FHIR staging?

**Answer:** Enable `ALTER TABLE claim_line ENABLE CHANGE_TRACKING`—downstream job reads `CHANGETABLE(CHANGES claim_line, @last_sync_version)` for inserts/updates/deletes since last watermark. Lighter than CDC when delete tracking sufficient without before-image.

**Example:** Incremental sync pulls 50K changes vs full 400M table scan—sync completes 8min vs 2h.

**How to Check:**
- `CHANGE_TRACKING_CURRENT_VERSION()` advances after DML
- Sync job stores `@last_sync_version` correctly
- Delete changes captured if required
- Retention period exceeds max sync outage window

**How to Fix:**
- Increase change tracking retention if sync was down too long—must full refresh
- Fix watermark reset if duplicate sync
- Enable CDC instead if before-image needed for audit

---

### Q422. How do you implement temporal tables for member eligibility history?

**Answer:** `ALTER TABLE eligibility ADD PERIOD FOR SYSTEM_TIME (ValidFrom, ValidTo)` + `SET (SYSTEM_VERSIONING = ON)`—automatic history table `eligibility_history`. Point-in-time query: `FOR SYSTEM_TIME AS OF @service_date` for claim adjudication retro checks.

**Example:** Claim service_date 2024-06-15 queries eligibility as of that date—returns PPO plan even though member now HMO.

**How to Check:**
- History table row count grows on updates
- AS OF query returns expected plan for test member
- Storage growth monitored on history table
- Retention policy on history if compliance allows purge

**How to Fix:**
- Disable versioning temporarily for bulk load then re-enable carefully
- Archive old history to cold storage if size excessive
- Fix application updating without respecting temporal semantics

---

### Q423. How do you use Query Store to fix regressed CMS reporting query?

**Answer:** Identify regressed query in Query Store by duration increase post-stats update—`sp_query_store_force_plan` to pin last known good plan while investigating root cause (parameter sniffing, stats skew).

**Example:** Monthly CMS rollup query 30s → 8min after stats auto-update—force plan_id 4421 → back to 35s while applying recompile fix.

**How to Check:**
- Query Store captures regressed query_id
- Forced plan duration restored
- Root cause documented (stats, CE change, index drop)
- Force plan removed after permanent fix deployed

**How to Fix:**
- Update statistics with full scan on skewed payer_id
- Add recompile hint or OPTIMIZE FOR UNKNOWN
- Restore dropped index if regression caused by DDL

---

### Q424. How do you implement inline TVF for reusable member coverage check?

**Answer:** `CREATE FUNCTION dbo.fn_member_coverage(@member_id varchar, @service_date date) RETURNS TABLE AS RETURN (...)`—joins eligibility temporal AS OF service_date with plan benefits. Inline TVF optimizes better than multi-statement TVF for FHIR Extract SQL path.

**Example:** Extract SQL `CROSS APPLY dbo.fn_member_coverage(m.member_id, c.service_date)`—plan tier available per claim line in one pass.

**How to Check:**
- Actual plan shows TVF inlined not loop nested
- Result matches manual eligibility lookup test cases
- NULL returned appropriately for uncovered dates
- Performance acceptable on Extract batch size

**How to Fix:**
- Convert MSTVF to inline if nested loop storm
- Add index on eligibility (member_id, effective_date)
- Fix AS OF date parameter wrong timezone

---

### Q425. How do you use Read Committed Snapshot isolation for concurrent claim loading?

**Answer:** Enable RCSI on database `ALTER DATABASE interop_dw SET READ_COMMITTED_SNAPSHOT ON`—readers don't block MERGE writers during nightly load; writers don't block CMS reporting queries. Accept tempdb version store overhead.

**Example:** MERGE claim_line during business hours reporting—reports see consistent snapshot without blocking locks.

**How to Check:**
- `is_read_committed_snapshot_on = 1`
- Version store size in DMVs during peak load
- No excessive blocking in `sys.dm_tran_locks` during MERGE
- Tempdb autogrowth events acceptable

**How to Fix:**
- Increase tempdb files if version store contention
- Schedule heavy MERGE off-peak if version store spikes
- Fix long-running open transactions holding versions

---

### Q426. How do you use Managed Identity for Azure SQL access from Databricks/Fabric?

**Answer:** `CREATE USER [databricks-export-sp] FROM EXTERNAL PROVIDER` in Azure SQL—grant SELECT on export views only. Connection string uses Active Directory Managed Identity—no SQL password in Databricks secret scope.

**Example:** Databricks JDBC to Azure SQL with MSI auth reads `v_claims_export` view—password rotation eliminated.

**How to Check:**
- Login exists as EXTERNAL PROVIDER type
- Connection succeeds from Databricks cluster with MSI
- Failed auth if wrong client ID in cluster config
- Permissions minimal on views not base tables

**How to Fix:**
- Add MSI user and grants if login failed
- Fix Azure AD admin misconfiguration on SQL server
- Use view if direct table access too broad

---

### Q427. How do you implement PARTITION FUNCTION for large claim history by service_year?

**Answer:** `CREATE PARTITION FUNCTION pf_service_year (date) AS RANGE RIGHT FOR VALUES ('2023-01-01','2024-01-01','2025-01-01')` + partition scheme on filegroups—switch out old year partition to archive filegroup for fast archival without DELETE scan.

**Example:** Switch partition 2022 to `FG_ARCHIVE` filegroup—seconds vs hours DELETE 80M rows.

**How to Check:**
- `$PARTITION.pf_service_year(service_date)` returns expected partition
- Partition elimination in query plan on date filter
- Switch operation logged in change ticket
- Archive filegroup backup policy separate

**How to Fix:**
- Merge split partitions if boundary wrong
- Rebalance filegroups if IO skew
- ALIGN indexes before SWITCH to avoid failure

---

### Q428. How do you use JSON_VALUE to parse FHIR extension fields in SQL staging?

**Answer:** Load raw FHIR JSON to staging column `resource_json nvarchar(max)`—extract with `JSON_VALUE(resource_json, '$.extension[0].valueCode')` for known extension URLs. For complex arrays use OPENJSON—validate in Silver before production MERGE.

**Example:** Extract US Core race extension: `JSON_VALUE(resource_json, '$.extension[?(@.url=="http://hl7.org/fhir/us/core/StructureDefinition/us-core-race")].extension[0].valueCoding.code')`—simplified path in prod with indexed computed column.

**How to Check:**
- Sample 100 resources JSON path matches expected value
- NULL rate documented for optional extensions
- Computed column persisted if used in joins
- Invalid JSON caught in TRY/CATCH load step

**How to Fix:**
- Fix JSON path if US Core profile URL changed
- Use OPENJSON for multi-value extensions
- Quarantine rows where JSON_VALUE returns unexpected type

---

### Q429. How do you use SqlPackage.exe DriftReport for interop warehouse schema governance?

**Answer:** CI runs `SqlPackage /Action:DriftReport` comparing deployed Azure SQL to DACPAC from Git—flags unauthorized prod DDL before CMS reporting breaks. Block deploy if drift detected unless approved hotfix ticket.

**Example:** DBA manual column add on `claims_summary` → drift report shows difference → blocked release until DACPAC updated in Git.

**How to Check:**
- DriftReport in CI pipeline artifact
- Zero unapproved drift on prod weekly scan
- DACPAC version tag matches deployed database
- Hotfix process documented for emergency DDL

**How to Fix:**
- Publish updated DACPAC from corrected Git schema
- Revert unauthorized prod change if not approved
- Sync dev/test from DACPAC not vice versa for governance

---

### Q430. How do you implement MCP SQL tool for Payer Ops Agent safely?

**Answer:** MCP SQL server exposes read-only connection to pre-approved views (`v_ingest_status`, `v_pipeline_sla`)—query whitelist regex blocks INSERT/UPDATE/multi-statement. Unity AI Gateway routes agent to MCP with row limit 1000 and 30s timeout.

**Example:** Agent query "Bronze lag by source" → MCP executes parameterized view select → returns JSON—attempt `DROP TABLE` rejected by whitelist.

**How to Check:**
- Pen-test MCP with injection and DDL attempts—all blocked
- Audit log every query with agent_id
- Result row count capped
- Connection uses read-only DB user

**How to Fix:**
- Tighten whitelist if agent constructed broad SELECT *
- Add view if legitimate question blocked
- Rotate read-only credential on schedule

---

### Q431. How do you use persisted computed columns for claim line allowed amount?

**Answer:** `allowed_amount AS (billed_amount - adjustment_amount) PERSISTED`—indexed for reporting filters; avoids runtime compute on 400M rows. Update base columns triggers recompute automatically.

**Example:** Index on persisted `allowed_amount`—filter `allowed_amount > 10000` seeks index vs full scan compute.

**How to Check:**
- `is_persisted = 1` in sys.computed_columns
- Index includes persisted column used in CMS cost reports
- Values match manual calculation spot check
- MERGE updates base columns recomputes correctly

**How to Fix:**
- Drop and recreate if formula changed—requires table rebuild
- Non-persisted if formula non-deterministic (not allowed persisted)
- Fix adjustment_amount sign convention if negative allowed amounts wrong

---

### Q432. How do you handle T-SQL error handling in claim load stored procedure?

**Answer:** `BEGIN TRY BEGIN TRAN ... MERGE ... COMMIT END TRY BEGIN CATCH IF @@TRANCOUNT > 0 ROLLBACK; THROW; END CATCH`—log error to `load_error_log` with batch_id before THROW to caller pipeline.

**Example:** MERGE fails FK constraint row 1.8M → full rollback → error_log row with batch_id → pipeline marks failed not partial corrupt state.

**How to Check:**
- Partial batch never committed on failure test
- error_log populated with ERROR_MESSAGE()
- Caller receives failure exit code
- Successful batch commits atomically

**How to Fix:**
- Fix staging data FK violations before rerun
- Increase log detail if insufficient for debug
- Deadlock retry wrapper if concurrent load conflicts

---

### Q433. How do you implement nonclustered columnstore index for real-time analytics on rowstore OLTP?

**Answer:** Rowstore clustered index on `pa_request` for OLTP inserts; nonclustered columnstore (`CREATE NONCLUSTERED COLUMNSTORE INDEX`) for analytics on status/dashboard queries—hybrid when need both fast singleton INSERT and aggregate scan.

**Example:** ePA requests inserted rowstore—dashboard `COUNT(*) BY status BY payer` uses columnstore index batch mode.

**How to Check:**
- Both indexes maintained on INSERT workload acceptable
- Analytics query uses columnstore index in plan
- OLTP insert latency within SLA
- Reorganize columnstore if fragmentated

**How to Fix:**
- Drop columnstore if OLTP insert regression unacceptable
- Filtered columnstore index if analytics on subset status only
- Schedule index maintenance off-peak

---

### Q434. How do you use IF NOT EXISTS pattern for idempotent reference data load?

**Answer:** `IF NOT EXISTS (SELECT 1 FROM procedure_code WHERE code = @code) INSERT ...` or MERGE for bulk—reference data scripts rerunnable in deploy pipeline without duplicate key failures on procedure codes, NUCC taxonomy, place of service.

**Example:** Deploy script adds 2025 new HCPCS codes—rerun deploy skips existing, inserts 47 new—zero errors.

**How to Check:**
- Deploy pipeline rerunnable green second time
- Reference row count matches source file
- No duplicate natural keys
- Updated codes handled via MERGE not INSERT only

**How to Fix:**
- Switch INSERT-only to MERGE for updatable reference
- Add unique constraint to catch duplicates early
- Version reference file in Git with effective date

---

### Q435. How do you tune nonclustered index for SLAP token lookup by member_id?

**Answer:** Narrow nonclustered index `CREATE INDEX ix_token_member ON api_token(member_id) INCLUDE (expiry_utc, scope)`—covers token validation query without key lookup to clustered index. Filtered index `WHERE revoked = 0` if soft-delete pattern.

**Example:** Patient Access API token validate by member_id—seek ix_token_member 2 logical reads vs 150 table scan.

**How to Check:**
- Actual plan shows Index Seek + Key Lookup absent (covering)
- Index usage stats user_seeks increasing
- Index size reasonable vs table
- Duplicate indexes absent on same key

**How to Fix:**
- Add INCLUDE columns if Key Lookup appeared
- Drop unused duplicate index increasing write overhead
- Rebuild if fragmentation > 30%

---

### Q436. Scenario: Azure SQL CMS report query timeout during month-end. Fix path?

**Answer:** Check Query Store for regressed plan, blocking chains, missing partition elimination, stats out of date on `service_date`. Quick fix: force good plan or add recompile; medium: update stats full scan; long-term: partition align, pre-aggregate monthly table, Read Scale-out replica for reporting.

**Example:** Timeout on 12min query—stats update + partition filter hint → 4min; pre-aggregate table next sprint.

**How to Check:**
- `sys.dm_exec_requests` during timeout—blocking vs CPU
- Query plan shows partition elimination
- Stats last_updated on filtered columns
- Replica lag if using read scale-out

**How to Fix:**
- Emergency: force plan or schedule report off MERGE window
- Update stats on payer_id, service_date
- Create/monthly aggregate indexed view

---

### Q437. How do you secure connection strings in Azure SQL linked to interop pipelines?

**Answer:** Use Key Vault references in ADF/Fabric/Databricks—not plaintext in repo. Managed Identity preferred over SQL auth. Rotate SQL auth password 90 days if legacy; audit `sys.dm_exec_connections` for unexpected client apps.

**Example:** ADF linked service `AzureKeyVaultSecured`—secret name `sql-interop-ro-password`—rotation auto-updates linked service on next pipeline run.

**How to Check:**
- No connection string in Git history (secret scan)
- Key Vault access policy least privilege
- MSI auth working for new pipelines
- Connection audit shows expected app names only

**How to Fix:**
- Rotate compromised password immediately
- Migrate plaintext linked service to Key Vault
- Revoke SQL login if unexpected client detected

---

### Q438. How do you implement vector index maintenance after formulary bulk update?

**Answer:** After MERGE 50K NDC rows, rebuild vector index `ALTER INDEX ix_formulary_embedding ON formulary_drug REBUILD`—or use incremental vector index if platform supports. Re-embed changed descriptions before index rebuild.

**Example:** Formulary update Tuesday 2am—embed job → index rebuild 15min—Provider Agent semantic search accurate by 3am SLA.

**How to Check:**
- Index rebuild completes before agent SLA
- VECTOR_DISTANCE query returns new NDC in top results
- Index fragmentation zero post-rebuild
- Embed version matches index build timestamp

**How to Fix:**
- Schedule embed+rebuild in maintenance window
- Fallback keyword search during rebuild window
- Fix embed job skipping NULL description rows

---

### Q439. How do you use BEGIN TRY/CATCH with THROW for API-facing SQL procedures?

**Answer:** CATCH block maps SQL errors to sanitized error codes for API layer—`THROW 51000, 'Invalid member_id', 1` not raw constraint message exposing schema. Log full detail server-side only.

**Example:** Invalid member lookup → THROW 51001 'Member not found'—API returns 404—not `FK_claim_member violated`.

**How to Check:**
- API never returns raw SQL error text
- Error log table has full detail for support
- Error codes documented in API spec
- Pen-test SQL injection returns generic error

**How to Fix:**
- Wrap procedures with standardized error handler
- Map constraint violations to business error codes
- Remove PRINT/debug in prod procedures

---

### Q440. How do you compare on-prem SQL Server vs Azure SQL for interop warehouse?

**Answer:** Azure SQL for cloud-native integration (MSI, Fabric, geo-redundant backup, elastic scale)—preferred for new interop analytics warehouse. On-prem only if payer contract mandates data residency in specific non-Azure DC—then linked server/export pattern to cloud SAM still required for Databricks FHIR path.

**Example:** Azure SQL `interop_dw` geo-redundant backup PITR 35 days—Fabric DirectQuery native. On-prem legacy RCM DB stays until migration—exports only to SAM.

**How to Check:**
- ADR documents platform choice criteria
- Azure SQL backup PITR tested restore quarterly
- On-prem exit strategy dated if temporary
- Latency acceptable Fabric ↔ Azure SQL same region

**How to Fix:**
- Migrate on-prem export to Azure SQL Managed Instance if hybrid needed
- Enable geo-replication if RTO requires cross-region
- Right-size vCore based on Query Store workload

---

### Q441. How do you implement hash-based Type 2 SCD comparison in T-SQL?

**Answer:** `HASHBYTES('SHA2_256', CONCAT(member_id, plan_id, effective_date, tier))` as `row_hash` in staging—compare to current dimension hash; mismatch closes old row inserts new. Faster than column-by-column compare on wide eligibility rows.

**Example:** Tier change only—hash differs—SCD closes prior row, opens new—hash same on rerun—no spurious SCD rows.

**How to Check:**
- Hash deterministic on same input (CONCAT null handling)
- SCD row count matches expected change volume
- No duplicate current rows per member
- Hash algorithm documented if column list changes

**How to Fix:**
- Include missing column in hash if changes not detected
- Fix NULL concat replacing with sentinels consistently
- Rebuild dimension if hash algorithm upgraded

---

### Q442. How do you use Azure SQL Database Ledger for tamper-evident audit tables?

**Answer:** Enable ledger on `cms_audit_submission` table—cryptographic hash chain detects unauthorized DBA tampering of compliance submission records. Upstream append-only; corrections via compensating insert not UPDATE.

**Example:** Auditor verifies ledger digest on submission table—proves records unaltered since insert for CMS inquiry.

**How to Check:**
- `sys.database_ledger_tables` includes audit tables
- Ledger verification script runs clean
- Application uses INSERT not UPDATE on ledger tables
- Digest verification documented in compliance runbook

**How to Fix:**
- Migrate UPDATE pattern to append-only before enabling ledger
- Restore from backup if verification fails—investigate tamper incident
- Disable ledger only with legal/compliance approval

---

### Q443. How do you expose aggregated SQL data to AI agents without VECTOR or raw PHI?

**Answer:** Pre-build aggregation views (`v_daily_ingest_health`, `v_api_error_rates`)—MCP SQL tool queries views only; no ad-hoc JOIN to member tables. Semantic layer documents column meanings for agent prompt grounding.

**Example:** Payer Ops Agent asks error rate → MCP queries `v_api_error_rates`—cannot SELECT from `members`—view not exposed in MCP whitelist.

**How to Check:**
- MCP whitelist includes views not base PHI tables
- View definitions aggregate above member grain
- Agent eval questions answerable from views alone
- Pen-test cross-view inference attack negligible

**How to Fix:**
- Add view for common agent question pattern
- Remove overly wide view from whitelist
- Add `GROUP BY` enforcement in MCP query parser

---

### Q444. How do you implement incremental export from Azure SQL to Databricks SAM?

**Answer:** Change Tracking or `modified_utc` watermark column—Databricks JDBC read with `WHERE modified_utc > @watermark` batch 500K rows—merge to SAM staging Delta. Watermark stored in Databricks control table not SQL side.

**Example:** Nightly export 80K changed claim lines via Change Tracking version 8844221 → Databricks MERGE to `claims_sam_staging`.

**How to Check:**
- Watermark advances each successful run
- Row count matches CHANGETABLE count
- Missed changes test: update row, verify next export includes
- Full refresh fallback if watermark reset

**How to Fix:**
- Increase JDBC partition parallelism if export slow
- Full refresh if change tracking retention exceeded outage
- Fix clock skew on modified_utc if duplicates/misses

---

### Q445. Scenario: Interview asks to design SQL layer supporting FHIR API, AI agents, and CMS reporting. Outline?

**Answer:** Three tiers: (1) OLTP/warehouse core rowstore+columnstore facts with RLS/DDM/temporal eligibility; (2) Export views and Change Tracking feeds to Databricks SAM/FHIR Extract—source of truth for clinical API; (3) Aggregated views + vector index for formulary AI + MCP read-only access. CMS reporting reads pre-aggregates/partitions—not live API logs. Fabric/Power BI consumes exports not direct PHI tables.

**Example:** Whiteboard: SQL DW center → arrows to Databricks (SAM/FHIR), Fabric (aggregates), MCP (views), SLAP metadata (narrow index tables)—RLS on all payer-scoped objects.

**How to Check:**
- Architecture matches implemented boundaries in prod
- No AI agent direct path to unmasked PHI tables
- CMS report query hits aggregate partition under 60s
- Interview diagram covers auth, RLS, and export cadence

**How to Fix:**
- Propose missing aggregate if reporting timeout chronic
- Add MCP view if agent questions blocked
- Document 2-minute version aligned with enterprise ADR

---
