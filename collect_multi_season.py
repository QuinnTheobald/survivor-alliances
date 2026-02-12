#!/usr/bin/env python3
"""
Multi-Season Survivor Data Collector
Collects voting data for multiple seasons (1-10) with pre-merge filtering
"""

import requests
from bs4 import BeautifulSoup
import json
from collections import defaultdict
from pathlib import Path
import time
from season_metadata import get_all_seasons

def fetch_season_page(season_url, max_retries=3):
    """Fetch the HTML content of a Survivor season wiki page with retry logic."""
    for attempt in range(max_retries):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            }
            response = requests.get(season_url, headers=headers, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            print(f"   ⚠ Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)
            else:
                raise
    return None

def find_voting_table(soup):
    """Find the voting history table in the page."""
    tables = soup.find_all('table', {'class': 'wikitable'})

    for table in tables:
        headers = table.find_all('th')
        header_text = [h.get_text(strip=True).lower() for h in headers]

        # Look for voting table indicators
        has_episode = any('episode' in h or 'day' in h or 'tribal' in h for h in header_text)
        has_votes = any('vote' in h or 'elimination' in h for h in header_text)

        # Voting tables usually have many columns (one per contestant)
        if (has_episode or has_votes) and len(headers) > 5:
            return table

    return None

def clean_name(name):
    """Clean player names by removing footnotes and extra characters."""
    # Remove common wiki markup
    name = name.replace('[', '').replace(']', '').replace('*', '')
    name = name.replace('†', '').replace('‡', '').strip()
    # Take only first name if multiple parts (some wikis use "First Last")
    # But keep both parts for disambiguation
    return name

def parse_voting_data(soup, season_num, merge_episode):
    """
    Parse voting data from the page.

    Returns:
        voting_history: List of tribal council dictionaries
        contestants: List of all contestant names
    """
    table = find_voting_table(soup)

    if not table:
        print("   ✗ Could not find voting table")
        return None, None

    # Try to extract contestant names and voting data
    # This is complex because wiki tables vary by season

    # Look for contestant names in the infobox or summary section
    contestants = set()
    voting_history = []

    # Parse the voting table structure
    rows = table.find_all('tr')

    # Attempt to identify the structure
    # Common patterns:
    # - First row: contestant names
    # - Subsequent rows: each tribal council

    # For now, return placeholder to test the pipeline
    # Real implementation would need season-specific parsing

    print("   ⚠ Voting table parsing needs season-specific implementation")
    return None, None

def calculate_alignments(voting_history):
    """Calculate how many times each pair voted together."""
    alignment_counts = defaultdict(int)

    for tribal_council in voting_history:
        votes = tribal_council.get('votes', {})
        voters = list(votes.keys())

        for i, voter1 in enumerate(voters):
            for voter2 in voters[i+1:]:
                if votes[voter1] == votes[voter2]:
                    pair = tuple(sorted([voter1, voter2]))
                    alignment_counts[pair] += 1

    return alignment_counts

def collect_season_data(season_num, metadata, output_dir='data/seasons'):
    """Collect data for a single season."""
    print(f"\n{'='*70}")
    print(f"SEASON {season_num}: {metadata['name']} ({metadata['year']})")
    print(f"{'='*70}")

    try:
        # Fetch page
        print(f"1. Fetching: {metadata['url']}")
        soup = fetch_season_page(metadata['url'])
        print("   ✓ Page fetched")

        # Parse voting data
        print(f"2. Parsing voting data (pre-merge only, up to episode {metadata['merge_episode']-1})")
        voting_history, contestants = parse_voting_data(soup, season_num, metadata['merge_episode'])

        if not voting_history:
            print(f"   ⚠ Using manual data for Season {season_num} (scraping not fully implemented)")
            return None

        # Calculate alignments
        print("3. Calculating vote alignments...")
        alignments = calculate_alignments(voting_history)
        print(f"   ✓ Found {len(alignments)} player pairs")

        # Save results
        season_dir = Path(output_dir) / f"season{season_num:02d}"
        season_dir.mkdir(parents=True, exist_ok=True)

        results = {
            "season": season_num,
            "season_name": metadata['name'],
            "year": metadata['year'],
            "analysis_type": "pre_merge_only",
            "merge_episode": metadata['merge_episode'],
            "contestants": list(contestants) if contestants else [],
            "finalists": metadata['finalists'],
            "winner": metadata['winner'],
            "voting_history": voting_history,
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
                for pair, count in sorted(alignments.items(), key=lambda x: x[1], reverse=True)
                if count >= 2
            ]
        }

        output_file = season_dir / "analysis_results.json"
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)

        print(f"4. ✓ Saved to {output_file}")

        return results

    except Exception as e:
        print(f"   ✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    """Main execution function."""
    print("🏝️  SURVIVOR MULTI-SEASON DATA COLLECTION")
    print("Collecting pre-merge voting data for Seasons 1-10")
    print("=" * 70)

    seasons = get_all_seasons(1, 10)
    results_summary = {}

    for season_num in sorted(seasons.keys()):
        metadata = seasons[season_num]
        result = collect_season_data(season_num, metadata)

        if result:
            results_summary[season_num] = {
                'name': metadata['name'],
                'status': 'success',
                'alliances': len(result.get('strong_alliances', []))
            }
        else:
            results_summary[season_num] = {
                'name': metadata['name'],
                'status': 'failed - needs manual data',
                'alliances': 0
            }

        # Be nice to the server
        time.sleep(2)

    # Print summary
    print("\n" + "=" * 70)
    print("COLLECTION SUMMARY")
    print("=" * 70)

    for season_num, info in results_summary.items():
        status_icon = "✓" if info['status'] == 'success' else "✗"
        print(f"{status_icon} Season {season_num:2d} - {info['name']:25s} | {info['status']}")

    print("\n" + "=" * 70)
    print("NOTE: Web scraping may fail due to varying table formats.")
    print("For failed seasons, manual data entry may be required.")
    print("=" * 70)

if __name__ == "__main__":
    main()
