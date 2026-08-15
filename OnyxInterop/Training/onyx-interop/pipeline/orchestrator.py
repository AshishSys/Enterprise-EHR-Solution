"""Onyx Interop pipeline orchestrator — coordinates workflow families in dependency order."""

import json
import yaml
from pathlib import Path
from typing import Optional

CONFIGS_DIR = Path(__file__).resolve().parents[1] / "configs" / "workflows"
MDP_SERVICES = Path(__file__).resolve().parents[1] / "configs" / "mdp" / "services.json"


class WorkflowOrchestrator:
    """Orchestrates Databricks workflow families with dependency enforcement."""

    def __init__(self, configs_dir: Optional[Path] = None):
        self.configs_dir = configs_dir or CONFIGS_DIR
        self.load_order = self._load_order()

    def _load_order(self) -> list[str]:
        if MDP_SERVICES.exists():
            with open(MDP_SERVICES) as f:
                return json.load(f).get("load_order", [])
        return ["pvd", "clinical", "claims", "formulary", "cms0057", "epa"]

    def load_config(self, family: str) -> dict:
        config_path = self.configs_dir / family / "extract_config.yaml"
        if not config_path.exists():
            raise FileNotFoundError(f"Extract config not found: {config_path}")
        with open(config_path) as f:
            return yaml.safe_load(f)

    def get_pipeline_steps(self, family: str) -> list[str]:
        return [
            "deidentify",
            "mdm_resolve",
            "preprocess",
            "transform",
            "extract",
            "upload",
            "terminate",
            "benchmark_engines",
            "observe",
        ]

    def validate_dependencies(self, family: str, completed: set[str]) -> bool:
        config = self.load_config(family)
        deps = config.get("depends_on", [])
        missing = [d for d in deps if d not in completed]
        if missing:
            raise RuntimeError(
                f"Workflow '{family}' blocked — missing dependencies: {missing}"
            )
        return True

    def get_execution_plan(self) -> list[dict]:
        plan = []
        completed = set()
        for family in self.load_order:
            config_path = self.configs_dir / family / "extract_config.yaml"
            if not config_path.exists():
                continue
            config = self.load_config(family)
            deps = config.get("depends_on", [])
            plan.append({
                "family": family,
                "depends_on": deps,
                "ready": all(d in completed for d in deps),
                "steps": self.get_pipeline_steps(family),
                "fhir_resources": config.get("fhir_resources", []),
            })
            completed.add(family)
        return plan

    def export_databricks_job(self, family: str, environment: str = "dev") -> dict:
        config = self.load_config(family)
        return {
            "name": f"onyx-{family}-{environment}",
            "tasks": [
                {"task_key": "deidentify", "python_wheel_task": {"entry_point": "deidentify"}},
                {"task_key": "mdm_resolve", "depends_on": [{"task_key": "deidentify"}],
                 "python_wheel_task": {"entry_point": "mdm_resolve"}},
                {"task_key": "preprocess", "depends_on": [{"task_key": "mdm_resolve"}],
                 "python_wheel_task": {"entry_point": "preprocess"}},
                {"task_key": "transform", "depends_on": [{"task_key": "preprocess"}],
                 "python_wheel_task": {"entry_point": "transform"}},
                {"task_key": "extract", "depends_on": [{"task_key": "transform"}],
                 "python_wheel_task": {"entry_point": "extract"}},
                {"task_key": "upload", "depends_on": [{"task_key": "extract"}],
                 "python_wheel_task": {"entry_point": "upload"}},
                {"task_key": "benchmark_engines", "depends_on": [{"task_key": "extract"}],
                 "python_wheel_task": {"entry_point": "benchmark_engines"}},
                {"task_key": "observe", "depends_on": [{"task_key": "upload"}],
                 "python_wheel_task": {"entry_point": "observe"}},
                {"task_key": "terminate", "depends_on": [{"task_key": "upload"}, {"task_key": "observe"}],
                 "python_wheel_task": {"entry_point": "terminate"}},
            ],
            "tags": {
                "workflow_family": family,
                "fhir_resources": ",".join(config.get("fhir_resources", [])),
            },
        }


if __name__ == "__main__":
    orch = WorkflowOrchestrator()
    print("Execution Plan:")
    for step in orch.get_execution_plan():
        status = "READY" if step["ready"] else "BLOCKED"
        print(f"  [{status}] {step['family']} → {step['fhir_resources']}")
