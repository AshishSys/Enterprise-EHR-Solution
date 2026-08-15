#!/usr/bin/env python3
"""Generate Section AB: CMS-0057 Auth, ePA A/B, Cambia BQ Ingest (Q536–553)."""
from pathlib import Path

OUT = Path("/Users/ashishsingh/Interview/Healthcare_Interop_Interview_Cheat_Sheet.md")
ROOT = "/Users/ashishsingh/OnyxInterop/Training/onyx-interop"
DOCS = f"{ROOT}/docs"

QUESTIONS = [
    ("What are the three CMS-0057 auth paths and how do they differ?",
     "PAA: member SAML→SMART PKCE→FITE us-core/carin-bb. PVA: Apigee→SLAP client_credentials→FITE /atr-consumer. P2P: Apigee→SLAP PDex token→FITE /pdexv2 bulk match/export.",
     "Shared: SLAP+FITE+Firely. Different: IGs, scopes, auth models.",
     f"Read {DOCS}/CMS0057_AUTH_PATHS.md",
     "cat configs/mdp/auth_paths.json | python3 -m json.tool",
     f"cat {ROOT}/configs/mdp/auth_paths.json | python3 -m json.tool",
     "FHIR Engineer | Associate Solution Architect"),
    ("Why is Patient Access NOT machine client_credentials auth?",
     "Path A requires member login via payer IdP SAML federation then SMART/OAuth with PKCE — third-party apps act on behalf of the member with consent.",
     "Provider/P2P paths use Backend Services client_credentials without member SAML.",
     "Compare auth_paths.json paa vs pva auth_model",
     "curl localhost:9000/.well-known/smart-configuration",
     "curl -s http://localhost:9000/.well-known/smart-configuration | head -5",
     "FHIR Engineer"),
    ("What is the Provider Access auth path end-to-end?",
     "External provider system → Apigee/Gateway → SLAP client_credentials → FITE /atr-consumer → attributed bulk $export → FHIR Store.",
     "Attribution Group resources link members to practitioners.",
     "Read CMS0057_AUTH_PATHS Path B",
     "provider_access.py on :9003 when services running",
     f"grep atr-consumer {DOCS}/CMS0057_AUTH_PATHS.md",
     "FHIR Engineer | Forward Deployed Engineer"),
    ("What is the Payer-to-Payer auth path?",
     "External payer → Apigee → SLAP client_credentials with PDex scope → FITE /pdexv2 → $bulk-member-match + NDJSON export with consent.",
     "CMS-0057 Jan 2027 deadline.",
     "Read auth_paths.json p2p entry",
     "p2p_member_match.py :9004",
     "python3 $HOME/OnyxInterop/p2p_member_match.py --help 2>/dev/null || ls $HOME/OnyxInterop/p2p_member_match.py",
     "FHIR Engineer"),
    ("Can a Patient Access SMART token call /pdexv2?",
     "No — auth paths must not mix. PAA scopes are patient compartment; P2P requires system-level PDex scopes via machine auth.",
     "FITE enforces scope + route binding; audit in Onyx Insights.",
     "auth_paths.json note field",
     "Review SLAP scope enforcement in slap_server.py",
     "grep -n scope $HOME/OnyxInterop/slap_server.py | head -5",
     "FHIR Engineer | Associate Solution Architect"),
    ("What is shared vs different across PAA, PVA, and P2P?",
     "Shared: SLAP, FITE, Firely. Different: IGs (US Core/CARIN vs PDex), scopes, auth (member SMART vs client_credentials), gateway (Apigee for B/C).",
     "Diagram: three columns, one footer.",
     f"Read {DOCS}/CMS0057_AUTH_PATHS.md design rules",
     "configs/mdp/auth_paths.json",
     f"cat {ROOT}/configs/mdp/auth_paths.json",
     "Associate Solution Architect"),
    ("What is the shared ePA ingress before Option A or B?",
     "Provider EHR → AWS ALB → APISIX Gateway → CDS Service (epa-appsvc) with dapr sidecar for CRD hooks.",
     "CRD is point-of-care; PAS may be batch (A) or real-time API (B).",
     f"Read {DOCS}/EPA_OPTION_A_B.md shared ingress",
     "curl localhost:9005/cds-services",
     "curl -s http://localhost:9005/cds-services 2>/dev/null | head -3 || echo 'start epa service first'",
     "Forward Deployed Engineer"),
    ("What is ePA Option A (Gainwell pattern)?",
     "Batch/SFTP path: Routing-DIR → AWS Transfer SFTP → Gainwell PAS vendor → ClaimResponse batch (837/275/CSV) → Databricks → Firely.",
     "Legacy PAS integrations; no real-time PAS API.",
     f"Read {DOCS}/EPA_OPTION_A_B.md Option A",
     "configs/workflows/epa/extract_config.yaml",
     f"head -20 {ROOT}/configs/workflows/epa/extract_config.yaml",
     "Data Engineer"),
    ("What is ePA Option B (Wellmark pattern)?",
     "Real-time: Auth table + 13 decision tables → Jiva PAS APIs + InterQual/Evicore DTR → Event notification → FHIR Subscription callback to Provider EHR.",
     "No SFTP for PAS; rules at point of care.",
     f"Read {DOCS}/EPA_OPTION_A_B.md Option B",
     "epa_burden_reduction_service.py CRD endpoint",
     "grep -n cds-services $HOME/OnyxInterop/epa_burden_reduction_service.py | head -3",
     "FHIR Engineer | AI Engineer"),
    ("What is the mandatory ePA/cloud deploy order?",
     "onyx.provision → onyx.epa → onyx.deploy → databricks.provision → databricks_continuous_deployment → databricks.onyx — each gates the next.",
     "Do not run Databricks ePA workflows before APISIX/CDS ingress is live.",
     f"grep -A8 'Deploy order' {DOCS}/EPA_OPTION_A_B.md",
     "Plan Phase 0-1 sequencing",
     f"grep -n 'onyx.provision' {DOCS}/EPA_OPTION_A_B.md",
     "DevOps Engineer | Forward Deployed Engineer"),
    ("What problem does Cambia BigQuery ingestion solve?",
     "Ingest Cambia pharmacy claims from GCP BigQuery into Abacus AWS S3 as NDJSON — cross-cloud without stored GCP service-account keys.",
     "Rail D hybrid ingest; Bronze load is separate ng-pipelines-cambia workflow.",
     f"Read {DOCS}/CAMBIA_BIGQUERY_INGESTION.md §1",
     "XPORT-2596 design goal",
     f"head -25 {DOCS}/CAMBIA_BIGQUERY_INGESTION.md",
     "Data Engineer"),
    ("How does Cambia BQ auth work with no stored credentials?",
     "EKS IRSA → AWS STS → Google WIF → iamcredentials impersonation → BigQuery token (1h TTL, memory only).",
     "Must export IRSA creds before Google auth lib init; pass GCP project explicitly.",
     "Read CAMBIA doc §3",
     f"grep -n 'IRSA' {DOCS}/CAMBIA_BIGQUERY_INGESTION.md | head -5",
     "grep -n workloadIdentity $HOME/OnyxInterop/Training/onyx-interop/docs/CAMBIA_BIGQUERY_INGESTION.md | head -3",
     "DevOps Engineer | Data Engineer"),
    ("What are the four Cambia BigQuery load modes?",
     "incremental (daily), full (initial/manual), refresh (monthly correctness), replay (operator window to replay/ prefix).",
     "Incremental fails closed without checkpoint — never auto-runs full.",
     "Read §4 load modes",
     f"grep -n 'Fail closed' {DOCS}/CAMBIA_BIGQUERY_INGESTION.md",
     f"grep -n 'load mode' {DOCS}/CAMBIA_BIGQUERY_INGESTION.md | head -5",
     "Associate Solution Architect"),
    ("Why is periodic full refresh required for Cambia BQ ingest?",
     "BigQuery change history and time travel unavailable to Abacus — restated rows with unchanged watermark are silently lost; monthly refresh recovers them.",
     "Not optional optimization — correctness requirement.",
     "Read §8.5",
     f"grep -A3 'change history' {DOCS}/CAMBIA_BIGQUERY_INGESTION.md",
     f"grep -n refresh {DOCS}/CAMBIA_BIGQUERY_INGESTION.md | head -5",
     "Data Engineer"),
    ("What is the S3 handoff contract between BQ ingest and Databricks?",
     "Connector lands NDJSON under raw/bigquery-claims/ with atomic staging publish; manifest in metadata bucket (non-PHI). Bronze pipespec in ng-pipelines-cambia consumes prefix.",
     "Same split as every platform connector: ingest ends at S3.",
     "Read §7-8 output contract",
     f"grep -n 'landing layout' {DOCS}/CAMBIA_BIGQUERY_INGESTION.md",
     f"grep -n 'raw/bigquery-claims' {DOCS}/CAMBIA_BIGQUERY_INGESTION.md",
     "Data Engineer | DevOps Engineer"),
    ("How does Cambia BQ ingest relate to Rail A/B/C?",
     "Rail D — hybrid GCP→AWS. Rail A=CSV, B=webhook/Kafka, C=FHIR JSON; D=partner BigQuery cross-cloud pull to same Bronze convergence.",
     "Medallion Autoloader reads S3 prefix regardless of upstream rail.",
     "Plan multi-rail section + CAMBIA doc",
     f"grep -n 'Rail D' {DOCS}/CAMBIA_BIGQUERY_INGESTION.md",
     f"grep -n 'Rail [ABCD]' /Users/ashishsingh/OnyxInterop/implementation_details.md | head -8",
     "Data Engineer | Associate Solution Architect"),
    ("What logging is forbidden in Cambia BQ ingest?",
     "Row values, claim/member/prescriber IDs, drug names, PHI query predicates, access tokens — only run_id, counts, job id, safe error category.",
     "PHI to PHI bucket; metadata to non-PHI bucket — never mixed.",
     "Read §10",
     f"grep -n Forbidden {DOCS}/CAMBIA_BIGQUERY_INGESTION.md",
     f"grep -A5 'Forbidden' {DOCS}/CAMBIA_BIGQUERY_INGESTION.md",
     "DevOps Engineer"),
    ("How do these three attachments change cloud build priority?",
     "Cloud needs: Apigee+SLAP auth paths (PVA/P2P), APISIX+ePA stack, EKS CronJob+WIF for Rail D, then Databricks Bronze — after Phase 0 Terraform.",
     "Local baseline still valid for FM/SAM/FHIR learning.",
     "CLOUD_BUILD_GUIDE.md + new docs",
     f"ls {DOCS}/CMS0057*.md {DOCS}/EPA*.md {DOCS}/CAMBIA*.md",
     f"grep -n 'Rail D\\|Apigee\\|APISIX' $HOME/CursorInteropSolution/CLOUD_BUILD_GUIDE.md | head -10",
     "Associate Solution Architect | DevOps Engineer"),
]


def render():
    lines = [
        "## Section AB: CMS-0057 Auth, ePA A/B & Cambia BQ Ingest (Q536–553)\n",
        "> Sources: CMS-0057 Auth Paths diagram, ePA Option A/B deployment diagram, "
        "Cambia BigQuery Ingestion Design (XPORT-2596).\n",
    ]
    for i, (q, ans, ex, check, fix, script, roles) in enumerate(QUESTIONS, start=536):
        lines += [
            f"### Q{i}. {q}\n",
            f"**Answer:** {ans}\n",
            f"**Example:** {ex}\n",
            "**How to Check:**",
            f"- {check}",
            f"- {fix}\n",
            "**How to Fix:**",
            f"- Re-read docs under `{DOCS}/`",
            "- Trace auth path in configs/mdp/auth_paths.json\n",
            f"**Script:** *(builds proficiency: {roles})*\n",
            "```bash",
            script,
            "```\n",
            "---\n",
        ]
    return "\n".join(lines)


def main():
    text = OUT.read_text()
    if "## Section AB:" in text:
        print("Section AB exists — skipping insert")
        return
    marker = "## Glossary"
    idx = text.find(marker)
    if idx < 0:
        raise SystemExit("Glossary not found")
    text = text[:idx] + render() + "\n" + text[idx:]
    text = text.replace("535 questions + Glossary", "553 questions + Glossary")
    if "Section AB:" not in text.split("## Table of Contents")[1][:2000] if "## Table of Contents" in text else True:
        text = text.replace(
            "- [Section AA: AI Governance & CCA Alignment (Q516–535)](#section-aa-ai-governance--cca-alignment-q516535)",
            "- [Section AA: AI Governance & CCA Alignment (Q516–535)](#section-aa-ai-governance--cca-alignment-q516535)\n"
            "- [Section AB: CMS-0057 Auth, ePA A/B & Cambia BQ (Q536–553)](#section-ab-cms-0057-auth-epa-ab--cambia-bq-ingest-q536553)",
        )
    OUT.write_text(text)
    print(f"Inserted Section AB ({len(QUESTIONS)} questions)")


if __name__ == "__main__":
    main()
