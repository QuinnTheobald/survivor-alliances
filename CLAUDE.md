# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Survivor TV show alliance analysis system** that creates network visualizations of voting patterns. The key insight: it analyzes **pre-merge votes only** to reveal original tribal alliances before strategic post-merge gameplay.

**Current Status:** Complete verified voting data for Seasons 1-10 (60+ tribal councils, ~400 votes)

## Core Commands

### Full Analysis Pipeline
```bash
# 1. Analyze all seasons with available data (creates JSON results)
python batch_analyze.py

# 2. Generate visualizations (creates PNG + HTML for each season)
python batch_visualize.py

# Or run both:
python batch_analyze.py && python batch_visualize.py
```

### Single Season (Legacy)
```bash
python analyze_season1_manual.py  # Analyze only Season 1
python visualize_season1.py       # Visualize only Season 1
```

### Dependencies
```bash
pip install networkx matplotlib plotly beautifulsoup4 requests pandas
```

## Architecture & Data Flow

### Two-Stage Pipeline

**Stage 1: Analysis (`batch_analyze.py`)**
- Imports `seasonX_manual_data.py` files dynamically
- Reads `season_metadata.py` for merge episode cutoffs
- Calculates vote alignments (who voted together)
- Filters for pre-merge votes only (before merge episode)
- Outputs: `data/seasons/seasonXX/analysis_results.json`

**Stage 2: Visualization (`batch_visualize.py`)**
- Loads analysis results from JSON files
- Creates NetworkX graphs (nodes = players, edges = vote alignments)
- Applies styling: gold (winner), silver (finalist), blue (others)
- Outputs: PNG (static), HTML (interactive Plotly)

### Critical Name Matching Requirement

**Finalist/winner names in `season_metadata.py` MUST exactly match contestant names in voting data.**

❌ Wrong:
```python
# season_metadata.py
"finalists": ["Richard Hatch", "Kelly Wiglesworth"]

# season1_manual_data.py
SEASON_CONTESTANTS = ["Richard", "Kelly", ...]
```

✅ Correct:
```python
# season_metadata.py
"finalists": ["Richard", "Kelly"]  # Use first names only

# season1_manual_data.py
SEASON_CONTESTANTS = ["Richard", "Kelly", ...]
```

This is because the visualization code checks `contestant in finalists` for highlighting.

### Pre-Merge Filtering Logic

The system filters votes by episode number in `calculate_vote_alignments()`:
```python
for tribal_council in voting_history:
    episode = tribal_council.get('episode', 999)
    if episode >= merge_episode:  # Skip merge and post-merge
        break
```

This means:
- Season metadata MUST have correct `merge_episode` values
- Vote data MUST have accurate `episode` numbers
- Merge votes themselves are excluded (e.g., if merge is Episode 7, only Episodes 1-6 are analyzed)

## Adding a New Season

### 1. Update Season Metadata
Edit `season_metadata.py`:
```python
11: {
    "name": "Guatemala",
    "merge_episode": 7,
    "finalists": ["Danni", "Stephenie"],  # First names only!
    "winner": "Danni",
    # ... other fields
}
```

### 2. Create Voting Data File
Copy `TEMPLATE_season_data.py` to `season11_manual_data.py`:
- Use **first names only** (or unique nicknames if duplicates)
- Include **only pre-merge tribal councils** (before merge episode)
- Match contestant names exactly across all votes
- Include quits/medevacs with `"quit": True` and empty votes dict

### 3. Run Pipeline
```bash
python batch_analyze.py && python batch_visualize.py
```

The scripts auto-detect new `seasonX_manual_data.py` files.

## Data File Structure

### seasonX_manual_data.py Format
```python
SEASON_CONTESTANTS = [
    # All contestants in elimination order (optional but helpful)
]

SEASON_VOTING_HISTORY = [
    {
        "episode": 1,              # Episode number (REQUIRED)
        "day": 3,                  # Day number (optional)
        "tribe": "TribeName",      # Tribe name (optional)
        "eliminated": "PlayerName", # Who was voted out (REQUIRED)
        "votes": {                 # Vote dictionary (REQUIRED)
            "Voter1": "Target1",   # All votes from this tribal
            "Voter2": "Target1",
            # ...
        }
    },
    # Only include episodes BEFORE merge
]
```

### Special Cases
- **Quits/Medevacs:** Set `"quit": True` or `"medevac": True`, use `"votes": {}`
- **Tribe Swaps:** Continue including all pre-merge votes with new tribe compositions
- **Ties/Revotes:** Include final vote only (the one that eliminated someone)

## Output Structure

```
visualizations/
├── seasons_comparison.png          # Bar chart of all seasons
├── season01/
│   ├── season01_alliances.png     # Static network diagram
│   └── season01_interactive.html  # Hover to see alliance stats
├── season02/...
└── season10/...

data/seasons/
├── season01/
│   └── analysis_results.json      # All alliance data + metadata
├── season02/...
└── season10/...
```

## Web Scraping Limitations

`survivor_data_collector.py` **does not work** because:
- Survivor Wiki (fandom.com) returns 403 Forbidden for automated requests
- Table structures vary significantly across seasons
- Manual data entry is the reliable approach

The scraper remains in the codebase as reference but should not be used.

## Key Analysis Metrics

- **Strong Alliance:** 2+ votes together (filters out random one-time alignments)
- **Vote Alignment:** When two players vote for the same target in the same tribal council
- **Edge Weight:** Number of times a pair voted together (displayed as edge thickness)

## Visualization Styling Rules

From `batch_visualize.py`:
- **Winner nodes:** Gold (#FFD700), size 4000, dark red border (6px)
- **Finalist nodes:** Silver (#E8E8E8), size 3500, dark red border (5px)
- **Regular nodes:** Sky blue (#87CEEB), size 2000, gray border (2px)
- **Edge thickness:** Scales from 1-10 based on vote count (max vote count determines scale)
- **Layout:** Spring layout with k=2, iterations=50, seed=42 (consistent positioning)

## Important Gotchas

1. **Season numbering:** File names use zero-padded numbers (`season01`) but metadata uses integers (`1`)
2. **Module imports:** `batch_analyze.py` uses `importlib` to dynamically load `seasonX_manual_data.py` modules
3. **Finalist highlighting only works if names match exactly** between metadata and voting data
4. **Pre-merge cutoff is exclusive:** If merge is Episode 7, only Episodes 1-6 are analyzed
5. **Empty votes dict for quits:** When someone quits, use `"votes": {}` not missing votes key

## Data Quality Notes

- **Seasons 1-10:** Complete verified pre-merge voting data from Survivor Wiki
- **Web scraping:** Not viable due to site blocking (403 errors)
- **Manual entry effort:** ~2-3 hours per season (6 tribal councils × ~10 votes each)
