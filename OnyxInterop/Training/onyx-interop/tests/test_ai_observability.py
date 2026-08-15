"""AI observability policy tests — PHI payloads must be rejected."""

from observability.ai_observer import AIObserver, ObservabilityPolicyError


def test_rejects_member_id():
    obs = AIObserver()
    try:
        obs.ingest_signal("trace", {"member_id": "M123"})
        assert False, "expected policy error"
    except ObservabilityPolicyError:
        pass


def test_accepts_deid_trace_and_explains():
    obs = AIObserver()
    obs.ingest_signal("trace", {"stage": "extract", "status": "failed", "workflow": "claims"})
    rca = obs.explain_incident(
        traces=[{"stage": "extract", "status": "failed"}],
        metrics={"p95_ms": 2400, "error_rate": 0.12},
    )
    assert rca["phi_in_prompt"] is False
    assert "extract" in rca["hypothesis"]


def test_anomaly_on_large_deviation():
    obs = AIObserver()
    hit = obs.detect_anomaly("job_seconds", 900, baseline=120)
    assert hit is not None
    assert hit["severity"] == "CRIT"
