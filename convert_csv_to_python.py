#!/usr/bin/env python3
"""
Convert CSV voting data from survivoR R package to Python manual_data files

Usage:
    python3 convert_csv_to_python.py seasons_21-25_premerge_votes.csv

This will create/update:
    - season21_manual_data.py
    - season22_manual_data.py
    - season23_manual_data.py
    - season24_manual_data.py
    - season25_manual_data.py
"""

import csv
import sys
from collections import defaultdict
from pathlib import Path

# Import season metadata to get finalist names
import sys
sys.path.append('..')
try:
    from season_metadata import SEASONS_METADATA
except ImportError:
    print("Warning: Could not import season_metadata.py")
    print("Make sure season_metadata.py is in the parent directory")
    SEASONS_METADATA = {}

def load_csv_data(csv_path):
    """Load voting data from CSV file"""
    votes_by_season = defaultdict(lambda: defaultdict(list))

    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            season = int(row['season'])
            episode = int(row['episode'])
            votes_by_season[season][episode].append(row)

    return votes_by_season

def format_tribal_council(episode_num, votes_data):
    """Format a single tribal council into Python dict format"""
    if not votes_data:
        return None

    # Get common data from first vote
    first_vote = votes_data[0]
    day = first_vote.get('day', 'TBD')
    tribe = first_vote.get('tribe', 'TBD')
    eliminated = first_vote.get('voted_out', 'TBD')

    # Build votes dictionary
    votes_dict = {}
    for vote in votes_data:
        voter = vote.get('castaway', '')
        target = vote.get('vote', '')
        if voter and target:
            votes_dict[voter] = target

    tribal = {
        'episode': episode_num,
        'day': day,
        'tribe': tribe,
        'eliminated': eliminated,
        'votes': votes_dict
    }

    return tribal

def format_python_file(season_num, tribal_councils):
    """Generate Python file content for a season"""
    metadata = SEASONS_METADATA.get(season_num, {})
    season_name = metadata.get('name', f'Season {season_num}')
    merge_ep = metadata.get('merge_episode', 'Unknown')
    url = metadata.get('url', f'https://survivor.fandom.com/wiki/Survivor:_Season_{season_num}')

    # Build header
    content = f'''"""
Survivor Season {season_num}: {season_name}

Pre-merge voting data for alliance analysis.
Merge Episode: {merge_ep} (only Episodes 1-{merge_ep-1} are included here)

Data Source: {url}
Data extracted from survivoR R package
"""

# Contestants in elimination order (from voting data)
SEASON_CONTESTANTS = [
'''

    # Extract eliminated players in order
    eliminated_players = []
    for ep in sorted(tribal_councils.keys()):
        tc = tribal_councils[ep]
        if tc['eliminated'] and tc['eliminated'] != 'TBD':
            eliminated_players.append(tc['eliminated'])

    for player in eliminated_players:
        content += f'    "{player}",\n'

    content += '''    # TODO: Add remaining contestants who weren't eliminated pre-merge
]

# Pre-merge tribal councils only
SEASON_VOTING_HISTORY = [
'''

    # Add tribal councils
    for ep in sorted(tribal_councils.keys()):
        tc = tribal_councils[ep]
        content += '    {\n'
        content += f'        "episode": {tc["episode"]},\n'
        content += f'        "day": {tc["day"]},\n'
        content += f'        "tribe": "{tc["tribe"]}",\n'
        content += f'        "eliminated": "{tc["eliminated"]}",\n'
        content += '        "votes": {\n'

        # Format votes
        for voter, target in sorted(tc["votes"].items()):
            content += f'            "{voter}": "{target}",\n'

        content += '        }\n'
        content += '    },\n'

    content += ''']

# Special cases handled:
# - Quits/medevacs: Add "quit": True or "medevac": True, use "votes": {}
# - Ties/revotes: Include only the final vote that eliminated someone
# - Tribe swaps: Continue including votes with new tribe compositions
'''

    return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 convert_csv_to_python.py seasons_21-25_premerge_votes.csv")
        sys.exit(1)

    csv_path = sys.argv[1]

    if not Path(csv_path).exists():
        print(f"Error: File not found: {csv_path}")
        print("\nDid you run the R script first?")
        print("  Rscript extract_voting_data.R")
        sys.exit(1)

    print(f"Loading voting data from {csv_path}...")
    votes_by_season = load_csv_data(csv_path)

    print(f"\nFound data for {len(votes_by_season)} seasons")

    for season_num in sorted(votes_by_season.keys()):
        print(f"\nProcessing Season {season_num}...")

        episodes = votes_by_season[season_num]
        tribal_councils = {}

        for ep_num in sorted(episodes.keys()):
            votes = episodes[ep_num]
            tc = format_tribal_council(ep_num, votes)
            if tc:
                tribal_councils[ep_num] = tc

        print(f"  Found {len(tribal_councils)} pre-merge tribal councils")

        # Generate Python file
        py_content = format_python_file(season_num, tribal_councils)
        output_file = f"season{season_num:02d}_manual_data.py"

        # Write file
        with open(output_file, 'w') as f:
            f.write(py_content)

        print(f"  ✓ Created {output_file}")

    print("\n" + "="*60)
    print("SUCCESS! All season data files created.")
    print("="*60)
    print("\nNext steps:")
    print("  1. Review the generated files for accuracy")
    print("  2. Verify finalist names match season_metadata.py")
    print("  3. Run: python batch_analyze.py")
    print("  4. Run: python batch_visualize.py")

if __name__ == "__main__":
    main()
