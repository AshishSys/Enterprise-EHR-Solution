#!/usr/bin/env python3
"""Generate Cambia Facets Claims Interview Cheat Sheet — aligned to 4 proficiency pillars."""

from __future__ import annotations

from pathlib import Path

OUT = Path("/Users/ashishsingh/Interview/Cambia_Facets_Claims_Interview_Cheat_Sheet.md")
BASE = "/Users/ashishsingh/CambiaFacetsClaims/Training/facets-claims"

# (section, title, q_start, q_end, roles, pillar)
SECTIONS: list[tuple[str, str, int, int, str, str]] = [
    ("A", "Opening & E2E Implementation Role Fit", 1, 10, "E2E Implementation Lead | Forward Deployed Engineer", "P1"),
    ("B", "TriZetto Facets Claims Domain SME", 11, 28, "Facets/TriZetto SME | Data Engineer", "P2"),
    ("C", "E2E Architecture & Implementation Design", 29, 45, "E2E Implementation Lead | Solution Architect", "P1"),
    ("D", "Medallion Implementation — Bronze/Silver/Gold", 46, 73, "Data Engineer | E2E Implementation Lead", "P1"),
    ("E", "FHIR/SAM API Implementation & Postman Validation", 74, 94, "Postman/API Engineer | FHIR Engineer", "P1+P4"),
    ("F", "Migration Security & On-Prem Compliance", 95, 112, "Migration Engineer | Forward Deployed Engineer", "P3"),
    ("G", "CDC Implementation — facets-core", 113, 124, "E2E Implementation Lead | Migration Engineer", "P1+P3"),
    ("H", "Dual Gold Implementation Paths", 125, 141, "Data Engineer | E2E Implementation Lead", "P1"),
    ("I", "E2E Operations & Troubleshooting", 142, 154, "E2E Implementation Lead | Forward Deployed Engineer", "P1"),
    ("J", "Implementation KPIs & Delivery Metrics", 155, 162, "E2E Implementation Lead | Data Engineer", "P1"),
    ("K", "Facets Claim Lifecycle & RCM SME", 163, 172, "Facets/TriZetto SME | Solution Architect", "P2"),
    ("L", "On-Prem → Cloud Migration Program Leadership", 173, 185, "Migration Engineer | Solution Architect", "P3"),
    ("M", "E2E Scenario Troubleshooting", 186, 195, "E2E Implementation Lead | Forward Deployed Engineer", "P1"),
    ("N", "Snowflake Egress Cloud Migration", 196, 205, "Migration Engineer | Data Engineer", "P3"),
    ("O", "Orchestration APIs — ng-orchestration-service", 206, 250, "Postman/API Engineer | Integration Engineer", "P1+P4"),
    ("P", "On-Prem Handoff — SFTP & Landing Zone", 251, 295, "Migration Engineer | Integration Engineer", "P3"),
    ("Q", "Databricks Engineering Implementation", 296, 330, "Data Engineer | E2E Implementation Lead", "P1"),
    ("R", "MDM/Reltio Cloud Migration", 331, 360, "Migration Engineer | Facets/TriZetto SME", "P3"),
    ("S", "VPN & On-Prem Network Migration", 361, 390, "Migration Engineer | Forward Deployed Engineer", "P3"),
    ("T", "SQL Server CDC & Facets Source SME", 391, 415, "Facets/TriZetto SME | Migration Engineer", "P2+P3"),
    ("U", "Production Scale & TriZetto Volume Profiles", 416, 445, "Facets/TriZetto SME | Data Engineer", "P2"),
    ("V", "De-Identification for Migration Analytics", 446, 455, "Migration Engineer | Data Engineer", "P3"),
    ("W", "Master Data Management — Facets Entities", 456, 465, "Facets/TriZetto SME | Migration Engineer", "P2+P3"),
    ("X", "Interop vs CDP Implementation Comparison", 466, 473, "E2E Implementation Lead | Data Engineer", "P1"),
    ("Y", "Observability & Delivery Monitoring", 474, 485, "E2E Implementation Lead | Forward Deployed Engineer", "P1"),
    ("Z", "DevOps & CI/CD for Cloud Migration", 486, 515, "DevOps Engineer | Migration Engineer", "P1+P3"),
    ("AA", "Governance & Migration Compliance", 516, 535, "Migration Engineer | Solution Architect", "P3"),
    ("AB", "Postman Collections & Cambia Cutover", 536, 553, "Postman/API Engineer | Migration Engineer", "P4+P3"),
]

PILLAR_LABELS = {
    "P1": "E2E Implementation Proficiency",
    "P2": "Facets & TriZetto SME",
    "P3": "On-Prem → Cloud Migration",
    "P4": "Postman API Role",
}

QUESTION_BANK: dict[int, tuple[str, str, str, str, str]] = {
    1: (
        "Tell me about your end-to-end implementation experience with payer claims migration pipelines.",
        "I led Cambia Facets Claims implementation from on-prem TriZetto Facets through VPN, bespoke CDC, encrypted landing, Databricks medallion, dual gold FM, and downstream SAM/FHIR + Snowflake. I personally owned manifest triggers, bronze SCD2 loads, and Postman-validated API handoffs—not architecture slides alone.",
        "Nightly Facets_BatchJobComplete trigger → ng-orchestration-service → bronze CMC_CLCL_CLAIM → silver.unified_timeline_claim → gold.fm_claim → Postman-validated FHIR Claim resources.",
        "Run phase0_architecture_trace.sh; verify Databricks job chain green for cambia02; Postman collection smoke on orchestration + FHIR endpoints.",
        "Map all 5 implementation stages to owners and Postman smoke tests before sprint 1.",
    ),
    2: (
        "What makes you a TriZetto Facets SME for this migration?",
        "I know Facets claim grain (CMC_CLCL_CLAIM header, CMC_CDML/CMC_CDDL line tables), CLCL status lifecycle (11/15/01/02/91), medical vs dental types (M/H vs D), and how Cambia nightly batch timing drives CDC trigger files—not just cloud pipeline mechanics.",
        "A pended claim (status 11) adjusting to final (02) creates two SCD2 versions in bronze and a new row in silver.unified_timeline_claim.",
        "Query bronze.cmc_clst_status joins; compare CLCL status distribution pre/post batch.",
        "Pair with Cambia claims ops for status code changes; never assume CMS semantics map 1:1 to Facets CLCL codes.",
    ),
    3: (
        "How do you approach on-prem client migration to cloud for Facets claims?",
        "I treat migration as phased cutover: VPN connectivity first, then historical CDC backfill (~99M claims), then incremental + nightly trigger parity, then medallion validation, then downstream Snowflake/Reltio with rollback checkpoints at each gate.",
        "facets-core runs outside HITRUST; encryption at CDC output before SFTP landing in cambia02 NextGen zone.",
        "Document 1.0 vs NextGen cutover state with #xform-xport; verify VPN uptime and CdcGlobals lock behavior during parallel run.",
        "Never big-bang cutover; maintain parallel validation window with row-count and signature bitmap checks.",
    ),
    4: (
        "What is your Postman API role in the Facets Claims implementation?",
        "I use Postman to validate orchestration callbacks, manifest-trigger endpoints, SAM/FHIR resource shapes, and cutover smoke tests—before declaring a migration phase complete. Collections are environment-scoped (dev/stg/prd) with no PHI in saved examples.",
        "Postman collection: orchestration manifest-received → Databricks job status poll → FHIR Claim GET by resource ID → assert US Core profiles.",
        "newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json",
        "Store tokens in Postman environment secrets; never commit credentials or member IDs to collection JSON.",
    ),
    11: (
        "Explain TriZetto Facets claim header and line table relationships.",
        "CMC_CLCL_CLAIM is the claim header grain. Medical lines live in CMC_CDML_CL_LINE (M/H types); dental in CMC_CDDL_CL_LINE (D type). Diagnosis, status, member, and subscriber tables join at claim_id. This is the source shape facets-core partitions into ~25 JSON files per CDC batch.",
        "One CLCL claim with 3 medical lines and 1 dental line → header JSON + CDML partition + CDDL partition + diagnosis partition in manifest.",
        "SELECT claim_id, COUNT(*) FROM bronze.cmc_cdml_cl_line GROUP BY claim_id LIMIT 10",
        "Never flatten dental into medical lines; Interop gold filters dental at FM layer, CDP retains all.",
    ),
    29: (
        "Walk through the E2E implementation architecture you would own.",
        "Stage 1: on-prem Facets SQL Server via Palo Alto VPN. Stage 2: facets-core CDC → encrypted JSON + manifest. Stage 3: SFTP landing → bronze SCD2 (AIR). Stage 4: silver unified timeline → dual gold FM. Stage 5: SAM/FHIR + Snowflake + Reltio. Postman validates each handoff.",
        "Implementation exit criteria per stage: VPN up, CDC manifest valid, bronze row counts match, gold Interop/CDP ratio expected, Postman FHIR smoke green.",
        "Run all phase0 scripts + Postman smoke collection against dev.",
        "Whiteboard all 5 stages with repo, owner, and Postman check at each boundary.",
    ),
    46: (
        "How do you implement bronze ingestion for Facets claims?",
        "Manifest-triggered Databricks workflows load encrypted JSON into 44+ bronze SCD2 tables via AIR library. I validate each batch: manifest file count (~25), checksums, and CMC_CLCL_CLAIM row delta vs CDC change IDs before promoting silver.",
        "420 Facets bronze tables in prod; key tables: CMC_CLCL_CLAIM, CMC_CDML_CL_LINE, CMC_CDDL_CL_LINE, CMC_CLST_STATUS, CMC_MEME_MEMBER, CMC_SBSB_SUBSC.",
        "SELECT COUNT(*) FROM bronze.cmc_clcl_claim WHERE _is_current = true",
        "Fail closed on manifest/schema mismatch; never run bronze without valid manifest.",
    ),
    74: (
        "How do you use Postman to validate FHIR/SAM output from gold Facets tables?",
        "After gold.fm_claim load, I run Postman requests against FITE/Firely (or dev FHIR gateway): GET Claim, ClaimCoverage, ClaimDiagnosis by test member; assert meta.profile US Core URLs; verify dental claims absent from Interop path but present in CDP validation collection.",
        "Collection folder: Interop Claims (75-group filter) vs CDP Claims (full set); separate environment variables for each path.",
        "newman run postman/fhir-claims-interop.json --folder 'Claim Read' -e postman/env/stg.json",
        "Rotate test patient IDs via environment; never hardcode PHI in collection bodies.",
    ),
    95: (
        "What security controls apply during on-prem to cloud migration?",
        "facets-core CDC is outside HITRUST boundary. Encryption before landing; VPN-only path to on-prem replica; IAM least privilege for air-cd on KMS keys; audit logs without PHI; Postman environments use synthetic test IDs only.",
        "KMS decrypt on landing zone keys granted to air-cd deployment role per workspace rules.",
        "Verify encryption on intermediate S3 objects; confirm no plaintext secrets in facets-infrastructure Terraform.",
        "Obtain security/compliance review before prod cutover; fail closed on missing secrets.",
    ),
    113: (
        "How do you implement Facets CDC extraction?",
        "SQL Server CDC on read replica → unique change IDs → partitioned JSON → encryption → manifest.json. Step Functions + Lambda + Batch. One job per domain via DynamoDB CdcGlobals lock. Nightly Facets_BatchJobComplete trigger file kicks CDC after Cambia batch.",
        "~25 JSON files per batch; intermediate S3 abacus-facets-intermediate-<env>/claims-incremental/.",
        "Step Functions execution history; CdcGlobals lock state; manifest at cambia/facets/cambia/claims/extension/incremental/*/*manifest.json",
        "Never query Facets primary; replica only. Drop overlapping CDC runs when lock held.",
    ),
    173: (
        "How do you lead an on-prem Facets client migration program?",
        "I run phased gates: (1) network/VPN, (2) historical backfill parity, (3) incremental schedule parity, (4) medallion validation, (5) downstream cutover. Each gate has row-count acceptance, Postman smoke, and rollback plan documented with Cambia + Abacus owners.",
        "Parallel run window: compare on-prem Facets report totals vs cambia02 gold.fm_claim_cambia signature bitmap for sample periods.",
        "Migration checklist in plan.md; sign-off from #xform-xport before prod promotion.",
        "Weekly steering with claim ops (Facets SME) and platform (E2E owner); escalate VPN/CDC as P1.",
    ),
    251: (
        "How does on-prem handoff work via SFTP and landing zone?",
        "Encrypted JSON + manifest land on Abacus SFTP / connector zone → NextGen raw S3 (cambia02). ng-abacus-inbound-infra owns landing infra. Nightly trigger file Facets_BatchJobComplete_* on SFTP signals Cambia batch complete and kicks CDC immediately.",
        "Validate ~25 files match manifest before ng-orchestration-service triggers bronze.",
        "SFTP connector logs; S3 listing under cambia02 raw prefix; Postman callback to orchestration manifest-received endpoint.",
        "Reject batches with manifest/file count mismatch; quarantine for facets-core replay.",
    ),
    361: (
        "How do you implement VPN connectivity for on-prem Facets migration?",
        "Site-to-site VPN via Palo Alto firewalls into dedicated AWS account cambia-facets-networking (697410135799). This is the only path from cloud CDC to on-prem SQL Server 2016 read replica. VPN flap = CDC stall; monitor as migration P1.",
        "Network diagram: Cambia on-prem → Palo Alto → cambia-facets-networking → facets-core Step Functions.",
        "VPN tunnel status dashboard; CDC lag metric correlated with tunnel uptime.",
        "Runbook for VPN failover; never route Facets queries over public internet.",
    ),
    391: (
        "As a Facets source SME, how does SQL Server CDC work on the read replica?",
        "CDC captures I/U/D on Facets tables; facets-core converts LSN watermarks to unique change IDs for idempotent JSON. Claim types: M/H medical, D dental. Status: 11=pended, 15=error, 01=pre-final, 02=final, 91=adjusted.",
        "Incremental: 500–1000 tx per 15-min window daytime; nightly batch 70k–120k claims spikes CDC volume.",
        "Compare CdcGlobals LSN watermark vs replica CDC latency; validate change ID monotonicity.",
        "Read replica only; coordinate with Cambia DBA for CDC retention and disk capacity during historical backfill.",
    ),
    536: (
        "What Postman collections do you maintain for Cambia Facets cutover?",
        "Three collections: (1) Orchestration — manifest trigger, job status, delivery monitor; (2) FHIR Interop — Claim/Coverage/Diagnosis reads for 75-group filter; (3) FHIR CDP — full claim set validation. Environment files per cambia02 dev/stg/prd with synthetic IDs.",
        "newman run postman/cambia-facets-cutover-gate.json -e postman/env/prd-smoke.json --bail",
        "Cutover gate: all Postman folders green + row-count parity + no open P1 incidents.",
        "Confirm workflow IDs and base URLs with #xform-xport before updating environment variables.",
    ),
}


def slug(s: str) -> str:
    return s.lower().replace(" & ", "-").replace(" — ", "-").replace(" ", "-").replace("/", "").replace("→", "to")


def default_question(q: int, sec: str, sec_title: str, pillar: str) -> tuple[str, str, str, str, str]:
    topics = {
        "A": "E2E implementation ownership and delivery accountability",
        "B": "TriZetto Facets claim domain, CMC tables, and status lifecycle",
        "C": "E2E architecture design and implementation boundaries",
        "D": "medallion layer implementation — bronze SCD2 through dual gold",
        "E": "FHIR/SAM API implementation and Postman contract validation",
        "F": "migration security, HITRUST boundary, and encryption handoff",
        "G": "facets-core CDC implementation and Batch orchestration",
        "H": "Interop vs CDP dual gold implementation and filtering",
        "I": "E2E deploy, monitor, restore, and incident response",
        "J": "implementation KPIs, batch SLAs, and delivery metrics",
        "K": "Facets claim lifecycle, adjustment logic, and RCM bridge",
        "L": "on-prem to cloud migration program leadership and cutover gates",
        "M": "E2E incident scenarios — missed batch, lock contention, manifest mismatch",
        "N": "Snowflake egress as part of cloud migration cutover",
        "O": "orchestration API contracts and Postman validation for ng-orchestration-service",
        "P": "on-prem SFTP handoff, landing zone, and migration file validation",
        "Q": "ng-pipelines-cambia Databricks implementation and pipespecs",
        "R": "Reltio MDM cloud migration from Facets silver feeds",
        "S": "VPN and on-prem network migration for Facets connectivity",
        "T": "SQL Server CDC and Facets source table SME knowledge",
        "U": "TriZetto production volumes and scale profiles",
        "V": "de-identification for migration analytics and safe harbor",
        "W": "MDM golden records from Facets member and provider entities",
        "X": "Interop vs CDP implementation path selection",
        "Y": "observability, delivery monitoring, and migration health dashboards",
        "Z": "DevOps, CI/CD, and IaC for cloud migration promotion",
        "AA": "governance, audit, and migration compliance sign-off",
        "AB": "Postman collections, cutover smoke tests, and cambia02 env promotion",
    }
    topic = topics.get(sec, "Facets Claims implementation")
    pl = PILLAR_LABELS.get(pillar.split("+")[0], pillar)
    return (
        f"How do you demonstrate proficiency in {topic}?",
        f"I own {topic} with measurable exit criteria: documented runbook, automated check, and Postman or SQL proof where applicable. Pillar: {pl}.",
        f"cambia02 example: CMC_CLCL_CLAIM → unified_timeline → gold.fm_claim; Postman smoke green before phase sign-off.",
        f"Run relevant Script below; verify Databricks job history and Postman/newman exit 0.",
        f"Escalate to facets-core (CDC), ng-orchestration-service (API), or ng-pipelines-cambia (transform) by failure layer.",
    )


def script_for(q: int, sec: str, roles: str) -> str:
    if sec in ("E", "O", "AB"):
        lang = "bash"
        body = f"""#!/usr/bin/env bash
# Q{q}: Postman API validation drill
set -euo pipefail
cd {BASE}
./scripts/postman_smoke_check.sh
# With Newman installed:
# newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail"""
    elif sec in ("G", "S", "T"):
        lang = "bash"
        body = f"""#!/usr/bin/env bash
# Q{q}: CDC / on-prem source implementation drill
set -euo pipefail
cd {BASE}
./scripts/phase0_architecture_trace.sh
./scripts/validate_manifest_pattern.sh
echo "Q{q}: CDC + VPN path verified"""
    elif sec in ("D", "Q", "N"):
        lang = "sql"
        body = f"""-- Q{q}: Medallion implementation check (cambia02 dev/stg)
SELECT 'bronze_claims' AS layer, COUNT(*) AS rows FROM bronze.cmc_clcl_claim WHERE _is_current = true
UNION ALL SELECT 'silver_unified', COUNT(*) FROM silver.unified_timeline_claim
UNION ALL SELECT 'gold_interop', COUNT(*) FROM gold.fm_claim
UNION ALL SELECT 'gold_cdp', COUNT(*) FROM gold.fm_claim_cambia;"""
    elif sec in ("F", "P", "L", "AA"):
        lang = "bash"
        body = f"""#!/usr/bin/env bash
# Q{q}: On-prem → cloud migration gate check
set -euo pipefail
cd {BASE}
./scripts/migration_cutover_checklist.sh
echo "Q{q}: migration gate checklist complete"""
    elif sec in ("B", "K", "U", "W"):
        lang = "sql"
        body = f"""-- Q{q}: TriZetto Facets SME — claim domain check
SELECT clcl_status, claim_type, COUNT(*) AS claims
FROM bronze.cmc_clcl_claim
WHERE _is_current = true
GROUP BY clcl_status, claim_type
ORDER BY claims DESC;"""
    elif sec == "Z":
        lang = "bash"
        body = f"""#!/usr/bin/env bash
# Q{q}: DevOps / migration CI gate
set -euo pipefail
cd {BASE}
./scripts/ci/run_ci_local.sh"""
    else:
        lang = "bash"
        body = f"""#!/usr/bin/env bash
# Q{q}: E2E implementation drill
set -euo pipefail
cd {BASE}
./scripts/phase0_architecture_trace.sh
./scripts/phase0_repo_map.sh
./scripts/compare_interop_cdp_counts.sh"""
    return f"**Script:** *(builds proficiency: {roles})*\n\n```{lang}\n{body}\n```"


def render_question(q: int, sec: str, sec_title: str, roles: str, pillar: str) -> str:
    if q in QUESTION_BANK:
        title, answer, example, check, fix = QUESTION_BANK[q]
        q_title = title if title.startswith("Q") else f"Q{q}. {title}"
    else:
        title, answer, example, check, fix = default_question(q, sec, sec_title, pillar)
        q_title = f"Q{q}. {title}"

    if not q_title.startswith("Q"):
        q_title = f"Q{q}. {q_title}"

    check_lines = check if check.startswith("-") else f"- {check}"
    fix_lines = fix if fix.startswith("-") else f"- {fix}"

    return f"""### {q_title}

**Pillar:** {pillar} — {", ".join(PILLAR_LABELS.get(p, p) for p in pillar.split("+"))}

**Answer:** {answer}

**Example:** {example}

**How to Check:**
{check_lines}

**How to Fix:**
{fix_lines}

{script_for(q, sec, roles)}
"""


def toc_entry(sec: str, title: str, start: int, end: int, pillar: str) -> str:
    anchor = f"section-{sec.lower()}-{slug(title)}-q{start}{end}"
    return f"- [Section {sec}: {title} (Q{start}–{end}) · {pillar}](#{anchor})"


def main() -> None:
    lines: list[str] = [
        "# Cambia Facets Claims — Interview Answer Cheat Sheet",
        "",
        "> TriZetto Facets on-prem → Abacus NextGen (cambia02) | 553 questions + Glossary",
        "> **Aligned to 4 proficiency pillars:** E2E Implementation · Facets/TriZetto SME · On-Prem→Cloud Migration · Postman API Role",
        f"> **Learn first:** [LEARN_FROM_STEP_1.md](/Users/ashishsingh/CambiaFacetsClaims/Training/LEARN_FROM_STEP_1.md)",
        "",
        "## Four Proficiency Pillars",
        "",
        "| Pillar | Focus | Primary Sections | Exit Proof |",
        "|--------|-------|------------------|------------|",
        "| **P1 — E2E Implementation** | Own full pipeline delivery | A, C, D, G, H, I, M, Q, X, Y, Z | All phase0 scripts green; Databricks chain validated |",
        "| **P2 — Facets/TriZetto SME** | Claim domain, CMC tables, volumes | B, K, T, U, W | Explain CLCL lifecycle + table joins without notes |",
        "| **P3 — On-Prem→Cloud Migration** | VPN, cutover, phased gates | F, L, N, P, R, S, V, AA, AB | migration_cutover_checklist.sh + parallel-run parity |",
        "| **P4 — Postman API Role** | Orchestration + FHIR contract testing | E, O, AB | newman smoke green on dev/stg before promotion |",
        "",
        "## Answer Format",
        "",
        "| Segment | Purpose |",
        "|---------|---------|",
        "| **Pillar** | Which proficiency area this question proves |",
        "| **Answer** | What to say (ownership voice) |",
        "| **Example** | Real Cambia Facets scenario |",
        "| **How to Check** | Verification steps / Postman / SQL |",
        "| **How to Fix** | Remediation if check fails |",
        "| **Script** | Runnable proof for role proficiency |",
        "",
        "## Role Map (by Pillar)",
        "",
        "| Target Role | Pillars | Primary Sections |",
        "|-------------|---------|------------------|",
        "| **E2E Implementation Lead** | P1 | A, C, D, G, H, I, M, Q, Y |",
        "| **Facets/TriZetto SME** | P2 | B, K, T, U, W |",
        "| **Migration Engineer** | P3 | F, L, N, P, R, S, AA |",
        "| **Postman/API Engineer** | P4 | E, O, AB |",
        "| **Data Engineer** | P1+P2 | D, Q, H, X |",
        "| **Forward Deployed Engineer** | P1+P3 | I, M, S, P |",
        "| **DevOps Engineer** | P1+P3 | Z |",
        "",
        "## Implementation Phases",
        "",
        "| Phase | Pillar | You Will Proficiently... |",
        "|-------|--------|--------------------------|",
        "| **Phase 0** | P1 | Trace E2E architecture; run local CI; map repos |",
        "| **Phase 1** | P2+P3 | Speak Facets domain; implement CDC + VPN path |",
        "| **Phase 2** | P1 | Build bronze→gold medallion; dual FM paths |",
        "| **Phase 3** | P4 | Postman collections for orchestration + FHIR smoke |",
        "| **Phase 4** | P3+P4 | Migration cutover gates; newman prod smoke; Snowflake/Reltio |",
        "",
        "## Table of Contents",
        "",
        "- [Learn From Step 1](/Users/ashishsingh/CambiaFacetsClaims/Training/LEARN_FROM_STEP_1.md)",
        "- [Postman API Role Guide](/Users/ashishsingh/CambiaFacetsClaims/docs/POSTMAN_API_ROLE.md)",
        "- [Glossary](#glossary)",
    ]

    for sec, title, start, end, _, pillar in SECTIONS:
        lines.append(toc_entry(sec, title, start, end, pillar))

    for sec, title, start, end, roles, pillar in SECTIONS:
        pl_names = ", ".join(PILLAR_LABELS.get(p, p) for p in pillar.split("+"))
        lines.extend(["", f"## Section {sec}: {title}", "", f"> **Pillar:** {pillar} — {pl_names}", ""])
        for q in range(start, end + 1):
            lines.append(render_question(q, sec, title, roles, pillar))

    lines.extend(["", "## Glossary", ""])
    lines.extend(glossary())
    lines.append("")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")


def glossary() -> list[str]:
    terms = [
        ("E2E Implementation", "P1", "Full pipeline delivery ownership from CDC through downstream", "Phase gates with script + Postman proof at each stage"),
        ("TriZetto Facets", "P2", "Cambia on-prem claims admin system on SQL Server 2016", "CMC_CLCL_CLAIM header; M/H medical, D dental"),
        ("CMC_CLCL_CLAIM", "P2", "Facets claim header bronze SCD2 table", "Primary grain for unified_timeline_claim"),
        ("CLCL status 02", "P2", "Facets final claim status", "11=pended, 15=error, 01=pre-final, 91=adjusted"),
        ("On-Prem Migration", "P3", "Phased cutover from Facets on-prem to cambia02 cloud", "VPN → historical backfill → incremental parity → downstream"),
        ("HITRUST boundary", "P3", "facets-core CDC outside HITRUST; encrypt before landing", "Encryption at JSON output before SFTP"),
        ("cambia-facets-networking", "P3", "AWS account 697410135799 for Palo Alto VPN", "Only cloud path to on-prem Facets replica"),
        ("Postman Collection", "P4", "API contract tests for orchestration and FHIR endpoints", "newman run with env-scoped synthetic IDs"),
        ("ng-orchestration-service", "P4", "Manifest-triggered workflow API", "Postman: manifest-received → job status poll"),
        ("FHIR Claim validation", "P4", "Postman GET Claim resources from gold.fm_claim SAM load", "Assert US Core meta.profile URLs"),
        ("facets-core", "P1+P3", "Bespoke CDC: SQL Server → JSON + manifest", "Step Functions + Batch"),
        ("manifest.json", "P1+P3", "Batch metadata for encrypted JSON files", "cambia/facets/cambia/claims/extension/incremental/*/*manifest.json"),
        ("gold.fm_claim", "P1", "Interop FM — filtered for CMS-9115 SAM/FHIR", "75 groups, Medicare; dental excluded"),
        ("gold.fm_claim_cambia", "P1", "CDP FM — full silver mapping + signature bitmap", "All claim types for migration parity checks"),
        ("Facets_BatchJobComplete", "P2+P3", "Nightly trigger file after Cambia batch", "Kicks CDC immediately post batch"),
        ("newman", "P4", "CLI runner for Postman collections in CI/cutover gates", "newman run collection.json -e env.json --bail"),
    ]
    lines = [
        "> Glossary organized by proficiency pillar.",
        "",
        "| Term | Pillar | Description | Example |",
        "|------|--------|-------------|---------|",
    ]
    for term, pillar, desc, ex in terms:
        lines.append(f"| **{term}** | {pillar} | {desc} | {ex} |")
    lines.extend(["", "---"])
    return lines


if __name__ == "__main__":
    main()
