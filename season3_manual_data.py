"""
Manual Data Entry for Survivor Season 3 (Africa)
Based on: https://survivor.fandom.com/wiki/Survivor:_Africa

Season 3: Africa (2001)
16 contestants, merge at Episode 7
Final 2: Ethan Zohn (winner), Kim Johnson

Tribes:
- Boran (Red): Brandon, Clarence, Ethan, Kelly, Kim J, Lex, Tom, Jessie
- Samburu (Yellow): Carl, Frank, Kim P, Linda, Lindsey, Silas, Teresa, T-Bird

Note: Tribe swap occurred in Episode 4
"""

# All contestants in elimination order
SEASON_CONTESTANTS = [
    # Pre-merge eliminations
    "Jessie",     # Episode 1 - Boran
    "Carl",       # Episode 2 - Samburu
    "Linda",      # Episode 3 - Samburu
    "Silas",      # Episode 4 - Samburu (after swap)
    "Lindsey",    # Episode 5 - Samburu
    "Clarence",   # Episode 6 - Boran
    # Merge Episode 7 onwards
    "Kelly",      # Episode 7 (first merge boot)
    "Brandon",    # Episode 8
    "Frank",      # Episode 9
    "Kim P",      # Episode 10
    "Teresa",     # Episode 11
    "Tom",        # Episode 12
    "Lex",        # Episode 13
    "Kim J",      # Final 2 (Runner-up)
    "Ethan",      # Final 2 (Winner)
]

# PRE-MERGE voting history (Episodes 1-6 only)
SEASON_VOTING_HISTORY = [
    # Episode 1, Day 3 - Jessie voted out (Boran tribe)
    {
        "episode": 1,
        "day": 3,
        "tribe": "Boran",
        "eliminated": "Jessie",
        "votes": {
            "Brandon": "Jessie",
            "Clarence": "Jessie",
            "Ethan": "Jessie",
            "Jessie": "Clarence",
            "Kelly": "Jessie",
            "Kim J": "Jessie",
            "Lex": "Jessie",
            "Tom": "Jessie",
        }
    },

    # Episode 2, Day 6 - Carl voted out (Samburu tribe)
    {
        "episode": 2,
        "day": 6,
        "tribe": "Samburu",
        "eliminated": "Carl",
        "votes": {
            "Carl": "Linda",
            "Frank": "Carl",
            "Kim P": "Carl",
            "Linda": "Carl",
            "Lindsey": "Carl",
            "Silas": "Carl",
            "Teresa": "Carl",
        }
    },

    # Episode 3, Day 9 - Linda voted out (Samburu tribe)
    {
        "episode": 3,
        "day": 9,
        "tribe": "Samburu",
        "eliminated": "Linda",
        "votes": {
            "Frank": "Silas",
            "Kim P": "Linda",
            "Linda": "Silas",
            "Lindsey": "Linda",
            "Silas": "Linda",
            "Teresa": "Linda",
        }
    },

    # Episode 4, Day 12 - Silas voted out (Samburu tribe, after swap)
    # Tribe swap: Frank, Teresa, Silas swapped
    {
        "episode": 4,
        "day": 12,
        "tribe": "Samburu",
        "eliminated": "Silas",
        "votes": {
            "Frank": "Silas",
            "Kim P": "Frank",
            "Lindsey": "Frank",
            "Silas": "Frank",
            "Teresa": "Silas",
        }
    },

    # Episode 5, Day 15 - Lindsey voted out (Samburu tribe)
    {
        "episode": 5,
        "day": 15,
        "tribe": "Samburu",
        "eliminated": "Lindsey",
        "votes": {
            "Frank": "Lindsey",
            "Kim P": "Lindsey",
            "Lindsey": "Teresa",
            "Teresa": "Lindsey",
        }
    },

    # Episode 6, Day 18 - Clarence voted out (Boran tribe)
    {
        "episode": 6,
        "day": 18,
        "tribe": "Boran",
        "eliminated": "Clarence",
        "votes": {
            "Brandon": "Clarence",
            "Clarence": "Lex",
            "Ethan": "Clarence",
            "Kelly": "Clarence",
            "Kim J": "Clarence",
            "Lex": "Clarence",
            "Tom": "Clarence",
        }
    },
]

if __name__ == "__main__":
    print("Survivor Season 3: Africa")
    print("=" * 50)
    print(f"Contestants: {len(SEASON_CONTESTANTS)}")
    print(f"Pre-merge tribal councils: {len(SEASON_VOTING_HISTORY)}")
    print(f"Winner: Ethan Zohn")
    print(f"\nPre-merge boots: {SEASON_CONTESTANTS[:6]}")
