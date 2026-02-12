# Survivor Alliance Network Analysis - Multi-Season Edition

## Overview
This project analyzes **pre-merge voting alliances** across multiple Survivor seasons, creating network visualizations to reveal tribal dynamics before strategic gameplay begins.

### Current Status: 3/10 Seasons Complete
- ✅ **Season 1: Borneo** (Complete data)
- ✅ **Season 2: The Australian Outback** (Sample data)
- ✅ **Season 3: Africa** (Sample data)
- 📋 **Seasons 4-10**: Ready for data entry

## Quick Start

### Prerequisites
```bash
pip install networkx matplotlib plotly beautifulsoup4 requests pandas
```

### Run Multi-Season Analysis
```bash
# Analyze all available seasons (pre-merge voting only)
python batch_analyze.py

# Generate visualizations for all seasons
python batch_visualize.py
```

### Output
- **Individual season networks**: `visualizations/seasonXX/`
  - PNG (high-resolution static image)
  - HTML (interactive, hoverable)
- **Comparison chart**: `visualizations/seasons_comparison.png`
- **Analysis data**: `data/seasons/seasonXX/analysis_results.json`

## Key Files

### Data Collection
- `season_metadata.py` - Season info (names, merge episodes, winners)
- `seasonX_manual_data.py` - Voting history for each season

### Analysis & Visualization
- `batch_analyze.py` - Analyze all seasons (pre-merge only)
- `batch_visualize.py` - Create network diagrams
- `visualize_season1.py` - Single season visualization (legacy)

### Legacy Scripts
- `survivor_data_collector.py` - Web scraper (limited by site blocking)
- `analyze_season1_manual.py` - Single season analysis

### Expected Output
The script will create a `data/` directory with:

- **season1_votes_raw.json** - Raw voting data for each tribal council
  ```json
  [
    {
      "round_number": 1,
      "episode": "Episode 1",
      "votes": {
        "Richard": "Sonja",
        "Kelly": "Sonja",
        ...
      }
    },
    ...
  ]
  ```

- **season1_alignments.csv** - Player pairs and vote alignment counts
  ```csv
  player1,player2,votes_together
  Richard,Rudy,8
  Kelly,Sue,7
  ...
  ```

- **season1_metadata.json** - Season information
  ```json
  {
    "season": 1,
    "season_name": "Borneo",
    "players": ["Richard", "Kelly", "Rudy", ...],
    "finalists": ["Richard", "Kelly"],
    "total_voting_rounds": 13
  }
  ```

## Data Processing Logic

### Vote Alignment Calculation
For each tribal council:
1. Identify all players who voted
2. For each pair of players, check if they voted for the same person
3. If yes, increment their alignment counter

Example:
```
Tribal Council 1:
- Richard votes for Sonja
- Kelly votes for Sonja
- Rudy votes for Sonja
- Sue votes for Dirk

Alignments created:
- Richard-Kelly: +1
- Richard-Rudy: +1
- Kelly-Rudy: +1
```

### Alliance Network Rules
- Only include pairs with 2+ votes together
- Edge thickness = number of votes together
- Highlight finalists with special visual treatment

## Why Pre-Merge Only?

Pre-merge voting reveals:
- **Original tribal alliances** before strategic gameplay
- **True social bonds** formed early in the game
- **Tribal dynamics** separate from individual strategy

Post-merge data would show different patterns (strategic alliances, final 3 deals, etc.)

## Key Findings So Far

### Season 1: Borneo
- **54 strong alliances** (most connected pre-merge)
- Strongest: Colleen ↔ Gervase (6 votes)
- Very distributed network (no dominant alliance yet)

### Season 2: The Australian Outback
- **24 strong alliances**
- More tribal cohesion
- Tighter voting blocks

### Season 3: Africa
- **24 strong alliances**
- Clear tribal divisions
- Strongest: Frank ↔ Teresa (3 votes)

## How to Add More Seasons

See [`MULTI_SEASON_GUIDE.md`](MULTI_SEASON_GUIDE.md) for complete instructions.

**Quick version:**
1. Create `seasonX_manual_data.py` (use `season1_manual_data.py` as template)
2. Add voting history for **pre-merge tribal councils only**
3. Run `python batch_analyze.py`
4. Run `python batch_visualize.py`

## Known Issues / Manual Steps

### Finalist Identification
The script attempts to automatically identify finalists but may require manual verification.

For Season 1 (Borneo):
- Finalists: **Richard Hatch** and **Kelly Wiglesworth**
- Winner: Richard Hatch

### Table Structure Variations
Different seasons may have slightly different table structures on the wiki. The parsing logic may need adjustment for:
- Hidden immunity idols (post-Season 11)
- Extra votes and advantages (post-Season 28)
- Fire-making challenges (Season 35+)

## Troubleshooting

### "Could not find voting history table"
- Check if the wiki page structure has changed
- Manually inspect the page and adjust `find_voting_table()` function
- Look for the table with class "wikitable" that contains voting data

### Missing or incorrect votes
- Wiki pages sometimes have typos or inconsistencies
- Cross-reference with episode summaries
- Check for footnotes indicating nullified votes or advantages

## Data Quality Notes

The voting history tables on survivor.fandom.com generally include:
- ✓ Regular votes at tribal council
- ✓ Revotes in case of ties
- ✓ Notes about hidden immunity idols
- ✗ May not clearly indicate nullified votes
- ✗ May have inconsistent naming (nicknames vs full names)
