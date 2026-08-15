# Pull & Setup Commands — Healthcare Interop

> **Your hub directory:** `/Users/ashishsingh/CursorInteropSolution`  
> **Runnable code:** `/Users/ashishsingh/OnyxInterop/Training/onyx-interop`  
> **Reference servers (SLAP/FITE/pipeline):** `/Users/ashishsingh/OnyxInterop`  
> Run blocks **in order** the first time. Re-run only the sections you need after that.

---

## 0. One-time: know your paths

```bash
# WHAT: Set variables for every session
# WHY:  All scripts assume these locations; avoids typos
export INTEROP_HUB="$HOME/CursorInteropSolution"
export INTEROP_CODE="$HOME/OnyxInterop/Training/onyx-interop"
export INTEROP_REF="$HOME/OnyxInterop"
export CHEAT_SHEET="$HOME/Interview/Healthcare_Interop_Interview_Cheat_Sheet.md"

cd "$INTEROP_HUB"
pwd && ls -la
```

---

## 1. Pull latest solution docs (local git — if using home repo)

Your commits live under `~/` git (branch `main`). CursorInteropSolution files may be copies; pull/sync from source of truth.

```bash
# WHAT: See what changed locally
# WHY:  Know before you overwrite CursorInteropSolution copies
cd "$HOME"
git status --short | grep -E 'OnyxInterop|Interview|CursorInterop' || true
git log -3 --oneline

# WHAT: Pull from remote (only if remote is configured and you have access)
# WHY:  Get team updates — skip if remote still broken
# git pull origin main   # uncomment when GitLab remote works
```

### Refresh CursorInteropSolution docs from canonical sources (recommended)

```bash
# WHAT: Copy latest implementation + learning guides into your hub
# WHY:  CursorInteropSolution copies may be older (e.g. implementation_details Jul 14)
cp "$INTEROP_REF/implementation_details.md" "$INTEROP_HUB/implementation_details.md"
cp "$INTEROP_REF/Training/LEARN_FROM_STEP_1.md" "$INTEROP_HUB/LEARN_FROM_STEP_1.md"
cp "$CHEAT_SHEET" "$INTEROP_HUB/Healthcare_Interop_Interview_Cheat_Sheet.md"
cp "$INTEROP_REF/cms_9115_vs_0057_implementation_map.md" "$INTEROP_HUB/"
cp "$INTEROP_REF/fhir_ig_quick_reference_guide.md" "$INTEROP_HUB/"
cp "$INTEROP_REF/onyx_component_ownership_matrix.md" "$INTEROP_HUB/"

echo "Docs refreshed in $INTEROP_HUB"
```

---

## 2. Pull / clone runnable stack (`onyx-interop`)

```bash
# WHAT: Go to the build directory
# WHY:  All Phase 0 scripts live here
cd "$INTEROP_CODE"
ls -la scripts/
```

### Python environment

```bash
# WHAT: Create venv + install dependencies
# WHY:  pytest, pandas, pyyaml required for baseline + CI
cd "$INTEROP_CODE"
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# HOW TO CHECK
python3 -c "import pandas, yaml, pytest; print('deps OK')"
which python3
```

### Access config template

```bash
# WHAT: Create access.env from example (no secrets committed)
# WHY:  GitLab/AWS/Databricks URLs for later Phase 0 access
cd "$INTEROP_CODE"
cp -n configs/access/access.env.example configs/access/access.env 2>/dev/null || true
# Edit when you have credentials:
#   nano configs/access/access.env
```

### Clone production repos (or create local stubs)

```bash
# WHAT: Attempt clone of ng-onyx-runtime, onyx-helmsman, etc.
# WHY:  Phase 0 training expects these paths; stubs OK for local learn
cd "$INTEROP_CODE"
chmod +x scripts/*.sh scripts/ci/*.sh 2>/dev/null || true
./scripts/clone_production_repos.sh

# HOW TO CHECK
ls -la repos/
# Expect clones OR README stubs per repo
```

Set GitLab before clone (when you have access):

```bash
# WHAT: Point clone script at your GitLab
# WHY:  Default is placeholder URL
export GITLAB_BASE="https://gitlab.com/YOUR_GROUP"   # replace
export GITLAB_TOKEN="your-token"                     # optional, for HTTPS
# Then re-run:
# ./scripts/clone_production_repos.sh
```

### Full environment setup (runs clone + shims + tooling check)

```bash
cd "$INTEROP_CODE"
./scripts/setup_environment.sh
```

---

## 3. Pull reference data & pipeline (parent OnyxInterop)

```bash
# WHAT: Verify source CSV + pipeline script exist
# WHY:  run_local_baseline.sh calls ../.. /interop_pipeline.py
ls "$INTEROP_REF/source_data/Patients.csv"
ls "$INTEROP_REF/interop_pipeline.py"
ls "$INTEROP_REF/slap_server.py" "$INTEROP_REF/fhir_server.py"
ls "$INTEROP_REF/onyx_insights_server.py" "$INTEROP_REF/mdp_server.py"
```

If missing, they live in `~/OnyxInterop/` — not a separate git pull unless you add a remote.

---

## 4. Optional: Nasco / PulseEHR reference repos

```bash
# WHAT: Clone webhook reference (Rail B) if you have access
# WHY:  Phase 1+ multi-rail ingestion
mkdir -p "$INTEROP_CODE/repos"
cd "$INTEROP_CODE/repos"

# If repo exists on your machine already:
ls "$HOME/NascoEventAPI" 2>/dev/null && echo "NascoEventAPI found at home"
ls "$HOME/PulseEHR" 2>/dev/null && echo "PulseEHR found at home"

# Clone when GitLab access works (example):
# git clone "$GITLAB_BASE/ng-nasco-event-api.git"
# git clone "$GITLAB_BASE/PulseEHR.git"   # if applicable
```

---

## 5. Quick health check (after pull/setup)

```bash
source "$INTEROP_CODE/.venv/bin/activate"
cd "$INTEROP_CODE"

./scripts/phase0_access_checklist.sh
./scripts/run_local_baseline.sh
./scripts/ci/run_ci_local.sh
```

---

## 6. Start local services (after Step 1 Learn — Do phase)

```bash
source "$INTEROP_CODE/.venv/bin/activate"
cd "$INTEROP_CODE"
./scripts/start_all_services.sh

# Smoke tests
curl -sf http://localhost:9002/health | head
curl -sf http://localhost:8080/fhir/metadata | head
curl -sf http://localhost:9000/.well-known/smart-configuration | head
curl -sf http://localhost:9001/health | head
```

Stop services: `pkill -f 'slap_server|fhir_server|onyx_insights|mdp_server'`

---

## Path cheat sheet

| What | Path |
|------|------|
| Your learning hub | `~/CursorInteropSolution` |
| Build / scripts / tests | `~/OnyxInterop/Training/onyx-interop` |
| Pipeline + runtime servers | `~/OnyxInterop/` |
| Latest cheat sheet (535 Q) | `~/Interview/Healthcare_Interop_Interview_Cheat_Sheet.md` |
| Learn guide | `~/OnyxInterop/Training/LEARN_FROM_STEP_1.md` |
| DevOps runbook | `~/OnyxInterop/Training/onyx-interop/docs/DEVOPS_CICD.md` |
| AI governance alignment | `~/OnyxInterop/Training/onyx-interop/docs/AI_GOVERNANCE_ALIGNMENT.md` |

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `env: bash\r: No such file or directory` | `sed -i '' $'s/\r$//' scripts/ci/run_ci_local.sh` |
| `No module named pytest` | `source .venv/bin/activate && pip install -r requirements.txt` |
| `interop_pipeline.py not found` | Confirm `INTEROP_REF=~/OnyxInterop` and file exists |
| Port 9001 connection refused | Run `./scripts/start_all_services.sh` first |
| GitLab clone fails | Stubs are OK for Step 1; fill `access.env` later |

---

*Next: [STEP1_LEARN_AND_BUILD.md](./STEP1_LEARN_AND_BUILD.md)*
