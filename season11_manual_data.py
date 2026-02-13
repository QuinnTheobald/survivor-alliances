"""
Manual Data Entry for Survivor Season 11 (Guatemala)
Based on: https://survivor.fandom.com/wiki/Survivor:_Guatemala

Season 11: Guatemala (2005)
18 contestants (including 2 returning players), merge at Episode 7
Final 2: Danni Boatwright (winner), Stephenie LaGrossa

Tribes:
- Nakúm (Blue): Blake, Brandon, Cindy, Danni, Margaret, Judd, Brooke
- Yaxhá (Yellow): Amy, Bobby Jon, Brian, Gary, Jamie, Lydia, Morgan, Rafe, Stephenie

Note: Stephenie and Bobby Jon were returning players from Palau
"""

# All contestants in elimination order
SEASON_CONTESTANTS = [
    # Pre-merge eliminations
    "Jim",        # Episode 1 - Nakúm (day 1 evac before tribes formed)
    "Morgan",     # Episode 1 - Yaxhá
    "Brooke",     # Episode 2 - Nakúm
    "Blake",      # Episode 3 - Nakúm
    "Margaret",   # Episode 4 - Nakúm
    "Brian",      # Episode 5 - Yaxhá
    "Amy",        # Episode 6 - Yaxhá
    # Merge Episode 7 onwards
    "Brandon",    # Episode 7 (first merge boot)
    "Bobby Jon",  # Episode 8
    "Jamie",      # Episode 9
    "Gary",       # Episode 10
    "Judd",       # Episode 11
    "Cindy",      # Episode 12
    "Lydia",      # Episode 13
    "Rafe",       # Episode 14
    "Stephenie", # Final 2 (Runner-up)
    "Danni",      # Final 2 (Winner)
]

# PRE-MERGE voting history (Episodes 1-6 only)
SEASON_VOTING_HISTORY = [
    # Episode 1, Day 3 - Morgan voted out (Yaxhá tribe)
    {
        "episode": 1,
        "day": 3,
        "tribe": "Yaxhá",
        "eliminated": "Morgan",
        "votes": {
            "Amy": "Morgan",
            "Bobby Jon": "Morgan",
            "Brian": "Morgan",
            "Gary": "Morgan",
            "Jamie": "Morgan",
            "Lydia": "Morgan",
            "Morgan": "Brian",
            "Rafe": "Morgan",
            "Stephenie": "Morgan",
        }
    },

    # Episode 2, Day 6 - Brooke voted out (Nakúm tribe)
    {
        "episode": 2,
        "day": 6,
        "tribe": "Nakúm",
        "eliminated": "Brooke",
        "votes": {
            "Blake": "Brooke",
            "Brandon": "Brooke",
            "Brooke": "Margaret",
            "Cindy": "Brooke",
            "Danni": "Brooke",
            "Judd": "Brooke",
            "Margaret": "Brooke",
        }
    },

    # Episode 3, Day 9 - Blake voted out (Nakúm tribe)
    {
        "episode": 3,
        "day": 9,
        "tribe": "Nakúm",
        "eliminated": "Blake",
        "votes": {
            "Blake": "Margaret",
            "Brandon": "Blake",
            "Cindy": "Blake",
            "Danni": "Blake",
            "Judd": "Blake",
            "Margaret": "Blake",
        }
    },

    # Episode 4, Day 12 - Margaret voted out (Nakúm tribe, after swap)
    {
        "episode": 4,
        "day": 12,
        "tribe": "Nakúm",
        "eliminated": "Margaret",
        "votes": {
            "Bobby Jon": "Margaret",
            "Brandon": "Margaret",
            "Judd": "Margaret",
            "Margaret": "Judd",
            "Stephenie": "Margaret",
        }
    },

    # Episode 5, Day 15 - Brian voted out (Yaxhá tribe)
    {
        "episode": 5,
        "day": 15,
        "tribe": "Yaxhá",
        "eliminated": "Brian",
        "votes": {
            "Amy": "Brian",
            "Brian": "Gary",
            "Cindy": "Brian",
            "Danni": "Brian",
            "Gary": "Brian",
            "Rafe": "Brian",
        }
    },

    # Episode 6, Day 18 - Amy voted out (Yaxhá tribe)
    {
        "episode": 6,
        "day": 18,
        "tribe": "Yaxhá",
        "eliminated": "Amy",
        "votes": {
            "Amy": "Gary",
            "Cindy": "Amy",
            "Danni": "Amy",
            "Gary": "Amy",
            "Lydia": "Amy",
            "Rafe": "Amy",
        }
    },
]

if __name__ == "__main__":
    print("Survivor Season 11: Guatemala")
    print("=" * 50)
    print(f"Contestants: {len(SEASON_CONTESTANTS)}")
    print(f"Pre-merge tribal councils: {len(SEASON_VOTING_HISTORY)}")
    print(f"Winner: Danni Boatwright")
    print(f"\nPre-merge boots: {SEASON_CONTESTANTS[:7]}")
