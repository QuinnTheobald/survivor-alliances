"""
Manual Data Entry for Survivor Season 7 (Pearl Islands)
Based on: https://survivor.fandom.com/wiki/Survivor:_Pearl_Islands

Season 7: Pearl Islands (2003)
16 contestants, merge at Episode 7
Final 2: Sandra Diaz-Twine (winner), Lillian Morris

Tribes:
- Drake (Red): Burton, Christa, Jon, Michelle, Rupert, Sandra, Shawn, Trish
- Morgan (Blue): Andrew, Darrah, Lillian, Nicole, Osten, Ryan O, Ryan S, Tijuana

Note: Outcasts twist in Episode 7 (Burton & Lillian returned)
"""

# All contestants in elimination order
SEASON_CONTESTANTS = [
    # Pre-merge eliminations
    "Nicole",     # Episode 1 - Morgan
    "Ryan O",     # Episode 2 - Morgan (quit)
    "Lillian",    # Episode 3 - Morgan
    "Burton",     # Episode 4 - Drake
    "Michelle",   # Episode 5 - Drake
    "Trish",      # Episode 6 - Drake
    # Merge Episode 7 onwards (Outcasts returned)
    "Shawn",      # Episode 7 (first merge boot)
    "Osten",      # Episode 8 (quit)
    "Andrew",     # Episode 9
    "Ryan S",     # Episode 10
    "Rupert",     # Episode 11
    "Tijuana",    # Episode 12
    "Christa",    # Episode 13
    "Jon",        # Episode 14
    "Darrah",     # Episode 15
    "Lillian",    # Final 2 (Runner-up) - returned from Outcasts
    "Sandra",     # Final 2 (Winner)
]

# PRE-MERGE voting history (Episodes 1-6 only)
SEASON_VOTING_HISTORY = [
    # Episode 1, Day 3 - Nicole voted out (Morgan tribe)
    {
        "episode": 1,
        "day": 3,
        "tribe": "Morgan",
        "eliminated": "Nicole",
        "votes": {
            "Andrew": "Nicole",
            "Darrah": "Nicole",
            "Lillian": "Nicole",
            "Nicole": "Tijuana",
            "Osten": "Nicole",
            "Ryan O": "Nicole",
            "Ryan S": "Nicole",
            "Tijuana": "Nicole",
        }
    },

    # Episode 2, Day 6 - Ryan O quit (Morgan tribe)
    # Note: No tribal council, Ryan O quit
    {
        "episode": 2,
        "day": 6,
        "tribe": "Morgan",
        "eliminated": "Ryan O",
        "quit": True,
        "votes": {}  # No votes, he quit
    },

    # Episode 3, Day 9 - Lillian voted out (Morgan tribe)
    {
        "episode": 3,
        "day": 9,
        "tribe": "Morgan",
        "eliminated": "Lillian",
        "votes": {
            "Andrew": "Lillian",
            "Darrah": "Lillian",
            "Lillian": "Osten",
            "Osten": "Lillian",
            "Ryan S": "Lillian",
            "Tijuana": "Lillian",
        }
    },

    # Episode 4, Day 12 - Burton voted out (Drake tribe)
    {
        "episode": 4,
        "day": 12,
        "tribe": "Drake",
        "eliminated": "Burton",
        "votes": {
            "Burton": "Rupert",
            "Christa": "Burton",
            "Jon": "Burton",
            "Michelle": "Burton",
            "Rupert": "Burton",
            "Sandra": "Burton",
            "Shawn": "Burton",
            "Trish": "Burton",
        }
    },

    # Episode 5, Day 15 - Michelle voted out (Drake tribe)
    {
        "episode": 5,
        "day": 15,
        "tribe": "Drake",
        "eliminated": "Michelle",
        "votes": {
            "Christa": "Michelle",
            "Jon": "Michelle",
            "Michelle": "Shawn",
            "Rupert": "Michelle",
            "Sandra": "Michelle",
            "Shawn": "Michelle",
            "Trish": "Michelle",
        }
    },

    # Episode 6, Day 18 - Trish voted out (Drake tribe)
    {
        "episode": 6,
        "day": 18,
        "tribe": "Drake",
        "eliminated": "Trish",
        "votes": {
            "Christa": "Trish",
            "Jon": "Trish",
            "Rupert": "Trish",
            "Sandra": "Trish",
            "Shawn": "Trish",
            "Trish": "Jon",
        }
    },
]

if __name__ == "__main__":
    print("Survivor Season 7: Pearl Islands")
    print("=" * 50)
    print(f"Contestants: {len(SEASON_CONTESTANTS)}")
    print(f"Pre-merge tribal councils: {len(SEASON_VOTING_HISTORY)}")
    print(f"Winner: Sandra Diaz-Twine")
    print(f"\nNote: Lillian returned via Outcasts twist after Episode 3")
