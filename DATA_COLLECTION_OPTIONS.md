# Survivor Seasons 21-25 Data Collection Options

## Problem Statement
You requested scraping Survivor Wiki for voting data for seasons 21-25. However, as documented in CLAUDE.md, **web scraping of Survivor Wiki does not work** due to 403 Forbidden errors and anti-bot protections.

## Three Options (Ranked by Efficiency)

### 🏆 Option 1: R Package Method (RECOMMENDED) - 15 minutes

**Pros:**
- Complete, verified data for all 5 seasons
- Automated - no manual entry errors
- CSV output can be automatically converted to Python format

**Steps:**
1. Install R: `brew install r` (on macOS)
2. Run: `Rscript extract_voting_data.R`
3. This creates `seasons_21-25_premerge_votes.csv`
4. I can then help convert CSV → Python data files automatically

**Files created:**
- `extract_voting_data.R` - The extraction script
- `INSTALL_R_AND_EXTRACT.md` - Detailed instructions

---

### 📝 Option 2: Manual Entry - 8-10 hours

**Pros:**
- No software installation required
- Direct control over data quality
- Good for learning the data intimately

**Cons:**
- Time-consuming (~2 hours per season)
- Risk of transcription errors
- Tedious for ~35 tribal councils

**Steps:**
1. Follow guide in `MANUAL_ENTRY_GUIDE.md`
2. Visit Survivor Wiki pages for each season
3. Find "Voting History" tables
4. Manually transcribe votes into Python files

---

### ⚠️ Option 3: Attempt Python Scraping - Will Likely Fail

**Why it exists:**
- Testing if anti-bot measures have changed
- Educational purposes

**Expected result:**
- 403 Forbidden errors (per CLAUDE.md)

**To try anyway:**
```bash
python3 attempt_scrape_voting.py
```

---

## My Recommendation

**Use Option 1 (R package method)** because:

1. ✅ Fastest (15 min vs 8-10 hours)
2. ✅ Most accurate (official data source)
3. ✅ No transcription errors
4. ✅ Easy to verify and reproduce
5. ✅ Can be automated to update if needed

## Quick Start (Option 1)

```bash
# Install R if needed
brew install r

# Run extraction
cd /Users/qtheo/Documents/coding-projects/survivor-alliances/21-30
Rscript extract_voting_data.R

# You should now have: seasons_21-25_premerge_votes.csv
# Then I can help convert it to Python files
```

## Sources Used in Research

- [Survivor: Nicaragua Wiki](https://survivor.fandom.com/wiki/Survivor:_Nicaragua)
- [Survivor: Redemption Island Wiki](https://survivor.fandom.com/wiki/Survivor:_Redemption_Island)
- [Survivor: South Pacific Wiki](https://survivor.fandom.com/wiki/Survivor:_South_Pacific)
- [Survivor: One World Wiki](https://survivor.fandom.com/wiki/Survivor:_One_World)
- [Survivor: Philippines Wiki](https://survivor.fandom.com/wiki/Survivor:_Philippines)
- [True Dork Times Boxscores](https://www.truedorktimes.com/survivor/boxscores/)
- [survivoR R Package (GitHub)](https://github.com/doehm/survivoR)
- [survivoR Package Documentation](https://cran.r-project.org/web/packages/survivoR/index.html)
- [Survivor Stats DB](https://survivorstatsdb.com)

## What Happens Next?

Once you have the CSV file (from Option 1) or manually entered data (from Option 2), I can:

1. Parse the CSV/data
2. Group by season and tribal council
3. Format into `seasonXX_manual_data.py` files
4. Verify finalist names match `season_metadata.py`
5. Test with `batch_analyze.py` and `batch_visualize.py`

Let me know which option you'd like to proceed with!
