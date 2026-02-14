# Seasons 21-30 Setup - Implementation Complete

## ✅ Completed Phases

### Phase 1: Helper Scripts (COMPLETE)
Created three automation tools in `scripts/` directory:

1. **`generate_season_template.py`** - Auto-generates season data file skeletons
   - Creates files with pre-populated tribal council placeholders
   - Uses merge episode from metadata to determine number of TCs
   - Usage: `python scripts/generate_season_template.py --range 21 30`

2. **`validate_season_data.py`** - Automated data quality checks
   - Validates name consistency (finalists match contestant list)
   - Checks episode ranges (only pre-merge data)
   - Verifies vote integrity (eliminated player received votes)
   - Usage: `python scripts/validate_season_data.py --range 21 30`

3. **`track_progress.py`** - Visual progress dashboard
   - Shows completion status for all stages (metadata → viz)
   - Progress bars with percentage completion
   - Suggests next steps automatically
   - Usage: `python scripts/track_progress.py`

### Phase 2: Metadata (COMPLETE)
Added complete metadata for seasons 21-30 to `season_metadata.py`:

| Season | Name | Year | Merge Ep | Pre-merge TCs | Winner |
|--------|------|------|----------|---------------|--------|
| 21 | Nicaragua | 2010 | 8 | 7 | Fabio |
| 22 | Redemption Island | 2011 | 8 | 7 | Rob |
| 23 | South Pacific | 2011 | 9 | 8 | Sophie |
| 24 | One World | 2012 | 8 | 7 | Kim |
| 25 | Philippines | 2012 | 8 | 7 | Denise |
| 26 | Caramoan | 2013 | 8 | 7 | Cochran |
| 27 | Blood vs Water | 2013 | 7 | 6 | Tyson |
| 28 | Cagayan | 2014 | 8 | 7 | Tony |
| 29 | San Juan del Sur | 2014 | 8 | 7 | Natalie |
| 30 | Worlds Apart | 2015 | 8 | 7 | Mike |

**Total TCs to fill:** 70 tribal councils (~2-3 hours per season = 20-30 hours total)

### Phase 3: Template Generation (COMPLETE)
Generated all 10 season data files:
- `season21_manual_data.py` through `season30_manual_data.py`
- Each file has:
  - Season docstring with wiki URL
  - Empty `SEASON_CONTESTANTS` list
  - Pre-populated tribal council placeholders (correct count based on merge episode)
  - TODO comments for guidance
  - Special case handling notes

**Verification:**
```bash
$ python scripts/track_progress.py
# Shows 20% completion for seasons 21-30 (metadata + file creation complete)
```

---

## 📋 Next Phase: Manual Data Entry

### Ready to Start Phase 4

**Current Status:** All infrastructure is set up. Template files are ready for data entry.

**Time Estimate:** 20-30 hours (2-3 hours per season × 10 seasons)

**Recommended Workflow:**
1. Work on 2-3 seasons per session
2. Validate after each season
3. Run partial pipeline every 2-3 seasons to verify visualizations

### Data Entry Instructions

For each season file (start with `season21_manual_data.py`):

#### Step 1: Open Survivor Wiki
Navigate to: `https://survivor.fandom.com/wiki/Survivor:[Season_Name]`
- Example: https://survivor.fandom.com/wiki/Survivor:Nicaragua

#### Step 2: Fill Contestant List
Use first names only (must match metadata exactly):
```python
SEASON_CONTESTANTS = [
    "Wendy",      # First eliminated
    "Shannon",    # Second eliminated
    # ... in elimination order
    "Fabio"       # Winner (last)
]
```

#### Step 3: Fill Tribal Council Data
Find "Voting History" section on wiki page (usually near bottom).

For each pre-merge tribal council:
```python
{
    "episode": 1,
    "day": 3,
    "tribe": "Espada",
    "eliminated": "Wendy",
    "votes": {
        "Jimmy": "Wendy",
        "Tyrone": "Wendy",
        "Holly": "Wendy",
        # ... all votes from this tribal
    }
}
```

#### Step 4: Validate
```bash
python scripts/validate_season_data.py 21
```
Fix any errors, then move to next season.

#### Step 5: Run Partial Pipeline (Every 2-3 Seasons)
```bash
python batch_analyze.py
python batch_visualize.py
```
Review visualizations to catch issues early.

---

## 🛠️ Helper Commands

### Check Overall Progress
```bash
python scripts/track_progress.py
```

### Validate Single Season
```bash
python scripts/validate_season_data.py 21
```

### Validate All Seasons 21-30
```bash
python scripts/validate_season_data.py --range 21 30
```

### Run Full Pipeline
```bash
python batch_analyze.py && python batch_visualize.py
```

### View Season Metadata
```bash
python season_metadata.py
```

---

## ✨ Features Implemented

### Template Generator
- ✅ Auto-detects merge episode from metadata
- ✅ Creates correct number of TC placeholders
- ✅ Includes helpful TODO comments
- ✅ Generates season-specific wiki URLs
- ✅ Supports batch generation (`--range` flag)

### Validation Checker
- ✅ Name consistency checks (finalists, winner, voters, targets)
- ✅ Episode range validation (pre-merge only)
- ✅ Vote integrity checks (eliminated player received votes)
- ✅ Metadata completeness checks
- ✅ Quit/medevac special case handling
- ✅ Detailed error messages with episode numbers
- ✅ Exit codes for CI/CD integration

### Progress Tracker
- ✅ Visual progress bars (0-100%)
- ✅ Stage-by-stage breakdown (metadata → viz)
- ✅ Tribal council count tracking (X/Y TCs complete)
- ✅ Color-coded status indicators (✅ ❌ ⚠️)
- ✅ Next steps suggestions
- ✅ Works with any season range (`--all`, `--range`)

---

## 📊 Expected Outputs (After Phase 4 + 5)

### Analysis Results
```
data/seasons/
├── season21/analysis_results.json
├── season22/analysis_results.json
...
└── season30/analysis_results.json
```

### Visualizations
```
visualizations/
├── seasons_comparison.png          # Bar chart with all 30 seasons!
├── season21/
│   ├── season21_alliances.png     # Gold/silver highlighting
│   └── season21_interactive.html  # Hover for alliance details
...
└── season30/
    ├── season30_alliances.png
    └── season30_interactive.html
```

---

## 🎯 Success Criteria

When Phase 4 (data entry) and Phase 5 (pipeline) are complete:

- [ ] All 10 seasons pass validation: `python scripts/validate_season_data.py --range 21 30`
- [ ] Progress tracker shows 100%: `python scripts/track_progress.py`
- [ ] All visualizations render correctly (PNG + HTML for each season)
- [ ] Updated comparison chart includes all 30 seasons
- [ ] Winner highlighting works (gold nodes)
- [ ] Finalist highlighting works (silver nodes)
- [ ] Alliance networks show clear tribal patterns

---

## 📝 Notes

### Critical Reminders
1. **Name matching is critical** - Finalist names in metadata must match contestant names exactly
2. **Pre-merge only** - If merge is Episode 8, only include Episodes 1-7
3. **First names only** - Use "Fabio" not "Fabio Birza" (unless duplicates exist)
4. **Validate early** - Run validation after each season to catch errors immediately

### Common Errors to Avoid
- ❌ Including merge episode votes (stop before merge!)
- ❌ Typos in contestant names (copy-paste from wiki)
- ❌ Missing votes from tribal council (count carefully)
- ❌ Finalist name mismatch (must match metadata exactly)

### Time-Saving Tips
- Use compact vote format (one line per vote) like Season 20
- Copy contestant names directly from wiki to avoid typos
- Do seasons in order (21, 22, 23...) for easier tracking
- Validate after each season (cheaper to fix early)

---

## 🚀 Current Status Summary

**Infrastructure Setup:** ✅ **COMPLETE**
- Helper scripts operational
- Metadata complete for seasons 21-30
- Template files generated and ready

**Next Step:** Begin Phase 4 - Manual data entry for Season 21
- Estimated time: 2-3 hours
- File: `season21_manual_data.py`
- Wiki: https://survivor.fandom.com/wiki/Survivor:Nicaragua

**Final Step:** Phase 5 - Run pipeline and verify outputs
- Command: `python batch_analyze.py && python batch_visualize.py`
- Review all visualizations
- Verify 100% completion

---

## 📚 Documentation

- **Main README:** `README.md` (project overview)
- **Claude Instructions:** `CLAUDE.md` (project-specific guidance)
- **Helper Scripts Guide:** `scripts/README.md` (detailed helper script docs)
- **Multi-Season Guide:** `MULTI_SEASON_GUIDE.md` (batch processing info)
- **This Document:** `SEASONS_21-30_SETUP.md` (implementation summary)

---

**Implementation Date:** 2026-02-13
**Status:** Phases 1-3 Complete, Ready for Phase 4 (Manual Data Entry)
