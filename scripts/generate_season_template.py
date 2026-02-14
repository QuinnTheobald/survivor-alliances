#!/usr/bin/env python3
"""
Template Generator for Survivor Season Data Files

Creates skeleton season data files with pre-populated tribal council placeholders
based on season metadata (merge episode determines number of pre-merge TCs).

Usage:
    python scripts/generate_season_template.py 21              # Single season
    python scripts/generate_season_template.py --range 21 30   # Multiple seasons
"""

import argparse
import sys
from pathlib import Path

# Add parent directory to path to import season_metadata
sys.path.insert(0, str(Path(__file__).parent.parent))
from season_metadata import SEASONS_METADATA


def generate_season_template(season_num, output_dir="."):
    """Generate a template season data file with placeholders."""

    # Get metadata for this season
    if season_num not in SEASONS_METADATA:
        print(f"❌ Season {season_num} not found in metadata. Add it to season_metadata.py first.")
        return False

    metadata = SEASONS_METADATA[season_num]
    season_name = metadata['name']
    merge_episode = metadata['merge_episode']
    year = metadata['year']

    # Calculate number of pre-merge tribal councils (merge episode is excluded)
    num_pre_merge_tcs = merge_episode - 1

    # Generate filename
    filename = f"season{season_num}_manual_data.py"
    filepath = Path(output_dir) / filename

    # Check if file already exists
    if filepath.exists():
        print(f"⚠️  File {filename} already exists. Skipping...")
        return False

    # Build tribal council placeholders
    tribal_councils = []
    for episode in range(1, merge_episode):
        tc = f"""    {{
        "episode": {episode},
        "day": "TBD",  # TODO: Fill from wiki
        "tribe": "TBD",  # TODO: Fill tribe name
        "eliminated": "TBD",  # TODO: Fill eliminated player name
        "votes": {{
            # TODO: Fill votes from wiki
            # Format: "Voter": "Target",
        }}
    }}"""
        tribal_councils.append(tc)

    tribal_councils_str = ",\n".join(tribal_councils)

    # Generate file content
    content = f'''"""
Survivor Season {season_num}: {season_name} ({year})

Pre-merge voting data for alliance analysis.
Merge Episode: {merge_episode} (only Episodes 1-{merge_episode - 1} are included here)

Data Source: https://survivor.fandom.com/wiki/Survivor:{season_name.replace(" ", "_")}
"""

# TODO: Fill contestant list with first names (in elimination order)
# Use first names only, or unique nicknames if there are duplicates
# These names MUST match exactly with names used in voting data below
SEASON_CONTESTANTS = [
    # "FirstEliminated",
    # "SecondEliminated",
    # ... add all contestants in order
]

# Pre-merge tribal councils only (Episodes 1-{merge_episode - 1})
# Stop BEFORE Episode {merge_episode} (merge episode)
SEASON_VOTING_HISTORY = [
{tribal_councils_str}
]

# Special cases to handle:
# - For quits/medevacs: Add "quit": True or "medevac": True, use "votes": {{}}
# - For ties/revotes: Include only the final vote that eliminated someone
# - Tribe swaps: Continue including votes with new tribe compositions
'''

    # Write file
    try:
        filepath.write_text(content)
        print(f"✅ Created {filename} with {num_pre_merge_tcs} tribal council placeholders")
        return True
    except Exception as e:
        print(f"❌ Error writing {filename}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Generate Survivor season data file templates"
    )
    parser.add_argument(
        "season",
        type=int,
        nargs="?",
        help="Season number to generate template for"
    )
    parser.add_argument(
        "--range",
        nargs=2,
        type=int,
        metavar=("START", "END"),
        help="Generate templates for a range of seasons (inclusive)"
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Output directory for generated files (default: current directory)"
    )

    args = parser.parse_args()

    # Determine which seasons to generate
    if args.range:
        start, end = args.range
        seasons = range(start, end + 1)
        print(f"Generating templates for Seasons {start}-{end}...")
        print("=" * 70)
    elif args.season:
        seasons = [args.season]
        print(f"Generating template for Season {args.season}...")
        print("=" * 70)
    else:
        parser.print_help()
        sys.exit(1)

    # Generate templates
    success_count = 0
    for season_num in seasons:
        if generate_season_template(season_num, args.output_dir):
            success_count += 1

    # Summary
    print("=" * 70)
    print(f"Generated {success_count}/{len(list(seasons))} template files")

    if success_count > 0:
        print("\nNext steps:")
        print("1. Fill in SEASON_CONTESTANTS list with first names")
        print("2. Fill in tribal council data from Survivor Wiki")
        print("3. Run validation: python scripts/validate_season_data.py <season>")


if __name__ == "__main__":
    main()
