# Step 1 — Learn Then Build (Day 1 Foundation)

> **Approach:** Learn → Do → Check → Teach  
> **Do not start Plan Phase 1 (Databricks)** until Step 1 exit criteria pass.  
> **Hub:** `~/CursorInteropSolution` · **Build:** `~/OnyxInterop/Training/onyx-interop`

Pull/setup first: [PULL_AND_SETUP_COMMANDS.md](./PULL_AND_SETUP_COMMANDS.md)

---

## What Step 1 is (and is not)

| | |
|--|--|
| **IS** | Understand Abacus vs Onyx, run local CSV→FHIR pipeline, validate output, optional local CI |
| **IS NOT** | Databricks deploy, Firely on EKS, production GitLab push, or CMS go-live |

**Memory checkpoint:** Draw this chain from memory before moving on:

```
CSV → FM → SAM → FHIR → Firely → SLAP → FITE → App
```

---

# Phase A — LEARN (45 min)

## A1. Glossary (15 min)

**WHAT:** Read 10 terms in order.  
**WHY:** Every command and interview answer uses this vocabulary.  
**HOW:** Open cheat sheet Glossary or skim Section A.

```bash
export CHEAT_SHEET="$HOME/Interview/Healthcare_Interop_Interview_Cheat_Sheet.md"
cd "$HOME/CursorInteropSolution"

# WHAT: Open glossary in editor or print first 10 terms
grep -A1 "^\| \*\*Abacus\*\*" "$CHEAT_SHEET" | head -4
grep -A1 "^\| \*\*Onyx\*\*" "$CHEAT_SHEET" | head -4
grep -A1 "^\| \*\*FM " "$CHEAT_SHEET" | head -4
grep -A1 "^\| \*\*SAM " "$CHEAT_SHEET" | head -4
```

**Terms (in order):** Abacus · Onyx · FM · SAM · SLAP · FITE · Firely · CMS-9115 · FHIR R4 · US Core

**You should be able to say:**
- Abacus = data plane (ingest, FM/SAM, extract)
- Onyx = API plane (SLAP, FITE, portal, insights)

---

## A2. System overview diagram (15 min)

**WHAT:** Read only the first diagram in `implementation_details.md`.  
**WHY:** Step 1 is about knowing the six local components before cloud complexity.  
**HOW:**

```bash
cd "$HOME/CursorInteropSolution"
sed -n '1,30p' implementation_details.md
# Or open in Cursor and read "System Overview" section only
```

**Components to name:** Pipeline · SLAP · FITE · Firely (store) · Onyx Insights · MDP

---

## A3. Cheat Sheet Q1–Q3 (15 min)

**WHAT:** Read Answer + Example only (not full memorization).  
**WHY:** Q1 frames end-to-end ownership; Q2–Q3 set Abacus/Onyx split.  
**HOW:**

```bash
# WHAT: Extract Q1–Q3 headers
grep -n "^### Q[123]\." "$CHEAT_SHEET"
# Read those sections in Cursor (Search: "### Q1.")
```

---

# Phase B — DO (60–90 min)

Run from your terminal. Activate venv once per session.

```bash
export INTEROP_HUB="$HOME/CursorInteropSolution"
export INTEROP_CODE="$HOME/OnyxInterop/Training/onyx-interop"
export INTEROP_REF="$HOME/OnyxInterop"

cd "$INTEROP_CODE"
source .venv/bin/activate   # if missing: see PULL_AND_SETUP_COMMANDS.md §2
```

---

## B1. Phase 0 access checklist

**WHAT:** `./scripts/phase0_access_checklist.sh`  
**WHY:** Confirms tooling paths before you blame the pipeline for failures.  
**HOW:** Prints OK/MISSING for python, docker, aws, git, optional databricks/terraform.

```bash
cd "$INTEROP_CODE"
chmod +x scripts/phase0_access_checklist.sh
./scripts/phase0_access_checklist.sh
```

**Expected:** Python + git OK. AWS/Databricks may be MISSING — OK for Step 1.

---

## B2. Environment setup (first time only)

**WHAT:** `./scripts/setup_environment.sh`  
**WHY:** Creates `.venv`, `access.env` template, repo stubs, tooling report.  
**HOW:** Idempotent — safe to re-run.

```bash
cd "$INTEROP_CODE"
./scripts/setup_environment.sh
```

---

## B3. Local baseline — the core build proof

**WHAT:** CSV → FM → SAM → FHIR → NDJSON (~9,997 resources)  
**WHY:** This is the Abacus data path in miniature; everything else hangs off it.  
**HOW:** Uses parent `interop_pipeline.py` + Synthea CSV in `source_data/`.

```bash
cd "$INTEROP_CODE"
./scripts/run_local_baseline.sh
```

**Alternative (manual, same result):**

```bash
python3 "$INTEROP_REF/interop_pipeline.py" \
  --input "$INTEROP_REF/source_data" \
  --output "$INTEROP_REF/fhir_output"

python3 "$INTEROP_CODE/scripts/validate_fhir_output.py" \
  "$INTEROP_REF/fhir_output/ndjson"
```

---

## B4. Unit tests

**WHAT:** `pytest tests/`  
**WHY:** Proves transformers and config contracts — same gate as GitLab CI.  
**HOW:**

```bash
cd "$INTEROP_CODE"
python3 -m pytest tests/ -v --tb=short
```

---

## B5. Local CI mirror (DevOps gate from Day 1)

**WHAT:** `./scripts/ci/run_ci_local.sh`  
**WHY:** Same validate+test stages as `.gitlab-ci.yml` before any push.  
**HOW:**

```bash
cd "$INTEROP_CODE"
chmod +x scripts/ci/run_ci_local.sh
./scripts/ci/run_ci_local.sh
```

**Note:** Terraform/Helm/Databricks steps may SKIP if tools not installed — OK for Step 1.

---

## B6. Cheat Sheet Scripts Q1 + Q8

**WHAT:** Runnable proof blocks from interview prep.  
**WHY:** Ties learning to interview proficiency track.  
**HOW:**

```bash
cd "$INTEROP_CODE"
./scripts/phase0_access_checklist.sh
./scripts/run_local_baseline.sh
python3 -m pytest tests/ -q
echo "Q1/Q8 Step 1 scripts complete"
```

---

## B7. (Optional) Start runtime services

**WHAT:** SLAP, FITE, Insights, MDP on ports 9000/8080/9001/9002  
**WHY:** Proves API plane locally; needed before Step 3 architecture curls.  
**HOW:**

```bash
cd "$INTEROP_CODE"
./scripts/start_all_services.sh

curl -s http://localhost:9002/health | python3 -m json.tool | head -20
curl -s http://localhost:8080/fhir/metadata | head -5
curl -s http://localhost:9001/audit | head -5
```

---

# Phase C — CHECK (15 min)

| # | Check | Command | Expected |
|---|-------|---------|----------|
| 1 | FHIR output exists | `ls "$INTEROP_REF/fhir_output/ndjson/"` | 8 `.ndjson` files |
| 2 | Resource scale | `wc -l "$INTEROP_REF/fhir_output/ndjson/"*.ndjson` | ~9,997 total lines |
| 3 | Validation | `python3 "$INTEROP_CODE/scripts/validate_fhir_output.py" "$INTEROP_REF/fhir_output/ndjson"` | Exit 0 |
| 4 | Tests | `cd "$INTEROP_CODE" && pytest tests/ -q` | All passed |
| 5 | Six components | say aloud | Pipeline, SLAP, FITE, Firely, Insights, MDP |
| 6 | Abacus vs Onyx | say aloud | Data plane vs API plane |

**One-liner summary check:**

```bash
cd "$INTEROP_REF/fhir_output/ndjson" && wc -l *.ndjson | tail -1
```

---

# Phase D — TEACH (15 min)

Write or say **5 bullets** (notes file in your hub):

```bash
cat > "$INTEROP_HUB/my_step1_notes.md" << 'EOF'
# My Step 1 Teach-Back Notes

1. Abacus owns: ...
2. Onyx owns: ...
3. Why CSV is not FHIR at ingest: ...
4. What FM vs SAM means: ...
5. Day 1 success = baseline green because: ...
EOF
open "$INTEROP_HUB/my_step1_notes.md"   # or use Cursor
```

---

## Step 1 exit gate (must pass before Step 2)

- [ ] Baseline green (`run_local_baseline.sh` exit 0)
- [ ] `pytest` green
- [ ] 10 glossary terms explained without notes
- [ ] Whiteboard chain: `CSV → FM → SAM → FHIR → Firely → SLAP → FITE → App`
- [ ] `my_step1_notes.md` written

---

## What I (the agent) will do next when you report back

When you paste terminal output from **B3 + B4 + C**, I will:

1. Confirm exit criteria pass/fail  
2. Explain any errors (paths, venv, ports, missing source_data)  
3. Give you **Step 2 — Week 1: CMS Rules & FHIR** commands (Section B of LEARN guide)

---

## Quick reference — copy/paste block (full Step 1 Do)

```bash
export INTEROP_HUB="$HOME/CursorInteropSolution"
export INTEROP_CODE="$HOME/OnyxInterop/Training/onyx-interop"
export INTEROP_REF="$HOME/OnyxInterop"

cd "$INTEROP_HUB"
# Refresh docs (optional)
cp "$INTEROP_REF/implementation_details.md" "$INTEROP_HUB/" 2>/dev/null || true

cd "$INTEROP_CODE"
python3 -m venv .venv 2>/dev/null || true
source .venv/bin/activate
pip install -q -r requirements.txt

chmod +x scripts/*.sh scripts/ci/*.sh 2>/dev/null || true
./scripts/phase0_access_checklist.sh
./scripts/setup_environment.sh
./scripts/run_local_baseline.sh
python3 -m pytest tests/ -v --tb=short
./scripts/ci/run_ci_local.sh

echo "=== Step 1 DO complete — run CHECK table above ==="
```

---

*Previous: [PULL_AND_SETUP_COMMANDS.md](./PULL_AND_SETUP_COMMANDS.md) · Next after exit: Step 2 in `LEARN_FROM_STEP_1.md`*
