#!/usr/bin/env bash
# P4 — Postman API role smoke check
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
POSTMAN_DIR="$ROOT/postman"

echo "=== Postman API Role Smoke Check (P4) ==="
echo ""

if ! command -v newman >/dev/null 2>&1; then
  echo "WARN: newman not installed — install with: npm install -g newman"
  echo "Collections to run when newman available:"
else
  echo "Newman: $(newman --version)"
fi

echo ""
echo "Collections:"
for f in cambia-facets-claims-smoke.json fhir-claims-interop.json fhir-claims-cdp.json cambia-facets-cutover-gate.json; do
  if [[ -f "$POSTMAN_DIR/$f" ]]; then
    echo "  [ok] postman/$f"
  else
    echo "  [template] postman/$f — create from docs/POSTMAN_API_ROLE.md"
  fi
done

echo ""
echo "Environments (gitignore secrets):"
for e in dev.json stg.json prd-smoke.json; do
  if [[ -f "$POSTMAN_DIR/env/$e" ]]; then
    echo "  [ok] postman/env/$e"
  else
    echo "  [create] postman/env/$e — use synthetic test IDs only"
  fi
done

echo ""
echo "Example:"
echo "  newman run postman/cambia-facets-claims-smoke.json -e postman/env/dev.json --bail"
echo ""
echo "PASS: Postman inventory check complete"
