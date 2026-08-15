#!/usr/bin/env bash
# Phase 0: Master script — environment access + production repo clone
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=== Phase 0: Access & Repo Setup ==="
echo ""

bash "$SCRIPT_DIR/setup_environment.sh"
echo ""
bash "$SCRIPT_DIR/phase0_access_checklist.sh"

echo ""
echo "Phase 0 access setup complete."
