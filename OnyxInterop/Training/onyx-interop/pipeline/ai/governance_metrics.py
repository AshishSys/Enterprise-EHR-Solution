#!/usr/bin/env python3
"""AI governance metrics — local reference for MLflow-style batch evaluation.

Aligned to AI Governance MVP (hallucination / bias / trustworthiness) and CCA
working-session requirement to define metrics early.

Flow:
  1. Collect interaction traces (inputs, outputs, tool calls)
  2. Batch job computes metrics vs golden / grounded sources
  3. Persist results (Delta in prod; JSON locally)
  4. Report via notebook or CSV

Usage:
  python pipeline/ai/governance_metrics.py --traces ./data/governance/sample_traces.json
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path

CONFIG_JSON = Path(__file__).resolve().parents[2] / "configs" / "ai" / "governance_metrics.json"


def load_config() -> dict:
    with open(CONFIG_JSON) as f:
        return json.load(f)


def semantic_similarity(expected: str, actual: str) -> float:
    """Cheap local stand-in for BERTScore / embedding cosine."""
    return SequenceMatcher(None, expected.lower(), actual.lower()).ratio()


def hallucination_rate(rows: list[dict]) -> float:
    """Fraction of rows where similarity to golden answer falls below warn threshold."""
    cfg = load_config()
    warn = 1.0 - cfg["core_metrics"]["hallucination_rate"]["threshold_warn"]
    failures = 0
    for row in rows:
        sim = semantic_similarity(row.get("expected", ""), row.get("actual", ""))
        if sim < warn:
            failures += 1
        row["similarity"] = round(sim, 4)
        row["hallucination_flag"] = sim < warn
    return failures / len(rows) if rows else 0.0


def behavioral_signal_invalid_tool(row: dict) -> bool:
    """Invalid MCP/FHIR tool or unknown table reference counts as hallucination signal."""
    tools = row.get("tools_called") or []
    allowed = {"search_patient", "get_observations", "get_eob", "get_pa_status",
               "get_pipeline_status", "get_api_metrics"}
    return any(t not in allowed for t in tools)


def trustworthiness_score(rows: list[dict]) -> float:
    """Phase-2 stub: citation coverage + policy pass rate."""
    if not rows:
        return 0.0
    scores = []
    for row in rows:
        cited = bool(row.get("citations"))
        policy_ok = row.get("gateway_policy_pass", True)
        scores.append((1.0 if cited else 0.5) * (1.0 if policy_ok else 0.0))
    return sum(scores) / len(scores)


def run_batch(traces_path: Path, out_path: Path) -> dict:
    rows = json.loads(traces_path.read_text())
    for row in rows:
        if behavioral_signal_invalid_tool(row):
            row["behavioral_hallucination_signal"] = True

    report = {
        "computed_at": datetime.now(timezone.utc).isoformat(),
        "trace_count": len(rows),
        "hallucination_rate": round(hallucination_rate(rows), 4),
        "trustworthiness_score": round(trustworthiness_score(rows), 4),
        "phase": "1-alpha",
        "rows": rows,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2))
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute AI governance metrics (batch)")
    parser.add_argument(
        "--traces",
        default=str(Path(__file__).resolve().parents[2] / "data" / "governance" / "sample_traces.json"),
    )
    parser.add_argument(
        "--out",
        default=str(Path(__file__).resolve().parents[2] / "data" / "governance" / "metrics_report.json"),
    )
    args = parser.parse_args()
    report = run_batch(Path(args.traces), Path(args.out))
    print(json.dumps({k: report[k] for k in report if k != "rows"}, indent=2))


if __name__ == "__main__":
    main()
