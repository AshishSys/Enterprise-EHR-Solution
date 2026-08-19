#!/usr/bin/env bash
# P3 — On-prem → cloud migration cutover gate checklist
set -euo pipefail

echo "=== Cambia Facets Migration Cutover Checklist (P3) ==="
echo ""
checks=(
  "VPN: Palo Alto tunnel to cambia-facets-networking (697410135799) stable"
  "CDC: facets-core historical backfill complete or in agreed parallel window"
  "Incremental: 4-hr schedule + Facets_BatchJobComplete nightly trigger verified"
  "HITRUST: facets-core outside boundary; encryption before SFTP landing"
  "Bronze: CMC_CLCL_CLAIM SCD2 row delta matches CDC batch IDs (sample)"
  "Gold: gold.fm_claim_cambia signature bitmap parity vs on-prem sample period"
  "Interop: dental excluded from gold.fm_claim; CDP retains all (P2 SME sign-off)"
  "Downstream: Snowflake chunked load (XFORM-3515) and/or Reltio feed validated"
  "Postman: newman cutover-gate collection green on stg (P4)"
  "Sign-off: #xform-xport confirmed workflow IDs for cambia02 env"
)
for i in "${!checks[@]}"; do
  printf "  [ ] %2d. %s\n" "$((i+1))" "${checks[$i]}"
done
echo ""
echo "PASS: Checklist printed — complete each item before stg→prd promotion."
