#!/usr/bin/env bash
# Local CI gate for Facets Claims training repo
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

echo "=== Facets Claims Local CI ==="
for script in phase0_architecture_trace.sh phase0_repo_map.sh validate_manifest_pattern.sh; do
  bash "scripts/$script" || exit 1
done
bash scripts/compare_interop_cdp_counts.sh || exit 1
echo ""
echo "PASS: All local CI checks green"
