"""
Manual Data Entry for Survivor Season 8 (All-Stars)
Based on: https://survivor.fandom.com/wiki/Survivor:_All-Stars

Season 8: All-Stars (2004)
18 contestants (all returning players), merge at Episode 7
Final 2: Amber Brkich (winner), Rob Mariano

Tribes:
- Chapera (Red): Amber, Rob M, Rupert, Sue, Tom
- Mogo Mogo (Blue): Colby, Ethan, Jenna L, Jenna M, Kathy, Lex, Richard, Shii Ann
- Saboga (Yellow): Jenna M, Jerri, Rudy, Tina

Note: Tribe dissolution in Episode 3, Saboga disbanded
"""

# All contestants in elimination order
SEASON_CONTESTANTS = [
    # Pre-merge eliminations
    "Tina",       # Episode 1 - Saboga
    "Rudy",       # Episode 2 - Saboga
    "Jenna M",    # Episode 3 - Mogo Mogo (quit)
    "Rob C",      # Episode 4 - Chapera
    "Richard",    # Episode 5 - Mogo Mogo
    "Sue",        # Episode 6 - Chapera (quit)
    # Merge Episode 7 onwards
    "Colby",      # Episode 7 (first merge boot)
    "Ethan",      # Episode 8
    "Jerri",      # Episode 9
    "Lex",        # Episode 10
    "Kathy",      # Episode 11
    "Alicia",     # Episode 12
    "Shii Ann",   # Episode 13
    "Tom",        # Episode 14
    "Rupert",     # Episode 15
    "Jenna L",    # Episode 16
    "Rob M",      # Final 2 (Runner-up)
    "Amber",      # Final 2 (Winner)
]

# PRE-MERGE voting history (Episodes 1-6 only)
SEASON_VOTING_HISTORY = [
    # Episode 1, Day 3 - Tina voted out (Saboga tribe)
    {
        "episode": 1,
        "day": 3,
        "tribe": "Saboga",
        "eliminated": "Tina",
        "votes": {
            "Ethan": "Tina",
            "Jenna M": "Tina",
            "Jerri": "Tina",
            "Rob C": "Tina",
            "Rudy": "Tina",
            "Tina": "Rudy",
        }
    },

    # Episode 2, Day 6 - Rudy voted out (Saboga tribe)
    {
        "episode": 2,
        "day": 6,
        "tribe": "Saboga",
        "eliminated": "Rudy",
        "votes": {
            "Ethan": "Rudy",
            "Jenna M": "Rudy",
            "Jerri": "Rudy",
            "Rob C": "Rudy",
            "Rudy": "Jenna M",
        }
    },

    # Episode 3, Day 9 - Jenna M quit (Mogo Mogo tribe)
    # Saboga dissolved; members joined other tribes
    # Jenna M quit (family emergency), no vote
    {
        "episode": 3,
        "day": 9,
        "tribe": "Mogo Mogo",
        "eliminated": "Jenna M",
        "quit": True,
        "votes": {}
    },

    # Episode 4, Day 12 - Rob C voted out (Chapera tribe)
    {
        "episode": 4,
        "day": 12,
        "tribe": "Chapera",
        "eliminated": "Rob C",
        "votes": {
            "Alicia": "Rob C",
            "Amber": "Rob C",
            "Rob C": "Alicia",
            "Rob M": "Rob C",
            "Sue": "Rob C",
            "Tom": "Rob C",
        }
    },

    # Episode 5, Day 15 - Richard voted out (Mogo Mogo tribe)
    {
        "episode": 5,
        "day": 15,
        "tribe": "Mogo Mogo",
        "eliminated": "Richard",
        "votes": {
            "Colby": "Richard",
            "Jenna L": "Richard",
            "Kathy": "Richard",
            "Lex": "Richard",
            "Richard": "Colby",
            "Shii Ann": "Richard",
        }
    },

    # Episode 6, Day 18 - Sue quit (Chapera tribe)
    # Sue quit after incident with Richard, no vote
    {
        "episode": 6,
        "day": 18,
        "tribe": "Chapera",
        "eliminated": "Sue",
        "quit": True,
        "votes": {}
    },
]

if __name__ == "__main__":
    print("Survivor Season 8: All-Stars")
    print("=" * 50)
    print(f"Contestants: {len(SEASON_CONTESTANTS)}")
    print(f"Pre-merge tribal councils: {len(SEASON_VOTING_HISTORY)}")
    print(f"Winner: Amber Brkich")
    print(f"\nNote: 2 quits (Jenna M, Sue) and tribe dissolution in Episode 3")
