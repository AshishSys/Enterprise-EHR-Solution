# Step 2 Day 4 — Teach-Back M1 (CMS → Component)

> **Time:** 30 min prepare + 15 min deliver (to yourself, peer, or record on phone)  
> **Goal:** Prove you can map CMS rules → Abacus/Onyx components without slides overload.

---

## LEARN (15 min) — assemble your story

Pull from notes you already wrote:

```bash
export INTEROP_HUB="$HOME/CursorInteropSolution"
cat "$INTEROP_HUB/my_step2_day1_cms_map.md"
cat "$INTEROP_HUB/my_step2_day2_profiles.md"
cat "$INTEROP_HUB/my_step2_day3_sam_map.md"
```

---

## DO (30 min) — build 5-slide outline (markdown)

```bash
cat > "$INTEROP_HUB/my_step2_day4_teachback.md" << 'EOF'
# M1 Teach-Back: CMS Interop → Our Platform (5 bullets)

## 1. Why we exist (30 sec)
CMS-9115/0057 require payers to expose FHIR APIs by fixed deadlines.
Jan 2026 metrics; Jan 2027 full 0057 APIs.

## 2. Two planes (45 sec)
- **Abacus** = data: ingest → FM → SAM → Extract → Firely/HealthLake
- **Onyx** = API: SLAP auth → FITE gateway → consumer apps
Apps never hit Firely directly.

## 3. Phase 1 APIs (60 sec)
| API | IG | Data path |
|-----|-----|-----------|
| Patient Access | US Core + CARIN BB EOB | Claims + Clinical SAM |
| Provider Directory | Plan-Net | PVD SAM (public) |
| Formulary | Da Vinci Formulary | formulary_sam |

## 4. Phase 2 adds (45 sec)
Provider Access ($export), P2P ($bulk-member-match), ePA (CRD/DTR/PAS) — Jan 2027.

## 5. What I proved locally (30 sec)
9997 FHIR resources, validation PASSED, profiles on Patient/EOB match US Core/CARIN BB.
Claims extract depends_on PVD — sequencing matters.

## Q&A I should handle
- Q: Patient Access vs Provider Access?
- Q: Why FITE not Firely?
- Q: What is Must Support / meta.profile?
EOF
```

---

## DELIVER (15 min)

Read `my_step2_day4_teachback.md` aloud twice:

1. **First pass** — with notes (slow, correct)  
2. **Second pass** — notes closed, ≤ 4 minutes total  

Optional record:

```bash
# macOS — record yourself (Ctrl+C to stop)
# screen recording or voice memo on phone works too
say "Starting teach-back" 2>/dev/null || true
```

---

## CHECK

| # | Without notes, can you answer in ≤30 sec? |
|---|------------------------------------------|
| 1 | CMS-9115 vs CMS-0057 |
| 2 | Abacus vs Onyx |
| 3 | Three Phase 1 APIs + their IGs |
| 4 | Why PVD before Claims |
| 5 | What SLAP and FITE do |

---

## Day 4 exit

- [ ] `my_step2_day4_teachback.md` created  
- [ ] Delivered teach-back twice  
- [ ] 5 Q&A items answered from memory  

---

# Step 2 Day 5 preview — Q11–Q20 + Must Support drill

```bash
export CHEAT_SHEET="$HOME/Interview/Healthcare_Interop_Interview_Cheat_Sheet.md"
grep -n "^### Q1[1-9]\.\|^### Q20\." "$CHEAT_SHEET"

# Re-run validation + explain one error type
python3 "$HOME/OnyxInterop/Training/onyx-interop/scripts/validate_fhir_output.py" \
  "$HOME/OnyxInterop/fhir_output/ndjson"
```

*Say **"Step 2 Day 4 done"** or **"Step 2 complete"** after Day 5.*
