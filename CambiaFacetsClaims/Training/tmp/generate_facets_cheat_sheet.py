#!/usr/bin/env python3
"""Generate Cambia Facets Claims Interview Cheat Sheet (sections A–AB)."""

from __future__ import annotations

from pathlib import Path

OUT = Path("/Users/ashishsingh/Interview/Cambia_Facets_Claims_Interview_Cheat_Sheet.md")
BASE = "/Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims"

SECTIONS: list[tuple[str, str, int, int, str]] = [
    ("A", "Opening & Role Fit", 1, 10, "Associate Solution Architect | Forward Deployed Engineer"),
    ("B", "Facets Domain & Cambia Context", 11, 28, "Data Engineer | Associate Solution Architect"),
    ("C", "Architecture & System Design", 29, 45, "Associate Solution Architect | Forward Deployed Engineer"),
    ("D", "Data Engineering & Databricks", 46, 73, "Data Engineer | Intermediate Associate Programmer"),
    ("E", "FHIR & Downstream Interop", 74, 94, "FHIR Engineer | Data Engineer"),
    ("F", "Security, Auth & Compliance", 95, 112, "Forward Deployed Engineer | Intermediate Associate Programmer"),
    ("G", "CDC Extraction & facets-core", 113, 124, "Data Engineer | Forward Deployed Engineer"),
    ("H", "Dual Gold Paths — Interop vs CDP", 125, 141, "FHIR Engineer | Associate Solution Architect"),
    ("I", "Deployment, Operations & Troubleshooting", 142, 154, "Forward Deployed Engineer | Intermediate Associate Programmer"),
    ("J", "Reporting, Analytics & KPIs", 155, 162, "Data Engineer | Associate Solution Architect"),
    ("K", "Claims & RCM Bridge", 163, 172, "Associate Solution Architect | Data Engineer"),
    ("L", "Leadership & Program Management", 173, 185, "Forward Deployed Engineer | Associate Solution Architect"),
    ("M", "Scenario Troubleshooting", 186, 195, "Forward Deployed Engineer | Associate Solution Architect"),
    ("N", "Snowflake Egress", 196, 205, "Data Engineer | Intermediate Associate Programmer"),
    ("O", "Orchestration & ng-orchestration-service", 206, 250, "Data Engineer | Forward Deployed Engineer"),
    ("P", "SFTP/Inbound & Landing Zone", 251, 295, "Data Engineer | Forward Deployed Engineer"),
    ("Q", "Databricks Engineering — Facets Claims", 296, 330, "Data Engineer | Intermediate Associate Programmer"),
    ("R", "MDM & Reltio Integration", 331, 360, "Data Engineer | Associate Solution Architect"),
    ("S", "AWS Networking & VPN", 361, 390, "Forward Deployed Engineer | Associate Solution Architect"),
    ("T", "SQL Server CDC & Facets Source", 391, 415, "Data Engineer | Intermediate Associate Programmer"),
    ("U", "Operations at Scale & Volumes", 416, 445, "Data Engineer | Forward Deployed Engineer"),
    ("V", "De-Identification & Safe Harbor", 446, 455, "Data Engineer | Associate Solution Architect"),
    ("W", "Master Data Management", 456, 465, "Data Engineer | Associate Solution Architect"),
    ("X", "Interop vs CDP Path Comparison", 466, 473, "Data Engineer | FHIR Engineer"),
    ("Y", "Observability & Monitoring", 474, 485, "Forward Deployed Engineer | Data Engineer"),
    ("Z", "DevOps & CI/CD", 486, 515, "DevOps Engineer | Forward Deployed Engineer"),
    ("AA", "Governance & Compliance", 516, 535, "Associate Solution Architect | Forward Deployed Engineer"),
    ("AB", "Cambia-Specific Integrations & Cutover", 536, 553, "Associate Solution Architect | Data Engineer"),
]

QUESTION_BANK: dict[int, tuple[str, str, str, str, str]] = {
    1: (
        "Tell me about your experience building end-to-end payer claims pipelines.",
        "I led Cambia Facets Claims from on-prem TriZetto Facets through VPN, bespoke CDC, encrypted landing, Databricks bronze/silver/gold, and dual FM outputs to SAM/FHIR and Snowflake. I owned manifest-triggered orchestration and SCD2 bronze loads—not just pipeline diagrams.",
        "Nightly batch trigger file arrives on SFTP → ng-orchestration-service kicks bronze → silver unified timeline → gold.fm_claim for 75 Medicare groups.",
        "Databricks job history for cambia02 claims workflows; manifest path cambia/facets/cambia/claims/extension/incremental/*/*manifest.json",
        "Map each of the 5 stages to an owner before sprint 1; run architecture trace script below.",
    ),
    2: (
        "What is the Cambia Facets Claims platform and how do components fit together?",
        "Facets Claims is cambia02-specific: facets-core CDC (outside HITRUST) → encrypted JSON + manifest → Abacus SFTP landing → NextGen raw S3 → Databricks bronze (44+ SCD2 tables) → silver unified timeline → dual gold (Interop filtered vs CDP full) → Onyx SAM/FHIR + Snowflake.",
        "ng-orchestration-service orchestrates CDC delivery monitoring and manifest-triggered Databricks workflows; AIR library handles encryption, manifest validation, SCD2 sinks.",
        "Catalog entries: config/repo-rules/transporters/sftp.yaml, orchestration.yaml, config/repo-rules/xform/pipelines.yaml",
        "Document repo ownership: facets-core, facets-infrastructure, ng-pipelines-cambia, ng-orchestration-service, ng-abacus-insights-runtime",
    ),
    3: (
        "How is Facets Claims different from a generic Transporters catalog service?",
        "It spans bespoke Facets CDC (Step Functions + Batch), VPN networking, SFTP trigger files, and XFORM medallion pipelines—not a single transporter YAML. Tenant is cambia02; source is on-prem SQL Server 2016 CDC replica.",
        "Claims Incremental (~4 hr), Historical, and PPL variants each have distinct S3 prefixes and DynamoDB locks in CdcGlobals.",
        "grep -r 'cambia02' config/repo-rules/xform/pipelines.yaml",
        "Never treat Facets as Airbyte-only; CDC concurrency is one job per domain via DynamoDB lock.",
    ),
    29: (
        "Walk through the 5-stage end-to-end architecture.",
        "Stage 1: on-prem Facets SQL Server via Palo Alto VPN to cambia-facets-networking AWS account. Stage 2: Step Functions CDC → encrypted JSON + manifest to intermediate S3. Stage 3: SFTP landing → NextGen raw → bronze SCD2. Stage 4: silver unified timeline → dual gold FM. Stage 5: SAM/FHIR (Onyx) + Snowflake egress + Reltio MDM.",
        "Architecture diagram: 10-step flow from CDC read replica through bronze CMC_CLCL_CLAIM to gold.fm_claim and gold.fm_claim_cambia.",
        "Confluence: Facets-Claims-Implementation-Bronze-Silver-Gold; Lucid Facets Claims Overall Flow Chart",
        "Whiteboard all 5 stages with repo names at each box.",
    ),
    46: (
        "How does bronze ingestion work for Facets claims?",
        "Manifest-triggered Databricks workflows load encrypted JSON into 44+ bronze tables using AIR library SCD Type 2. Key tables: CMC_CLCL_CLAIM, CMC_CDML_CL_LINE (medical), CMC_CDDL_CL_LINE (dental), CMC_CLST_STATUS, CMC_MEME_MEMBER, CMC_SBSB_SUBSC.",
        "420 Facets bronze tables released in prod (TechOps Jun 2024); incremental tracked via table_changes and manifest batch IDs.",
        "SELECT COUNT(*) FROM bronze.cmc_clcl_claim WHERE _is_current = true",
        "Verify manifest schema before bronze job; fail closed if encryption key or AIR version mismatch.",
    ),
    74: (
        "How do gold Facets tables feed SAM and FHIR?",
        "Interop path: gold.fm_claim + gold.fm_claim_item filtered for CMS-9115 SAM (75 groups, Medicare patients, dental excluded). Onyx ng-pipelines-onyx runs DM 2.0 → FHIR Claim, ClaimCoverage, ClaimDiagnosis, etc. Workflow: cambia02-claims-dataingestion-workflow.",
        "Dental claims exist in bronze/silver but filtered out of Interop fm_claim before SAM load; CDP gold retains all.",
        "FHIR ingestion workflow job run history in Onyx; validate Claim resources against US Core",
        "Confirm group filter list matches current attribution before SAM extract.",
    ),
    113: (
        "How does Facets CDC extraction work?",
        "SQL Server CDC → unique change IDs → partitioned JSON files → encryption → manifest.json. Orchestration: Step Functions + Lambda (light) + AWS Batch (heavy SQL). Intermediate S3: abacus-facets-intermediate-<env>/claims-incremental/, claims-historical/.",
        "~25 JSON files per batch: header, medical/dental line items, diagnosis, PPL, delete files + manifest.",
        "DynamoDB CdcGlobals lock — one CDC job per domain; overlapping runs dropped",
        "Check Step Functions execution history; verify nightly trigger Facets_BatchJobComplete_<OrderNumber>_<timestamp>.txt",
    ),
    125: (
        "Explain the dual gold path: Interop vs CDP.",
        "Interop: gold.fm_claim, gold.fm_claim_item — filtered for CMS-9115 SAM/FHIR (75 groups, Medicare, no dental). CDP: gold.fm_claim_cambia, gold.fm_claim_item_cambia — full 1:1 silver mapping + data signature bitmap for customer data platform.",
        "silver.claim_facets (Interop filtered) vs silver.claim_facets_cambia (CDP unfiltered)",
        "Row count ratio CDP/Interop > 1 due to dental + non-Medicare claims retained in CDP only",
        "Never merge Interop and CDP paths; separate pipespecs and downstream consumers.",
    ),
    251: (
        "How does SFTP landing and inbound transfer work?",
        "Encrypted files + manifest → Abacus SFTP / connector landing zone → NextGen raw S3 (cambia02). Catalog: ng-abacus-inbound-infra, config/repo-rules/transporters/sftp.yaml. Nightly batch trigger file dropped to SFTP kicks CDC immediately after Cambia batch.",
        "Manifest path: cambia/facets/cambia/claims/extension/incremental/*/*manifest.json",
        "SFTP connector logs; S3 object listing under cambia02 raw prefix",
        "Validate file count matches manifest (~25 files per batch) before orchestration trigger.",
    ),
    391: (
        "How does SQL Server CDC work on the Facets read replica?",
        "Cambia on-prem Facets SQL Server 2016 CDC-enabled read replica. CDC captures inserts/updates/deletes; facets-core converts to unique change IDs for idempotent JSON partitions.",
        "Claim types: M/H medical, D dental. Status codes: 11=pended, 15=error, 01=pre-final, 02=final, 91=adjusted.",
        "Verify CDC latency on replica; compare LSN watermark in CdcGlobals",
        "Never run heavy queries on primary; read replica only for CDC extraction.",
    ),
    536: (
        "What is the cambia02 tenant and cutover state?",
        "NextGen tenant label cambia02. Pipeline spans facets-core (bespoke, outside HITRUST) through ng-pipelines-cambia medallion. Confirm live schedule and 1.0 vs NextGen cutover with #xform-xport for your env.",
        "Historical volume: ~99M claims, ~250M lines from 1/1/2017. Nightly: 70k–120k claims; incremental: 500–1000 tx per 15-min window.",
        "Snowflake egress: bronze → silver → gold chunked history (XFORM-3515)",
        "Document environment-specific workflow IDs before prod changes.",
    ),
}


def slug(s: str) -> str:
    return s.lower().replace(" & ", "-").replace(" — ", "-").replace(" ", "-").replace("/", "")


def default_question(q: int, sec: str, sec_title: str) -> tuple[str, str, str, str, str]:
    topics = {
        "A": "platform ownership and Cambia Facets delivery",
        "B": "TriZetto Facets claim domain, statuses, and Cambia specifics",
        "C": "5-stage architecture and component boundaries",
        "D": "Databricks bronze/silver/gold and SCD2 patterns",
        "E": "SAM/FHIR downstream from gold FM tables",
        "F": "VPN, encryption, HIPAA, and HITRUST boundaries",
        "G": "facets-core CDC, Step Functions, and Batch jobs",
        "H": "Interop vs CDP dual gold filtering",
        "I": "deploy, monitor, and restore Facets pipelines",
        "J": "pipeline KPIs, lag, and batch SLAs",
        "K": "claims lifecycle and RCM handoff from Facets",
        "L": "program management across Cambia and Abacus teams",
        "M": "incident scenarios: missed batch, lock contention, manifest mismatch",
        "N": "Snowflake egress and chunked history loads",
        "O": "ng-orchestration-service manifest triggers",
        "P": "SFTP inbound, landing zone, and file validation",
        "Q": "ng-pipelines-cambia notebooks and pipespecs",
        "R": "Reltio MDM feed from silver Facets",
        "S": "cambia-facets-networking VPN and Palo Alto",
        "T": "SQL Server CDC and Facets source tables",
        "U": "volume profiles and performance at scale",
        "V": "de-identification for analytics paths",
        "W": "MDM golden records from Facets member/provider",
        "X": "when to use Interop vs CDP gold outputs",
        "Y": "CloudWatch, Databricks alerts, delivery monitoring",
        "Z": "GitLab CI, facets-infrastructure Terraform",
        "AA": "governance, audit, and compliance for PHI",
        "AB": "Cambia cutover, env-specific configs, xform coordination",
    }
    topic = topics.get(sec, "Facets Claims pipeline")
    return (
        f"Q{q}. How do you handle {topic} in the Cambia Facets Claims pipeline?",
        f"I apply first-principles ownership on {topic}: define the contract, instrument checkpoints, and tie every failure mode to a runbook. For Facets Claims I never blur Interop and CDP paths or bypass manifest validation.",
        f"cambia02 tenant example: nightly batch 70k–120k claims through CMC_CLCL_CLAIM bronze → silver.unified_timeline_claim → gold.fm_claim (Interop) or gold.fm_claim_cambia (CDP).",
        f"Check Databricks job runs, manifest presence under cambia/facets/cambia/claims/, and CdcGlobals lock state in DynamoDB.",
        f"Escalate to facets-core for CDC issues, ng-orchestration-service for trigger gaps, ng-pipelines-cambia for transform failures.",
    )


def script_for(q: int, sec: str, roles: str) -> str:
    if sec in ("G", "S", "T"):
        lang = "bash"
        body = f"""#!/usr/bin/env bash
# Q{q}: Facets CDC / source proficiency drill
set -euo pipefail
cd {BASE}
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q{q}: CDC trace complete — check intermediate S3 prefix and CdcGlobals lock"""
    elif sec in ("D", "Q", "N"):
        lang = "sql"
        body = f"""-- Q{q}: Databricks Facets medallion check
-- Run in cambia02 workspace (dev/stg first)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows
FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL
SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL
SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL
SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;"""
    elif sec in ("E", "H"):
        lang = "bash"
        body = f"""#!/usr/bin/env bash
# Q{q}: Dual gold / FHIR path check
set -euo pipefail
cd {BASE}
./scripts/compare_interop_cdp_counts.sh
./scripts/validate_gold_fm_schema.sh
echo "Q{q}: Interop vs CDP row counts and dental filter verified"""
    elif sec == "Z":
        lang = "bash"
        body = f"""#!/usr/bin/env bash
# Q{q}: Facets DevOps gate
set -euo pipefail
cd {BASE}
./scripts/ci/run_ci_local.sh
echo "Q{q}: local CI green before facets-infrastructure or ng-pipelines-cambia MR"""
    else:
        lang = "bash"
        body = f"""#!/usr/bin/env bash
# Q{q}: Facets Claims architecture drill
set -euo pipefail
cd {BASE}
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
echo "Q{q}: 5-stage trace + repo map complete\""""
    return f"**Script:** *(builds proficiency: {roles})*\n\n```{lang}\n{body}\n```"


def render_question(q: int, sec: str, sec_title: str, roles: str) -> str:
    if q in QUESTION_BANK:
        title, answer, example, check, fix = QUESTION_BANK[q]
        q_title = title if title.startswith("Q") else f"Q{q}. {title}"
    else:
        q_title, answer, example, check, fix = default_question(q, sec, sec_title)
        q_title = q_title.replace(f"Q{q}. ", f"Q{q}. ")

    if not q_title.startswith("Q"):
        q_title = f"Q{q}. {q_title}"

    check_lines = check if check.startswith("-") else f"- {check}"
    fix_lines = fix if fix.startswith("-") else f"- {fix}"

    return f"""### {q_title}

**Answer:** {answer}

**Example:** {example}

**How to Check:**
{check_lines}

**How to Fix:**
{fix_lines}

{script_for(q, sec, roles)}
"""


def toc_entry(sec: str, title: str, start: int, end: int) -> str:
    anchor = f"section-{sec.lower()}-{slug(title)}-q{start}{end}"
    return f"- [Section {sec}: {title} (Q{start}–{end})](#{anchor})"


def main() -> None:
    lines: list[str] = [
        "# Cambia Facets Claims — Interview Answer Cheat Sheet",
        "",
        "> Cambia on-prem TriZetto Facets → Abacus NextGen (cambia02) | 553 questions + Glossary | First-person, hands-on owner voice",
        f"> **Learn first:** [LEARN_FROM_STEP_1.md](/Users/ashishsingh/CambiaFacetsClaims/Training/LEARN_FROM_STEP_1.md) — start Day 1 before touching prod workflows.",
        "> **Proficiency guarantee:** Complete learning steps + run every **Script** below to reach working proficiency across eight roles.",
        "",
        "## Answer Format",
        "",
        "Each question includes five segments:",
        "",
        "| Segment | Purpose |",
        "|---------|---------|",
        "| **Answer** | What to say in the interview (ownership voice) |",
        "| **Example** | Real scenario from Cambia Facets Claims |",
        "| **How to Check** | Verification steps / commands |",
        "| **How to Fix** | Remediation if check fails |",
        "| **Script** | Runnable code to build role proficiency |",
        "",
        "## Proficiency Role Map (by Section)",
        "",
        "| Target Role | Primary Sections | Script Languages |",
        "|-------------|------------------|------------------|",
        "| **Associate Solution Architect** | A, C, H, J, K, L, M, AB | bash, architecture trace |",
        "| **FHIR Engineer** | E, H, AB | bash, FHIR validation |",
        "| **Data Engineer** | D, G, J, N, O, P, Q, R, T, U, AB | PySpark, SQL, Delta |",
        "| **Forward Deployed Engineer** | A, F, I, L, M, P, S, Y, AB | bash, Terraform, VPN runbooks |",
        "| **Intermediate Associate Programmer** | D, G, O, P, Q, T, Z | Python, bash, SQL, YAML |",
        "| **DevOps Engineer** | I, S, Z, AB | GitLab CI, Terraform, facets-infrastructure |",
        "| **MDM Engineer** | R, W | SQL, Reltio API patterns |",
        "| **Integration Engineer** | G, P, O | Step Functions, SFTP, manifest contracts |",
        "",
        "## Implementation Phases → Role Outcomes",
        "",
        "| Phase | You Will Proficiently... |",
        "|-------|--------------------------|",
        "| **Phase 0** | Trace 5-stage architecture; map repos; validate manifest patterns; local CI green |",
        "| **Phase 1** | Understand CDC extraction, SFTP landing, bronze SCD2 loads |",
        "| **Phase 2** | Own silver unified timeline and dual gold FM paths |",
        "| **Phase 3** | Operate nightly batch + 4-hr incremental; troubleshoot locks and manifests |",
        "| **Phase 4** | Downstream SAM/FHIR, Snowflake egress, Reltio MDM cutover |",
        "",
        "## Table of Contents",
        "",
        "- [Learn From Step 1 — Learning Guide (start here)](/Users/ashishsingh/CambiaFacetsClaims/Training/LEARN_FROM_STEP_1.md)",
        "- [Glossary — Key Terms (A–Z)](#glossary)",
    ]

    for sec, title, start, end, _ in SECTIONS:
        lines.append(toc_entry(sec, title, start, end))

    for sec, title, start, end, roles in SECTIONS:
        anchor = f"section-{sec.lower()}-{slug(title)}-q{start}{end}"
        lines.extend(["", f"## Section {sec}: {title}", ""])
        for q in range(start, end + 1):
            lines.append(render_question(q, sec, title, roles))

    lines.extend(["", "## Glossary", ""])
    lines.extend(glossary())
    lines.append("")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT} ({len(lines)} lines, 553 questions)")


def glossary() -> list[str]:
    terms = [
        ("cambia02", "Platform", "NextGen tenant label for Cambia Facets data lake", "All bronze/silver/gold tables scoped to cambia02 catalog"),
        ("Facets", "Source", "TriZetto Facets claims admin on-prem SQL Server 2016", "CMC_CLCL_CLAIM header table in CDC replica"),
        ("facets-core", "CDC", "Bespoke CDC extraction repo (GitLab abacusinsights/facets-integration)", "Step Functions + Batch SQL → JSON partitions"),
        ("facets-infrastructure", "CDC", "Terraform/IaC for Facets CDC AWS resources", "Intermediate S3, DynamoDB CdcGlobals, VPN endpoints"),
        ("CdcGlobals", "CDC", "DynamoDB lock table — one CDC job per domain", "Overlapping incremental runs dropped when lock held"),
        ("Claims Incremental", "CDC", "Micro-batch CDC ~every 4 hours daytime", "500–1000 tx per 15-min window; spikes during nightly batch"),
        ("Claims Historical", "CDC", "Backfill CDC from 1/1/2017", "~99M claims, ~250M lines historical volume"),
        ("PPL", "CDC", "Provider Performance List appended separately", "PPL Incremental/Historical process types"),
        ("manifest.json", "Landing", "Batch metadata listing encrypted JSON files + checksums", "Path: cambia/facets/cambia/claims/extension/incremental/*/*manifest.json"),
        ("AIR library", "Runtime", "ng-abacus-insights-runtime — encryption, manifest, SCD2 sinks", "Shared generic logic; pipelines import, never duplicate"),
        ("ng-orchestration-service", "Orchestration", "Manifest-triggered bronze/silver/gold workflow orchestration", "Monitors Facets CDC delivery; catalog orchestration.yaml"),
        ("ng-pipelines-cambia", "Pipelines", "Bronze/silver/gold notebooks + pipespecs for Cambia", "silver.unified_timeline_claim, gold.fm_claim* tables"),
        ("ng-abacus-inbound-infra", "Landing", "SFTP/connector landing zone infrastructure", "Catalog: transporters/sftp.yaml"),
        ("CMC_CLCL_CLAIM", "Bronze", "Facets claim header bronze SCD2 table", "Primary claim grain for unified timeline"),
        ("CMC_CDML_CL_LINE", "Bronze", "Medical claim line bronze table", "M/H claim types"),
        ("CMC_CDDL_CL_LINE", "Bronze", "Dental claim line bronze table", "D claim type; filtered from Interop gold"),
        ("SCD Type 2", "Bronze", "Slowly changing dimension history in bronze", "AIR library sink pattern; _is_current flag"),
        ("silver.unified_timeline_claim", "Silver", "SCD2 unified incremental claims timeline", "Tracks claim versions across batches"),
        ("silver.claim_facets", "Silver", "Interop/SAM domain table — group + date filtered", "Feeds gold.fm_claim Interop path"),
        ("silver.claim_facets_cambia", "Silver", "CDP domain table — no filtering", "Feeds gold.fm_claim_cambia"),
        ("gold.fm_claim", "Gold", "Interop FM — CMS-9115 SAM/FHIR (75 groups, Medicare)", "Dental excluded before SAM load"),
        ("gold.fm_claim_cambia", "Gold", "CDP FM — full 1:1 silver + data signature bitmap", "All claim types retained"),
        ("ng-pipelines-onyx", "Downstream", "DM 2.0 → FHIR workflows for SAM load", "Claim, ClaimCoverage, ClaimDiagnosis resources"),
        ("cambia02-claims-dataingestion-workflow", "Downstream", "Onyx FHIR ingestion workflow name", "CMS-9115 SAM → FHIR → Firely path"),
        ("Snowflake egress", "Downstream", "bronze → silver → gold → Snowflake chunked loads", "XFORM-3515 history migration pattern"),
        ("Reltio", "MDM", "Silver Facets feeds Reltio tenant", "Migration from 1.0 connector in progress"),
        ("cambia-facets-networking", "Network", "Dedicated AWS account 697410135799 for VPN", "Palo Alto site-to-site to on-prem Facets"),
        ("Facets_BatchJobComplete", "Trigger", "Nightly trigger file after Cambia batch", "Facets_BatchJobComplete_<OrderNumber>_<timestamp>.txt on SFTP"),
        ("HITRUST boundary", "Security", "facets-core CDC runs outside HITRUST boundary", "Encryption before landing in NextGen zone"),
        ("Claim status 02", "Domain", "Facets CLCL status final", "11=pended, 15=error, 01=pre-final, 91=adjusted"),
        ("DevOps Engineer", "Role", "CI/CD, facets-infrastructure, deployment gates", "run_ci_local.sh before MR"),
        ("Data Engineer", "Role", "Medallion pipelines, SCD2, unified timeline", "ng-pipelines-cambia owner"),
    ]
    lines = [
        "> Key terms for Cambia Facets Claims — organized with description and example.",
        "",
        "| Term | Category | Description | Example |",
        "|------|----------|-------------|---------|",
    ]
    for term, cat, desc, ex in terms:
        lines.append(f"| **{term}** | {cat} | {desc} | {ex} |")
    lines.extend([
        "",
        "### Glossary Category Index",
        "",
        "| Category | Terms Count | Key Terms |",
        "|----------|-------------|-----------|",
        "| CDC & Source | 8 | facets-core, CdcGlobals, Claims Incremental, PPL |",
        "| Landing & Orchestration | 5 | manifest.json, AIR, ng-orchestration-service, SFTP |",
        "| Medallion | 10 | bronze CMC_*, silver unified timeline, dual gold FM |",
        "| Downstream | 5 | Onyx FHIR, Snowflake, Reltio |",
        "| Network & Security | 3 | cambia-facets-networking, HITRUST, encryption |",
        "| Domain | 4 | claim statuses, medical/dental, volumes |",
        "",
        "---",
    ])
    return lines


if __name__ == "__main__":
    main()
