#!/usr/bin/env bash
# Phase 0: Environment setup for Onyx Interop production development
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PARENT_ROOT="$(cd "$PROJECT_ROOT/.." && pwd)"

echo "=== Onyx Interop — Environment Setup ==="

# Python virtual environment
if [ ! -d "$PROJECT_ROOT/.venv" ]; then
  python3 -m venv "$PROJECT_ROOT/.venv"
  echo "Created virtual environment at .venv"
fi
# shellcheck source=/dev/null
source "$PROJECT_ROOT/.venv/bin/activate"
pip install -q -r "$PROJECT_ROOT/requirements.txt"

# Access config template
ACCESS_ENV="$PROJECT_ROOT/configs/access/access.env"
ACCESS_EXAMPLE="$PROJECT_ROOT/configs/access/access.env.example"
if [ ! -f "$ACCESS_ENV" ] && [ -f "$ACCESS_EXAMPLE" ]; then
  cp "$ACCESS_EXAMPLE" "$ACCESS_ENV"
  echo "Created configs/access/access.env from template — fill in credentials"
fi

# Configure platform access
bash "$SCRIPT_DIR/configure_access.sh"

# Clone production repos
bash "$SCRIPT_DIR/clone_production_repos.sh"

# Repo-shims for Helm/Seiji
bash "$SCRIPT_DIR/setup_repo_shims.sh"

# Verify tooling
echo ""
echo "--- Tooling Check ---"
for cmd in python3 docker aws git; do
  if command -v "$cmd" &>/dev/null; then
    echo "  OK  $cmd: $(command -v "$cmd")"
  else
    echo "  MISSING  $cmd (install required for production deploy)"
  fi
done

for cmd in poetry databricks terraform seiji helm java; do
  if command -v "$cmd" &>/dev/null; then
    echo "  OK  $cmd"
  else
    echo "  OPTIONAL  $cmd not found"
  fi
done

# Link to parent reference code
REF_LINK="$PROJECT_ROOT/reference"
if [ ! -L "$REF_LINK" ]; then
  ln -sf "$PARENT_ROOT/.." "$REF_LINK" 2>/dev/null || ln -sf "$PARENT_ROOT" "$REF_LINK" 2>/dev/null || true
fi

# Create local data directories
mkdir -p "$PROJECT_ROOT/data/fhir_output/bundles"
mkdir -p "$PROJECT_ROOT/data/fhir_output/ndjson"
mkdir -p "$PROJECT_ROOT/data/logs"
mkdir -p "$PROJECT_ROOT/bin"

echo ""
echo "Setup complete. Next steps:"
echo "  1. Edit configs/access/access.env with AWS/Databricks/GitLab/Seiji credentials"
echo "  2. Re-run: ./scripts/phase0_access_checklist.sh"
echo "  3. Activate venv: source $PROJECT_ROOT/.venv/bin/activate"
