#!/usr/bin/env bash
# Compare Databricks vs Fabric cost/speed on the de-identified SAM contract.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"
PYTHON="${PROJECT_ROOT}/.venv/bin/python"
if [ ! -x "$PYTHON" ]; then
  PYTHON="python3"
fi
"$PYTHON" - <<'PY'
from pipeline.fabric_benchmark import FabricBenchmark

bench = FabricBenchmark()
# Placeholder timings from a 1M-row de-id Claims family bake-off.
db = bench.estimate_databricks(elapsed_seconds=420, dbus=8)
fab = bench.estimate_fabric(elapsed_seconds=510, capacity_cu=64)
result = bench.compare("claims", rows=1_000_000, databricks=db, fabric=fab)
for k, v in result.items():
    print(f"{k}: {v}")
PY
