#!/usr/bin/env bash
# Phase 0: Run local reference pipeline and validate FHIR output
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PARENT_ROOT="$(cd "$PROJECT_ROOT/../.." && pwd)"

echo "=== Phase 0: Local Baseline Validation ==="

# Setup venv if needed
if [ -f "$PROJECT_ROOT/.venv/bin/activate" ]; then
  source "$PROJECT_ROOT/.venv/bin/activate"
fi

SOURCE_DATA="$PARENT_ROOT/source_data"
OUTPUT_DIR="$PARENT_ROOT/fhir_output"
PIPELINE="$PARENT_ROOT/interop_pipeline.py"

if [ ! -f "$PIPELINE" ]; then
  echo "ERROR: interop_pipeline.py not found at $PIPELINE"
  exit 1
fi

echo ""
echo "--- Step 1: Run Data Pipeline ---"
python3 "$PIPELINE" --input "$SOURCE_DATA" --output "$OUTPUT_DIR"

echo ""
echo "--- Step 2: Validate FHIR Output ---"
python3 "$SCRIPT_DIR/validate_fhir_output.py" "$OUTPUT_DIR/ndjson"

echo ""
echo "--- Step 3: Resource Counts ---"
for f in "$OUTPUT_DIR/ndjson"/*.ndjson; do
  [ -f "$f" ] || continue
  count=$(wc -l < "$f" | tr -d ' ')
  echo "  $(basename "$f"): $count resources"
done

echo ""
echo "Local baseline validation complete."
