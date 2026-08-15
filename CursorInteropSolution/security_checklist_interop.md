# Security Checklist for Interop Deployments and Changes

## Artifact #10 — Onyx Interoperability Platform

| Field | Value |
|-------|-------|
| **Document ID** | ONYX-SEC-010 |
| **Version** | 1.0 |
| **Classification** | Internal — Restricted |
| **Owner** | Security & Compliance Team |
| **Last Updated** | 2026-07-07 |
| **Review Cadence** | Quarterly or on major change |
| **Applies To** | All Onyx interop deployments, infrastructure changes, and application releases |

---

## Table of Contents

1. [IAM & Access Control](#1-iam--access-control)
2. [Secret Management](#2-secret-management)
3. [Network Security](#3-network-security)
4. [Authentication & Authorization (CMS)](#4-authentication--authorization-cms)
5. [Data Security](#5-data-security)
6. [Operational Security](#6-operational-security)
7. [Compliance & Audit](#7-compliance--audit)
8. [Pre-Change Security Review Checklist](#8-pre-change-security-review-checklist)
9. [Security Incident Response](#9-security-incident-response)

---

## 1. IAM & Access Control

### 1.1 IAM Roles vs. Static Keys

| Requirement | Priority | Details |
|-------------|----------|---------|
| Use IAM Roles exclusively for service workloads | **CRITICAL** | No static AWS access keys in application code, configs, or environment variables |
| EC2/ECS/Lambda must use instance profiles or execution roles | **CRITICAL** | Attach roles via instance metadata service (IMDSv2 required) |
| Databricks clusters must use instance profiles | **HIGH** | Map workspace-level permissions to IAM roles via instance profiles |
| Eliminate all long-lived access keys | **HIGH** | Audit with `aws iam generate-credential-report`; rotate any remaining keys ≤ 90 days |
| Enforce IMDSv2 (token-required) on all EC2 instances | **HIGH** | Block IMDSv1 to prevent SSRF-based credential theft |

### 1.2 Least Privilege

| Requirement | Priority | Details |
|-------------|----------|---------|
| Scope IAM policies to specific resources (ARNs) | **CRITICAL** | Never use `Resource: "*"` except for actions that require it |
| Use condition keys to restrict access context | **HIGH** | `aws:SourceVpc`, `aws:SourceIp`, `aws:RequestedRegion`, `aws:PrincipalOrgID` |
| Deny wildcards in action statements | **HIGH** | No `Action: "s3:*"` or `Action: "*"` in production policies |
| Review IAM Access Analyzer findings weekly | **MEDIUM** | Remediate public/cross-account access findings within SLA |
| Use `NotAction` / `NotResource` sparingly and document | **MEDIUM** | These are error-prone; prefer explicit allow lists |

### 1.3 Service Accounts

| Requirement | Priority | Details |
|-------------|----------|---------|
| Dedicated service accounts per microservice | **CRITICAL** | No shared "onyx-service" accounts across components |
| Service account naming convention: `svc-onyx-<component>-<env>` | **HIGH** | e.g., `svc-onyx-fhir-ingest-prod` |
| Disable console access for service accounts | **HIGH** | Service accounts must not have passwords or MFA devices |
| Tag service accounts with owner, team, purpose | **MEDIUM** | Enable automated governance and orphan detection |
| Review service account permissions quarterly | **MEDIUM** | Use IAM Access Advisor last-accessed data |

### 1.4 Cross-Account Access

| Requirement | Priority | Details |
|-------------|----------|---------|
| Use AWS Organizations SCPs to enforce boundaries | **CRITICAL** | Deny actions outside approved regions, deny root usage |
| Cross-account roles require `ExternalId` condition | **HIGH** | Prevent confused deputy attacks |
| Limit cross-account trust to specific account IDs | **HIGH** | Never use `Principal: "*"` in trust policies |
| Document all cross-account access in architecture registry | **MEDIUM** | Maintain a matrix of account-to-account trust relationships |
| Use AWS RAM for resource sharing where possible | **MEDIUM** | Preferred over cross-account role assumptions for shared resources |

### 1.5 Permission Boundaries

| Requirement | Priority | Details |
|-------------|----------|---------|
| Apply permission boundaries to all developer-created roles | **CRITICAL** | Prevent privilege escalation beyond boundary |
| Boundary policy denies: IAM policy modification, boundary removal, org-level actions | **HIGH** | Developers cannot grant themselves more permissions |
| Separate boundaries per environment (dev/staging/prod) | **HIGH** | Prod boundary is strictly tighter than dev |
| Permission boundary ARN: `arn:aws:iam::<account>:policy/onyx-boundary-<env>` | **MEDIUM** | Standardized naming for automation |

---

## 2. Secret Management

### 2.1 Databricks Secret Scopes

| Requirement | Priority | Details |
|-------------|----------|---------|
| Use Azure Key Vault-backed or AWS-backed scopes (not Databricks-managed) | **CRITICAL** | External backing enables unified rotation and auditing |
| Scope naming: `onyx-<env>-<category>` | **HIGH** | e.g., `onyx-prod-fhir-credentials`, `onyx-prod-db-passwords` |
| Restrict scope ACLs to specific principals | **HIGH** | `MANAGE` permission only for automation service principals |
| Redact secrets in notebook outputs | **HIGH** | Databricks redacts by default; verify with `dbutils.secrets.get()` display behavior |
| Audit secret access via Databricks audit logs | **MEDIUM** | Forward to SIEM; alert on unexpected access patterns |

### 2.2 AWS Secrets Manager

| Requirement | Priority | Details |
|-------------|----------|---------|
| Store all database credentials, API keys, certificates in Secrets Manager | **CRITICAL** | No secrets in SSM Parameter Store standard parameters, env vars, or code |
| Enable automatic rotation (Lambda-based) | **CRITICAL** | Rotation interval ≤ 90 days for passwords, ≤ 365 days for API keys |
| Resource policy restricts access to specific IAM roles | **HIGH** | Deny cross-account access unless explicitly required |
| Enable `SecretVersionStagesChangedAt` monitoring | **HIGH** | Alert if rotation fails |
| Use separate secrets per environment | **HIGH** | Never reference prod secrets from non-prod accounts |
| Tag secrets: `onyx:environment`, `onyx:owner`, `onyx:rotation-schedule` | **MEDIUM** | Governance and compliance tracking |

### 2.3 SSM Parameter Store SecureString

| Requirement | Priority | Details |
|-------------|----------|---------|
| Use SecureString type for any sensitive configuration | **CRITICAL** | Encrypted with KMS; never use `String` type for sensitive data |
| Use customer-managed KMS keys (not `aws/ssm`) | **HIGH** | Enables key rotation control and cross-account access management |
| Parameter path hierarchy: `/onyx/<env>/<service>/<param>` | **HIGH** | Enables IAM path-based access control |
| Restrict `ssm:GetParameter*` to specific paths per role | **HIGH** | Prevent lateral access to other services' parameters |

### 2.4 Rotation & Revocation

| Requirement | Priority | Details |
|-------------|----------|---------|
| Automated rotation for all machine credentials | **CRITICAL** | No manual rotation processes in production |
| Rotation must be zero-downtime (multi-user/staged) | **HIGH** | Use Secrets Manager's staging labels (`AWSCURRENT`/`AWSPENDING`) |
| Emergency revocation procedure documented and tested | **HIGH** | Must be executable in < 15 minutes |
| Revocation triggers: employee departure, suspected compromise, failed rotation | **HIGH** | Automated alerts drive revocation workflows |
| Post-revocation validation: confirm access denied | **MEDIUM** | Automated test after revocation confirms lockout |

### 2.5 Secret Auditing

| Requirement | Priority | Details |
|-------------|----------|---------|
| All secret access logged to CloudTrail | **CRITICAL** | `GetSecretValue`, `GetParameter` events captured |
| Alert on secret access from unexpected roles/IPs | **HIGH** | SIEM correlation rule |
| Weekly report: secrets approaching rotation deadline | **MEDIUM** | Proactive rotation compliance |
| Quarterly: scan all repos/artifacts for hardcoded secrets | **MEDIUM** | Use tools like `trufflehog`, `gitleaks`, or AWS CodeGuru |

---

## 3. Network Security

### 3.1 WAF for FHIR APIs

| Requirement | Priority | Details |
|-------------|----------|---------|
| AWS WAF deployed on all FHIR API Gateway/ALB endpoints | **CRITICAL** | Protects Patient Access, Provider Directory, and Payer-to-Payer APIs |
| Rate limiting rules: per-IP and per-token | **CRITICAL** | Prevent abuse; align with CMS rate limit guidance |
| OWASP Core Rule Set (CRS) enabled | **HIGH** | SQL injection, XSS, path traversal, protocol attacks |
| Custom rules for FHIR-specific attacks | **HIGH** | Block malformed FHIR bundles, oversized `_include` chains, recursive `_revinclude` |
| Bot control: block known-bad user agents | **MEDIUM** | AWS WAF Bot Control managed rule group |
| Geo-restriction: US-only for CMS APIs (unless international payers) | **MEDIUM** | Configurable per API endpoint |
| WAF logging to S3/CloudWatch with 90-day retention | **HIGH** | Required for incident investigation |
| Monthly WAF rule review and tuning | **MEDIUM** | Reduce false positives; update for new attack patterns |

### 3.2 VPC Isolation

| Requirement | Priority | Details |
|-------------|----------|---------|
| Separate VPCs per environment (dev/staging/prod) | **CRITICAL** | No cross-environment network paths |
| FHIR API tier in public subnet (with WAF/ALB only) | **HIGH** | Compute in private subnets |
| Data tier (RDS, DynamoDB, S3) in isolated private subnets | **CRITICAL** | No internet gateway route |
| Databricks workspace VPC with no public subnets | **HIGH** | Use VPC peering/PrivateLink for data access |
| No default VPC usage | **HIGH** | Delete default VPCs in all regions |
| VPC Flow Logs enabled (ALL traffic) | **CRITICAL** | Sent to CloudWatch Logs + S3 for long-term retention |

### 3.3 Security Groups & NACLs

| Requirement | Priority | Details |
|-------------|----------|---------|
| Security groups: deny-all default, explicit allow only | **CRITICAL** | No `0.0.0.0/0` inbound rules except ALB port 443 |
| Reference security groups by ID (not CIDR) where possible | **HIGH** | Enables dynamic scaling without rule updates |
| FHIR API SG: allow 443 inbound from WAF/ALB SG only | **HIGH** | Compute nodes not directly internet-accessible |
| Database SG: allow inbound only from application tier SG | **CRITICAL** | Port 5432 (Postgres) or 3306 (MySQL) restricted |
| NACLs: stateless backup layer with explicit deny rules | **MEDIUM** | Block known malicious CIDR ranges at subnet level |
| Quarterly review: remove unused/stale security group rules | **MEDIUM** | Automated reporting via AWS Config |

### 3.4 AWS PrivateLink

| Requirement | Priority | Details |
|-------------|----------|---------|
| PrivateLink for all AWS service access (S3, Secrets Manager, KMS, STS) | **HIGH** | Traffic stays on AWS backbone; no internet traversal |
| PrivateLink for Databricks workspace connectivity | **HIGH** | Backend and front-end PrivateLink endpoints |
| Interface endpoints have restrictive security groups | **HIGH** | Only application-tier SGs can reach VPC endpoints |
| VPC endpoint policies restrict accessible resources | **MEDIUM** | e.g., S3 endpoint policy limits to specific buckets |
| Gateway endpoints for S3 and DynamoDB (cost-effective) | **MEDIUM** | Route table-based; no additional SG needed |

### 3.5 TLS & mTLS

| Requirement | Priority | Details |
|-------------|----------|---------|
| TLS 1.2+ enforced on all endpoints (no TLS 1.0/1.1) | **CRITICAL** | ALB security policy: `ELBSecurityPolicy-TLS13-1-2-2021-06` or newer |
| Certificates from AWS ACM (auto-renewal) | **HIGH** | No self-signed certificates in production |
| mTLS for payer-to-payer FHIR connections | **CRITICAL** | Mutual authentication per CMS trusted exchange requirements |
| mTLS for internal service-to-service communication | **HIGH** | Service mesh (App Mesh/Istio) or API Gateway mutual TLS |
| Certificate pinning for critical integrations | **MEDIUM** | Pin CA or leaf certificate for payer endpoints |
| HSTS headers on all FHIR API responses | **HIGH** | `Strict-Transport-Security: max-age=31536000; includeSubDomains` |

### 3.6 Egress Control

| Requirement | Priority | Details |
|-------------|----------|---------|
| NAT Gateway for controlled internet egress | **HIGH** | Single egress point for monitoring |
| Egress-only security groups: restrict outbound to known destinations | **HIGH** | Whitelist payer endpoints, CMS endpoints, package registries |
| AWS Network Firewall or proxy for egress filtering | **MEDIUM** | Domain-based filtering for outbound HTTPS |
| Block all egress from data-tier subnets | **CRITICAL** | Database instances must never reach the internet |
| Log all egress traffic via VPC Flow Logs | **HIGH** | Detect data exfiltration attempts |

---

## 4. Authentication & Authorization (CMS)

### 4.1 SMART on FHIR Security

| Requirement | Priority | Details |
|-------------|----------|---------|
| SMART App Launch Framework v2.0 compliance | **CRITICAL** | Support EHR Launch and Standalone Launch sequences |
| PKCE (Proof Key for Code Exchange) required for all public clients | **CRITICAL** | `code_challenge_method: S256` enforced |
| Validate `aud` parameter matches FHIR server URL | **HIGH** | Prevent token confusion attacks |
| Enforce `launch` context restrictions | **HIGH** | Apps only access data within launch context (patient/encounter) |
| App registration review: verify redirect URIs, scopes requested | **HIGH** | No wildcard redirect URIs; exact match only |
| Capability Statement (`/metadata`) must declare security extensions | **MEDIUM** | `security.service` coding for OAuth2 endpoints |
| Support SMART Scopes v2: granular resource-level permissions | **HIGH** | `patient/Condition.read` not `patient/*.read` where possible |

### 4.2 OAuth2 Token Security

| Requirement | Priority | Details |
|-------------|----------|---------|
| Access token lifetime ≤ 15 minutes | **CRITICAL** | Short-lived tokens limit blast radius |
| Refresh token lifetime ≤ 24 hours (patient-facing), ≤ 1 hour (backend) | **HIGH** | Configurable per client type |
| Token introspection endpoint for resource servers | **HIGH** | Real-time token validation; support revocation |
| Refresh token rotation on every use | **HIGH** | Detect token replay/theft |
| Store tokens server-side (not in browser localStorage) | **CRITICAL** | Use secure, HttpOnly, SameSite cookies for session binding |
| Token binding to client identity (DPoP or mTLS) | **MEDIUM** | Prevent token theft/replay |
| Revoke all tokens on password change/account compromise | **HIGH** | Immediate invalidation across all sessions |

### 4.3 Scope Enforcement

| Requirement | Priority | Details |
|-------------|----------|---------|
| Resource server validates scopes on every request | **CRITICAL** | Authorization middleware checks token scopes vs. requested resource |
| Deny by default: no scope = no access | **CRITICAL** | Missing scope claim results in 403 |
| Clinical scopes: `patient/`, `user/`, `system/` prefixes enforced | **HIGH** | Patient-context tokens cannot access system-level resources |
| Write scopes (`*.write`, `*.create`) require additional approval | **HIGH** | Elevated review for apps requesting write access |
| Scope downscoping at token exchange | **MEDIUM** | Backend services request minimum necessary scopes per operation |
| Log all scope enforcement decisions (allow/deny) | **HIGH** | Audit trail for access decisions |

### 4.4 Consent Management

| Requirement | Priority | Details |
|-------------|----------|---------|
| Patient consent tracked as FHIR `Consent` resources | **HIGH** | Machine-readable consent records |
| Consent enforcement at data access layer | **CRITICAL** | Queries filtered by active consent policies |
| Support opt-in and opt-out consent models | **HIGH** | Configurable per payer/program requirements |
| Consent revocation effective within 1 hour | **HIGH** | Near-real-time propagation to all access points |
| Consent audit: log all consent grants, revocations, and access decisions | **HIGH** | HIPAA requirement |
| Sensitive data categories require explicit consent | **CRITICAL** | 42 CFR Part 2 (substance abuse), mental health, HIV/AIDS |

### 4.5 $member-match Security

| Requirement | Priority | Details |
|-------------|----------|---------|
| $member-match endpoint restricted to authenticated payer systems | **CRITICAL** | mTLS + OAuth2 backend services authentication |
| Rate limit $member-match requests per client | **HIGH** | Prevent enumeration attacks |
| Input validation: require minimum demographics for matching | **HIGH** | Block requests with insufficient identifiers |
| Log all $member-match requests and results | **CRITICAL** | Audit trail for payer-to-payer member identification |
| No member data in error responses | **HIGH** | Error messages must not leak PHI |
| Match confidence scoring with threshold enforcement | **MEDIUM** | Reject low-confidence matches; require manual review |
| Timeout: $member-match must respond within 30 seconds or fail | **MEDIUM** | Prevent resource exhaustion |

### 4.6 Backend Services JWT

| Requirement | Priority | Details |
|-------------|----------|---------|
| RS384 or ES384 algorithm for JWT signing | **CRITICAL** | No symmetric algorithms (HS256) for backend services |
| JWT `exp` claim ≤ 5 minutes from `iat` | **HIGH** | Short-lived assertions prevent replay |
| Unique `jti` claim with server-side replay detection | **HIGH** | Reject reused JWT IDs within expiration window |
| Private keys stored in HSM or Secrets Manager | **CRITICAL** | Never on disk or in code repositories |
| JWKS endpoint for public key distribution | **HIGH** | `/.well-known/jwks.json` with key rotation support |
| Key rotation: at least annually, immediate on suspected compromise | **HIGH** | Support multiple active keys during rotation window |
| Validate `iss` matches registered client_id | **HIGH** | Prevent JWT forgery from unauthorized issuers |

---

## 5. Data Security

### 5.1 PHI/PII Handling (HIPAA)

| Requirement | Priority | Details |
|-------------|----------|---------|
| Identify and classify all PHI/PII data elements | **CRITICAL** | FHIR resources containing PHI: Patient, Condition, Observation, MedicationRequest, etc. |
| Minimum necessary standard: return only requested data | **CRITICAL** | `_elements` parameter support; no full resource dumps by default |
| PHI never stored in logs, error messages, or debug output | **CRITICAL** | Log sanitization at application and infrastructure layers |
| BAA (Business Associate Agreement) with all data processors | **CRITICAL** | AWS BAA, Databricks BAA, third-party integrations |
| De-identification for analytics: Safe Harbor or Expert Determination | **HIGH** | HIPAA §164.514 compliance for secondary use |
| Data segmentation for sensitive categories | **HIGH** | 42 CFR Part 2, mental health, genetic data |

### 5.2 Encryption at Rest

| Requirement | Priority | Details |
|-------------|----------|---------|
| S3: SSE-KMS with customer-managed keys (CMK) | **CRITICAL** | Default encryption on all buckets; deny `PutObject` without encryption |
| RDS: encrypted with CMK; encrypted snapshots | **CRITICAL** | Cannot be enabled after creation; enforce via SCP |
| DynamoDB: encryption at rest with CMK | **HIGH** | Default since 2018; verify CMK vs. AWS-owned |
| EBS volumes: encrypted with CMK | **CRITICAL** | Enforce via SCP: deny `RunInstances` with unencrypted volumes |
| Databricks: customer-managed keys for workspace storage | **HIGH** | DBFS encryption with customer CMK |
| KMS key policy: restrict to specific IAM roles | **HIGH** | Separate keys per environment and data classification |
| KMS key rotation: automatic annual rotation enabled | **MEDIUM** | AWS manages rotation; previous versions retained for decryption |

### 5.3 Encryption in Transit

| Requirement | Priority | Details |
|-------------|----------|---------|
| TLS 1.2+ for all data in transit | **CRITICAL** | Enforced at ALB, API Gateway, and client SDK level |
| S3: enforce `aws:SecureTransport` condition | **CRITICAL** | Bucket policy denies HTTP requests |
| RDS: `require_ssl` parameter enabled | **HIGH** | Reject unencrypted database connections |
| Internal service communication: TLS with service mesh | **HIGH** | No plaintext traffic within VPC |
| FHIR payload encryption for payer-to-payer exchange | **MEDIUM** | Application-layer encryption for sensitive bundles |

### 5.4 Masking & Tokenization

| Requirement | Priority | Details |
|-------------|----------|---------|
| Tokenize patient identifiers in non-production environments | **CRITICAL** | No real MBIs, SSNs, or MRNs in dev/staging |
| Dynamic data masking for support/debugging access | **HIGH** | Mask PHI fields in database views for support roles |
| Log tokenization: replace PHI with correlation tokens | **HIGH** | Enable tracing without PHI exposure |
| Test data generation: synthetic FHIR data for dev/test | **HIGH** | Use Synthea or similar synthetic data generators |
| Masking rules documented per data element | **MEDIUM** | Classification-driven masking policy |

### 5.5 Audit Trails

| Requirement | Priority | Details |
|-------------|----------|---------|
| FHIR AuditEvent resources for all data access | **CRITICAL** | Who accessed what patient data, when, from where |
| Immutable audit log storage (S3 Object Lock / WORM) | **CRITICAL** | Prevent tampering with compliance evidence |
| Audit log retention: minimum 6 years (HIPAA) | **CRITICAL** | CMS may require longer; verify per program |
| Real-time audit streaming to SIEM | **HIGH** | Enable immediate breach detection |
| Audit log includes: user, action, resource, timestamp, outcome | **HIGH** | FHIR AuditEvent.entity, .agent, .outcome |
| Regular audit log integrity verification | **MEDIUM** | CloudTrail log file validation; S3 object checksums |

### 5.6 Retention & Disposal

| Requirement | Priority | Details |
|-------------|----------|---------|
| Data retention policy per data category documented | **CRITICAL** | Clinical data: 6+ years; operational logs: 1-3 years |
| Automated lifecycle policies (S3 lifecycle, RDS snapshot retention) | **HIGH** | No manual deletion processes |
| Secure disposal: cryptographic erasure via KMS key deletion | **HIGH** | Schedule key deletion (7-30 day waiting period) |
| Verify disposal: confirm data inaccessibility post-deletion | **MEDIUM** | Automated validation job |
| Third-party data return/destruction on BAA termination | **HIGH** | Contractual and operational procedures |

---

## 6. Operational Security

### 6.1 Signed Artifacts

| Requirement | Priority | Details |
|-------------|----------|---------|
| All container images signed with cosign/Notation | **CRITICAL** | Verify signatures before deployment admission |
| Helm charts signed and verified | **HIGH** | `helm verify` in CI/CD pipeline |
| Lambda deployment packages: SHA256 integrity check | **HIGH** | Store checksums in parameter store; verify at deploy |
| Infrastructure-as-Code templates signed | **MEDIUM** | Git commit signing (GPG) for all IaC changes |
| Artifact provenance: SLSA Level 2+ | **HIGH** | Build system generates provenance attestations |

### 6.2 Image Scanning

| Requirement | Priority | Details |
|-------------|----------|---------|
| ECR image scanning on push (enhanced scanning) | **CRITICAL** | Block deployment of images with CRITICAL/HIGH CVEs |
| Base image policy: approved base images only | **HIGH** | Maintain curated base image registry |
| Scan frequency: continuous (not just on push) | **HIGH** | New CVEs discovered post-push must trigger alerts |
| SLA: CRITICAL CVE patched within 48 hours | **CRITICAL** | HIGH within 7 days; MEDIUM within 30 days |
| No root user in container images | **HIGH** | Dockerfile: `USER nonroot` enforced by admission controller |
| Minimal images: distroless or Alpine-based | **MEDIUM** | Reduce attack surface |

### 6.3 CI/CD Security

| Requirement | Priority | Details |
|-------------|----------|---------|
| Pipeline credentials: short-lived, scoped IAM roles | **CRITICAL** | No long-lived secrets in CI/CD environment variables |
| Branch protection: require PR review + status checks | **CRITICAL** | No direct push to `main`/`release` branches |
| Separate pipelines per environment with approval gates | **HIGH** | Prod deployment requires explicit approval |
| Pipeline audit trail: immutable logs of all deployments | **HIGH** | Who deployed what, when, with what approval |
| Secrets not passed via environment variables in build steps | **HIGH** | Use secret injection at runtime only |
| SAST (Static Application Security Testing) in pipeline | **HIGH** | Block merge on HIGH/CRITICAL findings |
| Pipeline isolation: no shared build environments | **MEDIUM** | Ephemeral build containers per execution |

### 6.4 Dependency Scanning

| Requirement | Priority | Details |
|-------------|----------|---------|
| SCA (Software Composition Analysis) on every build | **CRITICAL** | Snyk, Dependabot, or OWASP Dependency-Check |
| Block builds with known-exploited vulnerabilities (KEV) | **CRITICAL** | CISA KEV catalog integration |
| License compliance scanning | **MEDIUM** | Flag GPL/AGPL dependencies in proprietary code |
| SBOM (Software Bill of Materials) generated per release | **HIGH** | CycloneDX or SPDX format; stored with release artifacts |
| Dependency pinning: exact versions in lock files | **HIGH** | No floating versions (`^`, `~`, `*`) in production |
| Private package registry: proxy public registries | **MEDIUM** | Prevent dependency confusion attacks |

### 6.5 Runtime Monitoring

| Requirement | Priority | Details |
|-------------|----------|---------|
| Container runtime security (Falco, GuardDuty for EKS) | **HIGH** | Detect unexpected process execution, file access, network connections |
| AWS GuardDuty enabled in all accounts/regions | **CRITICAL** | Threat detection for AWS environment |
| CloudWatch anomaly detection for API metrics | **HIGH** | Alert on unusual request patterns, error rates, latency spikes |
| Application-level WAF + RASP (Runtime Application Self-Protection) | **MEDIUM** | Defense-in-depth beyond network WAF |
| File integrity monitoring on critical configuration | **HIGH** | Alert on unauthorized changes to config files, certificates |
| Memory protection: ASLR, stack canaries, NX bit | **MEDIUM** | Default on modern OS; verify in container runtime |

---

## 7. Compliance & Audit

### 7.1 CMS Audit Requirements

| Requirement | Priority | Details |
|-------------|----------|---------|
| Annual security risk assessment (SRA) | **CRITICAL** | NIST 800-66 or equivalent framework |
| CMS MARS-E 2.0 compliance for Marketplace integrations | **CRITICAL** | Minimum Acceptable Risk Standards for Exchanges |
| Patient Access API: track and report third-party app access | **HIGH** | CMS requires transparency reporting |
| Interoperability rule compliance documentation | **HIGH** | CMS-9115-F, CMS-9123-F documentation artifacts |
| Annual penetration testing of FHIR APIs | **CRITICAL** | External firm; remediate findings within SLA |
| Provider Directory API: data accuracy validation | **MEDIUM** | CMS No Surprises Act compliance |
| Prior Authorization API: decision audit trail | **HIGH** | CMS-0057-F compliance; 72-hour response SLA |

### 7.2 HIPAA Technical Safeguards

| Requirement | Priority | Details |
|-------------|----------|---------|
| **Access Control** (§164.312(a)): Unique user identification | **CRITICAL** | No shared accounts; unique IDs for all users and systems |
| **Access Control**: Emergency access procedure | **HIGH** | Break-glass procedure documented and tested annually |
| **Access Control**: Automatic logoff | **HIGH** | Session timeout ≤ 15 minutes idle for PHI-accessing applications |
| **Access Control**: Encryption and decryption | **CRITICAL** | AES-256 at rest; TLS 1.2+ in transit |
| **Audit Controls** (§164.312(b)): Record and examine activity | **CRITICAL** | Comprehensive logging; regular log review |
| **Integrity** (§164.312(c)): PHI alteration/destruction protection | **HIGH** | Checksums, versioning, backup verification |
| **Authentication** (§164.312(d)): Verify identity of those seeking access | **CRITICAL** | MFA for all human access to PHI systems |
| **Transmission Security** (§164.312(e)): Integrity controls | **HIGH** | Message authentication (HMAC/signatures) for FHIR exchanges |
| **Transmission Security**: Encryption | **CRITICAL** | TLS 1.2+ for all PHI transmission |

### 7.3 Access Logging

#### CloudTrail

| Requirement | Priority | Details |
|-------------|----------|---------|
| Organization-level trail covering all accounts | **CRITICAL** | Multi-region; management + data events |
| Data events for S3 (PHI buckets) and Lambda | **HIGH** | Who accessed which objects/functions |
| Log file validation enabled | **HIGH** | Detect log tampering |
| CloudTrail Lake for SQL-based analysis | **MEDIUM** | 7-year retention for compliance queries |
| Deny `cloudtrail:StopLogging` and `cloudtrail:DeleteTrail` via SCP | **CRITICAL** | Prevent log suppression |

#### VPC Flow Logs

| Requirement | Priority | Details |
|-------------|----------|---------|
| Enabled on all VPCs, subnets, and ENIs (data tier) | **CRITICAL** | Format v5 with additional fields (tcp-flags, pkt-src/dst-addr) |
| Retention: 90 days in CloudWatch, 1 year in S3 | **HIGH** | Tiered retention balances cost and compliance |
| Automated analysis: detect unusual traffic patterns | **HIGH** | Guard Duty network threat detection |
| Alert on rejected traffic to/from data tier | **MEDIUM** | Potential lateral movement indicator |

#### FHIR AuditEvent

| Requirement | Priority | Details |
|-------------|----------|---------|
| Generate AuditEvent for every FHIR interaction | **CRITICAL** | CRUD operations, searches, batch/transaction bundles |
| AuditEvent.agent: identity of requester (user, system, patient) | **HIGH** | Link to OAuth2 token claims |
| AuditEvent.entity: resources accessed (Patient, Condition, etc.) | **HIGH** | Support compliance queries: "who accessed Patient/123?" |
| AuditEvent.outcome: success (0) or failure (4, 8, 12) | **HIGH** | Track access denials for threat detection |
| Store AuditEvents in dedicated, immutable repository | **HIGH** | Separate from clinical data; different access controls |
| Retention: 6 years minimum | **CRITICAL** | HIPAA and CMS requirements |

### 7.4 Third-Party App Security

| Requirement | Priority | Details |
|-------------|----------|---------|
| App attestation before Patient Access API registration | **CRITICAL** | Privacy policy, security practices, data use disclosure |
| Annual re-attestation for registered apps | **HIGH** | Validate ongoing compliance |
| App developer identity verification | **HIGH** | Verified organization identity (D-U-N-S, EIN) |
| App-specific rate limiting and monitoring | **HIGH** | Detect abusive data harvesting patterns |
| Patient notification of third-party app access | **MEDIUM** | Transparency per CMS requirements |
| Ability to revoke app access immediately | **CRITICAL** | Kill switch for compromised/malicious applications |
| App security assessment questionnaire (SIG/CAIQ) | **MEDIUM** | Standardized security evaluation |

---

## 8. Pre-Change Security Review Checklist

### Instructions

Complete this checklist for **every** interoperability deployment or infrastructure change before production release. All CRITICAL items must pass. HIGH items require documented risk acceptance if deferred.

| # | Category | Check Item | Priority | Pass/Fail/NA | Reviewer | Notes |
|---|----------|-----------|----------|--------------|----------|-------|
| **IAM & Access** | | | | | | |
| 1 | IAM | No static AWS access keys introduced or required | CRITICAL | ☐ | | |
| 2 | IAM | All new IAM policies follow least privilege (no `*` resources) | CRITICAL | ☐ | | |
| 3 | IAM | Permission boundaries applied to any new roles | HIGH | ☐ | | |
| 4 | IAM | Cross-account access uses `ExternalId` and specific account IDs | HIGH | ☐ | | |
| 5 | IAM | Service accounts are unique per component with restricted permissions | HIGH | ☐ | | |
| **Secrets** | | | | | | |
| 6 | Secrets | No secrets hardcoded in code, configs, or environment variables | CRITICAL | ☐ | | |
| 7 | Secrets | All new secrets stored in Secrets Manager or SSM SecureString | CRITICAL | ☐ | | |
| 8 | Secrets | Rotation configured for new credentials (≤ 90 days) | HIGH | ☐ | | |
| 9 | Secrets | Secret access restricted to minimum required IAM roles | HIGH | ☐ | | |
| **Network** | | | | | | |
| 10 | Network | No new public endpoints without WAF protection | CRITICAL | ☐ | | |
| 11 | Network | Security groups follow deny-all-except-explicit-allow | CRITICAL | ☐ | | |
| 12 | Network | No `0.0.0.0/0` inbound rules (except ALB:443) | CRITICAL | ☐ | | |
| 13 | Network | TLS 1.2+ enforced on all new endpoints | CRITICAL | ☐ | | |
| 14 | Network | VPC Flow Logs enabled for new subnets/ENIs | HIGH | ☐ | | |
| 15 | Network | Egress limited to documented destination allowlist | HIGH | ☐ | | |
| 16 | Network | PrivateLink used for AWS service access from private subnets | HIGH | ☐ | | |
| **Authentication** | | | | | | |
| 17 | Auth | OAuth2/SMART on FHIR tokens validated on every request | CRITICAL | ☐ | | |
| 18 | Auth | PKCE required for public clients | CRITICAL | ☐ | | |
| 19 | Auth | Token lifetimes within policy (access ≤ 15 min, refresh ≤ 24 hr) | HIGH | ☐ | | |
| 20 | Auth | Scope enforcement tested for new endpoints | CRITICAL | ☐ | | |
| 21 | Auth | Backend service JWTs use RS384/ES384 with short expiration | HIGH | ☐ | | |
| **Data Security** | | | | | | |
| 22 | Data | PHI/PII classified and handling documented | CRITICAL | ☐ | | |
| 23 | Data | Encryption at rest enabled (CMK) for new data stores | CRITICAL | ☐ | | |
| 24 | Data | No PHI in logs, error messages, or debug output | CRITICAL | ☐ | | |
| 25 | Data | Audit logging (AuditEvent) implemented for new data access paths | CRITICAL | ☐ | | |
| 26 | Data | Data retention/disposal policy documented for new data stores | HIGH | ☐ | | |
| 27 | Data | Test/dev environments use synthetic or tokenized data only | HIGH | ☐ | | |
| **Operational** | | | | | | |
| 28 | Ops | Container images scanned; no CRITICAL/HIGH CVEs | CRITICAL | ☐ | | |
| 29 | Ops | Dependencies scanned; no known-exploited vulnerabilities | CRITICAL | ☐ | | |
| 30 | Ops | Deployment artifacts signed and verified | HIGH | ☐ | | |
| 31 | Ops | SBOM generated and stored with release | HIGH | ☐ | | |
| 32 | Ops | CI/CD pipeline uses short-lived credentials only | HIGH | ☐ | | |
| 33 | Ops | Rollback procedure documented and tested | HIGH | ☐ | | |
| **Compliance** | | | | | | |
| 34 | Compliance | Change documented in change management system | CRITICAL | ☐ | | |
| 35 | Compliance | HIPAA technical safeguards verified for new components | CRITICAL | ☐ | | |
| 36 | Compliance | CloudTrail logging confirmed for new services/actions | HIGH | ☐ | | |
| 37 | Compliance | Third-party app attestation current (if applicable) | HIGH | ☐ | | |
| 38 | Compliance | BAA in place for any new data processors | CRITICAL | ☐ | | |
| **Incident Readiness** | | | | | | |
| 39 | Incident | Alerting configured for new components (anomaly detection) | HIGH | ☐ | | |
| 40 | Incident | Incident response runbook updated for new architecture | HIGH | ☐ | | |
| 41 | Incident | Emergency access/revocation procedures tested | MEDIUM | ☐ | | |

### Sign-Off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Security Engineer | | | |
| Platform Engineer | | | |
| Compliance Officer | | | |
| Change Manager | | | |

---

## 9. Security Incident Response

### 9.1 Breach Detection

#### Detection Sources

| Source | What It Detects | Response Time |
|--------|----------------|---------------|
| AWS GuardDuty | Compromised credentials, unusual API activity, crypto-mining, C2 communication | Real-time (< 5 min) |
| CloudTrail anomaly alerts | Unusual IAM actions, policy changes, data access patterns | Near real-time (< 15 min) |
| WAF alerts | Attack patterns, rate limit violations, bot activity | Real-time |
| FHIR AuditEvent analysis | Unauthorized PHI access, bulk data exfiltration patterns | Near real-time |
| VPC Flow Log analysis | Lateral movement, data exfiltration, port scanning | Near real-time |
| Container runtime alerts | Unexpected process execution, file system modifications | Real-time |
| User/patient reports | Account takeover, unauthorized access notifications | Variable |
| Third-party threat intelligence | Compromised credentials on dark web, zero-day disclosures | Variable |

#### Detection Rules (Critical)

```
RULE: PHI_BULK_ACCESS
  TRIGGER: Single token accesses > 100 unique Patient resources in 1 hour
  ACTION: Alert SOC + auto-revoke token + page on-call

RULE: CREDENTIAL_ANOMALY
  TRIGGER: IAM role assumption from unexpected IP/region
  ACTION: Alert SOC + block IP + investigate

RULE: DATA_EXFILTRATION
  TRIGGER: Egress traffic > 1GB from data-tier subnet in 1 hour
  ACTION: Alert SOC + isolate instance + forensic snapshot

RULE: MEMBER_MATCH_ENUMERATION
  TRIGGER: > 50 failed $member-match requests from single client in 10 minutes
  ACTION: Rate limit → block client → alert SOC

RULE: PRIVILEGE_ESCALATION
  TRIGGER: IAM policy/role modification outside change window
  ACTION: Alert SOC + revert change + investigate
```

### 9.2 Response Procedures

#### Severity Classification

| Severity | Description | Response Time | Examples |
|----------|-------------|---------------|----------|
| **SEV-1 (Critical)** | Confirmed PHI breach, active data exfiltration, system compromise | Immediate (< 15 min) | Ransomware, mass PHI access, credential compromise with data access |
| **SEV-2 (High)** | Suspected breach, vulnerability actively exploited, unauthorized access attempt | < 1 hour | Failed bulk access attempts, suspicious API patterns, CVE exploitation |
| **SEV-3 (Medium)** | Security misconfiguration, policy violation, failed controls | < 4 hours | Open security group, missing encryption, expired certificate |
| **SEV-4 (Low)** | Informational, minor policy deviation, proactive finding | < 24 hours | Unused permissions, stale credentials, non-critical patching |

#### Incident Response Phases

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    ONYX INCIDENT RESPONSE WORKFLOW                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  1. DETECTION        2. TRIAGE           3. CONTAINMENT                 │
│  ┌──────────┐       ┌──────────┐        ┌──────────────┐              │
│  │ Alert    │──────▶│ Classify │───────▶│ Isolate      │              │
│  │ Received │       │ Severity │        │ Preserve     │              │
│  └──────────┘       └──────────┘        │ Communicate  │              │
│                                          └──────┬───────┘              │
│                                                 │                       │
│  6. LESSONS         5. RECOVERY          4. ERADICATION                │
│  ┌──────────┐       ┌──────────┐        ┌──────────────┐              │
│  │ Post-    │◀──────│ Restore  │◀───────│ Root Cause   │              │
│  │ Mortem   │       │ Validate │        │ Remediate    │              │
│  └──────────┘       └──────────┘        └──────────────┘              │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

#### Phase 1: Detection & Initial Response (0-15 minutes)

| Step | Action | Owner |
|------|--------|-------|
| 1.1 | Alert received and acknowledged in incident management system | On-call engineer |
| 1.2 | Initial assessment: confirm alert is not false positive | On-call engineer |
| 1.3 | Classify severity (SEV-1 through SEV-4) | On-call engineer |
| 1.4 | Open incident channel; notify incident commander | On-call engineer |
| 1.5 | For SEV-1/2: Page security team lead and CISO | Incident commander |

#### Phase 2: Containment (15 min - 2 hours)

| Step | Action | Owner |
|------|--------|-------|
| 2.1 | Isolate affected systems (security group lockdown, route removal) | Security engineer |
| 2.2 | Revoke compromised credentials/tokens immediately | Security engineer |
| 2.3 | Preserve forensic evidence (EBS snapshots, memory dumps, logs) | Security engineer |
| 2.4 | Block attacker indicators (IP, user agent, client ID) at WAF/SG | Security engineer |
| 2.5 | Assess blast radius: what data/systems were potentially accessed | Incident commander |
| 2.6 | Notify legal/privacy team if PHI may be involved | Incident commander |

#### Phase 3: Eradication (2-48 hours)

| Step | Action | Owner |
|------|--------|-------|
| 3.1 | Root cause analysis: identify attack vector and entry point | Security engineer |
| 3.2 | Remove attacker persistence (backdoors, unauthorized accounts, modified configs) | Security engineer |
| 3.3 | Patch vulnerability that enabled the breach | Platform engineer |
| 3.4 | Rotate all credentials that may have been exposed | Security engineer |
| 3.5 | Verify no additional compromised systems via threat hunting | Security team |

#### Phase 4: Recovery (24-72 hours)

| Step | Action | Owner |
|------|--------|-------|
| 4.1 | Restore systems from known-good state (verified backups) | Platform engineer |
| 4.2 | Gradually restore network connectivity with enhanced monitoring | Security engineer |
| 4.3 | Validate data integrity (checksums, row counts, consistency checks) | Data engineer |
| 4.4 | Confirm security controls operational (WAF, logging, alerting) | Security engineer |
| 4.5 | Return to normal operations with 30-day enhanced monitoring period | Incident commander |

### 9.3 HIPAA Breach Notification Requirements

#### Notification Timeline

| Notification | Deadline | Recipient | Condition |
|-------------|----------|-----------|-----------|
| **HHS/OCR** | ≤ 60 days from discovery | Department of Health and Human Services | All breaches of unsecured PHI |
| **Affected Individuals** | ≤ 60 days from discovery | Each individual whose PHI was breached | All breaches |
| **Media** | ≤ 60 days from discovery | Prominent media outlets in affected states | Breaches affecting ≥ 500 individuals in a state |
| **CMS** | Per BAA terms (typically ≤ 24-72 hours) | CMS Program Office | Breaches affecting CMS program data |
| **State Attorneys General** | Varies by state (often ≤ 30-60 days) | State AG offices | Varies by state law; most triggered by ≥ 500 residents |

#### Breach Risk Assessment (4 Factors)

Before notification, assess whether breach exception applies:

1. **Nature and extent of PHI involved** — Types of identifiers, clinical data sensitivity
2. **Unauthorized person who used/accessed PHI** — Internal vs. external; their obligations
3. **Whether PHI was actually acquired or viewed** — Evidence of access vs. mere exposure
4. **Extent of risk mitigation** — Immediate actions to reduce harm

> If the assessment demonstrates **low probability** that PHI was compromised, notification may not be required. Document the assessment thoroughly.

#### Notification Content (Required Elements)

- Description of the breach (what happened, dates)
- Types of PHI involved (names, SSN, MBI, diagnoses, etc.)
- Steps individuals should take to protect themselves
- Description of what the organization is doing to investigate, mitigate, and prevent recurrence
- Contact information for questions (toll-free number, email, website)

### 9.4 Forensics

#### Evidence Preservation

| Evidence Type | Collection Method | Storage | Retention |
|--------------|-------------------|---------|-----------|
| EBS volumes | Snapshot + copy to forensic account | Encrypted S3 in isolated account | Until investigation complete + 7 years |
| Memory | EC2 memory dump via SSM/hibernation | Encrypted S3 | Until analysis complete |
| CloudTrail logs | Already in S3; copy to forensic bucket | Immutable S3 (Object Lock) | 7 years |
| VPC Flow Logs | Already in CloudWatch/S3; snapshot relevant timeframe | Forensic S3 bucket | 7 years |
| Container images | `docker save` running containers | Encrypted S3 | Until investigation complete |
| Application logs | Copy from CloudWatch/ELK to forensic store | Immutable S3 | 7 years |
| WAF logs | Copy relevant timeframe from S3 | Forensic S3 bucket | 7 years |
| Network captures | VPC Traffic Mirroring (if enabled) | Encrypted S3 | Until analysis complete |

#### Chain of Custody

| Requirement | Details |
|-------------|---------|
| Hash all evidence at collection time | SHA-256; record in incident management system |
| Document collector identity and method | Who, when, how, from where |
| Restrict access to forensic storage | Separate IAM roles; require approval |
| Log all access to forensic evidence | CloudTrail data events on forensic S3 bucket |
| Use write-once storage | S3 Object Lock (Governance or Compliance mode) |
| Maintain timeline of evidence handling | Every access, copy, or analysis logged |

#### Forensic Analysis Procedures

```
1. TIMELINE RECONSTRUCTION
   - Correlate CloudTrail, VPC Flow Logs, application logs, WAF logs
   - Establish: first compromise → lateral movement → data access → exfiltration
   - Tools: Amazon Detective, Athena queries, SIEM correlation

2. CREDENTIAL ANALYSIS
   - Identify all credentials used during incident timeframe
   - Determine which are legitimate vs. attacker-controlled
   - Check for privilege escalation path
   - Verify credential rotation completeness

3. DATA ACCESS ANALYSIS
   - Query FHIR AuditEvents for accessed resources during incident window
   - Identify unique patients/records potentially accessed
   - Determine if data was exported/exfiltrated (S3 GET patterns, egress volume)
   - Quantify breach scope for notification determination

4. INDICATOR OF COMPROMISE (IOC) EXTRACTION
   - IP addresses, user agents, client IDs
   - File hashes, modified configurations
   - Attack patterns, tools used
   - Share IOCs with industry ISACs (H-ISAC for healthcare)

5. ROOT CAUSE DOCUMENTATION
   - Attack vector (phishing, vulnerability, misconfiguration, insider)
   - Contributing factors (missing controls, detection gaps)
   - Remediation actions taken
   - Preventive measures implemented
```

---

## Appendix A: Quick Reference — Security Contacts

| Role | Contact | Escalation Path |
|------|---------|-----------------|
| Security On-Call | PagerDuty: `onyx-security-oncall` | Auto-escalates after 15 min |
| CISO | [CISO Name] | Via incident commander for SEV-1 |
| Privacy Officer | [Privacy Officer Name] | For any suspected PHI breach |
| Legal Counsel | [Legal Contact] | For breach notification decisions |
| CMS Liaison | [CMS Contact] | For CMS-specific program breaches |
| AWS TAM | [TAM Contact] | For AWS-level security incidents |

## Appendix B: Related Documents

| Document | ID | Description |
|----------|-----|-------------|
| Onyx Architecture Overview | ONYX-ARCH-001 | System architecture and data flows |
| FHIR API Security Design | ONYX-SEC-003 | FHIR-specific security architecture |
| Incident Response Plan | ONYX-IRP-001 | Full incident response plan |
| Business Continuity Plan | ONYX-BCP-001 | Disaster recovery and continuity |
| Data Classification Policy | ONYX-DCP-001 | PHI/PII classification taxonomy |
| Vendor Security Assessment | ONYX-VSA-001 | Third-party risk management |
| Change Management Policy | ONYX-CMP-001 | Change approval workflows |
| Key Management Policy | ONYX-KMP-001 | KMS key lifecycle management |

## Appendix C: Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-07-07 | Security & Compliance Team | Initial release |

---

*This document is a living artifact. Report gaps or improvements to the Security & Compliance Team. All Onyx team members are responsible for security.*
