"""
Manual Data Entry for Survivor Season 6 (The Amazon)
Based on: https://survivor.fandom.com/wiki/Survivor:_The_Amazon

Season 6: The Amazon (2003)
16 contestants, merge at Episode 7
Final 2: Jenna Morasca (winner), Matthew von Ertfelda

Tribes:
- Jaburu (Women): Christy, Deena, Heidi, Jenna, JoAnna, Jeanne, Janet, Shawna
- Tambaqui (Men): Alex, Butch, Daniel, Dave, Matthew, Rob, Roger, Ryan

Note: Tribe swap occurred in Episode 5
"""

# All contestants in elimination order
SEASON_CONTESTANTS = [
    # Pre-merge eliminations
    "Ryan",       # Episode 1 - Tambaqui
    "Janet",      # Episode 2 - Jaburu
    "Daniel",     # Episode 3 - Tambaqui
    "JoAnna",     # Episode 4 - Jaburu
    "Jeanne",     # Episode 5 - Tambaqui (after swap)
    "Shawna",     # Episode 6 - Jaburu (after swap)
    # Merge Episode 7 onwards
    "Roger",      # Episode 7 (first merge boot)
    "Dave",       # Episode 8
    "Deena",      # Episode 9
    "Alex",       # Episode 10
    "Christy",    # Episode 11
    "Heidi",      # Episode 12
    "Rob",        # Episode 13
    "Butch",      # Episode 14
    "Matthew",    # Final 2 (Runner-up)
    "Jenna",      # Final 2 (Winner)
]

# PRE-MERGE voting history (Episodes 1-6 only)
SEASON_VOTING_HISTORY = [
    # Episode 1, Day 3 - Ryan voted out (Tambaqui tribe)
    {
        "episode": 1,
        "day": 3,
        "tribe": "Tambaqui",
        "eliminated": "Ryan",
        "votes": {
            "Alex": "Ryan",
            "Butch": "Ryan",
            "Daniel": "Ryan",
            "Dave": "Ryan",
            "Matthew": "Ryan",
            "Rob": "Ryan",
            "Roger": "Ryan",
            "Ryan": "Daniel",
        }
    },

    # Episode 2, Day 6 - Janet voted out (Jaburu tribe)
    {
        "episode": 2,
        "day": 6,
        "tribe": "Jaburu",
        "eliminated": "Janet",
        "votes": {
            "Christy": "Janet",
            "Deena": "Janet",
            "Heidi": "Janet",
            "Janet": "Deena",
            "Jenna": "Janet",
            "JoAnna": "Janet",
            "Jeanne": "Janet",
            "Shawna": "JoAnna",
        }
    },

    # Episode 3, Day 9 - Daniel voted out (Tambaqui tribe)
    {
        "episode": 3,
        "day": 9,
        "tribe": "Tambaqui",
        "eliminated": "Daniel",
        "votes": {
            "Alex": "Daniel",
            "Butch": "Daniel",
            "Daniel": "Roger",
            "Dave": "Daniel",
            "Matthew": "Daniel",
            "Rob": "Daniel",
            "Roger": "Daniel",
        }
    },

    # Episode 4, Day 12 - JoAnna voted out (Jaburu tribe)
    {
        "episode": 4,
        "day": 12,
        "tribe": "Jaburu",
        "eliminated": "JoAnna",
        "votes": {
            "Christy": "JoAnna",
            "Deena": "JoAnna",
            "Heidi": "JoAnna",
            "Jenna": "JoAnna",
            "JoAnna": "Deena",
            "Jeanne": "Deena",
            "Shawna": "JoAnna",
        }
    },

    # Episode 5, Day 15 - Jeanne voted out (Tambaqui tribe, after swap)
    # Swap: Deena, Jeanne, Shawna to Tambaqui; Alex, Matthew, Rob to Jaburu
    {
        "episode": 5,
        "day": 15,
        "tribe": "Tambaqui",
        "eliminated": "Jeanne",
        "votes": {
            "Butch": "Jeanne",
            "Dave": "Jeanne",
            "Deena": "Roger",
            "Jeanne": "Roger",
            "Roger": "Jeanne",
            "Shawna": "Jeanne",
        }
    },

    # Episode 6, Day 18 - Shawna voted out (Tambaqui tribe)
    {
        "episode": 6,
        "day": 18,
        "tribe": "Tambaqui",
        "eliminated": "Shawna",
        "votes": {
            "Butch": "Shawna",
            "Dave": "Shawna",
            "Deena": "Shawna",
            "Roger": "Shawna",
            "Shawna": "Roger",
        }
    },
]

if __name__ == "__main__":
    print("Survivor Season 6: The Amazon")
    print("=" * 50)
    print(f"Contestants: {len(SEASON_CONTESTANTS)}")
    print(f"Pre-merge tribal councils: {len(SEASON_VOTING_HISTORY)}")
    print(f"Winner: Jenna Morasca")
    print(f"\nPre-merge boots: {SEASON_CONTESTANTS[:6]}")
