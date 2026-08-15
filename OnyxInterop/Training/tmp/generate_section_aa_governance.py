#!/usr/bin/env python3
"""Generate Section AA: AI Governance & CCA Alignment (Q516–535)."""
from pathlib import Path

OUT = Path("/Users/ashishsingh/Interview/Healthcare_Interop_Interview_Cheat_Sheet.md")
ROOT = "/Users/ashishsingh/OnyxInterop/Training/onyx-interop"

QUESTIONS = [
    ("What did the AI Governance MVP session prioritize over broad governance scope?",
     "Focused execution: MLflow tracing, hallucination/bias/trustworthiness metrics via daily batch pipelines — not duplicate PHI/RBAC/version controls.",
     "Leadership: start simple, prove core metrics, then scale.",
     "Read docs/AI_GOVERNANCE_ALIGNMENT.md Part 1",
     "grep -l hallucination configs/ai/governance_metrics.yaml",
     f"cd {ROOT} && cat docs/AI_GOVERNANCE_ALIGNMENT.md | head -40",
     "AI Engineer | Associate Solution Architect"),
    ("What are the three core governance metrics and their phases?",
     "Phase 1: hallucination rate. Phase 2: bias + trustworthiness. Phase 3: real-time/drift (future).",
     "Daily batch to Delta; notebook/CSV reports initially.",
     "cat configs/ai/governance_metrics.yaml | grep -A2 phases",
     "Verify phase_1 metrics list includes hallucination_rate",
     f"cd {ROOT} && python3 -c \"import yaml; print(yaml.safe_load(open('configs/ai/governance_metrics.yaml'))['phases']['phase_1']['metrics'])\"",
     "AI Engineer"),
    ("How does MLflow fit the agreed governance architecture?",
     "Captures inputs/outputs/traces per interaction → Delta audit tables → daily batch computes metrics → queryable results.",
     "Same pattern as Purple Labs eval but using Synthea/golden query set.",
     "Read governance_metrics.py module docstring",
     "python3 pipeline/ai/governance_metrics.py --help",
     f"cd {ROOT} && python3 pipeline/ai/governance_metrics.py",
     "AI Engineer | Data Engineer"),
    ("Why was standalone PHI screening deprioritized for governance?",
     "HIPAA-compliant architecture + Unity AI Gateway PII mask already covers perimeter; duplicate screening adds low value.",
     "De-ID remains for analytics path, not primary governance eval.",
     "grep deprioritized configs/ai/governance_metrics.yaml",
     "Confirm block_external_phi in plan Unity AI Gateway policies",
     f"cd {ROOT} && grep -A3 deprioritized configs/ai/governance_metrics.yaml",
     "AI Engineer | Associate Solution Architect"),
    ("How does FHIR ontology/IG reduce agent hallucinations?",
     "MDP IG registry + MCP read-only allowlist prevents invalid FHIR paths and unknown tables — same principle as ontology in Genie.",
     "Behavioral signal flags invalid tool names in governance batch.",
     "curl localhost:9002/igs | head",
     "MCP tool not in allowlist → behavioral_hallucination_signal true",
     f"cd {ROOT} && python3 pipeline/ai/governance_metrics.py && grep behavioral data/governance/metrics_report.json",
     "AI Engineer | FHIR Engineer"),
    ("What is the controlled query set target for governance eval?",
     "Minimum 50, target 200 questions from golden eval + CMS RAG slice + IG ontology queries.",
     "Compare expected vs actual; compute hallucination rate.",
     "grep controlled_query_set configs/ai/governance_metrics.yaml",
     "trace_count and hallucination_rate in metrics_report.json",
     f"cd {ROOT} && python3 pipeline/ai/governance_metrics.py --traces data/governance/sample_traces.json",
     "AI Engineer"),
    ("What CCA 'aha moment' did the working session identify?",
     "Summarize medical records and surface evidence that supports or changes DRG validation — if one capability must be chosen.",
     "Not CMS interop scope; adjacent Phase 5 product on same platform.",
     "Read AI_GOVERNANCE_ALIGNMENT.md §2.2",
     "Confirm interop plan Phase 4 is CMS agents not DRG audit UI",
     f"grep -n 'CCA' {ROOT}/docs/AI_GOVERNANCE_ALIGNMENT.md | head",
     "Associate Solution Architect | AI Engineer"),
    ("Why must metrics be defined early per CCA session?",
     "Stanislav: metrics reduce hallucinations and give measurable targets before building GenAI features — not only phase-two KPIs.",
     "Interop gates agent UAT on 4E-1 hallucination batch green.",
     "grep 'Metrics defined early' docs/AI_GOVERNANCE_ALIGNMENT.md",
     "Step 8 LEARN_FROM_STEP_1 requires governance before agent UAT",
     f"grep -n 'metrics' /Users/ashishsingh/OnyxInterop/Training/LEARN_FROM_STEP_1.md | head -5",
     "AI Engineer"),
    ("What is the data-before-AI dependency from CCA?",
     "AI work happens after claims + medical records (and SAM marts) exist — cannot fully parallelize on missing tables.",
     "Interop Phase 1 SAM before Phase 4 agents.",
     "Read plan Phase 4 prerequisite in LEARN Step 8",
     "Phase 1 exit criteria before Step 8",
     "grep 'Data before AI' /Users/ashishsingh/OnyxInterop/Training/LEARN_FROM_STEP_1.md",
     "Data Engineer | AI Engineer"),
    ("What risk does synthetic medical data create for demos?",
     "Synthea/PulseEHR subset may not impress auditors or clients if labeled as production-ready — realism gap.",
     "Label readiness level: demo vs POC vs production-client.",
     "grep synthetic docs/AI_GOVERNANCE_ALIGNMENT.md",
     "Demos use source_data/Synthea — document in slide footer",
     f"ls /Users/ashishsingh/OnyxInterop/source_data/Patients.csv",
     "Forward Deployed Engineer | Associate Solution Architect"),
    ("What UI/application architecture gap did CCA surface?",
     "UI appears unowned — AI Engineering can build agents but not full UX/application scaffolding without Replit, Product Eng, or Deepa's team.",
     "Developer Portal covers API registration, not CCA auditor UI.",
     "Read CCA decision log table in alignment doc",
     "RACI shows Unity AI Gateway owner ≠ CCA UI owner",
     f"grep 'UI owner' {ROOT}/docs/AI_GOVERNANCE_ALIGNMENT.md",
     "Associate Solution Architect | AI Engineer"),
    ("What SecOps concern applies to customer-facing AI UI?",
     "External penetration testing and involved security review — Ali noted this could consume much of a 60-day window.",
     "Mapped to security_checklist + DevOps Wiz gate before prod.",
     "grep SecOps docs/AI_GOVERNANCE_ALIGNMENT.md",
     "deploy-prod manual job requires CMS go-live checklist",
     f"grep -i wiz {ROOT}/docs/DEVOPS_CICD.md | head -3",
     "DevOps Engineer | Forward Deployed Engineer"),
    ("Why should implementation (Mahesh) teams join planning earlier?",
     "Client-deployable GenAI needs delivery runbooks, client data access, and operational readiness — not demo-only engineering.",
     "Phase 3 Forward Deployed tabletop includes implementation handoff.",
     "grep implementation docs/AI_GOVERNANCE_ALIGNMENT.md",
     "teach_back Forward Deployed track includes deploy gates",
     "grep Mahesh /Users/ashishsingh/OnyxInterop/Training/onyx-interop/docs/AI_GOVERNANCE_ALIGNMENT.md",
     "Forward Deployed Engineer"),
    ("What build-vs-buy question remains for CCA rules engine?",
     "Coverself has rules engine/UI; Abacus needs CCA-specific audit content — partner vs build undecided.",
     "Not interop CMS rules; leadership decision in alignment doc.",
     "Read §2.4 leadership decision log",
     "No Coverself integration in onyx-interop repo — intentional",
     f"grep -i coverself {ROOT}/docs/AI_GOVERNANCE_ALIGNMENT.md",
     "Associate Solution Architect"),
    ("What are demo vs POC vs production-client readiness levels?",
     "Demo: local Synthea. POC: stage subset + internal users. Production-client: SecOps sign-off + implementation runbook + pen test.",
     "John's production-ready expectation = production-client, not demo.",
     "grep Readiness levels docs/AI_GOVERNANCE_ALIGNMENT.md",
     "CMS go-live checklist only for production-client path",
     f"grep -A5 'Readiness levels' {ROOT}/docs/AI_GOVERNANCE_ALIGNMENT.md",
     "Forward Deployed Engineer | DevOps Engineer"),
    ("How do hallucination detection methods combine?",
     "Statistical similarity (BERTScore/local proxy), LLM-as-judge, SME feedback, behavioral signals (invalid SQL/tools).",
     "governance_metrics.py uses SequenceMatcher locally; Databricks uses embeddings in prod.",
     "Read core_metrics.hallucination_rate.methods in yaml",
     "sample trace t002 flags high hallucination",
     f"cd {ROOT} && python3 pipeline/ai/governance_metrics.py && jq '.hallucination_rate,.rows[1].hallucination_flag' data/governance/metrics_report.json",
     "AI Engineer"),
    ("What replaces Purple Labs in this interop evaluation baseline?",
     "Synthea 10-patient local baseline + PulseEHR 1K subset for scale; same role as controlled governance dataset.",
     "evaluation_dataset: synthea_baseline in yaml.",
     "grep evaluation_dataset configs/ai/governance_metrics.yaml",
     "interop_pipeline produces ~9997 resources",
     "python3 /Users/ashishsingh/OnyxInterop/interop_pipeline.py --help",
     "Data Engineer | AI Engineer"),
    ("What Phase 4E gate blocks agent production-client deploy?",
     "4E-1 hallucination batch green for 2 consecutive weeks + controlled query set ≥50 documented.",
     "In addition to 4D gateway policies and spend caps.",
     "grep '4E-1' /Users/ashishsingh/OnyxInterop/Training/.cursor/plans/healthcare_interop_solution_6dadfbad.plan.md",
     "Plan exit criteria lists daily governance batch",
     "grep hallucination /Users/ashishsingh/OnyxInterop/Training/.cursor/plans/healthcare_interop_solution_6dadfbad.plan.md | tail -5",
     "AI Engineer | DevOps Engineer"),
    ("How does Component 13 relate to Component 11 AI Observability?",
     "Component 13: governance efficacy metrics (hallucination/bias/trust) on agent traces. Component 11: RCA/anomaly on de-id pipeline telemetry.",
     "Both use Unity AI Gateway; neither replaces Onyx Insights CMS filings.",
     "grep 'Component 13' /Users/ashishsingh/OnyxInterop/implementation_details.md",
     "ai_observer rejects PHI keys; governance uses de-id golden set",
     f"cd {ROOT} && python3 -c \"from observability.ai_observer import AIObserver; o=AIObserver(); print('ok')\"",
     "AI Engineer"),
    ("What should Section AA Scripts build for interview proficiency?",
     "Run governance batch, read alignment doc, explain phased metrics, CCA adjacency, and deprioritized backlog items from memory.",
     "Maps to AI Engineer + Solution Architect roles.",
     "Run all AA Scripts once",
     "Can whiteboard MLflow → Delta → daily batch flow",
     f"cd {ROOT} && python3 pipeline/ai/governance_metrics.py && wc -l docs/AI_GOVERNANCE_ALIGNMENT.md",
     "AI Engineer | Associate Solution Architect"),
]


def render_section() -> str:
    lines = [
        "## Section AA: AI Governance & CCA Alignment (Q516–535)\n",
        "> Source: AI Governance MVP (May 2026) + CCA Dev Milestones (June 2026). "
        "Maps leadership concerns to Components 13, Phase 4E, and adjacent CCA patterns.\n",
    ]
    for i, (q, ans, ex, check, fix, script, roles) in enumerate(QUESTIONS, start=516):
        lines += [
            f"### Q{i}. {q}\n",
            f"**Answer:** {ans}\n",
            f"**Example:** {ex}\n",
            "**How to Check:**",
            f"- {check}",
            f"- {fix}\n",
            "**How to Fix:**",
            "- Re-read [AI_GOVERNANCE_ALIGNMENT.md](file:///Users/ashishsingh/OnyxInterop/Training/onyx-interop/docs/AI_GOVERNANCE_ALIGNMENT.md) section for this topic",
            "- Re-run governance batch until metric output matches expectation\n",
            f"**Script:** *(builds proficiency: {roles})*\n",
            "```bash",
            script,
            "```\n",
            "---\n",
        ]
    return "\n".join(lines)


def main():
    text = OUT.read_text()
    marker = "## Glossary"
    if "## Section AA:" in text:
        print("Section AA already present")
        return
    idx = text.find(marker)
    if idx == -1:
        raise SystemExit("Glossary marker not found")
    section = render_section()
    new_text = text[:idx] + section + "\n" + text[idx:]
    # Update header counts
    new_text = new_text.replace("515 questions + Glossary", "535 questions + Glossary")
    new_text = new_text.replace(
        "- [Section Z: DevOps & CI/CD (Q486–515)](#section-z-devops--cicd-q486515)",
        "- [Section Z: DevOps & CI/CD (Q486–515)](#section-z-devops--cicd-q486515)\n"
        "- [Section AA: AI Governance & CCA Alignment (Q516–535)](#section-aa-ai-governance--cca-alignment-q516535)",
    )
    if "| **AI Engineer** | O, R |" in new_text and "AA" not in new_text.split("| **AI Engineer**")[1][:40]:
        new_text = new_text.replace(
            "| **AI Engineer** | O, R | RAG, MCP, Unity AI Gateway, ai_events, Agents |",
            "| **AI Engineer** | O, R, AA | RAG, MCP, Gateway, governance_metrics, Agents |",
            1,
        )
    OUT.write_text(new_text)
    print(f"Inserted Section AA ({len(QUESTIONS)} questions)")


if __name__ == "__main__":
    main()
