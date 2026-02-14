# Helper Scripts for Survivor Data Collection

This directory contains helper scripts to accelerate and validate data collection for Seasons 21-30.

## Quick Start Guide

### 1. Check Progress
```bash
python scripts/track_progress.py
```
Shows completion status for all seasons 21-30.

### 2. Fill Voting Data (Manual Entry)

For each season file (`season21_manual_data.py` - `season30_manual_data.py`):

#### Step A: Fill Contestant List
```python
SEASON_CONTESTANTS = [
    "FirstEliminated",
    "SecondEliminated",
    # ... all contestants in elimination order
]
```
**CRITICAL:** Use first names only (e.g., "Fabio", "Chase", "Sash")
- Must match finalist names in `season_metadata.py` exactly
- Use nicknames for duplicates (e.g., "Rob M" vs "Rob C")

#### Step B: Fill Tribal Council Data

Navigate to: `https://survivor.fandom.com/wiki/Survivor:[Season_Name]`
- Find "Voting History" section (usually near bottom of page)
- For each pre-merge tribal council:

```python
{
    "episode": 1,
    "day": 3,               # Day number from wiki
    "tribe": "Espada",      # Tribe name
    "eliminated": "Wendy",  # Who was voted out
    "votes": {
        "Player1": "Wendy",  # All votes from this tribal
        "Player2": "Wendy",
        "Player3": "Jimmy",
        # ... etc
    }
}
```

#### Special Cases
```python
# Quit or medevac (no voting):
{
    "episode": 5,
    "day": 13,
    "eliminated": "NaOnka",
    "quit": True,
    "votes": {}  # Empty!
}

# Medevac:
{
    "episode": 3,
    "day": 8,
    "eliminated": "Russell",
    "medevac": True,
    "votes": {}
}
```

### 3. Validate After Each Season
```bash
python scripts/validate_season_data.py 21
```

Fix errors before moving to next season. Common errors:
- ❌ Name mismatch between metadata and voting data
- ❌ Eliminated player didn't receive most votes (check for ties/revotes)
- ❌ Voter name not in contestant list (typo)

### 4. Run Pipeline After Completing 2-3 Seasons
```bash
python batch_analyze.py
python batch_visualize.py
```

Check visualizations to catch systematic issues early.

### 5. Final Validation (All 10 Seasons)
```bash
python scripts/validate_season_data.py --range 21 30
python batch_analyze.py && python batch_visualize.py
python scripts/track_progress.py
```

Should show 100% completion for all seasons.

---

## Script Reference

### `generate_season_template.py`
Generates skeleton season data files with pre-populated tribal council placeholders.

```bash
# Single season
python scripts/generate_season_template.py 21

# Range of seasons
python scripts/generate_season_template.py --range 21 30
```

**Requirements:** Season must exist in `season_metadata.py` first.

---

### `validate_season_data.py`
Validates season data for common errors before running analysis pipeline.

```bash
# Single season
python scripts/validate_season_data.py 21

# Range of seasons
python scripts/validate_season_data.py --range 21 30

# Metadata only (skip data file checks)
python scripts/validate_season_data.py --metadata-only --range 21 30
```

**Validation Checks:**
- ✅ Name consistency (finalists, winner in contestant list)
- ✅ Episode ranges (all episodes < merge episode)
- ✅ Vote integrity (eliminated player received most votes)
- ✅ Metadata completeness (required fields present)

---

### `track_progress.py`
Visual dashboard showing completion status for data collection.

```bash
# Default: seasons 21-30
python scripts/track_progress.py

# Custom range
python scripts/track_progress.py --range 21 30

# All seasons
python scripts/track_progress.py --all
```

**Progress Indicators:**
- 📊 Progress bar (0-100%)
- ✅ Metadata complete
- ✅ File created
- ✅ Contestants filled
- ⚠️  Votes partially filled
- ✅ Votes complete
- ✅ Analysis generated
- ✅ Visualizations created

---

## Tips for Efficient Data Entry

### Time-Saving Strategies
1. **Do seasons in order** (21, 22, 23...) for easier tracking
2. **Validate after each season** to catch errors early
3. **Run partial pipeline** every 2-3 seasons to verify visualizations
4. **Use compact format** for votes (like Season 20 style) to save typing

### Common Pitfalls to Avoid
1. ❌ **Name mismatch** - "Richard Hatch" in metadata vs "Richard" in data
   - ✅ Use first names consistently
2. ❌ **Including merge episode** - If merge is Episode 8, stop at Episode 7
   - ✅ Only pre-merge tribal councils
3. ❌ **Typos in names** - "Russel" vs "Russell"
   - ✅ Copy-paste names from wiki
4. ❌ **Missing votes** - Not including all votes from tribal council
   - ✅ Count votes carefully from wiki table

### Data Entry Workflow
```
1. Open wiki page for season
2. Fill SEASON_CONTESTANTS list
3. Fill tribal councils (episodes 1 to merge-1)
4. Validate: python scripts/validate_season_data.py <season>
5. Fix errors, re-validate
6. Move to next season
```

---

## Time Estimates

| Task | Time | Effort |
|------|------|--------|
| **Per Season** | 2-3 hours | Manual data entry from wiki |
| **Validation** | 5 minutes | Run validation, fix errors |
| **All 10 Seasons** | 20-30 hours | Total manual effort |

**Suggestion:** Spread over 2-4 weeks, doing 2-3 seasons per session.

---

## Output Structure

After completing all seasons and running the pipeline:

```
data/seasons/
├── season21/analysis_results.json
├── season22/analysis_results.json
...
└── season30/analysis_results.json

visualizations/
├── seasons_comparison.png          # Bar chart with all 30 seasons
├── season21/
│   ├── season21_alliances.png     # Static network diagram
│   └── season21_interactive.html  # Interactive visualization
...
└── season30/
    ├── season30_alliances.png
    └── season30_interactive.html
```

---

## Next Steps

Current status: **Template generation complete (Phase 3)**

**Phase 4 - Manual Data Entry:** Fill voting data for seasons 21-30 (~20-30 hours)
- Use Survivor Wiki as data source
- Fill SEASON_CONTESTANTS and SEASON_VOTING_HISTORY for each season
- Validate after each season

**Phase 5 - Batch Processing:** Run analysis pipeline when complete
- `python batch_analyze.py && python batch_visualize.py`
- Review all visualizations for quality
- Verify 100% completion with `python scripts/track_progress.py`
