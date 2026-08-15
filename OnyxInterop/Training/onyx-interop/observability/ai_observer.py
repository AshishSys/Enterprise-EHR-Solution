"""AI observability — RCA and anomaly explanation on de-identified telemetry.

Prompts never include names, MRNs, member IDs, or raw clinical values.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

CONFIG_PATH = Path(__file__).resolve().parents[1] / "configs" / "observability" / "ai_models.yaml"

PHI_KEYS = {
    "name", "first", "last", "ssn", "mrn", "member_id", "email", "phone",
    "address", "birthdate", "patient", "subscriber_id",
}


class ObservabilityPolicyError(RuntimeError):
    """Raised when a payload would leak PHI into an AI model."""


class AIObserver:
    """Collects de-id signals and produces RCA / anomaly records."""

    def __init__(self, config_path: Path | None = None):
        self.config_path = config_path or CONFIG_PATH
        with open(self.config_path) as f:
            self.config = yaml.safe_load(f)
        self.events: list[dict] = []

    def _assert_deidentified(self, payload: dict) -> None:
        lowered = {str(k).lower() for k in payload}
        leaked = lowered & PHI_KEYS
        if leaked:
            raise ObservabilityPolicyError(
                f"Refusing AI observability payload — forbidden keys present: {sorted(leaked)}"
            )
        for value in payload.values():
            if isinstance(value, str) and "@" in value:
                raise ObservabilityPolicyError("Refusing payload that looks like an email")

    def ingest_signal(self, signal_type: str, payload: dict) -> dict:
        self._assert_deidentified(payload)
        event = {
            "signal_type": signal_type,
            "payload": payload,
            "ingested_at": datetime.now(timezone.utc).isoformat(),
        }
        self.events.append(event)
        return event

    def detect_anomaly(self, metric: str, value: float, baseline: float, sigma: float = 3.0) -> dict | None:
        if baseline <= 0:
            return None
        deviation = abs(value - baseline) / baseline
        if deviation < 0.5 and abs(value - baseline) < sigma * max(baseline * 0.1, 1):
            return None
        record = {
            "metric": metric,
            "value": value,
            "baseline": baseline,
            "deviation": round(deviation, 4),
            "model": self.config["models"]["anomaly"]["name"],
            "severity": "WARN" if deviation < 1.0 else "CRIT",
        }
        self._assert_deidentified(record)
        return record

    def explain_incident(self, traces: list[dict], metrics: dict) -> dict:
        for item in traces:
            self._assert_deidentified(item)
        self._assert_deidentified(metrics)
        failed_stages = [t.get("stage") for t in traces if t.get("status") == "failed"]
        return {
            "model": self.config["models"]["rca"]["name"],
            "gateway": self.config.get("gateway"),
            "hypothesis": (
                f"Failure concentrated in stages={failed_stages or ['unknown']}; "
                f"latency_p95={metrics.get('p95_ms')} error_rate={metrics.get('error_rate')}"
            ),
            "recommended_action": "Replay from last watermark; do not re-process identified PHI in Fabric.",
            "phi_in_prompt": False,
        }

    def shift_summary(self) -> dict:
        return {
            "model": self.config["models"]["summarizer"]["name"],
            "event_count": len(self.events),
            "signal_types": sorted({e["signal_type"] for e in self.events}),
            "note": "Summary contains counts and stage names only — no identifiers.",
        }
