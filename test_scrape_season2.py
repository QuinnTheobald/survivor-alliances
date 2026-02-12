#!/usr/bin/env python3
"""
Test web scraping for Season 2 to see if we can extract voting data
"""

import requests
from bs4 import BeautifulSoup
from season_metadata import get_season_info

def test_scrape(season_num=2):
    """Test scraping a season's wiki page."""
    metadata = get_season_info(season_num)

    print(f"Testing Season {season_num}: {metadata['name']}")
    print(f"URL: {metadata['url']}")
    print("=" * 70)

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        response = requests.get(metadata['url'], headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        print("\n✓ Page fetched successfully")

        # Look for voting tables
        print("\nSearching for voting tables...")
        tables = soup.find_all('table', {'class': 'wikitable'})
        print(f"Found {len(tables)} wikitable(s)")

        for i, table in enumerate(tables[:5], 1):  # Check first 5 tables
            headers = table.find_all('th')
            if headers:
                header_texts = [h.get_text(strip=True)[:30] for h in headers[:10]]
                print(f"\nTable {i} headers (first 10): {header_texts}")

                # Check if it looks like a voting table
                header_str = ' '.join(header_texts).lower()
                if 'vote' in header_str or 'day' in header_str or 'episode' in header_str:
                    print(f"  → This might be a voting table!")

                    # Try to get first few rows
                    rows = table.find_all('tr')
                    print(f"  → Has {len(rows)} rows")

    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_scrape(2)
