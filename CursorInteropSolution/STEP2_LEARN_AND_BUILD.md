# Step 2 — Learn Then Build (Week 1: CMS Rules & FHIR)

> **Prerequisite:** Step 1 exit ✅ (baseline + validation + pytest)  
> **Hub:** `~/CursorInteropSolution` · **Build:** `~/OnyxInterop/Training/onyx-interop`  
> **Goal:** Speak CMS and FHIR before writing transforms or touching Databricks.

Step 1 complete: [STEP1_LEARN_AND_BUILD.md](./STEP1_LEARN_AND_BUILD.md)

---

## Step 1 exit — confirmed ✅

You achieved:

- Pipeline: **9,997** FHIR resources
- Validation: **PASSED** (US Core + CARIN BB)
- pytest: **14/14** green

---

## Step 2 weekly map

| Day | Learn | Do | Exit |
|-----|-------|-----|------|
| **Mon** | CMS-9115 vs CMS-0057 | Phase 1 vs Phase 2 API table | Notes file |
| **Tue** | US Core + CARIN BB | Inspect `meta.profile` on 3 resources | Profiles explained |
| **Wed** | Plan-Net + Formulary | Read PVD/Formulary extract configs | SAM → resource map |
| **Thu** | Teach-back M1 | Present CMS → component map | 5 bullets aloud |
| **Fri** | Cheat Sheet Q11–20 | Profile/Must Support drill | Explain one IG error |

---

# Day 1 (Monday) — CMS-9115 vs CMS-0057

## LEARN (45 min)

**WHAT:** Understand which CMS rules apply when, and which APIs belong to Plan Phase 1 vs 2.  
**WHY:** Every architecture decision traces back to CMS-9115 (Patient Access, PVD, Formulary) vs CMS-0057 (Provider Access, P2P, ePA).  
**HOW:** Read artifact + cheat sheet Section B intro.

```bash
export INTEROP_HUB="$HOME/CursorInteropSolution"
export INTEROP_REF="$HOME/OnyxInterop"
export CHEAT_SHEET="$HOME/Interview/Healthcare_Interop_Interview_Cheat_Sheet.md"

cd "$INTEROP_HUB"

# Refresh canonical CMS map (if needed)
cp "$INTEROP_REF/cms_9115_vs_0057_implementation_map.md" "$INTEROP_HUB/" 2>/dev/null || true

# Open in Cursor — read "Phase 1" and "Phase 2" sections only (first ~30 min)
sed -n '1,80p' "$INTEROP_HUB/cms_9115_vs_0057_implementation_map.md"

# Cheat Sheet: find Section B (Q11+)
grep -n "^## Section B" "$CHEAT_SHEET"
# Read Q11–Q15 (Answer + Example)
```

**Memory targets:**

| Rule | Deadline | Key APIs |
|------|----------|----------|
| **CMS-9115** | Patient Access live; metrics Jan 2026 | Patient Access, Provider Directory, Formulary |
| **CMS-0057** | Jan 2027 | Provider Access `$export`, P2P, ePA (CRD/DTR/PAS) |

---

## DO (45 min)

**WHAT:** Build your Phase 1 vs Phase 2 API table tied to components.  
**WHY:** Proves you can map regulation → Abacus/Onyx component (interview + architect skill).  
**HOW:**

```bash
cat > "$INTEROP_HUB/my_step2_day1_cms_map.md" << 'EOF'
# CMS API → Component Map (my notes)

## Phase 1 — CMS-9115 (Abacus + Onyx)

| CMS API | FHIR resources | Abacus (data) | Onyx (runtime) |
|---------|----------------|---------------|----------------|
| Patient Access | Patient, EOB, Observation, ... | Claims/Clinical SAM → Extract | SLAP + FITE + Firely |
| Provider Directory | Practitioner, Organization, Role | PVD SAM | FITE (public) |
| Formulary | MedicationKnowledge | Formulary SAM | FITE (public) |

## Phase 2 — CMS-0057

| CMS API | Pattern | Component |
|---------|---------|-----------|
| Provider Access | Backend Services + `$export` | SLAP + FITE |
| P2P | `$bulk-member-match` + consent | p2p_member_match.py |
| ePA | CRD / DTR / PAS | epa_burden_reduction_service.py |

## My one-sentence summary
CMS-9115 = member-facing access; CMS-0057 = provider/payer advanced exchange by Jan 2027.
EOF

open "$INTEROP_HUB/my_step2_day1_cms_map.md"   # or edit in Cursor
```

Cross-check against implementation:

```bash
# WHAT: See which IGs are registered locally
# WHY:  MDP is the config brain — same pattern in prod
grep -l "9115\|0057\|Plan-Net\|CARIN" "$INTEROP_REF/Training/onyx-interop/configs/mdp/"*.json 2>/dev/null \
  || ls "$INTEROP_REF/Training/onyx-interop/configs/mdp/"

# Inspect IG registry (if services not running, read file directly)
cat "$INTEROP_REF/Training/onyx-interop/configs/mdp/ig_registry.json" | python3 -m json.tool | head -40
```

---

## CHECK (15 min)

| # | Can you answer without notes? |
|---|------------------------------|
| 1 | What three APIs are CMS-9115 Phase 1? |
| 2 | What is the CMS-0057 hard deadline? |
| 3 | Which component serves FHIR to apps — Firely or FITE? |
| 4 | Where does EOB come from in the pipeline? (Claims SAM) |
| 5 | Is Provider Directory authenticated or public? |

---

## TEACH (15 min)

Say aloud or record 5 bullets:

1. CMS-9115 vs CMS-0057 in one sentence each  
2. Why PVD must load before Claims (practitioner refs on EOB)  
3. What Patient Access API returns (`$everything`, EOB, clinical)  
4. What Jan 2027 adds  
5. Why Step 2 comes before Databricks  

---

## Day 1 exit

- [ ] `my_step2_day1_cms_map.md` filled in  
- [ ] 5 check questions answered from memory  
- [ ] Read Cheat Sheet Q11–Q15  

---

# Day 2 preview (Tuesday) — US Core profiles

```bash
source "$HOME/OnyxInterop/Training/onyx-interop/.venv/bin/activate"

# Inspect profiles you fixed in Step 1
python3 << 'PY'
import json
from pathlib import Path
ndjson = Path("$HOME/OnyxInterop/fhir_output/ndjson")
for name in ["Patient.ndjson", "Condition.ndjson", "ExplanationOfBenefit.ndjson"]:
    line = (ndjson / name).read_text().splitlines()[0]
    r = json.loads(line)
    print(name, "→", r.get("meta", {}).get("profile"))
PY
```

---

*When Day 1 exit is done, say **"Step 2 Day 1 done"** for Day 2 commands.*

---

# Day 2 (Tuesday) — US Core + CARIN BB Profiles

## LEARN (45 min)

**WHAT:** `meta.profile` declares which IG profile a resource claims to conform to.  
**WHY:** Validators, Firely, and CMS compliance all check profiles + Must Support elements.  
**HOW:** Read IG quick reference § US Core + § CARIN BB; Cheat Sheet Q80–Q82.

```bash
export INTEROP_HUB="$HOME/CursorInteropSolution"
export INTEROP_REF="$HOME/OnyxInterop"
export INTEROP_CODE="$HOME/OnyxInterop/Training/onyx-interop"
export CHEAT_SHEET="$HOME/Interview/Healthcare_Interop_Interview_Cheat_Sheet.md"

cp "$INTEROP_REF/fhir_ig_quick_reference_guide.md" "$INTEROP_HUB/" 2>/dev/null || true

# US Core + CARIN sections (adjust line range after skim)
grep -n "^## [0-9]" "$INTEROP_HUB/fhir_ig_quick_reference_guide.md" | head -15

# Cheat Sheet Q80–Q82
grep -n "^### Q8[0-2]\." "$CHEAT_SHEET"
```

**Key concepts:**

| IG | Used for | Example profile URL |
|----|----------|---------------------|
| **US Core** | Clinical + Patient Access | `.../us-core-patient` |
| **US Core variants** | Condition/Obs types | `.../us-core-condition-encounter-diagnosis`, `.../us-core-vital-signs` |
| **CARIN BB (C4BB)** | Claims / EOB for members | `.../C4BB-ExplanationOfBenefit-Inpatient-Institutional` |

**Must Support:** If data exists, element must be present or explicitly absent — validation fails if missing.

---

## DO (60 min)

### 1. Inspect profiles on real output (the Step 1 fix you lived through)

```bash
source "$INTEROP_CODE/.venv/bin/activate"
export INTEROP_REF="$HOME/OnyxInterop"

python3 << 'PY'
import json
from pathlib import Path

ndjson = Path("$HOME/OnyxInterop/fhir_output/ndjson")
samples = {
    "Patient": "us-core-patient",
    "Condition": "us-core-condition",
    "Observation": "us-core-observation",
    "ExplanationOfBenefit": "C4BB-ExplanationOfBenefit",
}

for fname, hint in samples.items():
    path = ndjson / f"{fname}.ndjson"
    if not path.exists():
        print(f"SKIP {fname}")
        continue
    r = json.loads(path.read_text().splitlines()[0])
    profiles = r.get("meta", {}).get("profile", [])
    print(f"\n=== {fname} ===")
    print("  profile:", profiles)
    print("  id:", r.get("id"))
    # Must Support spot-check
    if fname == "Patient":
        print("  name.family:", r.get("name", [{}])[0].get("family", "MISSING"))
    if fname == "ExplanationOfBenefit":
        print("  billablePeriod:", r.get("billablePeriod", "MISSING"))
        print("  patient:", r.get("patient", "MISSING"))
PY
```

### 2. Compare validator allowed profiles vs pipeline output

```bash
# WHAT: See which profiles the validator accepts
grep -A20 "REQUIRED_PROFILES" "$INTEROP_CODE/scripts/validate_fhir_output.py" | head -25

# WHAT: Re-run validation (should still PASS)
python3 "$INTEROP_CODE/scripts/validate_fhir_output.py" "$INTEROP_REF/fhir_output/ndjson"
```

### 3. Must Support drill — intentionally break then fix

```bash
# WHAT: Copy one Patient, remove name.family, see validation impact
python3 << 'PY'
import json, shutil, tempfile
from pathlib import Path

ndjson = Path("$INTEROP_REF/fhir_output/ndjson")
patient_file = ndjson / "Patient.ndjson"
backup = ndjson / "Patient.ndjson.bak"
if not backup.exists():
    shutil.copy(patient_file, backup)

lines = patient_file.read_text().splitlines()
r = json.loads(lines[0])
if r.get("name"):
    r["name"][0].pop("family", None)
lines[0] = json.dumps(r)
patient_file.write_text("\n".join(lines) + "\n")
print("Removed name.family from first Patient — re-run validator mentally:")
print("  (Our script checks required fields + profiles; production IG validator would flag Must Support)")
PY

# Restore
cp "$INTEROP_REF/fhir_output/ndjson/Patient.ndjson.bak" \
   "$INTEROP_REF/fhir_output/ndjson/Patient.ndjson" 2>/dev/null || \
   python3 "$INTEROP_REF/interop_pipeline.py" --input "$INTEROP_REF/source_data" --output "$INTEROP_REF/fhir_output"
```

### 4. Document your findings

```bash
cat > "$INTEROP_HUB/my_step2_day2_profiles.md" << 'EOF'
# Step 2 Day 2 — Profile notes

## Three resources I inspected
1. Patient → profile: ...
2. Condition → profile: ... (why encounter-diagnosis variant?)
3. EOB → profile: ... + billablePeriod: ...

## US Core vs CARIN BB (my words)
- US Core covers: ...
- CARIN BB covers: ...

## Must Support example
- Element: Patient.name.family
- What happens if missing: ...

## One interview sentence
"A resource's meta.profile tells validators which StructureDefinition applies; Must Support means..."
EOF
```

---

## CHECK (15 min)

Answer without notes:

| # | Question |
|---|----------|
| 1 | What does `meta.profile` do? |
| 2 | Why did Condition use `us-core-condition-encounter-diagnosis`? |
| 3 | Which IG governs ExplanationOfBenefit for Patient Access? |
| 4 | What is Must Support? |
| 5 | Name two US Core resource types in your baseline output |

---

## TEACH (15 min)

Explain aloud to an imaginary interviewer:

> "Walk me through how you validate FHIR output against US Core and CARIN BB."

Use: pipeline output → `meta.profile` → validator → Firely `$validate` in prod.

---

## Day 2 exit

- [ ] Inspected Patient, Condition, EOB profiles  
- [ ] Validation still PASSED  
- [ ] `my_step2_day2_profiles.md` completed  
- [ ] Read Cheat Sheet Q80–Q82  

---

# Day 3 preview (Wednesday) — Plan-Net + Formulary configs

```bash
cat "$INTEROP_CODE/configs/workflows/claims/extract_config.yaml"
ls "$INTEROP_CODE/configs/workflows/" 2>/dev/null
grep -r "Practitioner\|MedicationKnowledge" "$INTEROP_CODE/configs/workflows/" 2>/dev/null | head -10
```

*Say **"Step 2 Day 2 done"** when ready for Day 3.*

