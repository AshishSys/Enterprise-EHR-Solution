"""Orchestrator includes de-id, MDM, bake-off, and observe steps."""

from pipeline.orchestrator import WorkflowOrchestrator


def test_pipeline_steps_include_new_layers():
    steps = WorkflowOrchestrator().get_pipeline_steps("claims")
    assert steps[:3] == ["deidentify", "mdm_resolve", "preprocess"]
    assert "benchmark_engines" in steps
    assert "observe" in steps
