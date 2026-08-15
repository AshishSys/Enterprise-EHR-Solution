#!/usr/bin/env bash
# Phase 0: Clone production repos referenced in training sessions
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
REPOS_DIR="$PROJECT_ROOT/repos"
mkdir -p "$REPOS_DIR"

# Load GitLab base from access.env if available
ACCESS_ENV="$PROJECT_ROOT/configs/access/access.env"
if [ -f "$ACCESS_ENV" ]; then
  # shellcheck source=/dev/null
  source "$ACCESS_ENV"
fi
GITLAB_BASE="${GITLAB_BASE:-https://gitlab.example.com/onyx}"

# repo_name|stub_subdirs (comma-separated chart/helm paths to create on stub)
REPOS=(
  "ng-onyx-runtime|runtime,tests"
  "onyx-helmsman|charts"
  "onyx-infrastructure|terraform"
  "firely-fsi-image|helm,docker"
  "mdp-gateway|src,configs"
  "kitchen-sous-chef|charts"
  "ng-nasco-event-api|terraform,lambda"
)

create_stub() {
  local repo="$1"
  local subdirs="$2"
  local target="$REPOS_DIR/$repo"
  mkdir -p "$target"
  IFS=',' read -ra dirs <<< "$subdirs"
  for d in "${dirs[@]}"; do
    mkdir -p "$target/$d"
    touch "$target/$d/.gitkeep"
  done
  cat > "$target/README.md" <<EOF
# $repo

Local stub — clone from production GitLab when access is available.

\`\`\`bash
export GITLAB_BASE="$GITLAB_BASE"
git clone \$GITLAB_BASE/$repo.git
\`\`\`

Referenced in Phase 0 training (\`20260204_*\` environment access session).
EOF
  echo "  STUB  $repo (remote unavailable)"
}

echo "=== Cloning Production Repos to $REPOS_DIR ==="
echo "GitLab base: $GITLAB_BASE"
echo "Set GITLAB_BASE and GITLAB_TOKEN in configs/access/access.env for authenticated clone"
echo ""

cloned=0
stubbed=0

for entry in "${REPOS[@]}"; do
  repo="${entry%%|*}"
  subdirs="${entry#*|}"
  target="$REPOS_DIR/$repo"

  if [ -d "$target/.git" ]; then
    echo "  SKIP  $repo (already cloned)"
    cloned=$((cloned + 1))
    continue
  fi

  echo "  CLONE $repo"
  if git clone "$GITLAB_BASE/$repo.git" "$target" 2>/dev/null; then
    echo "  OK    $repo"
    cloned=$((cloned + 1))
  else
    create_stub "$repo" "$subdirs"
    stubbed=$((stubbed + 1))
  fi
done

echo ""
echo "Summary: $cloned cloned, $stubbed stubbed"
echo "Repo directory: $REPOS_DIR"
