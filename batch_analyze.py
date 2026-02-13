#!/usr/bin/env python3
"""
Batch Analysis Script for Multiple Seasons
Analyzes pre-merge voting patterns for all available season data
"""

import json
from pathlib import Path
from collections import defaultdict
from season_metadata import get_all_seasons
import importlib.util

def import_season_data(season_num):
    """Dynamically import season data module if it exists."""
    module_path = Path(f"season{season_num}_manual_data.py")

    if not module_path.exists():
        return None

    spec = importlib.util.spec_from_file_location(f"season{season_num}_data", module_path)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    return None

def calculate_vote_alignments(voting_history, merge_episode):
    """
    Calculate how many times each pair of players voted together (pre-merge only).

    Args:
        voting_history: List of tribal council dictionaries
        merge_episode: Episode number when merge occurred
    """
    alignment_counts = defaultdict(int)

    for tribal_council in voting_history:
        # Only analyze pre-merge votes
        episode = tribal_council.get('episode', 999)
        if episode >= merge_episode:
            break

        votes = tribal_council.get('votes', {})
        voters = list(votes.keys())

        for i, voter1 in enumerate(voters):
            for voter2 in voters[i+1:]:
                if votes[voter1] == votes[voter2]:
                    pair = tuple(sorted([voter1, voter2]))
                    alignment_counts[pair] += 1

    return alignment_counts

def analyze_season(season_num, metadata, data_module):
    """Analyze a single season's voting data."""
    print(f"\nAnalyzing Season {season_num}: {metadata['name']}")
    print("-" * 60)

    # Get voting history from the module
    voting_history = getattr(data_module, 'SEASON_VOTING_HISTORY',
                            getattr(data_module, f'SEASON_{season_num}_VOTING_HISTORY', None))

    if not voting_history:
        print(f"  ✗ No voting history found")
        return None

    contestants = getattr(data_module, 'SEASON_CONTESTANTS',
                         getattr(data_module, f'SEASON_{season_num}_CONTESTANTS', None))

    # Calculate pre-merge alignments only
    merge_episode = metadata['merge_episode']
    pre_merge_tcs = sum(1 for tc in voting_history if tc.get('episode', 999) < merge_episode)

    print(f"  Pre-merge tribal councils: {pre_merge_tcs}")

    alignments = calculate_vote_alignments(voting_history, merge_episode)
    strong_alliances = {k: v for k, v in alignments.items() if v >= 2}

    print(f"  Player pairs analyzed: {len(alignments)}")
    print(f"  Strong alliances (2+ votes): {len(strong_alliances)}")

    if strong_alliances:
        sorted_alliances = sorted(strong_alliances.items(), key=lambda x: x[1], reverse=True)
        top_alliance = sorted_alliances[0]
        print(f"  Strongest: {top_alliance[0][0]} ↔ {top_alliance[0][1]} ({top_alliance[1]} votes)")

    # Create results structure
    results = {
        "season": season_num,
        "season_name": metadata['name'],
        "year": metadata['year'],
        "analysis_type": "pre_merge_only",
        "merge_episode": merge_episode,
        "total_tribal_councils": pre_merge_tcs,
        "total_tribal_councils_all_season": len(voting_history),
        "contestants": contestants if contestants else [],
        "finalists": metadata['finalists'],
        "winner": metadata['winner'],
        "all_alignments": [
            {
                "player1": pair[0],
                "player2": pair[1],
                "votes_together": count
            }
            for pair, count in sorted(alignments.items(), key=lambda x: x[1], reverse=True)
        ],
        "strong_alliances": [
            {
                "player1": pair[0],
                "player2": pair[1],
                "votes_together": count
            }
            for pair, count in sorted(strong_alliances.items(), key=lambda x: x[1], reverse=True)
        ]
    }

    return results

def save_season_results(season_num, results, output_dir='data/seasons'):
    """Save analysis results for a season."""
    season_dir = Path(output_dir) / f"season{season_num:02d}"
    season_dir.mkdir(parents=True, exist_ok=True)

    output_file = season_dir / "analysis_results.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"  ✓ Saved to {output_file}")
    return output_file

def main():
    """Main execution function."""
    print("🏝️  SURVIVOR BATCH ANALYSIS - PRE-MERGE ALLIANCES")
    print("Analyzing Seasons 1-20")
    print("=" * 70)

    seasons = get_all_seasons(1, 20)
    results_summary = []

    for season_num in sorted(seasons.keys()):
        metadata = seasons[season_num]

        # Try to import season data
        data_module = import_season_data(season_num)

        if not data_module:
            print(f"\n✗ Season {season_num}: {metadata['name']} - No data file found")
            print(f"  Create 'season{season_num}_manual_data.py' to analyze this season")
            results_summary.append({
                'season': season_num,
                'name': metadata['name'],
                'status': 'no_data'
            })
            continue

        try:
            results = analyze_season(season_num, metadata, data_module)

            if results:
                save_season_results(season_num, results)
                results_summary.append({
                    'season': season_num,
                    'name': metadata['name'],
                    'status': 'success',
                    'alliances': len(results['strong_alliances'])
                })
            else:
                results_summary.append({
                    'season': season_num,
                    'name': metadata['name'],
                    'status': 'failed'
                })

        except Exception as e:
            print(f"  ✗ Error: {e}")
            import traceback
            traceback.print_exc()
            results_summary.append({
                'season': season_num,
                'name': metadata['name'],
                'status': 'error'
            })

    # Print summary
    print("\n" + "=" * 70)
    print("BATCH ANALYSIS SUMMARY")
    print("=" * 70)

    for item in results_summary:
        season_num = item['season']
        name = item['name']
        status = item['status']

        if status == 'success':
            alliances = item.get('alliances', 0)
            print(f"✓ Season {season_num:2d} - {name:30s} | {alliances} strong alliances")
        elif status == 'no_data':
            print(f"○ Season {season_num:2d} - {name:30s} | No data file")
        else:
            print(f"✗ Season {season_num:2d} - {name:30s} | {status}")

    success_count = sum(1 for s in results_summary if s['status'] == 'success')
    print("\n" + "=" * 70)
    print(f"Successfully analyzed: {success_count}/{len(results_summary)} seasons")
    print("=" * 70)

if __name__ == "__main__":
    main()
