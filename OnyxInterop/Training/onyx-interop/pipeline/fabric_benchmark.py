"""Compare Databricks vs Microsoft Fabric on the same de-identified SAM contract."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

CONFIG_PATH = Path(__file__).resolve().parents[1] / "configs" / "fabric" / "workspace.yaml"

# Published list prices used only for local bake-off estimates (not invoices).
DATABRICKS_DBU_USD = 0.55
FABRIC_CU_HOUR_USD = 0.18


class FabricBenchmark:
    """Normalize elapsed time and estimated cost across engines."""

    def __init__(self, config_path: Path | None = None):
        self.config_path = config_path or CONFIG_PATH
        with open(self.config_path) as f:
            self.config = yaml.safe_load(f)

    def estimate_databricks(self, elapsed_seconds: float, dbus: float) -> dict[str, float]:
        hours = elapsed_seconds / 3600.0
        cost = dbus * DATABRICKS_DBU_USD * hours
        return {"engine": "databricks", "elapsed_seconds": elapsed_seconds, "cost_usd": round(cost, 4)}

    def estimate_fabric(self, elapsed_seconds: float, capacity_cu: float) -> dict[str, float]:
        hours = elapsed_seconds / 3600.0
        cost = capacity_cu * FABRIC_CU_HOUR_USD * hours
        return {"engine": "fabric", "elapsed_seconds": elapsed_seconds, "cost_usd": round(cost, 4)}

    def compare(
        self,
        family: str,
        rows: int,
        databricks: dict[str, float],
        fabric: dict[str, float],
    ) -> dict[str, Any]:
        if rows <= 0:
            raise ValueError("rows must be positive")
        db_cost_m = databricks["cost_usd"] / rows * 1_000_000
        fab_cost_m = fabric["cost_usd"] / rows * 1_000_000
        faster = "databricks" if databricks["elapsed_seconds"] <= fabric["elapsed_seconds"] else "fabric"
        cheaper = "databricks" if databricks["cost_usd"] <= fabric["cost_usd"] else "fabric"
        return {
            "family": family,
            "rows_processed": rows,
            "input_contract": self.config["benchmark"]["same_input_contract"],
            "databricks": {**databricks, "cost_per_million_rows": round(db_cost_m, 4)},
            "fabric": {**fabric, "cost_per_million_rows": round(fab_cost_m, 4)},
            "winner_speed": faster,
            "winner_cost": cheaper,
            "recommendation": (
                "Keep Databricks on CMS critical path; use Fabric for Gold/BI "
                f"when cost winner is fabric and speed delta is acceptable ({family})."
            ),
        }
