"""
Survivor Season 1 (Borneo) Voting History Data Collector

This script scrapes voting data from survivor.fandom.com and processes it
for alliance network analysis.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from collections import defaultdict

def fetch_season_page(season_url):
    """Fetch the HTML content of a Survivor season wiki page."""
    response = requests.get(season_url)
    response.raise_for_status()
    return BeautifulSoup(response.content, 'html.parser')

def find_voting_table(soup):
    """
    Find the voting history table in the page.
    The voting table typically has headers like 'Episode', player names, etc.
    """
    tables = soup.find_all('table', {'class': 'wikitable'})
    
    for table in tables:
        # Look for table that contains voting information
        headers = table.find_all('th')
        header_text = [h.get_text(strip=True) for h in headers]
        
        # Check if this looks like a voting table
        # Voting tables usually have episode numbers and player names
        if any('Episode' in h or 'Day' in h for h in header_text):
            # Check if it has multiple player name columns
            if len(header_text) > 3:
                return table
    
    return None

def parse_voting_table(table):
    """
    Parse the voting history table and extract vote-by-vote data.
    
    Returns:
        - votes_data: List of dictionaries with voting information
        - players: List of all players in the season
    """
    rows = table.find_all('tr')
    
    # Get headers (player names)
    header_row = rows[0]
    headers = header_row.find_all('th')
    
    # First few columns are usually episode info, rest are player names
    players = []
    for i, h in enumerate(headers):
        header_text = h.get_text(strip=True)
        # Skip metadata columns (Episode, Day, Voted Out, etc.)
        if header_text and header_text not in ['Episode', 'Day', 'Eliminated', 'Votes', 'Voter', '']:
            players.append(header_text)
    
    print(f"Found {len(players)} players: {players}")
    
    # Parse each voting round (each row represents a tribal council)
    votes_data = []
    
    for row_idx, row in enumerate(rows[1:], start=1):  # Skip header row
        cells = row.find_all(['td', 'th'])
        
        if len(cells) < 2:
            continue
        
        # Extract episode/day information
        episode_info = cells[0].get_text(strip=True) if cells else ""
        
        # Create a voting round entry
        voting_round = {
            'round_number': row_idx,
            'episode': episode_info,
            'votes': {}
        }
        
        # Parse each player's vote
        # The table structure typically has: [Episode/Day info] [Player1 vote] [Player2 vote] ...
        for cell_idx, cell in enumerate(cells[1:], start=0):
            if cell_idx >= len(players):
                break
                
            voter = players[cell_idx]
            vote_text = cell.get_text(strip=True)
            
            # Clean up the vote text (remove footnotes, special characters)
            vote_text = vote_text.replace('[', '').replace(']', '').replace('*', '').strip()
            
            if vote_text and vote_text != '-' and vote_text != '':
                voting_round['votes'][voter] = vote_text
        
        if voting_round['votes']:  # Only add if there are votes
            votes_data.append(voting_round)
    
    return votes_data, players

def calculate_vote_alignments(votes_data, players):
    """
    Calculate how many times each pair of players voted together.
    
    Returns:
        - alignment_matrix: Dictionary of player pairs and their vote alignment count
    """
    alignment_counts = defaultdict(int)
    
    for voting_round in votes_data:
        votes = voting_round['votes']
        
        # For each pair of players who both voted in this round
        voters = list(votes.keys())
        
        for i, voter1 in enumerate(voters):
            for voter2 in voters[i+1:]:
                # Check if they voted for the same person
                if votes[voter1] == votes[voter2]:
                    # Create a sorted tuple as key (so order doesn't matter)
                    pair = tuple(sorted([voter1, voter2]))
                    alignment_counts[pair] += 1
    
    return alignment_counts

def identify_finalists(soup):
    """
    Identify the finalists (final 2 or final 3) from the page.
    This typically requires looking at the final tribal council section.
    """
    # This is season-specific and may need adjustment
    # For Season 1, the finalists were Richard Hatch and Kelly Wiglesworth
    
    # Try to find this information in the page
    text = soup.get_text()
    
    # Look for "Final Tribal Council" or similar sections
    finalists = []
    
    # For now, return empty - this needs to be implemented based on page structure
    # In practice, you might manually verify or use additional parsing
    return finalists

def save_data(votes_data, alignment_counts, players, finalists, output_dir='data'):
    """Save the collected data in multiple formats."""
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    # Save raw voting data
    with open(f'{output_dir}/season1_votes_raw.json', 'w') as f:
        json.dump(votes_data, f, indent=2)
    
    # Save alignment counts
    alignment_list = [
        {
            'player1': pair[0],
            'player2': pair[1],
            'votes_together': count
        }
        for pair, count in alignment_counts.items()
    ]
    
    df_alignments = pd.DataFrame(alignment_list)
    df_alignments = df_alignments.sort_values('votes_together', ascending=False)
    df_alignments.to_csv(f'{output_dir}/season1_alignments.csv', index=False)
    
    # Save player list and finalists
    metadata = {
        'season': 1,
        'season_name': 'Borneo',
        'players': players,
        'finalists': finalists,
        'total_voting_rounds': len(votes_data)
    }
    
    with open(f'{output_dir}/season1_metadata.json', 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"\nData saved to {output_dir}/")
    print(f"- season1_votes_raw.json: {len(votes_data)} voting rounds")
    print(f"- season1_alignments.csv: {len(alignment_list)} player pairs")
    print(f"- season1_metadata.json: season metadata")

def main():
    """Main execution function."""
    print("Survivor Season 1 (Borneo) Data Collection")
    print("=" * 50)
    
    # Season 1 URL
    url = "https://survivor.fandom.com/wiki/Survivor:_Borneo"
    
    print(f"\n1. Fetching page: {url}")
    soup = fetch_season_page(url)
    
    print("\n2. Finding voting history table...")
    voting_table = find_voting_table(soup)
    
    if not voting_table:
        print("ERROR: Could not find voting history table!")
        return
    
    print("✓ Found voting table")
    
    print("\n3. Parsing voting data...")
    votes_data, players = parse_voting_table(voting_table)
    print(f"✓ Parsed {len(votes_data)} voting rounds")
    
    print("\n4. Calculating vote alignments...")
    alignment_counts = calculate_vote_alignments(votes_data, players)
    print(f"✓ Calculated alignments for {len(alignment_counts)} player pairs")
    
    # Filter for pairs with at least 2 votes together
    strong_alignments = {k: v for k, v in alignment_counts.items() if v >= 2}
    print(f"✓ Found {len(strong_alignments)} pairs with 2+ votes together")
    
    print("\n5. Identifying finalists...")
    finalists = identify_finalists(soup)
    if not finalists:
        print("⚠ Could not automatically identify finalists")
        print("  For Season 1, finalists were: Richard Hatch, Kelly Wiglesworth")
        finalists = ["Richard", "Kelly"]  # Manual entry for Season 1
    
    print("\n6. Saving data...")
    save_data(votes_data, alignment_counts, players, finalists)
    
    print("\n" + "=" * 50)
    print("Data collection complete!")
    print("\nTop 5 strongest alliances (votes together):")
    sorted_alignments = sorted(alignment_counts.items(), key=lambda x: x[1], reverse=True)
    for pair, count in sorted_alignments[:5]:
        print(f"  {pair[0]} <-> {pair[1]}: {count} votes together")

if __name__ == "__main__":
    main()
