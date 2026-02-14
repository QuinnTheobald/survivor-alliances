#!/usr/bin/env python3
"""
Progress Tracker for Survivor Data Collection

Visual dashboard showing completion status for data collection, analysis, and visualization.
Displays progress bars and status indicators for each season.

Usage:
    python scripts/track_progress.py                  # Default: seasons 21-30
    python scripts/track_progress.py --range 21 30    # Custom range
    python scripts/track_progress.py --all            # All seasons in metadata
"""

import argparse
import importlib
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))
from season_metadata import SEASONS_METADATA


def check_season_progress(season_num):
    """Check progress for a single season."""
    status = {
        'season': season_num,
        'metadata': False,
        'file_exists': False,
        'contestants_filled': False,
        'votes_filled': False,
        'expected_tcs': 0,
        'actual_tcs': 0,
        'analysis_exists': False,
        'viz_exists': False,
        'completion_pct': 0
    }

    # Check metadata
    if season_num in SEASONS_METADATA:
        status['metadata'] = True
        metadata = SEASONS_METADATA[season_num]
        status['season_name'] = metadata.get('name', 'Unknown')
        status['expected_tcs'] = metadata.get('merge_episode', 0) - 1
    else:
        status['season_name'] = 'Unknown'
        return status

    # Check data file exists
    module_name = f"season{season_num}_manual_data"
    try:
        season_module = importlib.import_module(module_name)
        status['file_exists'] = True

        # Check contestants list
        if hasattr(season_module, 'SEASON_CONTESTANTS'):
            contestants = season_module.SEASON_CONTESTANTS
            if contestants and len(contestants) > 0:
                # Check if it's not just empty/placeholder
                if not all(c == "" or "TODO" in str(c) for c in contestants):
                    status['contestants_filled'] = True

        # Check voting history
        if hasattr(season_module, 'SEASON_VOTING_HISTORY'):
            voting_history = season_module.SEASON_VOTING_HISTORY

            # Count TCs with actual data (not "TBD" placeholders)
            actual_tcs = 0
            for tc in voting_history:
                votes = tc.get('votes', {})
                eliminated = tc.get('eliminated', 'TBD')

                # Check if this TC has real data
                if votes and eliminated != 'TBD':
                    # Check votes aren't just empty/TODO
                    if any(voter != 'TBD' for voter in votes.keys()):
                        actual_tcs += 1

            status['actual_tcs'] = actual_tcs
            if actual_tcs > 0:
                status['votes_filled'] = True

    except ModuleNotFoundError:
        pass  # File doesn't exist
    except Exception as e:
        pass  # Import error

    # Check analysis results
    season_padded = f"{season_num:02d}"
    analysis_path = Path(f"data/seasons/season{season_padded}/analysis_results.json")
    status['analysis_exists'] = analysis_path.exists()

    # Check visualizations
    viz_png = Path(f"visualizations/season{season_padded}/season{season_padded}_alliances.png")
    viz_html = Path(f"visualizations/season{season_padded}/season{season_padded}_interactive.html")
    status['viz_exists'] = viz_png.exists() and viz_html.exists()

    # Calculate overall completion percentage
    if status['expected_tcs'] > 0:
        # Weight different stages
        progress = 0
        progress += 10 if status['metadata'] else 0
        progress += 10 if status['file_exists'] else 0
        progress += 15 if status['contestants_filled'] else 0
        progress += 40 * (status['actual_tcs'] / status['expected_tcs']) if status['expected_tcs'] > 0 else 0
        progress += 15 if status['analysis_exists'] else 0
        progress += 10 if status['viz_exists'] else 0
        status['completion_pct'] = min(100, progress)
    else:
        status['completion_pct'] = 10 if status['metadata'] else 0

    return status


def draw_progress_bar(percentage, width=20):
    """Draw a text-based progress bar."""
    filled = int(width * percentage / 100)
    empty = width - filled
    bar = "█" * filled + "░" * empty
    return f"[{bar}] {percentage:3.0f}%"


def format_status_icon(value):
    """Return a status icon based on boolean value."""
    return "✅" if value else "❌"


def print_season_status(status):
    """Print detailed status for a single season."""
    season_num = status['season']
    season_name = status['season_name']

    # Progress bar
    progress_bar = draw_progress_bar(status['completion_pct'])

    # Title line
    tc_info = ""
    if status['expected_tcs'] > 0:
        tc_info = f" ({status['actual_tcs']}/{status['expected_tcs']} TCs)"

    print(f"\nSeason {season_num} ({season_name}): {progress_bar}{tc_info}")

    # Status indicators
    metadata_icon = format_status_icon(status['metadata'])
    file_icon = format_status_icon(status['file_exists'])
    contestants_icon = format_status_icon(status['contestants_filled'])

    # Votes status (can be partial)
    if status['votes_filled'] and status['actual_tcs'] == status['expected_tcs']:
        votes_icon = "✅"
    elif status['votes_filled']:
        votes_icon = "⚠️ "
    else:
        votes_icon = "❌"

    analysis_icon = format_status_icon(status['analysis_exists'])
    viz_icon = format_status_icon(status['viz_exists'])

    print(f"  {metadata_icon} Metadata  "
          f"{file_icon} File  "
          f"{contestants_icon} Contestants  "
          f"{votes_icon} Votes  "
          f"{analysis_icon} Analysis  "
          f"{viz_icon} Viz")


def main():
    parser = argparse.ArgumentParser(
        description="Track progress of Survivor data collection"
    )
    parser.add_argument(
        "--range",
        nargs=2,
        type=int,
        metavar=("START", "END"),
        help="Track progress for a range of seasons (default: 21-30)"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Track all seasons in metadata"
    )

    args = parser.parse_args()

    # Determine which seasons to track
    if args.all:
        seasons = sorted(SEASONS_METADATA.keys())
        title = "All Seasons"
    elif args.range:
        start, end = args.range
        seasons = range(start, end + 1)
        title = f"Seasons {start}-{end}"
    else:
        # Default to 21-30
        seasons = range(21, 31)
        title = "Seasons 21-30"

    print(f"Survivor Data Collection Progress: {title}")
    print("=" * 70)

    # Check progress for each season
    all_statuses = []
    for season_num in seasons:
        status = check_season_progress(season_num)
        all_statuses.append(status)
        print_season_status(status)

    # Overall summary
    print("\n" + "=" * 70)

    total_seasons = len(all_statuses)
    completed_seasons = sum(1 for s in all_statuses if s['completion_pct'] >= 100)
    avg_completion = sum(s['completion_pct'] for s in all_statuses) / total_seasons if total_seasons > 0 else 0

    print(f"Overall Progress: {completed_seasons}/{total_seasons} seasons complete ({avg_completion:.0f}% average)")

    # Breakdown by stage
    metadata_complete = sum(1 for s in all_statuses if s['metadata'])
    files_created = sum(1 for s in all_statuses if s['file_exists'])
    contestants_filled = sum(1 for s in all_statuses if s['contestants_filled'])
    votes_complete = sum(1 for s in all_statuses if s['votes_filled'] and s['actual_tcs'] == s['expected_tcs'])
    analyzed = sum(1 for s in all_statuses if s['analysis_exists'])
    visualized = sum(1 for s in all_statuses if s['viz_exists'])

    print(f"\nStage Breakdown:")
    print(f"  Metadata:    {metadata_complete}/{total_seasons}")
    print(f"  Files:       {files_created}/{total_seasons}")
    print(f"  Contestants: {contestants_filled}/{total_seasons}")
    print(f"  Votes:       {votes_complete}/{total_seasons}")
    print(f"  Analysis:    {analyzed}/{total_seasons}")
    print(f"  Viz:         {visualized}/{total_seasons}")

    # Next steps suggestion
    print(f"\n💡 Next Steps:")
    if metadata_complete < total_seasons:
        print(f"  1. Add metadata for remaining {total_seasons - metadata_complete} season(s)")
    if files_created < metadata_complete:
        print(f"  2. Run template generator for {metadata_complete - files_created} season(s)")
    if votes_complete < files_created:
        print(f"  3. Fill voting data for {files_created - votes_complete} season(s)")
    if analyzed < votes_complete:
        print(f"  4. Run: python batch_analyze.py")
    if visualized < analyzed:
        print(f"  5. Run: python batch_visualize.py")


if __name__ == "__main__":
    main()
