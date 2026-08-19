#!/usr/bin/env bash
# Local CI gate — all 4 proficiency pillars
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

echo "=== Facets Claims Local CI (P1–P4) ==="
for script in phase0_architecture_trace.sh phase0_repo_map.sh validate_manifest_pattern.sh compare_interop_cdp_counts.sh migration_cutover_checklist.sh postman_smoke_check.sh; do
  bash "scripts/$script"
done
echo ""
echo "PASS: All pillar checks green"
