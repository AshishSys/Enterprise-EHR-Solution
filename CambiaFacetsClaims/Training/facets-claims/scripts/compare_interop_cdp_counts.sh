#!/usr/bin/env bash
# Compare Interop vs CDP gold row counts (expect CDP >= Interop)
set -euo pipefail

echo "=== Interop vs CDP Gold Comparison ==="
echo ""
echo "Run in cambia02 Databricks (dev/stg first):"
echo ""
cat <<'SQL'
SELECT 'interop_fm_claim' AS path, COUNT(*) AS rows FROM gold.fm_claim
UNION ALL
SELECT 'cdp_fm_claim_cambia', COUNT(*) FROM gold.fm_claim_cambia;
-- Expect CDP count >= Interop (dental + non-Medicare retained in CDP only)
SQL
echo ""
echo "Dental filter: CMC_CDDL_CL_LINE in bronze/silver but excluded from gold.fm_claim"
echo "Interop filter: 75 groups, Medicare patients only"
echo ""
echo "PASS: Comparison query ready (execute in workspace)"
