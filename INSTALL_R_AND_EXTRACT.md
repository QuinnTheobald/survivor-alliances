# How to Extract Voting Data Using R

## Step 1: Install R

### On macOS:
```bash
# Using Homebrew
brew install r

# OR download from: https://cran.r-project.org/bin/macosx/
```

### On Linux:
```bash
sudo apt-get install r-base  # Debian/Ubuntu
# OR
sudo yum install R  # RedHat/CentOS
```

## Step 2: Run the Extraction Script

```bash
cd /Users/qtheo/Documents/coding-projects/survivor-alliances/21-30
Rscript extract_voting_data.R
```

This will create `seasons_21-25_premerge_votes.csv` with all the voting data.

## Step 3: Convert CSV to Python Data Files

Once you have the CSV, I can help you convert it into the Python `seasonXX_manual_data.py` format automatically.

## Expected Output

The CSV will contain columns:
- season
- season_name
- episode
- day
- tribe
- castaway (voter name)
- vote (who they voted for)
- voted_out (person eliminated)

This has ALL the data needed to populate the Python files.
