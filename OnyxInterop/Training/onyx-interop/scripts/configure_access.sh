#!/usr/bin/env bash
# Phase 0: Load and validate AWS, Databricks, GitLab, and Seiji access
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
ACCESS_ENV="$PROJECT_ROOT/configs/access/access.env"
ACCESS_EXAMPLE="$PROJECT_ROOT/configs/access/access.env.example"

echo "=== Phase 0: Configure Access ==="

if [ -f "$ACCESS_ENV" ]; then
  # shellcheck source=/dev/null
  source "$ACCESS_ENV"
  echo "  Loaded $ACCESS_ENV"
elif [ -f "$ACCESS_EXAMPLE" ]; then
  echo "  [WARN] access.env not found — copy from access.env.example"
  # shellcheck source=/dev/null
  source "$ACCESS_EXAMPLE"
else
  echo "  [WARN] No access config found"
fi

export REPO_SHIMS_DIR="${REPO_SHIMS_DIR:-$PROJECT_ROOT/configs/repo-shims}"

# AWS profile setup
if [ -n "${AWS_PROFILE:-}" ]; then
  export AWS_PROFILE
  echo "  AWS profile: $AWS_PROFILE"
fi
export AWS_REGION="${AWS_REGION:-us-east-1}"

# Databricks CLI profile
if [ -n "${DATABRICKS_HOST:-}" ] && [ -n "${DATABRICKS_TOKEN:-}" ]; then
  databricks configure --token \
    --host "$DATABRICKS_HOST" \
    --profile "${DATABRICKS_CONFIG_PROFILE:-onyx-dev}" 2>/dev/null || true
  echo "  Databricks profile: ${DATABRICKS_CONFIG_PROFILE:-onyx-dev}"
fi

# GitLab credential helper (store token for clone script)
if [ -n "${GITLAB_TOKEN:-}" ] && [ -n "${GITLAB_BASE:-}" ]; then
  git config --global "url.https://oauth2:${GITLAB_TOKEN}@${GITLAB_BASE#https://}.insteadOf" \
    "$GITLAB_BASE" 2>/dev/null || true
  echo "  GitLab: token configured for $GITLAB_BASE"
fi

# Seiji home (project-local so Phase 0 works without writing $HOME)
export SEIJI_HOME="${SEIJI_HOME:-$PROJECT_ROOT/.seiji}"
mkdir -p "$SEIJI_HOME"
export PATH="$PROJECT_ROOT/bin:${PATH}"

echo ""
echo "Access configuration complete."
