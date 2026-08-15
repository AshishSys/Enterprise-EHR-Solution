# Production Issue Taxonomy & RCA Library
## Onyx Interoperability Platform — Artifact #8

**Version:** 1.0
**Last Updated:** 2026-07-07
**Classification:** Internal — Operations & Engineering
**Owner:** Platform Reliability Engineering

---

## Table of Contents

1. [Defect Classification System](#1-defect-classification-system)
2. [Defect Class Deep Dives](#2-defect-class-deep-dives)
3. [Production Triggers & Expected Failures](#3-production-triggers--expected-failures)
4. [RCA Template & Process](#4-rca-template--process)
5. [Pattern Library](#5-pattern-library)
6. [Monitoring & Early Detection](#6-monitoring--early-detection)
7. [Escalation Matrix](#7-escalation-matrix)

---

## 1. Defect Classification System

### 1.1 Defect Classes

| Class ID | Defect Class | Code | Scope |
|----------|-------------|------|-------|
| DC-1 | Data Quality | DQ | Issues with source data integrity, format violations, missing/invalid values |
| DC-2 | Mapping | MAP | FHIR mapping errors, terminology translation failures, resource construction defects |
| DC-3 | Workflow Configuration | WFC | Step Function misconfigurations, Lambda settings, pipeline orchestration errors |
| DC-4 | Deployment | DEP | Infrastructure provisioning, code deployment, environment configuration drift |
| DC-5 | Auth/Network | AUTH | Authentication failures, network connectivity, TLS/certificate issues, IAM permissions |
| DC-6 | Firely/HealthLake | FHL | FHIR server errors, validation failures, storage issues, SDK incompatibilities |
| DC-7 | Performance | PERF | Throughput degradation, memory exhaustion, timeout cascades, resource contention |
| DC-8 | Operational Sequencing | SEQ | Race conditions, ordering violations, dependency timing, idempotency failures |

### 1.2 Severity Levels

| Severity | Label | Response Time | Resolution Target | Description |
|----------|-------|---------------|-------------------|-------------|
| **P1** | Critical | ≤ 15 minutes | ≤ 4 hours | Complete service outage, data loss in progress, regulatory compliance breach, all states affected |
| **P2** | High | ≤ 30 minutes | ≤ 8 hours | Major functionality degraded, single state pipeline completely blocked, data corruption detected |
| **P3** | Medium | ≤ 2 hours | ≤ 24 hours | Partial degradation, non-critical workflow failures, single file processing failures with retry available |
| **P4** | Low | ≤ 8 hours | ≤ 72 hours | Cosmetic issues, minor logging gaps, non-blocking warnings, documentation discrepancies |

### 1.3 Impact Categories

| Impact Category | Code | Definition | Typical Severity | Recovery Complexity |
|----------------|------|------------|------------------|---------------------|
| **Data Loss** | DLOSS | Irreversible loss of source or transformed data | P1 | High — requires source re-extraction |
| **Data Corruption** | DCORR | Data written incorrectly to HealthLake/downstream; silent errors | P1-P2 | Very High — requires identification + correction of affected records |
| **Service Outage** | SOUT | Complete inability to process incoming data | P1 | Medium — typically infrastructure recovery |
| **Degraded Performance** | DPERF | Processing continues but below SLA thresholds | P2-P3 | Low-Medium — scaling or optimization |
| **Incorrect Responses** | IRESP | API returns wrong data; FHIR resources have wrong values | P2 | High — requires downstream notification and correction |

### 1.4 Classification Decision Tree

```
Incident Detected
├── Is data being lost or corrupted RIGHT NOW?
│   ├── YES → P1 (Data Loss / Data Corruption)
│   └── NO ↓
├── Is the pipeline completely stopped for any state?
│   ├── YES, all states → P1 (Service Outage)
│   ├── YES, single state → P2 (Service Outage)
│   └── NO ↓
├── Is processing occurring but producing wrong results?
│   ├── YES, affecting downstream consumers → P2 (Incorrect Responses)
│   └── NO ↓
├── Is processing slower than SLA thresholds?
│   ├── YES, missing delivery windows → P2 (Degraded Performance)
│   ├── YES, approaching limits → P3 (Degraded Performance)
│   └── NO ↓
└── Other observable anomaly → P3/P4 based on scope
```

---

## 2. Defect Class Deep Dives

---

### 2.1 DC-1: Data Quality (DQ)

#### Definition & Scope
Data Quality defects originate from source systems (payer/state flat files, EDI transactions, API responses) delivering data that violates expected schemas, contains invalid values, has structural corruption, or exhibits unexpected volume/format changes. These issues manifest before or during the initial parsing and validation stage.

#### Common Symptoms

| # | Symptom | Observable In |
|---|---------|---------------|
| 1 | Spike in validation rejection counts | CloudWatch metrics, DLQ depth |
| 2 | File parsing Lambda throwing `MalformedInputException` | Lambda logs, error handler |
| 3 | Unexpected NULL/empty values in required fields | Validation report outputs |
| 4 | Character encoding errors (mojibake in patient names) | Transformed output inspection |
| 5 | Record count mismatch between header/trailer and actual rows | Reconciliation checks |
| 6 | Date fields with impossible values (e.g., `2099-13-45`) | FHIR validation errors |
| 7 | Duplicate record identifiers within a single file | Deduplication stage alerts |
| 8 | File size anomalies (0 bytes, 10x normal, truncated) | S3 event metadata, file monitors |

#### Root Cause Patterns

| # | Root Cause | Frequency | Detection Difficulty |
|---|-----------|-----------|---------------------|
| 1 | Source system schema change without notification | High | Medium |
| 2 | Encoding mismatch (source sends Latin-1, pipeline expects UTF-8) | Medium | Low |
| 3 | Upstream ETL job failure producing partial/corrupted output | Medium | Medium |
| 4 | Delimiter collision in unquoted fields (commas in addresses) | High | Low |
| 5 | Date format variation across source systems (MM/DD/YYYY vs YYYY-MM-DD) | High | Low |
| 6 | Payer system upgrade introducing new field values not in mapping tables | Medium | High |
| 7 | Network interruption during SFTP transfer causing truncated files | Low | Medium |
| 8 | Source system timezone handling producing duplicate/missing records at DST boundaries | Low | High |

#### Diagnostic Steps

1. **Retrieve source file:** Pull the raw file from S3 raw-landing zone; confirm MD5/SHA matches source manifest
2. **Validate file structure:** Run schema validator against expected format spec; check header/trailer counts
3. **Isolate failing records:** Extract specific rows from DLQ messages; identify common field patterns
4. **Compare to baseline:** Diff file structure against last 5 successful files from same source
5. **Check source changelog:** Contact payer/state IT for any recent system changes
6. **Encoding analysis:** Use `file` command and hex dump on raw bytes to confirm encoding
7. **Volume analysis:** Compare record counts and file sizes to 30-day rolling average

#### Corrective Fixes (Immediate)

- Quarantine the problematic file; prevent partial processing from propagating
- If encoding issue: apply correct encoding transformation and reprocess
- If truncated: request re-transmission from source
- If schema drift: apply emergency field mapping override in configuration
- If delimiter issue: switch to alternate parsing mode (fixed-width fallback)
- Manually correct critical records if small volume and deadline imminent

#### Preventive Fixes (Long-term)

- Implement pre-ingestion schema validation gate with strict rejection + alerting
- Establish automated file fingerprinting (structure, encoding, delimiter detection)
- Create source system change notification contracts (30-day advance notice SLA)
- Build adaptive parser that auto-detects delimiter and encoding per file
- Deploy file-size and record-count anomaly detection using 30-day baselines
- Implement checksum verification on all file transfers
- Create source-specific data quality scorecards with trending

#### Example Incident — RCA Writeup

```
INCIDENT ID: INC-2026-0142
TITLE: Colorado Eligibility File — 47,000 Records Rejected Due to Date Format Change
SEVERITY: P2
DURATION: 6.5 hours (detection to resolution)

TIMELINE:
- 03:15 UTC: CO eligibility file arrives in S3 (scheduled window: 02:00-04:00)
- 03:17 UTC: Parser Lambda invoked; begins processing
- 03:22 UTC: Validation stage rejects 47,312 of 48,100 records (98.4%)
- 03:23 UTC: DLQ depth alarm fires (threshold: >1000 records in 5 min)
- 03:45 UTC: On-call engineer acknowledges; begins investigation
- 04:15 UTC: Root cause identified — date format changed from MM/DD/YYYY to YYYY-MM-DD
- 05:30 UTC: Configuration updated to accept both formats
- 06:00 UTC: File reprocessed successfully
- 09:45 UTC: All downstream FHIR resources validated and available

ROOT CAUSE: Colorado MMIS system upgraded from v4.2 to v5.0 over the weekend.
The new version outputs ISO-8601 dates. No advance notification was provided.

5-WHYS:
1. Why were records rejected? → Date validation expected MM/DD/YYYY format
2. Why did validation expect that format? → State-specific config hardcoded the format
3. Why wasn't the format change detected earlier? → No pre-processing format detection
4. Why was there no advance notification? → No formal change notification SLA with CO
5. Why is there no change notification SLA? → Oversight in onboarding contract

CORRECTIVE ACTIONS:
- [x] Updated CO date parser to accept ISO-8601 and legacy format
- [x] Reprocessed all 48,100 records successfully
- [x] Verified downstream FHIR resources

PREVENTIVE ACTIONS:
- [ ] Implement auto-detection date format parser for all states (Due: 2026-08-01)
- [ ] Establish change notification SLA with all state partners (Due: 2026-09-01)
- [ ] Add format-drift detection to pre-ingestion checks (Due: 2026-08-15)
```

---

### 2.2 DC-2: Mapping (MAP)

#### Definition & Scope
Mapping defects occur when source data is incorrectly translated into FHIR resources — including terminology code mapping failures, incorrect resource relationships, profile conformance violations, and structural errors in the FHIR output. These issues produce syntactically valid but semantically incorrect healthcare data.

#### Common Symptoms

| # | Symptom | Observable In |
|---|---------|---------------|
| 1 | FHIR validation errors on StructureDefinition conformance | Firely SDK validation logs |
| 2 | Terminology codes not found in ValueSet bindings | $validate-code operation failures |
| 3 | Missing required FHIR extensions for US Core/DaVinci profiles | Profile validation output |
| 4 | Incorrect Reference targets (e.g., Condition pointing to wrong Patient) | Referential integrity checks |
| 5 | CodeSystem version mismatch (ICD-10 2025 vs 2026 codes) | Terminology service logs |
| 6 | Unmapped source values producing `unknown` or fallback codes | Data quality reports |
| 7 | Bundle resources failing transaction integrity constraints | HealthLake PUT/POST errors |
| 8 | Quantity units not conforming to UCUM standard | Validation layer output |

#### Root Cause Patterns

| # | Root Cause | Frequency | Detection Difficulty |
|---|-----------|-----------|---------------------|
| 1 | Terminology update (new ICD/CPT/SNOMED codes) not reflected in mapping tables | High | Medium |
| 2 | Source field overloaded with multiple concepts mapped to single FHIR element | Medium | High |
| 3 | State-specific value sets not loaded or outdated in terminology service | Medium | Medium |
| 4 | FHIR profile version upgrade introducing new required elements | Low | Low |
| 5 | Conditional mapping logic error (wrong branching on discriminator fields) | Medium | High |
| 6 | Reference resolution failure due to resource creation ordering | Medium | Medium |
| 7 | ConceptMap entries with incorrect equivalence relationships | Low | Very High |
| 8 | Multi-byte character handling in code descriptions causing truncation | Low | Medium |

#### Diagnostic Steps

1. **Identify failing resource type:** Determine which FHIR resource(s) are failing validation
2. **Extract validation errors:** Pull OperationOutcome details from Firely validation
3. **Trace to source record:** Map the failing FHIR resource back to source file row/field
4. **Check mapping configuration:** Review the active ConceptMap/StructureMap for the affected elements
5. **Verify terminology service:** Query $lookup on the failing code against active CodeSystems
6. **Compare to known-good:** Diff the failed resource against a previously successful resource of same type
7. **Check profile version:** Confirm which IG version the validator is using vs. what mappings target

#### Corrective Fixes (Immediate)

- Add missing code mappings to ConceptMap and reprocess affected records
- Apply temporary mapping override for unmapped values (map to explicit "unmapped" code with extension)
- Fix reference target paths and resubmit affected Bundles
- Roll back profile validator version if new profile introduced breaking change
- Manually patch critical resources in HealthLake if small volume

#### Preventive Fixes (Long-term)

- Implement automated terminology update pipeline (monthly ICD/CPT/SNOMED refresh)
- Build mapping coverage reports showing percentage of source values with valid maps
- Create pre-release mapping validation suite testing all known source values against maps
- Establish FHIR IG upgrade process with mapping impact assessment
- Deploy real-time unmapped-value tracking with automatic alerting at threshold
- Implement semantic validation layer beyond structural FHIR validation
- Build mapping regression test suite with golden-file comparisons

#### Example Incident — RCA Writeup

```
INCIDENT ID: INC-2026-0198
TITLE: 12,000 Procedures Mapped to Wrong SNOMED Codes After CPT Update
SEVERITY: P2
DURATION: 14 hours (corruption period); 8 hours (remediation)

TIMELINE:
- 2026-06-01 00:00: Annual CPT code update effective date
- 2026-06-01 03:00: First files with new CPT codes arrive
- 2026-06-01 03:15: Mapping engine uses stale 2025 ConceptMap
- 2026-06-01 03:15–17:00: ~12,000 procedures mapped to deprecated SNOMED targets
- 2026-06-01 17:30: QA analyst notices statistical anomaly in procedure code distribution
- 2026-06-01 18:00: Investigation confirms wrong mappings
- 2026-06-02 02:00: Corrected ConceptMap deployed; affected resources reprocessed

ROOT CAUSE: The CPT-to-SNOMED ConceptMap scheduled update job failed silently
on 2026-05-28 due to an expired API credential for the terminology service.
The stale 2025 map contained deprecated SNOMED targets for 340 CPT codes.

5-WHYS:
1. Why were procedures mapped incorrectly? → ConceptMap had stale SNOMED targets
2. Why was the ConceptMap stale? → Scheduled update job failed on 05-28
3. Why did the job fail? → API credential for terminology service expired
4. Why was the expired credential not detected? → No health check on terminology update job
5. Why no health check? → Job was added ad-hoc without standard observability

CORRECTIVE ACTIONS:
- [x] Updated ConceptMap with 2026 CPT-to-SNOMED mappings
- [x] Identified and reprocessed all 12,000 affected Procedure resources
- [x] Notified downstream consumers of correction window

PREVENTIVE ACTIONS:
- [ ] Add health check + alerting to terminology update job (Due: 2026-06-15)
- [ ] Implement credential rotation monitoring for all service accounts (Due: 2026-07-01)
- [ ] Add mapping freshness check — alert if ConceptMap age > 7 days past update date (Due: 2026-06-30)
```

---

### 2.3 DC-3: Workflow Configuration (WFC)

#### Definition & Scope
Workflow Configuration defects involve misconfigurations in AWS Step Functions, Lambda functions, Glue jobs, and pipeline orchestration settings that cause incorrect execution flow, missed steps, improper error handling, or resource allocation failures. These are infrastructure-logic errors rather than data or mapping problems.

#### Common Symptoms

| # | Symptom | Observable In |
|---|---------|---------------|
| 1 | Step Function execution stuck in `RUNNING` state indefinitely | Step Functions console, CloudWatch |
| 2 | Lambda timeout errors with no output produced | Lambda CloudWatch logs |
| 3 | Workflow steps executing in wrong order or skipping steps | Step Functions execution history |
| 4 | Retry loops exhausting maximum attempts without resolution | Step Functions retry metrics |
| 5 | Parallel branches not joining correctly (orphaned executions) | Execution graph visualization |
| 6 | State machine input/output filtering dropping required fields | Step Functions I/O inspection |
| 7 | Glue job memory errors with `OutOfMemoryError` in logs | Glue job run logs |
| 8 | Choice state routing to wrong branch due to incorrect condition expressions | Execution path analysis |

#### Root Cause Patterns

| # | Root Cause | Frequency | Detection Difficulty |
|---|-----------|-----------|---------------------|
| 1 | Lambda memory/timeout set too low for production data volumes | High | Low |
| 2 | Step Function `ResultPath` or `OutputPath` misconfigured, dropping state | Medium | Medium |
| 3 | Missing or incorrect error handling catch blocks | Medium | Medium |
| 4 | Environment variable mismatch between stages (dev config in prod) | Medium | Low |
| 5 | Concurrent execution limit exceeded causing throttling | Medium | Medium |
| 6 | IAM role missing permissions added in recent code change | High | Low |
| 7 | Glue job partition strategy inefficient for actual data distribution | Low | High |
| 8 | Step Function definition not updated after Lambda function rename/refactor | Low | Medium |

#### Diagnostic Steps

1. **Check execution history:** Review Step Functions execution events for the failed workflow
2. **Inspect state I/O:** Examine input/output at each state transition for data loss
3. **Review Lambda configuration:** Verify memory, timeout, environment variables, layers
4. **Check concurrency:** Look for throttling events in Lambda/Step Functions metrics
5. **Compare to definition:** Diff current ASL definition against last known working version
6. **Verify IAM permissions:** Check CloudTrail for AccessDenied events from the execution role
7. **Test with reduced data:** Run workflow with minimal input to isolate scaling vs. logic issues

#### Corrective Fixes (Immediate)

- Increase Lambda memory/timeout for immediate unblocking
- Fix ResultPath/OutputPath configuration and re-execute failed workflows
- Add missing IAM permissions to execution role
- Manually advance stuck executions or terminate and restart
- Apply environment variable corrections
- Reduce concurrency temporarily to avoid throttling cascade

#### Preventive Fixes (Long-term)

- Implement infrastructure-as-code validation in CI/CD (cfn-lint, custom ASL validators)
- Create workflow integration test suite that runs against staging with production-scale data
- Build Step Function definition diff alerting on every deployment
- Implement automated Lambda right-sizing based on CloudWatch metrics
- Deploy canary executions that validate workflow end-to-end daily
- Establish configuration management with drift detection
- Create runbooks for common workflow failure patterns

#### Example Incident — RCA Writeup

```
INCIDENT ID: INC-2026-0156
TITLE: Texas Pipeline Stalled — Step Function OutputPath Dropping Member IDs
SEVERITY: P2
DURATION: 4 hours

TIMELINE:
- 08:00 UTC: TX daily pipeline triggered on schedule
- 08:05 UTC: File parsing completes successfully
- 08:06 UTC: Mapping step receives input but member_id array is empty
- 08:06 UTC: Mapping step produces 0 FHIR resources (no error, just empty output)
- 08:10 UTC: Pipeline completes "successfully" with 0 records processed
- 10:00 UTC: Morning QA check detects 0 TX records for the day
- 10:15 UTC: Investigation begins
- 12:00 UTC: Root cause identified; configuration fixed; pipeline re-executed

ROOT CAUSE: A deployment the previous day updated the parsing step's 
ResultPath from "$.parsed_output" to "$.parsing_result" but did not update 
the subsequent mapping step's InputPath which still referenced "$.parsed_output".
The mapping step received an empty object and produced no output (valid behavior
for empty input — no error raised).

5-WHYS:
1. Why did the mapping step produce 0 resources? → Input was empty
2. Why was input empty? → InputPath referenced a non-existent key in state
3. Why was the key non-existent? → Previous step's ResultPath was renamed
4. Why wasn't the rename caught? → No integration test validates state I/O contracts
5. Why no integration test? → Test suite only validates individual Lambda logic

CORRECTIVE ACTIONS:
- [x] Updated mapping step InputPath to match new ResultPath
- [x] Re-executed TX pipeline successfully (all 52,000 records processed)

PREVENTIVE ACTIONS:
- [ ] Add Step Function I/O contract tests to CI/CD pipeline (Due: 2026-07-15)
- [ ] Implement "zero output" alerting for any pipeline step (Due: 2026-07-10)
- [ ] Require Step Function definition review in PR process (Due: 2026-07-08)
```

---

### 2.4 DC-4: Deployment (DEP)

#### Definition & Scope
Deployment defects arise from failures in the release process — including infrastructure provisioning errors, code deployment issues, configuration drift between environments, incomplete rollouts, and environment-specific incompatibilities. These typically manifest immediately after or shortly following a deployment event.

#### Common Symptoms

| # | Symptom | Observable In |
|---|---------|---------------|
| 1 | New errors appearing immediately after deployment timestamp | CloudWatch Logs Insights |
| 2 | Lambda function returning `ModuleNotFoundError` or import failures | Lambda invocation logs |
| 3 | CloudFormation stack in `ROLLBACK_COMPLETE` or `UPDATE_FAILED` state | CloudFormation console |
| 4 | Environment-specific behavior differences (works in staging, fails in prod) | Cross-environment comparison |
| 5 | Missing or incorrect SSM Parameter Store values post-deployment | Application error logs |
| 6 | Container image pull failures or ECS task launch failures | ECS/ECR event logs |
| 7 | API Gateway returning 5xx errors after deployment | API Gateway CloudWatch metrics |
| 8 | Database migration scripts partially applied | RDS logs, application ORM errors |

#### Root Cause Patterns

| # | Root Cause | Frequency | Detection Difficulty |
|---|-----------|-----------|---------------------|
| 1 | Missing dependency in Lambda layer or deployment package | High | Low |
| 2 | Infrastructure-as-code template error not caught by linting | Medium | Medium |
| 3 | Secrets/parameter store values not propagated to new environment | High | Low |
| 4 | Deployment pipeline deploying to wrong stage/account | Low | Low |
| 5 | Race condition between infrastructure and application deployment | Medium | High |
| 6 | Docker image built on wrong architecture (x86 vs ARM) | Low | Medium |
| 7 | Blue/green deployment not properly draining old version connections | Low | High |
| 8 | Feature flag configuration not enabled for production environment | Medium | Low |

#### Diagnostic Steps

1. **Correlate with deployments:** Check deployment history for changes in the last 24 hours
2. **Compare environments:** Diff production configuration against staging/dev
3. **Check CloudFormation events:** Review stack events for failed resource operations
4. **Verify deployment artifacts:** Confirm Lambda package contents, container image tags
5. **Review parameter store:** Validate all SSM parameters and secrets are present and current
6. **Check IAM changes:** Look for any permission modifications in recent deployments
7. **Inspect rollback state:** If rollback occurred, identify which resource failed

#### Corrective Fixes (Immediate)

- Roll back to last known working version using deployment pipeline
- Manually apply missing configuration values to unblock production
- Fix CloudFormation template and redeploy
- Add missing dependencies to Lambda layer
- Correct Docker image architecture and redeploy container
- Enable missing feature flags for production

#### Preventive Fixes (Long-term)

- Implement progressive deployment (canary → 10% → 50% → 100%) with automatic rollback
- Add deployment verification tests that run post-deploy (smoke tests)
- Create environment parity checker that diffs configurations across stages
- Enforce deployment freeze windows during critical processing periods
- Implement deployment approval gates with diff review
- Build immutable infrastructure patterns reducing configuration drift
- Create comprehensive pre-deployment checklist automation

#### Example Incident — RCA Writeup

```
INCIDENT ID: INC-2026-0171
TITLE: All Pipelines Failed — Lambda Layer Missing boto3 Upgrade
SEVERITY: P1
DURATION: 2.5 hours

TIMELINE:
- 14:00 UTC: Deployment pipeline executes scheduled release v2.14.0
- 14:05 UTC: All Lambda functions updated successfully (per deployment logs)
- 14:15 UTC: First pipeline trigger fires; Lambda returns ImportError
- 14:16 UTC: Cascading failures across all state pipelines
- 14:18 UTC: P1 alert fires (>50% Lambda error rate)
- 14:25 UTC: On-call engineer acknowledges
- 14:45 UTC: Root cause identified — Lambda layer incompatibility
- 15:30 UTC: Rollback to v2.13.2 completed
- 16:30 UTC: All pipelines recovered; backlog processing initiated

ROOT CAUSE: Release v2.14.0 upgraded application code to use boto3 1.34 
features (S3 Express One Zone). The Lambda layer still contained boto3 1.28. 
The ImportError occurred on first invocation of new API calls. The staging 
environment had boto3 1.34 installed directly (not via layer), masking the issue.

5-WHYS:
1. Why did Lambdas fail? → ImportError on boto3 1.34 feature
2. Why wasn't boto3 1.34 available? → Lambda layer contained 1.28
3. Why wasn't the layer updated? → Layer update was in a separate PR, not merged
4. Why did staging pass? → Staging had boto3 installed differently (not via layer)
5. Why is staging configured differently? → Environment parity not enforced

CORRECTIVE ACTIONS:
- [x] Rolled back to v2.13.2
- [x] Processed backlog (45-minute data delay for all states)
- [x] Updated Lambda layer to include boto3 1.34

PREVENTIVE ACTIONS:
- [ ] Enforce environment parity validation in CI/CD (Due: 2026-07-15)
- [ ] Add Lambda import validation step to deployment pipeline (Due: 2026-07-10)
- [ ] Implement canary deployment pattern for Lambda updates (Due: 2026-08-01)
```

---

### 2.5 DC-5: Auth/Network (AUTH)

#### Definition & Scope
Auth/Network defects encompass authentication failures, authorization errors, network connectivity issues, TLS/certificate problems, IAM permission gaps, and cross-account access failures. These prevent the platform from communicating with internal services, external APIs, and cloud resources.

#### Common Symptoms

| # | Symptom | Observable In |
|---|---------|---------------|
| 1 | `AccessDeniedException` in Lambda/service logs | CloudWatch Logs, CloudTrail |
| 2 | Connection timeout errors to external endpoints | Application logs, VPC Flow Logs |
| 3 | TLS handshake failures (`CERTIFICATE_VERIFY_FAILED`) | SSL debug logs |
| 4 | OAuth token refresh failures causing 401 responses | Authentication service logs |
| 5 | Cross-account AssumeRole failures | CloudTrail, STS logs |
| 6 | DNS resolution failures for internal services | VPC DNS logs |
| 7 | Security group or NACL blocking traffic (connection refused) | VPC Flow Logs |
| 8 | API key rotation causing immediate authentication failures | API Gateway access logs |

#### Root Cause Patterns

| # | Root Cause | Frequency | Detection Difficulty |
|---|-----------|-----------|---------------------|
| 1 | IAM policy missing newly required permissions after service update | High | Low |
| 2 | Certificate expiration (server or client certificates) | Medium | Low (if monitored) |
| 3 | OAuth client secret rotated without updating secrets manager | Medium | Low |
| 4 | VPC security group rule removed or tightened by automation | Medium | Medium |
| 5 | Cross-account trust policy not updated after account restructuring | Low | Medium |
| 6 | KMS key policy not granting access to new service role | Medium | Medium |
| 7 | Network ACL rule conflict from infrastructure change | Low | High |
| 8 | DNS TTL caching stale endpoint after failover | Low | High |

#### Diagnostic Steps

1. **Check CloudTrail:** Search for AccessDenied/Unauthorized events for the service role
2. **Test connectivity:** Use VPC Reachability Analyzer or Lambda-based connectivity test
3. **Verify credentials:** Check secrets manager and parameter store for credential freshness
4. **Certificate inspection:** Validate certificate chain and expiration dates
5. **IAM policy simulation:** Use IAM Policy Simulator with the exact action and resource
6. **VPC flow log analysis:** Filter for REJECT entries from the service's ENI
7. **DNS resolution test:** Verify DNS resolution from within the VPC

#### Corrective Fixes (Immediate)

- Add missing IAM permissions to the affected role
- Rotate and update expired/revoked credentials
- Renew or replace expired certificates
- Add security group rules to restore connectivity
- Manually refresh OAuth tokens and restart affected services
- Update DNS records or flush DNS caches

#### Preventive Fixes (Long-term)

- Implement certificate expiration monitoring with 30/14/7-day alerts
- Automate credential rotation with zero-downtime patterns
- Deploy least-privilege IAM with automated permission boundary testing
- Create network connectivity canary tests running continuously
- Implement infrastructure change approval workflow with blast radius analysis
- Build cross-account permission audit running weekly
- Deploy mutual TLS (mTLS) with automated certificate management

#### Example Incident — RCA Writeup

```
INCIDENT ID: INC-2026-0183
TITLE: HealthLake Writes Failing — KMS Key Policy Not Granting New Lambda Role
SEVERITY: P1
DURATION: 3 hours

TIMELINE:
- 09:00 UTC: Infrastructure team deploys new Lambda execution role as part of security hardening
- 09:15 UTC: First pipeline execution with new role begins
- 09:20 UTC: HealthLake FHIR writes fail with AccessDeniedException
- 09:21 UTC: All state pipelines entering error state
- 09:25 UTC: P1 alert fires (HealthLake write error rate 100%)
- 09:35 UTC: On-call identifies KMS AccessDenied in CloudTrail
- 10:15 UTC: KMS key policy updated to include new role ARN
- 10:20 UTC: Pipelines resume successfully
- 12:00 UTC: All backlog cleared

ROOT CAUSE: Security hardening project created new Lambda execution roles 
with more restrictive permissions. The new role ARN was added to IAM policies 
but not to the KMS key policy for the HealthLake encryption key. HealthLake 
requires KMS:Decrypt and KMS:GenerateDataKey on its CMK for all write operations.

5-WHYS:
1. Why did HealthLake writes fail? → AccessDenied on KMS operations
2. Why was KMS access denied? → New Lambda role not in KMS key policy
3. Why wasn't it in the key policy? → KMS policies managed separately from IAM
4. Why wasn't this caught in testing? → Staging uses AWS-managed key (no custom policy)
5. Why does staging differ? → Cost optimization — CMK only in production

CORRECTIVE ACTIONS:
- [x] Added new role ARN to KMS key policy
- [x] Reprocessed all failed pipeline executions
- [x] Verified all state data delivered within recovery SLA

PREVENTIVE ACTIONS:
- [ ] Use CMK in staging environment to match production (Due: 2026-07-20)
- [ ] Add KMS policy validation to infrastructure deployment checks (Due: 2026-07-15)
- [ ] Implement pre-deployment smoke test that validates write path end-to-end (Due: 2026-07-30)
```

---

### 2.6 DC-6: Firely/HealthLake (FHL)

#### Definition & Scope
Firely/HealthLake defects involve issues specific to the FHIR server infrastructure — including Firely SDK validation errors, HealthLake API limitations, FHIR resource storage failures, search index inconsistencies, and FHIR specification compliance issues. These represent the unique challenges of operating a FHIR-based data platform.

#### Common Symptoms

| # | Symptom | Observable In |
|---|---------|---------------|
| 1 | HealthLake returning `ThrottlingException` on FHIR operations | HealthLake CloudWatch metrics |
| 2 | Firely validator rejecting resources that passed previous validation | Firely SDK logs |
| 3 | Bundle transaction failures with partial resource creation | HealthLake response bodies |
| 4 | Search queries returning stale or incomplete results | API response validation |
| 5 | `OperationOutcome` with `HAPI-` error codes from HealthLake | FHIR response inspection |
| 6 | Resource versioning conflicts (`409 Conflict` on updates) | HealthLake audit logs |
| 7 | Large Bundle (>160 resources) hitting HealthLake payload limits | API Gateway/HealthLake logs |
| 8 | Custom SearchParameter not returning expected results | Search operation debugging |

#### Root Cause Patterns

| # | Root Cause | Frequency | Detection Difficulty |
|---|-----------|-----------|---------------------|
| 1 | HealthLake throughput limits exceeded during peak processing | High | Low |
| 2 | FHIR profile version mismatch between Firely validator and HealthLake expectations | Medium | Medium |
| 3 | Bundle size exceeding HealthLake's transaction limits | Medium | Low |
| 4 | HealthLake eventual consistency causing read-after-write failures | Medium | High |
| 5 | Firely SDK version incompatibility with HealthLake's FHIR version support | Low | Medium |
| 6 | SearchParameter indexing delay causing stale query results | Medium | High |
| 7 | HealthLake service degradation (AWS-side) affecting operations | Low | Low |
| 8 | Circular references in FHIR resources causing processing loops | Low | High |

#### Diagnostic Steps

1. **Check HealthLake metrics:** Review CloudWatch for throttling, latency, error rates
2. **Inspect OperationOutcome:** Parse the full OperationOutcome response for specific error details
3. **Validate resource locally:** Run Firely validator independently on the failing resource
4. **Check Bundle composition:** Verify Bundle size, reference integrity, and transaction semantics
5. **Test with single resource:** Submit individual resources to isolate Bundle-level vs resource-level failures
6. **Verify HealthLake status:** Check AWS Health Dashboard for service events
7. **Review SDK version compatibility:** Cross-reference Firely SDK version against HealthLake FHIR version

#### Corrective Fixes (Immediate)

- Implement exponential backoff and retry for throttling errors
- Split oversized Bundles into smaller transaction sets
- Use conditional creates (`If-None-Exist`) to handle version conflicts
- Switch to batch mode if transaction mode is failing
- Apply Firely validation bypass for known false-positive rejections (with logging)
- Wait and retry for eventual consistency issues (add read-after-write delay)

#### Preventive Fixes (Long-term)

- Implement adaptive throughput management with pre-provisioned capacity
- Build Bundle-sizing logic that respects HealthLake limits dynamically
- Create FHIR version compatibility matrix and automated testing
- Deploy read-after-write consistency layer with verification
- Implement HealthLake capacity planning based on processing schedules
- Build FHIR resource dependency graph to optimize Bundle ordering
- Create Firely SDK upgrade testing pipeline with regression suite

#### Example Incident — RCA Writeup

```
INCIDENT ID: INC-2026-0205
TITLE: HealthLake Throttling During Multi-State Concurrent Processing
SEVERITY: P2
DURATION: 5 hours

TIMELINE:
- 03:00 UTC: Five state pipelines trigger simultaneously (normal schedule)
- 03:15 UTC: HealthLake write throughput reaches capacity
- 03:16 UTC: ThrottlingException rate climbs to 40%
- 03:20 UTC: Retry storms amplify load; effective throughput drops
- 03:25 UTC: Alert fires on HealthLake error rate
- 04:00 UTC: On-call implements emergency rate limiting
- 05:00 UTC: Staggered reprocessing begins
- 08:00 UTC: All state data successfully written

ROOT CAUSE: Pipeline scheduling placed 5 states in the same 03:00 window.
Combined write volume (~180,000 resources in 15 minutes) exceeded HealthLake's
provisioned throughput. Retry logic without jitter created thundering herd,
further degrading throughput.

5-WHYS:
1. Why was HealthLake throttling? → Write volume exceeded provisioned throughput
2. Why was volume so high? → 5 states processing simultaneously
3. Why are 5 states scheduled at the same time? → Default schedule not optimized for load distribution
4. Why isn't there load distribution? → Pipeline scheduler doesn't consider HealthLake capacity
5. Why doesn't retry logic include jitter? → Standard exponential backoff implemented without jitter

CORRECTIVE ACTIONS:
- [x] Staggered reprocessing with rate limiting
- [x] All state data delivered within 5-hour extended SLA

PREVENTIVE ACTIONS:
- [ ] Implement pipeline scheduling with load distribution (15-min stagger) (Due: 2026-07-20)
- [ ] Add jitter to all retry logic across the platform (Due: 2026-07-10)
- [ ] Implement token bucket rate limiter for HealthLake writes (Due: 2026-07-25)
- [ ] Create capacity planning model mapping state volumes to throughput needs (Due: 2026-08-01)
```

---

### 2.7 DC-7: Performance (PERF)

#### Definition & Scope
Performance defects involve throughput degradation, excessive latency, memory exhaustion, CPU saturation, and resource contention that cause the platform to miss processing SLAs without complete failure. The system continues operating but below acceptable performance thresholds.

#### Common Symptoms

| # | Symptom | Observable In |
|---|---------|---------------|
| 1 | Pipeline completion time exceeding SLA window | Step Functions duration metrics |
| 2 | Lambda functions hitting timeout limits consistently | Lambda duration/timeout metrics |
| 3 | Memory utilization at >90% causing GC pressure or OOM kills | Lambda/ECS memory metrics |
| 4 | Glue job shuffle spilling to disk with dramatic slowdown | Glue job Spark UI metrics |
| 5 | API response latency p99 exceeding acceptable thresholds | API Gateway latency metrics |
| 6 | DynamoDB consumed capacity exceeding provisioned (throttling) | DynamoDB CloudWatch |
| 7 | S3 request rate limiting (503 SlowDown) | S3 request metrics |
| 8 | Cold start latency spikes after deployment or idle periods | Lambda init duration metrics |

#### Root Cause Patterns

| # | Root Cause | Frequency | Detection Difficulty |
|---|-----------|-----------|---------------------|
| 1 | Data volume growth exceeding original capacity planning | High | Medium |
| 2 | Inefficient FHIR resource serialization/deserialization in hot path | Medium | High |
| 3 | N+1 query pattern in reference resolution (fetching related resources one-by-one) | Medium | Medium |
| 4 | Lambda cold starts compounding with high concurrency bursts | Medium | Medium |
| 5 | Unbounded batch sizes causing memory pressure | High | Low |
| 6 | Missing or inefficient database/search indexes | Medium | Medium |
| 7 | Synchronous calls where async would suffice (blocking on I/O) | Medium | High |
| 8 | Logging/tracing overhead in high-throughput code paths | Low | High |

#### Diagnostic Steps

1. **Establish baseline:** Compare current performance metrics to 7/30-day historical baselines
2. **Identify bottleneck:** Profile execution to find which step/component consumes most time
3. **Check data volumes:** Compare current file sizes and record counts to historical averages
4. **Memory analysis:** Review Lambda/ECS memory utilization patterns and GC logs
5. **Concurrency analysis:** Check concurrent execution counts and queuing delays
6. **I/O profiling:** Measure time spent in network calls, disk I/O, and serialization
7. **Resource utilization:** Review CPU, memory, network, and disk utilization across all components

#### Corrective Fixes (Immediate)

- Increase Lambda memory/timeout for affected functions
- Scale up ECS tasks or Glue DPUs
- Implement emergency batch-size reduction
- Enable provisioned concurrency for critical Lambdas
- Switch to on-demand DynamoDB capacity mode
- Add S3 request prefixing to distribute load
- Kill and restart stuck/degraded processing jobs

#### Preventive Fixes (Long-term)

- Implement automatic scaling policies based on data volume metrics
- Build performance regression testing in CI/CD with production-scale data
- Create capacity planning model with growth projections
- Optimize hot paths with profiling-driven refactoring
- Implement adaptive batch sizing based on available memory and data volume
- Deploy caching layers for frequently accessed reference data
- Create SLA-aware pipeline scheduling that reserves processing windows

#### Example Incident — RCA Writeup

```
INCIDENT ID: INC-2026-0212
TITLE: California Pipeline Missing 08:00 Delivery SLA — 340% Volume Increase
SEVERITY: P2
DURATION: Ongoing degradation (3 weeks); acute failure (1 day)

TIMELINE:
- 2026-06-15: CA file sizes begin increasing (open enrollment pre-registration)
- 2026-06-15 to 07-01: Pipeline completion time gradually increases from 2h to 4.5h
- 2026-07-01: CA file arrives at 180MB (vs 52MB historical average)
- 2026-07-01 03:00: Pipeline starts processing
- 2026-07-01 07:45: Pipeline still processing at 60% complete
- 2026-07-01 08:00: SLA window missed
- 2026-07-01 09:30: Pipeline completes (6.5h total vs 2h SLA)

ROOT CAUSE: California open enrollment pre-registration increased file volume 
by 340%. The mapping Lambda's batch size was fixed at 5,000 records, causing 
70 sequential invocations instead of the normal 20. Additionally, each invocation 
was hitting memory pressure at the increased record complexity, causing GC pauses.

5-WHYS:
1. Why did the pipeline miss SLA? → Processing took 6.5h instead of 2h
2. Why so slow? → 70 sequential batches + GC pressure in each
3. Why sequential? → Fixed batch size didn't account for volume growth
4. Why fixed batch size? → No adaptive sizing implemented
5. Why no capacity planning for enrollment? → Seasonal volume patterns not modeled

CORRECTIVE ACTIONS:
- [x] Increased Lambda memory from 1GB to 3GB for CA mapping function
- [x] Reduced batch size to 2,500 but increased parallelism (Map state)
- [x] Reprocessed to meet extended SLA

PREVENTIVE ACTIONS:
- [ ] Implement adaptive batch sizing based on file volume (Due: 2026-07-15)
- [ ] Build seasonal capacity planning model (Due: 2026-07-30)
- [ ] Add parallel Map state for all state mapping functions (Due: 2026-07-20)
- [ ] Create early warning alerts when pipeline duration exceeds 50% of SLA window (Due: 2026-07-10)
```

---

### 2.8 DC-8: Operational Sequencing (SEQ)

#### Definition & Scope
Operational Sequencing defects involve race conditions, dependency ordering violations, timing-sensitive failures, idempotency violations, and state management errors. These occur when operations execute in an unexpected order or when the system fails to properly handle concurrent or repeated operations.

#### Common Symptoms

| # | Symptom | Observable In |
|---|---------|---------------|
| 1 | Duplicate FHIR resources created for the same source entity | HealthLake search results |
| 2 | Reference integrity failures (resource references non-existent resource) | FHIR validation, referential integrity checks |
| 3 | Stale data overwriting newer data (last-write-wins race condition) | Resource version history |
| 4 | Pipeline processing file that depends on not-yet-arrived predecessor | Pipeline error logs |
| 5 | Reprocessing creating duplicate side effects (double notifications, etc.) | Downstream system logs |
| 6 | State machine resuming from wrong checkpoint after failure recovery | Step Functions execution history |
| 7 | Concurrent modifications to same resource producing inconsistent state | HealthLake conflict logs |
| 8 | Dependency resources not available when referenced during processing | Reference resolution logs |

#### Root Cause Patterns

| # | Root Cause | Frequency | Detection Difficulty |
|---|-----------|-----------|---------------------|
| 1 | Missing idempotency keys on resource creation operations | High | Medium |
| 2 | S3 event notifications delivering out-of-order for related files | Medium | High |
| 3 | Concurrent pipeline executions processing overlapping data sets | Medium | Medium |
| 4 | Missing dependency check before processing (e.g., Provider file not yet loaded) | High | Medium |
| 5 | Checkpoint/cursor not updated atomically with processing | Low | Very High |
| 6 | Retry of partially-completed batch without proper deduplication | Medium | Medium |
| 7 | Clock skew between distributed components affecting ordering logic | Low | Very High |
| 8 | File-level dependencies not encoded in pipeline orchestration | Medium | Medium |

#### Diagnostic Steps

1. **Timeline reconstruction:** Build precise chronological timeline of all operations with timestamps
2. **Identify ordering violations:** Determine which operations executed in unexpected sequence
3. **Check idempotency:** Verify if reprocessing the same input produces different results
4. **Concurrency analysis:** Look for overlapping executions of related workflows
5. **Dependency graph review:** Map file/resource dependencies and verify satisfaction order
6. **State inspection:** Examine checkpoints, cursors, and processing markers
7. **Duplicate detection:** Search for duplicate resources or side effects in downstream systems

#### Corrective Fixes (Immediate)

- Deduplicate affected resources in HealthLake (merge or delete duplicates)
- Reprocess in correct dependency order after ensuring prerequisites are met
- Apply idempotency markers retroactively and reprocess
- Lock concurrent pipelines to prevent further race conditions
- Restore correct state from last known consistent checkpoint
- Manually fix out-of-order data effects

#### Preventive Fixes (Long-term)

- Implement idempotency keys on all mutating operations (conditional creates in FHIR)
- Build dependency-aware pipeline orchestration (file dependency graph)
- Deploy optimistic concurrency control with version-based conflict detection
- Create exactly-once processing guarantees using transactional outbox pattern
- Implement ordering guarantees for related file processing (sequencing queue)
- Build state machine with explicit dependency satisfaction gates
- Deploy distributed locking for resources under concurrent modification

#### Example Incident — RCA Writeup

```
INCIDENT ID: INC-2026-0223
TITLE: 3,400 Duplicate Patient Resources Created — Missing Idempotency on Retry
SEVERITY: P2
DURATION: 22 hours (detection); 8 hours (remediation)

TIMELINE:
- 04:00 UTC: OH pipeline begins processing 85,000 member records
- 04:25 UTC: Lambda timeout at batch #14 (5,000 records created, next 5,000 in flight)
- 04:25 UTC: Step Function retry triggers; batch #14 re-executes from beginning
- 04:35 UTC: Batch #14 completes on retry — but 3,400 records already created
-            in the first attempt are now duplicated
- 04:35 UTC: Pipeline continues and completes normally
- 06:00 UTC: No alert fires (total record count within expected range ±5%)
- Next day: Downstream analytics team reports duplicate patient matches
- 26 hours later: Duplicates identified and remediation begins

ROOT CAUSE: Lambda processing batch #14 had created 3,400 Patient resources 
before timing out. The retry re-executed the entire batch without checking for 
existing resources (no conditional create / If-None-Exist header). HealthLake 
created duplicates because each POST generated a new resource ID.

5-WHYS:
1. Why were duplicates created? → Same records POSTed twice to HealthLake
2. Why were they POSTed twice? → Retry re-executed the full batch
3. Why did retry reprocess already-created records? → No checkpoint within batch
4. Why no checkpoint? → Lambda processes batch atomically (all-or-nothing design)
5. Why no idempotency? → Original design assumed Lambdas wouldn't timeout mid-batch

CORRECTIVE ACTIONS:
- [x] Identified all 3,400 duplicate Patient resources via matching algorithm
- [x] Merged duplicates (kept oldest, updated references pointing to newer)
- [x] Notified downstream consumers of resource ID changes

PREVENTIVE ACTIONS:
- [ ] Implement conditional create (If-None-Exist) for all Patient resources (Due: 2026-07-15)
- [ ] Add intra-batch checkpointing for large batches (Due: 2026-08-01)
- [ ] Deploy duplicate detection job running daily (Due: 2026-07-20)
- [ ] Implement strict duplicate alerting with lower tolerance (±1%) (Due: 2026-07-12)
```

---

## 3. Production Triggers & Expected Failures

### 3.1 File Arrival & Trigger Mechanisms

#### S3 Event Triggers

| Trigger Type | Mechanism | Typical Latency | Failure Modes |
|-------------|-----------|-----------------|---------------|
| S3 Event Notification → SQS → Lambda | S3 `s3:ObjectCreated:*` event | < 1 second | SQS DLQ, Lambda throttling, event loss during S3 replication |
| S3 Event → EventBridge → Step Functions | EventBridge rule matching prefix/suffix | 1-5 seconds | Rule mismatch, target invocation failure, EventBridge throttling |
| S3 Inventory → Batch Processing | Daily/weekly inventory report triggers batch | Hours (scheduled) | Inventory report generation failure, manifest parsing error |

#### Cron-Based Triggers

| Schedule | Trigger | Purpose | Failure Mode |
|----------|---------|---------|--------------|
| `cron(0 3 * * ? *)` | EventBridge Rule | Daily state file processing window open | Rule disabled, target removed |
| `cron(0 */6 * * ? *)` | EventBridge Rule | Reconciliation check every 6 hours | Accumulating drift undetected |
| `cron(0 8 * * MON *)` | EventBridge Rule | Weekly summary report generation | Holiday/calendar edge cases |
| `cron(0 0 1 * ? *)` | EventBridge Rule | Monthly aggregation and reporting | Month boundary processing |

#### Common Trigger Issues

| Issue | Cause | Detection | Resolution |
|-------|-------|-----------|------------|
| Event not firing | S3 event notification disabled/misconfigured | Missing pipeline execution in expected window | Verify S3 bucket notification configuration |
| Duplicate events | S3 multipart upload generating multiple events | Duplicate processing/resources | Implement deduplication on event ID |
| Delayed events | SQS visibility timeout + retry backoff | Pipeline starting late in window | Monitor SQS age metrics |
| Out-of-order events | Multiple files arriving near-simultaneously | Dependency violations | Implement ordering queue |
| Missing events | S3 event notification eventual consistency | Pipeline never triggers | S3 inventory reconciliation job |

### 3.2 State-Specific Workflow Schedules

#### Daily Processing Windows

| State | File Arrival Window | Processing Trigger | Expected Volume | Delivery SLA |
|-------|--------------------|--------------------|-----------------|--------------|
| California (CA) | 01:00-03:00 UTC | S3 event | 40,000-180,000 records | 08:00 UTC |
| Texas (TX) | 02:00-04:00 UTC | S3 event | 35,000-90,000 records | 09:00 UTC |
| New York (NY) | 03:00-05:00 UTC | S3 event | 50,000-120,000 records | 10:00 UTC |
| Florida (FL) | 02:30-04:30 UTC | S3 event | 30,000-75,000 records | 09:30 UTC |
| Ohio (OH) | 04:00-06:00 UTC | S3 event | 20,000-60,000 records | 11:00 UTC |
| Colorado (CO) | 03:00-04:00 UTC | S3 event | 15,000-50,000 records | 09:00 UTC |
| Pennsylvania (PA) | 02:00-03:30 UTC | S3 event | 25,000-65,000 records | 09:00 UTC |
| Illinois (IL) | 03:30-05:30 UTC | S3 event | 22,000-55,000 records | 10:00 UTC |

#### Weekly/Monthly Schedules

| Process | Schedule | States | Expected Volume | Notes |
|---------|----------|--------|-----------------|-------|
| Provider roster refresh | Sunday 00:00-06:00 UTC | All | 500,000-2M records | Full replacement |
| Pharmacy network update | Wednesday 02:00 UTC | All | 100,000-300,000 records | Delta only |
| Monthly eligibility reconciliation | 1st of month, 00:00 UTC | All | Full population snapshot | Compare against daily deltas |
| Quarterly plan benefit reload | Jan/Apr/Jul/Oct 1st | All | 50,000-150,000 records | Full replacement + validation |

### 3.3 Expected Failures vs True Defects

#### Expected Failures (Normal Operations)

| Scenario | Expected Behavior | Why It's Normal | Action Required |
|----------|-------------------|-----------------|-----------------|
| Source file arrives empty (0 records) | Pipeline validates, produces empty output, logs warning | Source system had no changes that day | None — monitor for consecutive empty files (>3 days = investigate) |
| Small percentage of records fail validation (<2%) | Records sent to DLQ, remainder processed | Real-world data always has some invalid records | Review DLQ weekly; escalate if >2% |
| Lambda cold start timeout on first invocation | Single retry succeeds | Normal Lambda lifecycle behavior | None — provisioned concurrency for critical paths |
| HealthLake throttling during peak (brief) | Exponential backoff succeeds within 3 retries | Burst capacity exceeded momentarily | None — review if consistent (>5% requests throttled) |
| Network timeout to external terminology service | Retry with cached fallback succeeds | Transient network issues are normal | None — investigate if >3 consecutive failures |
| File arrives outside expected window (±30 min) | Pipeline processes normally, just late | Source system maintenance, slight delays | None — alert only if >2 hours outside window |

#### True Defect Indicators (Requires Investigation)

| Indicator | Threshold | Likely Defect Class |
|-----------|-----------|---------------------|
| Validation failure rate > 5% for a single file | >5% rejection | DQ or MAP |
| Same error recurring across 3+ consecutive pipeline runs | 3+ occurrences | WFC, DEP, or AUTH |
| Pipeline completes but produces 0 output (non-empty input) | Zero output with valid input | WFC or SEQ |
| Error type never seen before in production | Novel error signature | Any — investigate immediately |
| Performance degradation > 50% from 7-day baseline | >50% slowdown | PERF |
| Resource creation count differs from expected by >10% | >10% variance | MAP, SEQ, or FHL |
| Cross-state impact (same error in multiple state pipelines) | 2+ states affected | DEP, AUTH, or FHL |
| Alert firing continuously for >30 minutes without auto-resolution | Sustained alert | Varies — not self-healing |

#### Decision Matrix: Expected vs True Defect

```
Is this the FIRST occurrence?
├── YES → Has it auto-resolved within the retry window?
│   ├── YES → Log as expected transient failure
│   └── NO → Investigate as potential defect
└── NO → Is the same error repeating?
    ├── 2 occurrences → Monitor closely; prepare investigation
    ├── 3+ occurrences → Declare true defect; open incident
    └── Pattern matches known seasonal behavior? 
        ├── YES → Expected (document for future reference)
        └── NO → True defect
```

### 3.4 Seasonal & Volume Patterns

#### Annual Volume Calendar

| Period | Dates | Impact | Expected Volume Change | Preparation |
|--------|-------|--------|----------------------|-------------|
| **Open Enrollment** | Nov 1 - Jan 15 | Eligibility files 200-400% increase | 200-400% | Pre-scale infrastructure Oct 15 |
| **Year-End Close** | Dec 15 - Jan 5 | All file types spike; reconciliation files arrive | 150-300% | Extended processing windows |
| **Annual Code Updates** | Jan 1 (ICD/CPT effective) | Mapping table updates; validation changes | Normal volume, new codes | Update terminology maps by Dec 15 |
| **State Fiscal Year** | Jul 1 (most states) | Plan/benefit changes; provider roster refreshes | 120-150% | Pre-load new plan configurations |
| **Redetermination Waves** | Varies by state | Eligibility churn increases | 150-250% for affected states | Monitor state-specific schedules |
| **Quarterly Reporting** | Jan/Apr/Jul/Oct | Additional reporting extracts running | +20-30% platform load | Schedule reports in off-peak hours |
| **Tax Season** | Feb-Apr | 1095 form generation load | Additive load +15% | Ensure reporting pipeline capacity |

#### Weekly Patterns

| Day | Pattern | Impact |
|-----|---------|--------|
| Monday | Highest volume — weekend backlog from source systems | +30-50% over daily average |
| Tuesday-Thursday | Normal steady-state volume | Baseline |
| Friday | Slightly elevated — weekly batch jobs from payers | +10-20% |
| Saturday-Sunday | Minimal volume — batch-only, no real-time feeds | -70-80% |

#### Monthly Patterns

| Period | Pattern | Impact |
|--------|---------|--------|
| 1st-3rd of month | Monthly reconciliation files; plan effective dates | +40-60% |
| 15th-16th | Mid-month eligibility updates (semi-monthly payers) | +20-30% |
| Last 2 days | End-of-month reporting extracts | +25-35% |
| Other days | Standard daily volume | Baseline |

---

## 4. RCA Template & Process

### 4.1 Standard RCA Template

```markdown
# Root Cause Analysis Report

## Incident Summary
- **Incident ID:** INC-YYYY-NNNN
- **Title:** [Brief descriptive title]
- **Severity:** P1/P2/P3/P4
- **Defect Class:** [DQ/MAP/WFC/DEP/AUTH/FHL/PERF/SEQ]
- **Impact Category:** [Data Loss/Corruption/Outage/Degraded Performance/Incorrect Responses]
- **Date Detected:** YYYY-MM-DD HH:MM UTC
- **Date Resolved:** YYYY-MM-DD HH:MM UTC
- **Duration:** X hours Y minutes
- **Affected States:** [List of affected states]
- **Affected Records:** [Count of affected records/resources]
- **Reported By:** [Person/System that detected]
- **Incident Commander:** [Lead responder]

## Impact Assessment
- **Data Impact:** [Description of data affected]
- **Downstream Impact:** [Systems/consumers affected]
- **SLA Impact:** [Which SLAs were missed and by how much]
- **Customer Impact:** [End-user/stakeholder impact description]
- **Regulatory Impact:** [Any compliance implications]
- **Financial Impact:** [Estimated cost if applicable]

## Timeline
| Time (UTC) | Event | Actor |
|------------|-------|-------|
| HH:MM | [Event description] | [System/Person] |
| HH:MM | [Event description] | [System/Person] |
| ... | ... | ... |

## Detection
- **How was it detected?** [Alert/Manual observation/Customer report]
- **Time to detect:** [Minutes from occurrence to detection]
- **Could it have been detected earlier?** [Yes/No — explain]
- **Detection gap:** [What monitoring was missing?]

## Root Cause Analysis

### Direct Cause
[The immediate technical cause of the failure]

### Contributing Factors
1. [Factor 1]
2. [Factor 2]
3. [Factor 3]

### 5-Whys Analysis
1. **Why** did [symptom] occur?
   → Because [cause 1]
2. **Why** did [cause 1] happen?
   → Because [cause 2]
3. **Why** did [cause 2] happen?
   → Because [cause 3]
4. **Why** did [cause 3] happen?
   → Because [cause 4]
5. **Why** did [cause 4] happen?
   → Because [root cause]

### Root Cause Statement
[Single clear statement of the fundamental root cause]

## Resolution

### Immediate Actions Taken
| # | Action | Owner | Completed |
|---|--------|-------|-----------|
| 1 | [Action] | [Owner] | [Timestamp] |
| 2 | [Action] | [Owner] | [Timestamp] |

### Verification Steps
- [ ] [How resolution was verified]
- [ ] [Downstream impact confirmed resolved]
- [ ] [Monitoring confirms normal operation]

## Corrective Actions (Short-term)

| # | Action | Owner | Due Date | Status |
|---|--------|-------|----------|--------|
| 1 | [Immediate fix to prevent recurrence] | [Owner] | [Date] | [Status] |
| 2 | [Additional immediate mitigation] | [Owner] | [Date] | [Status] |

## Preventive Actions (Long-term)

| # | Action | Owner | Due Date | Status | Tracks To |
|---|--------|-------|----------|--------|-----------|
| 1 | [Systemic improvement] | [Owner] | [Date] | [Status] | [Jira/Ticket] |
| 2 | [Process improvement] | [Owner] | [Date] | [Status] | [Jira/Ticket] |
| 3 | [Monitoring improvement] | [Owner] | [Date] | [Status] | [Jira/Ticket] |

## Lessons Learned
1. [Key lesson 1]
2. [Key lesson 2]
3. [Key lesson 3]

## Related Incidents
- [Links to similar past incidents]

## Appendix
- [Links to relevant logs, dashboards, communications]
```

### 4.2 RCA Review Process

#### Review Workflow

```
Incident Resolved
       │
       ▼
Draft RCA (within 48h for P1/P2, 5 days for P3/P4)
       │
       ▼
Technical Peer Review (1-2 engineers not involved in incident)
       │
       ├── Feedback → Revise draft
       │
       ▼
Management Review (Engineering Manager + Product Owner)
       │
       ├── Additional actions identified → Add to action items
       │
       ▼
Blameless Post-Mortem Meeting (all stakeholders)
       │
       ├── Discussion → Refine root cause and actions
       │
       ▼
RCA Finalized and Published
       │
       ▼
Action Items Tracked to Completion (weekly review)
```

#### Review Criteria

| Criterion | Requirement |
|-----------|-------------|
| **Completeness** | All template sections filled; no "TBD" in final version |
| **Accuracy** | Timeline verified against system logs; no speculation |
| **Blameless** | Focuses on systems/processes, not individuals |
| **Actionable** | Every preventive action has clear owner, due date, and acceptance criteria |
| **Root Cause Depth** | 5-Whys reaches systemic cause (not just "human error") |
| **Detection Analysis** | Explains why existing monitoring didn't catch it earlier |
| **Reproducibility** | Someone unfamiliar could understand the failure from the RCA alone |

#### Meeting Protocol for Blameless Post-Mortem

1. **Facilitator** opens meeting; reminds team of blameless culture principles
2. **Incident Commander** presents timeline and immediate actions taken
3. **RCA Author** presents root cause analysis and 5-Whys
4. **Open Discussion** — team asks clarifying questions, suggests additional causes
5. **Action Review** — team reviews proposed corrective/preventive actions
6. **Priority Alignment** — agree on action priority relative to other work
7. **Closing** — facilitator summarizes decisions; publishes notes within 24h

### 4.3 Action Item Tracking

#### Action Item Lifecycle

| Status | Definition | Owner Responsibility |
|--------|-----------|---------------------|
| **Open** | Action identified and assigned | Acknowledge within 24h |
| **In Progress** | Work actively underway | Provide weekly status update |
| **In Review** | Implementation complete, pending verification | Demonstrate effectiveness |
| **Verified** | Confirmed effective in production | Provide evidence of prevention |
| **Closed** | Action complete and verified | No further action |
| **Deferred** | Intentionally delayed (with justification) | Provide new target date + rationale |
| **Cancelled** | No longer applicable (with justification) | Document reason for cancellation |

#### Weekly Action Review

- **When:** Every Monday 10:00 AM (local team time)
- **Attendees:** Engineering leads, SRE team, Product Owner
- **Agenda:**
  1. Review overdue actions (any past due date)
  2. Status update on P1/P2 incident actions
  3. Assess if deferred actions should be reactivated
  4. Review new incident patterns that may create additional actions
- **Output:** Updated action tracker; escalation of blocked items

#### Action Effectiveness Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Mean time to action completion (P1) | ≤ 14 days | Action open date → verified date |
| Mean time to action completion (P2) | ≤ 30 days | Action open date → verified date |
| Action completion rate | ≥ 90% within target | Completed on time / total actions |
| Repeat incident rate | ≤ 5% | Incidents with same root cause recurring |
| Action effectiveness | ≥ 80% | Actions that provably prevented recurrence |

---

## 5. Pattern Library

### 5.1 Pattern Catalog (40+ Patterns)

| Pattern ID | Class | Symptom | Root Cause | Detection Method | Corrective Action | Preventive Action | Affected Components | Historical Frequency |
|-----------|-------|---------|------------|------------------|-------------------|-------------------|--------------------|--------------------|
| PAT-001 | DQ | File validation rejects >50% of records | Source system schema change (new/removed columns) | Validation rejection rate alert (>5%) | Apply emergency schema override; reprocess | Source change notification SLA; adaptive parser | Parser Lambda, Validation Service | 4-6x / year |
| PAT-002 | DQ | Character encoding errors (garbled names) | Source sending Latin-1/Windows-1252 instead of UTF-8 | String validation failures on non-ASCII characters | Apply correct encoding transformation; reprocess | Auto-detect encoding per file; encoding validation gate | Parser Lambda, S3 Landing Zone | 2-3x / year |
| PAT-003 | DQ | Record count mismatch (header says 50K, file has 48K) | Source ETL job terminated prematurely producing truncated file | Header/trailer reconciliation check failure | Request retransmission from source | Implement checksum + record count validation before processing | Reconciliation Lambda | 3-4x / year |
| PAT-004 | DQ | Date fields with impossible values (13th month, 32nd day) | Source system data entry errors passed through without validation | FHIR date validation failures | Quarantine invalid records; process remainder | Source system data quality feedback loop; relaxed parsing with flagging | Validation Service, Mapping Engine | 8-12x / year |
| PAT-005 | DQ | Duplicate member IDs within single file | Source system merge/split event creating dual records | Deduplication stage duplicate count alert | Apply deduplication rules; process unique records | Implement pre-processing dedup with merge strategy; source system coordination | Dedup Lambda, Data Quality Service | 2-3x / year |
| PAT-006 | DQ | File arrives as 0 bytes | SFTP transfer failure; source system export error | File size check (0-byte detection) | Request retransmission; verify source system health | Implement minimum file size gate; source system transfer verification | S3 Landing Zone, Trigger Lambda | 6-8x / year |
| PAT-007 | DQ | Unexpected delimiter in field values (comma in address) | Source not properly quoting fields with delimiters | CSV parsing errors; field count mismatch | Switch to qualified (quoted) parsing mode | Implement robust CSV parser with configurable quoting; validate field counts | Parser Lambda | 4-5x / year |
| PAT-008 | DQ | Sudden 10x increase in file size | Source system change (full extract instead of delta) | File size anomaly detection (>3 std dev from mean) | Confirm intent with source; scale processing if legitimate | File size baseline with anomaly alerting; capacity auto-scaling | Pipeline Orchestrator, All downstream | 1-2x / year |
| PAT-009 | MAP | FHIR validation rejects resources — missing required extension | FHIR IG profile updated with new required element | Firely validation error rate increase | Add mapping for new required element; reprocess | IG version monitoring with impact assessment pipeline | Mapping Engine, Firely Validator | 2-3x / year |
| PAT-010 | MAP | Terminology code not found in ValueSet | New source codes not yet mapped in ConceptMap | $validate-code failures; unmapped code counter | Add code to ConceptMap; reprocess affected resources | Automated new-code detection and alerting; terminology refresh pipeline | Terminology Service, Mapping Engine | 6-10x / year |
| PAT-011 | MAP | Wrong SNOMED code assigned to procedures | ConceptMap equivalence relationship incorrect | Statistical anomaly in code distribution | Correct ConceptMap entry; identify and reprocess affected resources | Mapping peer review process; golden-file regression testing | Mapping Engine, ConceptMap | 1-2x / year |
| PAT-012 | MAP | Patient reference points to wrong resource | Reference resolution error in Bundle construction | Referential integrity check failures | Fix affected references; resubmit corrected Bundle | Implement reference validation pre-submission; reference registry | Bundle Builder, HealthLake | 2-4x / year |
| PAT-013 | MAP | UCUM unit validation failures on Observation quantities | Source units not mapped to UCUM standard | Firely UCUM validation errors | Add unit mapping; reprocess | Comprehensive unit mapping table with coverage monitoring | Mapping Engine, Firely Validator | 3-4x / year |
| PAT-014 | MAP | Resources failing US Core profile validation | Missing required US Core elements (race, ethnicity extensions) | Profile validation error count increase | Add missing element mappings with appropriate null-flavor handling | US Core compliance testing in CI/CD; complete element coverage matrix | Mapping Engine, Firely Validator | 4-6x / year |
| PAT-015 | MAP | Bundle transaction fails — circular references detected | Resource A references B and B references A within same Bundle | HealthLake Bundle rejection; circular reference error | Restructure Bundle ordering; break circular references | Implement dependency-sorted Bundle construction; reference cycle detection | Bundle Builder | 1-2x / year |
| PAT-016 | WFC | Step Function execution stuck in RUNNING >2 hours | Lambda timeout + no error handling catch block for TimeoutError | Execution duration alarm exceeds threshold | Terminate stuck execution; add catch block; re-execute | Add comprehensive catch blocks for all error types; execution time alarms | Step Functions, Lambda | 3-4x / year |
| PAT-017 | WFC | Pipeline produces 0 output with valid input | OutputPath/ResultPath dropping data between states | Zero-output detection alert | Fix state machine I/O configuration; re-execute | State machine I/O contract testing; zero-output alerting | Step Functions | 2-3x / year |
| PAT-018 | WFC | Wrong workflow branch executed (Choice state mismatch) | Choice state condition using wrong comparison operator or field | Unexpected execution path in audit trail | Correct Choice state conditions; re-execute affected workflows | Choice state unit testing; branch coverage monitoring | Step Functions | 1-2x / year |
| PAT-019 | WFC | Lambda OOM error on large files | Memory allocation too low for production data volumes | Lambda MemorySize exceeded error | Increase Lambda memory; implement streaming for large files | Adaptive memory allocation based on input size; load testing | Lambda Functions | 6-8x / year |
| PAT-020 | WFC | Glue job fails with executor memory error | Partition skew causing single executor to process disproportionate data | Glue job failure logs; Spark executor OOM | Repartition data; increase executor memory; optimize partitioning strategy | Implement adaptive partitioning; data skew detection and redistribution | Glue Jobs | 2-3x / year |
| PAT-021 | WFC | Pipeline steps executing in wrong order | Map state concurrency with dependencies between items | Dependency violation errors; inconsistent output | Add explicit ordering constraints; reprocess sequentially | Implement dependency-aware parallel execution; topological sort | Step Functions, Map State | 1-2x / year |
| PAT-022 | DEP | All Lambdas fail with ImportError after deployment | Missing dependency in Lambda layer or package | Lambda invocation errors spike post-deployment | Rollback to previous version; fix package | Import validation in CI/CD; deployment canary testing | Lambda Functions, Deployment Pipeline | 2-3x / year |
| PAT-023 | DEP | CloudFormation stack rollback leaves orphaned resources | Partial stack update failure without clean rollback | CloudFormation stack in ROLLBACK_COMPLETE state | Manual cleanup of orphaned resources; redeploy from clean state | Stack update dry-run validation; resource dependency mapping | CloudFormation, Infrastructure | 1-2x / year |
| PAT-024 | DEP | Environment variable mismatch (dev values in prod) | Deployment pipeline variable substitution failure | Wrong endpoint/configuration behavior in production | Correct environment variables; restart affected functions | Environment-specific validation checks; configuration drift detection | Lambda Functions, ECS Tasks | 3-4x / year |
| PAT-025 | DEP | Feature works in staging but fails in production | Environmental difference (VPC, IAM, encryption, endpoints) | Production-only errors not seen in lower environments | Identify environmental difference; apply production-specific fix | Environment parity enforcement; production-mirroring in staging | All Components | 4-6x / year |
| PAT-026 | AUTH | HealthLake writes fail with AccessDeniedException | KMS key policy not updated for new service role | CloudTrail AccessDenied events | Update KMS key policy with new role ARN | KMS policy validation in deployment checks; pre-deploy smoke tests | HealthLake, KMS, IAM | 2-3x / year |
| PAT-027 | AUTH | External API calls fail with 401 Unauthorized | OAuth token/API key expired or rotated | HTTP 401 response errors in logs | Refresh credential in Secrets Manager; restart service | Credential expiry monitoring; automated rotation | External Integrations, Secrets Manager | 4-6x / year |
| PAT-028 | AUTH | Lambda cannot reach external endpoint (timeout) | Security group or NACL blocking outbound traffic | Connection timeout errors; VPC flow log REJECT entries | Update security group rules to allow traffic | Network connectivity canary tests; infrastructure change review | VPC, Security Groups, Lambda | 2-3x / year |
| PAT-029 | AUTH | Cross-account access fails after infrastructure change | Trust policy not updated for new role/account | AssumeRole failures in CloudTrail | Update trust policy in target account | Cross-account permission audit; automated trust policy validation | IAM, STS, Cross-Account | 1-2x / year |
| PAT-030 | AUTH | TLS handshake failure to partner endpoint | Certificate expired or CA not in trust store | SSL/TLS connection errors | Update certificate or trust store | Certificate expiry monitoring (30/14/7 day alerts); automated renewal | Network, TLS, Certificates | 2-3x / year |
| PAT-031 | FHL | HealthLake throttling during peak processing | Write throughput exceeds provisioned capacity | ThrottlingException rate in CloudWatch | Implement rate limiting with backoff; stagger processing | Pipeline scheduling with load distribution; capacity planning model | HealthLake, Pipeline Scheduler | 4-6x / year |
| PAT-032 | FHL | Bundle transaction partial failure | Bundle exceeds size limits or contains conflicting operations | HealthLake Bundle rejection with OperationOutcome | Split Bundle into smaller transactions; resubmit | Adaptive Bundle sizing; transaction conflict pre-validation | Bundle Builder, HealthLake | 3-4x / year |
| PAT-033 | FHL | Search returns stale results after write | HealthLake eventual consistency (index lag) | Read-after-write returns outdated data | Add read-after-write delay; retry search | Consistency-aware read layer; polling until consistent | HealthLake, Search Operations | 2-4x / year |
| PAT-034 | FHL | Firely validator version mismatch with HealthLake | SDK upgrade introduces stricter validation not aligned with HealthLake support | Validation passes locally but HealthLake rejects (or vice versa) | Align Firely version with HealthLake capabilities | Version compatibility matrix; automated compatibility testing | Firely SDK, HealthLake | 1-2x / year |
| PAT-035 | FHL | Resource versioning conflict on concurrent updates | Multiple pipeline instances updating same resource simultaneously | HTTP 409 Conflict responses | Implement optimistic locking with retry; serialize conflicting updates | Distributed locking for resource-level operations; conflict detection | HealthLake, Pipeline Concurrency | 2-3x / year |
| PAT-036 | PERF | Pipeline exceeds SLA window due to volume growth | Data volume exceeds capacity planning without scaling | Pipeline duration metric exceeding SLA threshold | Scale up resources (Lambda memory, concurrency, Glue DPUs) | Adaptive auto-scaling; capacity planning with growth projections | All Pipeline Components | 4-6x / year |
| PAT-037 | PERF | Lambda cold starts causing cascading timeouts | High concurrency burst after idle period; no provisioned concurrency | Init duration spikes; timeout errors on first batch | Enable provisioned concurrency for critical functions | Provisioned concurrency for critical paths; warm-up invocations | Lambda Functions | 3-5x / year |
| PAT-038 | PERF | Glue job running 5x longer than normal | Data skew in partition key causing uneven distribution | Glue job duration alarm; Spark stage hanging | Repartition with better key; increase parallelism | Data distribution analysis; adaptive partitioning strategy | Glue Jobs | 2-3x / year |
| PAT-039 | PERF | API response latency p99 > 5 seconds | HealthLake search query scanning full resource set (missing index) | API latency alarm; CloudWatch metrics | Add search parameter index; optimize query | Regular query performance review; index coverage monitoring | API Gateway, HealthLake | 2-4x / year |
| PAT-040 | PERF | Memory pressure causing Lambda GC pauses | Large in-memory data structures; batch size too high for available memory | Memory utilization >90%; duration variance increase | Reduce batch size; increase memory; implement streaming | Right-size Lambdas; adaptive batch sizing; streaming architecture | Lambda Functions | 4-6x / year |
| PAT-041 | SEQ | Duplicate FHIR resources created | Missing idempotency on retry after partial failure | Duplicate count detection; unexpected resource count increase | Deduplicate (merge/delete); add idempotency keys | Conditional creates (If-None-Exist); intra-batch checkpointing | HealthLake, Lambda Functions | 4-6x / year |
| PAT-042 | SEQ | Reference integrity failure — resource references missing resource | Resource creation order violation (reference created before target) | Reference resolution errors; FHIR validation failures | Reprocess in correct order; create missing referenced resources | Dependency-sorted processing; reference existence validation | Bundle Builder, HealthLake | 3-4x / year |
| PAT-043 | SEQ | Pipeline processes file before dependency file arrives | S3 events arrive out of order; no dependency check | Processing errors referencing missing prerequisite data | Wait for dependency; reprocess after dependency arrives | File dependency graph; dependency satisfaction gate in orchestration | Pipeline Orchestrator, S3 Events | 2-3x / year |
| PAT-044 | SEQ | Stale data overwrites newer data | Race condition between concurrent pipeline executions | Data inconsistency; version mismatch in HealthLake | Restore correct version from history; implement ordering | Version-based conflict detection; last-writer-wins prevention | HealthLake, Concurrent Pipelines | 1-2x / year |
| PAT-045 | SEQ | Reprocessing causes duplicate downstream notifications | No idempotency on side effects (notifications, events) | Duplicate notifications reported by downstream consumers | Deduplicate notifications; implement idempotency markers | Exactly-once side effect delivery; outbox pattern | Event Publisher, Notification Service | 2-3x / year |

### 5.2 Pattern Relationships

```
Common Pattern Chains (one defect triggering another):

PAT-008 (DQ: 10x file size) → PAT-019 (WFC: Lambda OOM)
   ↓
PAT-036 (PERF: SLA breach)

PAT-001 (DQ: Schema change) → PAT-010 (MAP: Unmapped codes)
   ↓
PAT-014 (MAP: Profile validation failure)

PAT-022 (DEP: ImportError) → PAT-031 (FHL: Throttling on retry storm)
   ↓
PAT-041 (SEQ: Duplicates from retries)

PAT-027 (AUTH: Token expired) → PAT-043 (SEQ: Dependency not met)
   ↓
PAT-012 (MAP: Wrong references)
```

---

## 6. Monitoring & Early Detection

### 6.1 Key Metrics by Defect Class

#### DC-1: Data Quality Metrics

| Metric | CloudWatch Name | Normal Range | Warning Threshold | Critical Threshold |
|--------|----------------|--------------|--------------------|--------------------|
| Validation rejection rate | `dq/validation_rejection_rate` | 0-2% | >3% | >5% |
| File size deviation from baseline | `dq/file_size_deviation_pct` | ±20% | ±50% | ±80% |
| Record count anomaly | `dq/record_count_anomaly` | ±5% | ±15% | ±30% |
| Encoding error count | `dq/encoding_errors` | 0-5 per file | >20 | >100 |
| DLQ message depth | `dq/dlq_depth` | 0-100 | >500 | >2000 |
| Empty file arrivals (consecutive) | `dq/consecutive_empty_files` | 0 | 2 | 3 |

#### DC-2: Mapping Metrics

| Metric | CloudWatch Name | Normal Range | Warning Threshold | Critical Threshold |
|--------|----------------|--------------|--------------------|--------------------|
| FHIR validation failure rate | `map/validation_failure_rate` | 0-1% | >2% | >5% |
| Unmapped code count | `map/unmapped_codes` | 0-10 per run | >25 | >100 |
| ConceptMap age (days since update) | `map/conceptmap_age_days` | 0-7 | >14 | >30 |
| Profile conformance score | `map/profile_conformance_pct` | 98-100% | <97% | <95% |
| Reference resolution failures | `map/reference_resolution_failures` | 0-5 | >20 | >50 |
| Mapping coverage percentage | `map/mapping_coverage_pct` | 98-100% | <97% | <95% |

#### DC-3: Workflow Configuration Metrics

| Metric | CloudWatch Name | Normal Range | Warning Threshold | Critical Threshold |
|--------|----------------|--------------|--------------------|--------------------|
| Step Function failure rate | `wfc/execution_failure_rate` | 0-1% | >3% | >10% |
| Execution duration deviation | `wfc/duration_deviation_pct` | ±20% | ±50% | ±100% |
| Lambda timeout rate | `wfc/lambda_timeout_rate` | 0-0.5% | >1% | >5% |
| Stuck executions (>2h) | `wfc/stuck_execution_count` | 0 | 1 | 3 |
| Zero-output executions | `wfc/zero_output_executions` | 0 | 1 | 2 |
| Retry exhaustion rate | `wfc/retry_exhaustion_rate` | 0% | >1% | >5% |

#### DC-4: Deployment Metrics

| Metric | CloudWatch Name | Normal Range | Warning Threshold | Critical Threshold |
|--------|----------------|--------------|--------------------|--------------------|
| Post-deployment error rate | `dep/post_deploy_error_rate` | 0% | >1% | >5% |
| CloudFormation stack drift count | `dep/stack_drift_count` | 0 | 1 | 3 |
| Deployment rollback count | `dep/rollback_count` | 0 | 1 per week | 2 per week |
| Configuration drift items | `dep/config_drift_items` | 0 | 3 | 10 |
| Failed deployment count | `dep/failed_deployments` | 0 | 1 | 2 consecutive |

#### DC-5: Auth/Network Metrics

| Metric | CloudWatch Name | Normal Range | Warning Threshold | Critical Threshold |
|--------|----------------|--------------|--------------------|--------------------|
| AccessDenied event count | `auth/access_denied_count` | 0 | >5 in 10 min | >20 in 10 min |
| Certificate days to expiry | `auth/cert_days_to_expiry` | >30 | <30 | <7 |
| Connection timeout rate | `auth/connection_timeout_rate` | 0-0.1% | >1% | >5% |
| OAuth token refresh failures | `auth/token_refresh_failures` | 0 | 1 | 3 consecutive |
| VPC flow log REJECT count | `auth/vpc_reject_count` | 0-10/min | >50/min | >200/min |

#### DC-6: Firely/HealthLake Metrics

| Metric | CloudWatch Name | Normal Range | Warning Threshold | Critical Threshold |
|--------|----------------|--------------|--------------------|--------------------|
| HealthLake throttling rate | `fhl/throttling_rate` | 0-1% | >3% | >10% |
| HealthLake write latency p99 | `fhl/write_latency_p99` | <500ms | >1000ms | >3000ms |
| Bundle rejection rate | `fhl/bundle_rejection_rate` | 0-0.5% | >2% | >5% |
| HealthLake error rate (5xx) | `fhl/error_rate_5xx` | 0% | >1% | >5% |
| Search query latency p99 | `fhl/search_latency_p99` | <2000ms | >5000ms | >10000ms |
| Version conflict rate | `fhl/version_conflict_rate` | 0-0.1% | >1% | >5% |

#### DC-7: Performance Metrics

| Metric | CloudWatch Name | Normal Range | Warning Threshold | Critical Threshold |
|--------|----------------|--------------|--------------------|--------------------|
| Pipeline SLA adherence | `perf/sla_adherence_pct` | 100% | <99% | <95% |
| Lambda memory utilization | `perf/lambda_memory_pct` | 40-70% | >80% | >90% |
| Processing throughput (records/sec) | `perf/throughput_rps` | State-specific | <70% baseline | <50% baseline |
| Cold start percentage | `perf/cold_start_pct` | <5% | >10% | >25% |
| Queue processing lag | `perf/queue_lag_seconds` | <60s | >300s | >900s |
| Glue job duration deviation | `perf/glue_duration_deviation` | ±20% | ±50% | ±100% |

#### DC-8: Operational Sequencing Metrics

| Metric | CloudWatch Name | Normal Range | Warning Threshold | Critical Threshold |
|--------|----------------|--------------|--------------------|--------------------|
| Duplicate resource detection rate | `seq/duplicate_rate` | 0-0.1% | >0.5% | >1% |
| Out-of-order processing events | `seq/out_of_order_count` | 0 | >3 per day | >10 per day |
| Reference integrity violations | `seq/reference_integrity_failures` | 0 | >5 | >20 |
| Concurrent execution conflicts | `seq/concurrency_conflicts` | 0 | >3 | >10 |
| Idempotency key collisions | `seq/idempotency_collisions` | 0-1% | >3% | >5% |
| Checkpoint staleness (seconds) | `seq/checkpoint_staleness_sec` | <300 | >600 | >1800 |

### 6.2 Alert Configuration

#### Alert Priority Matrix

| Alert Level | Notification Channel | Response Expected | Auto-Escalation |
|-------------|---------------------|-------------------|-----------------|
| **CRITICAL** | PagerDuty + Slack #incidents + Email | Immediate (acknowledge in 5 min) | Manager notified at 15 min if unacknowledged |
| **WARNING** | Slack #platform-alerts + Email | Within 30 minutes | Escalate to CRITICAL if persists >1 hour |
| **INFO** | Slack #platform-monitoring | Next business day review | No escalation |

#### Composite Alert Examples

```yaml
# Example: Data Quality Composite Alert
alert_name: "DQ_Pipeline_Health_Degraded"
condition: >
  (dq/validation_rejection_rate > 5% for 5 minutes) OR
  (dq/dlq_depth > 2000 for 3 minutes) OR
  (dq/file_size_deviation_pct > 80% AND dq/record_count_anomaly > 30%)
severity: CRITICAL
runbook: "https://wiki.internal/runbooks/dq-pipeline-degraded"
notification:
  - channel: pagerduty
    service: onyx-platform-oncall
  - channel: slack
    target: "#incidents"
    message: "🚨 P1 Data Quality Alert: {condition_detail}"

# Example: Performance SLA Warning
alert_name: "PERF_SLA_At_Risk"
condition: >
  (perf/pipeline_duration_current > 0.7 * perf/sla_window_remaining) AND
  (perf/processing_progress_pct < 60%)
severity: WARNING
runbook: "https://wiki.internal/runbooks/sla-risk-mitigation"
notification:
  - channel: slack
    target: "#platform-alerts"
    message: "⚠️ SLA at risk for {state_id}: {progress}% complete with {time_remaining} remaining"
```

### 6.3 Dashboard Recommendations

#### Dashboard 1: Platform Health Overview

| Panel | Visualization | Data Source | Refresh |
|-------|--------------|-------------|---------|
| Pipeline Status (all states) | Status grid (green/yellow/red) | Step Functions API | 1 min |
| Active incidents | Count + severity breakdown | Incident tracker | 1 min |
| 24h error rate trend | Line chart | CloudWatch Logs Insights | 5 min |
| SLA adherence (today) | Gauge per state | Custom metric | 5 min |
| HealthLake throughput | Area chart (reads/writes) | HealthLake CloudWatch | 1 min |
| DLQ depth (all queues) | Bar chart | SQS CloudWatch | 1 min |

#### Dashboard 2: Per-State Pipeline Detail

| Panel | Visualization | Data Source | Refresh |
|-------|--------------|-------------|---------|
| Today's processing timeline | Gantt chart (step durations) | Step Functions history | 5 min |
| Record counts (expected vs actual) | Bar comparison | Custom metric | 5 min |
| Validation pass/fail ratio | Pie chart | Validation service metrics | 5 min |
| Error breakdown by type | Stacked bar | CloudWatch Logs Insights | 5 min |
| Historical trend (7-day) | Sparkline | Custom metrics | 15 min |
| Resource creation rate | Line chart | HealthLake metrics | 1 min |

#### Dashboard 3: Infrastructure & Performance

| Panel | Visualization | Data Source | Refresh |
|-------|--------------|-------------|---------|
| Lambda concurrency (all functions) | Stacked area | Lambda CloudWatch | 1 min |
| Lambda memory utilization heatmap | Heatmap | Custom metric | 5 min |
| HealthLake latency percentiles | Line (p50, p90, p99) | HealthLake CloudWatch | 1 min |
| Throttling events | Bar chart by service | CloudWatch | 1 min |
| VPC network throughput | Area chart | VPC flow logs | 5 min |
| Cost burn rate (today) | Gauge vs budget | Cost Explorer API | 1 hour |

#### Dashboard 4: Data Quality Intelligence

| Panel | Visualization | Data Source | Refresh |
|-------|--------------|-------------|---------|
| Validation rejection trend (30-day) | Line per state | Custom metric | 15 min |
| Top 10 validation errors today | Table (count, error, state) | Validation logs | 5 min |
| Unmapped code tracker | Table with trending | Terminology service | 15 min |
| File arrival timing | Timeline vs expected window | S3 events | 5 min |
| DLQ message age distribution | Histogram | SQS metrics | 5 min |
| Data quality score by state | Scorecard | Composite metric | 15 min |

### 6.4 Proactive Health Checks

#### Scheduled Health Checks

| Check | Frequency | What It Validates | Alert If Failed |
|-------|-----------|-------------------|-----------------|
| End-to-end canary (synthetic record) | Every 15 min | Full pipeline path from S3 to HealthLake | WARNING after 1 failure; CRITICAL after 3 |
| HealthLake read/write test | Every 5 min | FHIR CRUD operations functional | CRITICAL immediately |
| Terminology service availability | Every 5 min | $lookup operation on known code | WARNING after 2 failures |
| Certificate expiry scan | Daily at 06:00 UTC | All certificates >7 days from expiry | WARNING at 30 days; CRITICAL at 7 days |
| Cross-account connectivity | Every 30 min | AssumeRole + S3 access to all partner accounts | CRITICAL immediately |
| Mapping coverage check | Daily at 07:00 UTC | All ConceptMaps cover >97% of recent source values | WARNING below 97% |
| Pipeline schedule verification | Every 6 hours | All EventBridge rules active and correctly configured | CRITICAL if rule disabled |
| DLQ drain rate | Every 15 min | DLQ messages being consumed (not growing unbounded) | WARNING if growing >100/hour |
| Capacity headroom | Daily at 00:00 UTC | All services have >30% headroom vs peak | WARNING if <30% |
| Configuration drift scan | Daily at 05:00 UTC | Infrastructure matches IaC definitions | WARNING if drift detected |

#### Pre-Processing Readiness Checks (Run Before Each Pipeline)

```python
# Pseudo-code for pre-processing health check
def pre_processing_health_check(state_id, file_key):
    checks = [
        check_file_integrity(file_key),          # File exists, >0 bytes, valid checksum
        check_healthlake_available(),            # HealthLake responding to reads
        check_terminology_service(),             # Terminology service lookup works
        check_lambda_cold_start_pool(),          # Critical Lambdas warm
        check_concurrent_execution_capacity(),    # Not at concurrency limit
        check_prerequisite_files_processed(),     # Dependency files already done
        check_target_account_accessible(),       # Cross-account access works
    ]
    
    failures = [c for c in checks if not c.passed]
    if failures:
        if any(c.severity == 'CRITICAL' for c in failures):
            abort_pipeline(state_id, failures)
        else:
            proceed_with_warnings(state_id, failures)
    else:
        proceed_normally(state_id)
```

---

## 7. Escalation Matrix

### 7.1 Escalation by Class and Severity

| Defect Class | P4 | P3 | P2 | P1 |
|-------------|-----|-----|-----|-----|
| **Data Quality** | Team Slack channel; next sprint | On-call engineer; same-day fix | On-call + Engineering lead; 8h resolution | War room; all hands; immediate |
| **Mapping** | Mapping team backlog | Mapping team lead; same-day | On-call + Mapping lead + Clinical SME; 8h | War room + Clinical leadership |
| **Workflow Config** | Platform team backlog | On-call engineer; same-day | On-call + Platform lead; 4h resolution | War room; all hands |
| **Deployment** | DevOps team backlog | On-call + DevOps; rollback if needed | On-call + DevOps lead; immediate rollback | War room; immediate rollback; all deployments halted |
| **Auth/Network** | Security team ticket | On-call + Security; same-day | On-call + Security lead + Infra; 4h | War room + Security + AWS support |
| **Firely/HealthLake** | Platform team backlog | On-call + FHIR SME; same-day | On-call + FHIR lead + AWS support; 8h | War room + AWS Premium Support |
| **Performance** | Performance backlog | On-call; scale resources | On-call + Platform lead; scale + optimize | War room; emergency scaling; traffic shedding |
| **Operational Sequencing** | Platform team backlog | On-call; manual intervention | On-call + Platform lead; halt processing | War room; halt all pipelines; assess data integrity |

### 7.2 Escalation Timing

```
T+0 min:   Alert fires → On-call engineer paged
T+5 min:   If unacknowledged → Secondary on-call paged
T+15 min:  If P1 unacknowledged → Engineering Manager paged
T+30 min:  P1 war room opens (if not already)
T+60 min:  If unresolved P1 → VP Engineering notified
T+120 min: If unresolved P1 → Executive briefing initiated
T+240 min: If unresolved P1 → Customer communication sent
```

### 7.3 Communication Templates

#### P1 Initial Notification (Slack + Email)

```
🚨 P1 INCIDENT DECLARED

Incident: INC-{YYYY}-{NNNN}
Title: {Brief description}
Severity: P1 — {Impact category}
Detected: {timestamp} UTC
Affected: {states/systems affected}
Impact: {Brief impact description}
Status: INVESTIGATING

Incident Commander: {Name}
War Room: {Slack channel / Zoom link}

Next update: {timestamp + 30 min} UTC
```

#### P1 Status Update (Every 30 Minutes)

```
📊 P1 STATUS UPDATE — {HH:MM} UTC

Incident: INC-{YYYY}-{NNNN}
Title: {Brief description}
Duration: {time since detection}
Status: {INVESTIGATING | IDENTIFIED | MITIGATING | RESOLVED}

Current Understanding:
{2-3 sentences on current root cause hypothesis}

Actions in Progress:
• {Action 1 — Owner — ETA}
• {Action 2 — Owner — ETA}

Impact Update:
• Records affected: {count}
• States affected: {list}
• SLA impact: {description}

Next update: {timestamp + 30 min} UTC
```

#### P1 Resolution Notification

```
✅ P1 INCIDENT RESOLVED

Incident: INC-{YYYY}-{NNNN}
Title: {Brief description}
Duration: {total incident duration}
Resolution: {Brief description of fix applied}

Impact Summary:
• Records affected: {count}
• States affected: {list}
• SLA impact: {description}
• Data recovery status: {Complete/In progress/Pending}

Next Steps:
• RCA to be completed by: {date}
• Post-mortem meeting: {date/time}
• Affected data fully recovered by: {ETA}

Thank you to all responders. No further updates unless new developments.
```

#### P2 Stakeholder Notification

```
⚠️ P2 INCIDENT — Stakeholder Update

Incident: INC-{YYYY}-{NNNN}
Title: {Brief description}
Severity: P2
Detected: {timestamp} UTC
Affected: {states/systems}

What's happening:
{2-3 sentences in non-technical language}

What we're doing:
{2-3 sentences describing response}

Expected resolution: {ETA}
Impact to your workflow: {description for this stakeholder}

Contact: {Incident Commander} if questions
Next update: {When to expect next update}
```

#### Customer/Partner Communication (External)

```
Subject: [Onyx Platform] Service Advisory — {Brief Description}

Dear {Partner Name},

We are currently experiencing {non-technical description of impact}.

Impact to You:
• {Specific impact description relevant to this partner}
• Expected duration: {ETA for resolution}
• Data affected: {Period/scope}

What We're Doing:
Our engineering team is actively working to resolve this issue.
We will provide an update by {time} or sooner if resolved.

No action is needed from you at this time.
{OR: Please take the following action: {specific action needed}}

We apologize for any inconvenience and appreciate your patience.

Best regards,
{Name}
Onyx Platform Operations
{Contact information}
```

### 7.4 War Room Procedures

#### War Room Activation Criteria

A war room is activated for:
- Any P1 incident
- Any P2 incident lasting >2 hours without resolution
- Any incident affecting 3+ states simultaneously
- Any incident with confirmed data loss or corruption
- Engineering Manager or VP discretion

#### War Room Roles

| Role | Responsibility | Required For |
|------|---------------|--------------|
| **Incident Commander (IC)** | Overall coordination; decision authority; communication | All war rooms |
| **Technical Lead** | Drives technical investigation; proposes solutions | All war rooms |
| **Communications Lead** | Stakeholder updates; customer communication | All P1; P2 with customer impact |
| **Scribe** | Records timeline, decisions, actions in real-time | All war rooms |
| **Subject Matter Expert(s)** | Domain expertise (FHIR, infrastructure, data, etc.) | As needed by defect class |
| **Operations Lead** | Monitors system health; validates fixes in production | All war rooms |
| **Executive Liaison** | Keeps leadership informed; authorizes exceptional actions | P1 lasting >1 hour |

#### War Room Playbook

```
PHASE 1: ASSEMBLE (T+0 to T+10 min)
├── IC opens war room channel/call
├── IC assigns roles (Technical Lead, Comms, Scribe)
├── Scribe begins real-time timeline documentation
├── IC states known facts and current hypothesis
└── Technical Lead assigns initial investigation tasks

PHASE 2: INVESTIGATE (T+10 to T+N)
├── Technical Lead coordinates parallel investigation tracks
├── IC provides status update every 30 minutes
├── Communications Lead sends initial stakeholder notification
├── Team shares findings in war room channel
├── IC decides on mitigation vs. root cause fix approach
└── If >1 hour: Executive Liaison provides leadership briefing

PHASE 3: MITIGATE (Once root cause identified)
├── Technical Lead proposes fix options with risk assessment
├── IC decides on approach (immediate fix vs. rollback vs. workaround)
├── Operations Lead validates fix in pre-production (if time allows)
├── Fix deployed to production
├── Operations Lead monitors for recovery
└── Communications Lead sends "mitigating" status update

PHASE 4: VERIFY & CLOSE (Once fix deployed)
├── Operations Lead confirms metrics returning to normal
├── Technical Lead verifies no secondary failures
├── Backlog processing initiated (if data queued)
├── IC confirms incident resolved
├── Communications Lead sends resolution notification
├── IC assigns RCA owner and due date
└── War room stood down

POST-WAR ROOM:
├── Scribe publishes final timeline within 2 hours
├── RCA draft due within 48 hours (P1) / 5 days (P2)
├── Post-mortem meeting scheduled within 1 week
└── Action items tracked to completion
```

#### War Room Anti-Patterns (Avoid These)

| Anti-Pattern | Why It's Harmful | What To Do Instead |
|-------------|------------------|-------------------|
| Too many people in the room | Noise overwhelms signal; decisions slow | IC limits active participants; observers in separate channel |
| No clear IC | Duplicate efforts; conflicting decisions | Always designate IC first; IC wears the hat visibly |
| Deploying fixes without validation | May worsen the situation | Always validate in lower environment or with limited blast radius |
| Blaming individuals | Shuts down information sharing | Explicitly remind team of blameless culture at start |
| Not documenting in real-time | RCA will be inaccurate; learnings lost | Scribe records everything; timestamp all decisions |
| Scope creep (fixing other issues) | Delays resolution of the primary incident | IC keeps focus; park other issues for later |

---

## Appendix A: Quick Reference Card

### Incident Response Cheat Sheet

```
1. DETECT: Alert fires or anomaly observed
2. ASSESS: Determine severity (P1-P4) using decision tree
3. CLASSIFY: Assign defect class (DQ/MAP/WFC/DEP/AUTH/FHL/PERF/SEQ)
4. RESPOND: Follow escalation matrix for severity + class
5. COMMUNICATE: Send initial notification per templates
6. INVESTIGATE: Follow diagnostic steps for the defect class
7. MITIGATE: Apply corrective fix (immediate)
8. VERIFY: Confirm resolution; monitor for recurrence
9. DOCUMENT: Complete RCA within SLA (48h P1, 5d P3/P4)
10. PREVENT: Implement preventive actions; track to completion
```

### Common First-Response Actions by Class

| Class | First Thing To Check | First Thing To Do |
|-------|---------------------|-------------------|
| DQ | Source file structure vs last known good | Quarantine file; check if partial processing is safe |
| MAP | Validation OperationOutcome details | Check ConceptMap freshness; compare to recent success |
| WFC | Step Functions execution history + I/O | Check for recent deployments; inspect state transitions |
| DEP | Deployment timeline (last 24h) | Prepare rollback; compare to previous version |
| AUTH | CloudTrail for AccessDenied events | Verify credentials and certificates; check IAM changes |
| FHL | HealthLake CloudWatch metrics | Check for throttling; verify service health |
| PERF | Compare current metrics to 7-day baseline | Scale resources; reduce load; check data volume |
| SEQ | Timeline of events; concurrent executions | Halt processing to prevent further damage; check for duplicates |

---

## Appendix B: Glossary

| Term | Definition |
|------|-----------|
| **ASL** | Amazon States Language — JSON-based language for Step Functions |
| **ConceptMap** | FHIR resource mapping codes between terminology systems |
| **DLQ** | Dead Letter Queue — holds messages that failed processing |
| **DPU** | Data Processing Unit — Glue job capacity unit |
| **Firely** | .NET FHIR SDK used for validation and resource manipulation |
| **HealthLake** | AWS managed FHIR datastore |
| **IC** | Incident Commander — person coordinating incident response |
| **Idempotency** | Property ensuring repeated operations produce the same result |
| **OperationOutcome** | FHIR resource communicating processing errors |
| **RCA** | Root Cause Analysis |
| **SLA** | Service Level Agreement — committed performance target |
| **StructureMap** | FHIR resource defining data transformation rules |
| **UCUM** | Unified Code for Units of Measure |
| **ValueSet** | FHIR resource defining a set of allowed coded values |

---

## Appendix C: Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-07-07 | Platform Reliability Engineering | Initial creation |

---

*This document is a living artifact. Update the pattern library as new incidents occur. Review and refresh quarterly or after any P1 incident.*
