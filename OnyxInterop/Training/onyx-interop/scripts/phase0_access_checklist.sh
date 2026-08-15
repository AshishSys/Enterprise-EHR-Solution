#!/usr/bin/env bash
# Phase 0: Verify environment access per Feb 4 training session
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
REPOS_DIR="$PROJECT_ROOT/repos"

PASS=0
FAIL=0
WARN=0

check() {
  local name="$1"
  local cmd="$2"
  if eval "$cmd" &>/dev/null; then
    echo "  [PASS] $name"
    PASS=$((PASS + 1))
  else
    echo "  [FAIL] $name"
    FAIL=$((FAIL + 1))
  fi
}

warn_check() {
  local name="$1"
  local cmd="$2"
  if eval "$cmd" &>/dev/null; then
    echo "  [PASS] $name"
    PASS=$((PASS + 1))
  else
    echo "  [WARN] $name (configure via configs/access/access.env)"
    WARN=$((WARN + 1))
  fi
}

# Load access env if present
ACCESS_ENV="$PROJECT_ROOT/configs/access/access.env"
if [ -f "$ACCESS_ENV" ]; then
  # shellcheck source=/dev/null
  source "$ACCESS_ENV"
fi
export PATH="$PROJECT_ROOT/bin:${PATH}"

echo "=== Phase 0 Access Checklist ==="
echo ""

echo "Core Tools:"
check "Python 3.9+" "python3 -c 'import sys; assert sys.version_info >= (3,9)'"
check "pip" "pip --version"
check "git" "git --version"
check "Docker" "docker --version"
warn_check "JDK (Firely tooling)" "java -version"
warn_check "Poetry" "poetry --version"

echo ""
echo "Cloud & Platform:"
warn_check "AWS CLI configured" "aws sts get-caller-identity"
warn_check "Terraform" "terraform version"
warn_check "kubectl" "kubectl version --client"
warn_check "Helm" "helm version"
warn_check "Databricks CLI" "databricks --version"
warn_check "Databricks auth profile" "databricks auth describe --profile ${DATABRICKS_CONFIG_PROFILE:-onyx-dev}"
warn_check "GitLab reachable" "curl -sf --max-time 5 ${GITLAB_BASE:-https://gitlab.example.com/onyx} -o /dev/null"
warn_check "Seiji deploy tool" "seiji --version"

echo ""
echo "Access Configuration:"
if [ -f "$ACCESS_ENV" ]; then
  echo "  [PASS] configs/access/access.env present"
  PASS=$((PASS + 1))
else
  echo "  [WARN] configs/access/access.env missing (copy from access.env.example)"
  WARN=$((WARN + 1))
fi

if [ -f "$PROJECT_ROOT/configs/repo-shims/shims.yaml" ]; then
  echo "  [PASS] repo-shims config present"
  PASS=$((PASS + 1))
else
  echo "  [FAIL] repo-shims config missing"
  FAIL=$((FAIL + 1))
fi

if [ -f "$PROJECT_ROOT/configs/repo-shims/.shim-index" ]; then
  echo "  [PASS] repo-shims index generated"
  PASS=$((PASS + 1))
else
  echo "  [WARN] repo-shims not initialized (run ./scripts/setup_repo_shims.sh)"
  WARN=$((WARN + 1))
fi

echo ""
echo "Production Repos (via scripts/clone_production_repos.sh):"
REPOS=(
  "ng-onyx-runtime"
  "onyx-helmsman"
  "onyx-infrastructure"
  "firely-fsi-image"
  "mdp-gateway"
  "kitchen-sous-chef"
  "ng-nasco-event-api"
)
for repo in "${REPOS[@]}"; do
  if [ -d "$REPOS_DIR/$repo" ]; then
    if [ -d "$REPOS_DIR/$repo/.git" ]; then
      echo "  [PASS] $repo cloned"
    else
      echo "  [WARN] $repo stub present (awaiting GitLab access)"
      WARN=$((WARN + 1))
    fi
    PASS=$((PASS + 1))
  else
    echo "  [WARN] $repo not present (run clone_production_repos.sh)"
    WARN=$((WARN + 1))
  fi
done

echo ""
echo "MDP Service Registry:"
if [ -f "$PROJECT_ROOT/configs/mdp/services.json" ]; then
  echo "  [PASS] MDP services.json present"
  PASS=$((PASS + 1))
else
  echo "  [FAIL] MDP services.json missing"
  FAIL=$((FAIL + 1))
fi

echo ""
echo "New platform layers:"
for cfg in \
  "configs/deid/safe_harbor.yaml" \
  "configs/mdm/mdm_rules.yaml" \
  "configs/fabric/workspace.yaml" \
  "configs/observability/ai_models.yaml"
do
  if [ -f "$PROJECT_ROOT/$cfg" ]; then
    echo "  [PASS] $cfg"
    PASS=$((PASS + 1))
  else
    echo "  [FAIL] $cfg missing"
    FAIL=$((FAIL + 1))
  fi
done

echo ""
echo "=== Summary: $PASS passed, $FAIL failed, $WARN warnings ==="
[ "$FAIL" -eq 0 ] || exit 1
