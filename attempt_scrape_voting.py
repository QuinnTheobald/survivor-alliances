#!/usr/bin/env python3
"""
Attempt to scrape Survivor voting data from Survivor Wiki
WARNING: This may fail with 403 Forbidden errors (see CLAUDE.md)

Alternative: Use the R script (extract_voting_data.R) instead
"""

import requests
from bs4 import BeautifulSoup
import json
import time

# Season metadata
SEASONS = {
    21: {
        "name": "Nicaragua",
        "url": "https://survivor.fandom.com/wiki/Survivor:_Nicaragua",
        "merge_episode": 8
    },
    22: {
        "name": "Redemption_Island",
        "url": "https://survivor.fandom.com/wiki/Survivor:_Redemption_Island",
        "merge_episode": 8
    },
    23: {
        "name": "South_Pacific",
        "url": "https://survivor.fandom.com/wiki/Survivor:_South_Pacific",
        "merge_episode": 8
    },
    24: {
        "name": "One_World",
        "url": "https://survivor.fandom.com/wiki/Survivor:_One_World",
        "merge_episode": 7
    },
    25: {
        "name": "Philippines",
        "url": "https://survivor.fandom.com/wiki/Survivor:_Philippines",
        "merge_episode": 7
    }
}

def scrape_season_voting(season_num):
    """
    Attempt to scrape voting data for a season
    Returns voting data or None if scraping fails
    """
    season_info = SEASONS[season_num]
    url = season_info["url"]

    print(f"\n{'='*60}")
    print(f"Attempting to scrape Season {season_num}: {season_info['name']}")
    print(f"URL: {url}")
    print(f"{'='*60}")

    try:
        # Add headers to try to avoid blocking (may not work)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        }

        response = requests.get(url, headers=headers, timeout=30)

        if response.status_code == 403:
            print("❌ FAILED: 403 Forbidden (as expected per CLAUDE.md)")
            print("   Use the R script method instead (extract_voting_data.R)")
            return None

        if response.status_code != 200:
            print(f"❌ FAILED: HTTP {response.status_code}")
            return None

        print(f"✓ Successfully fetched page (status {response.status_code})")

        soup = BeautifulSoup(response.content, 'html.parser')

        # Try to find voting history table
        # Note: Table structure varies by season, this is a best-effort attempt
        tables = soup.find_all('table', class_='wikitable')

        print(f"Found {len(tables)} wiki tables on page")

        # Look for voting history table (usually has "Voted Out" or "Votes Against" headers)
        for i, table in enumerate(tables):
            headers = [th.get_text().strip() for th in table.find_all('th')]
            if any('vote' in h.lower() or 'eliminated' in h.lower() for h in headers):
                print(f"✓ Possible voting table found (table {i+1})")
                print(f"  Headers: {headers[:5]}...")  # Show first 5 headers
                # TODO: Parse table structure (varies by season)
                # This would require custom parsing logic for each table format

        print("\nNote: Automated parsing of voting tables is complex due to varying formats")
        print("Recommendation: Use R script or manual entry guide instead")

        return None

    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    print("Survivor Voting Data Scraper")
    print("="*60)
    print("WARNING: This script will likely encounter 403 Forbidden errors")
    print("See CLAUDE.md for why web scraping doesn't work")
    print("\nRecommended alternative: Use extract_voting_data.R instead")
    print("="*60)

    input("\nPress Enter to attempt scraping anyway...")

    results = {}
    for season_num in sorted(SEASONS.keys()):
        result = scrape_season_voting(season_num)
        results[season_num] = result
        time.sleep(2)  # Be polite, wait between requests

    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    successful = sum(1 for r in results.values() if r is not None)
    print(f"Successfully scraped: {successful}/5 seasons")

    if successful == 0:
        print("\n❌ No seasons successfully scraped (as expected)")
        print("\n📋 Next steps:")
        print("   1. Install R: brew install r")
        print("   2. Run: Rscript extract_voting_data.R")
        print("   3. OR: Follow MANUAL_ENTRY_GUIDE.md")

if __name__ == "__main__":
    main()
