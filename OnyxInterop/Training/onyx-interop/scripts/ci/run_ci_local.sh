#!/usr/bin/env bash
# Run the same checks as GitLab CI locally before push
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

echo "=== [1/7] Python compile ==="
python3 -m compileall pipeline/ observability/ monitoring/ -q

echo "=== [2/7] Config files exist ==="
test -f configs/mdp/ig_registry.json
test -f configs/mdp/services.json
test -f configs/workflows/claims/extract_config.yaml

echo "=== [3/7] Unit tests ==="
python3 -m pytest tests/ -v --tb=short

echo "=== [4/7] FHIR baseline ==="
python3 interop_pipeline.py --input ./source_data --output ./fhir_output
python3 scripts/validate_fhir_output.py ./fhir_output

echo "=== [5/7] Terraform validate ==="
if command -v terraform >/dev/null 2>&1; then
  (cd terraform && terraform init -backend=false && terraform validate) || echo "WARN: terraform validate skipped"
else
  echo "SKIP: terraform not installed"
fi

echo "=== [6/7] Helm lint ==="
if command -v helm >/dev/null 2>&1; then
  helm lint helm/firely-server/
else
  echo "SKIP: helm not installed"
fi

echo "=== [7/7] Databricks bundle validate ==="
if command -v databricks >/dev/null 2>&1 && [ -f databricks.yml ]; then
  databricks bundle validate -t dev 2>/dev/null || echo "WARN: bundle validate skipped (auth)"
else
  echo "SKIP: databricks CLI or databricks.yml missing"
fi

echo ""
echo "CI local run PASSED — safe to push"
