"""
Manual Data Entry for Survivor Season 4 (Marquesas)
Based on: https://survivor.fandom.com/wiki/Survivor:_Marquesas

Season 4: Marquesas (2002)
13 contestants, merge at Episode 7
Final 2: Vecepia Towery (winner), Neleh Dennis

Tribes:
- Maraamu (Yellow): Gabriel, Gina, John, Neleh, Patricia, Peter, Sarah, Vecepia
- Rotu (Purple): Hunter, Kathy, Paschal, Robert, Sean, Tammy, Zoe

Note: Tribe swap occurred in Episode 4
"""

# All contestants in elimination order
SEASON_CONTESTANTS = [
    # Pre-merge eliminations
    "Peter",      # Episode 1 - Maraamu
    "Patricia",   # Episode 2 - Maraamu
    "Hunter",     # Episode 3 - Rotu
    "Sarah",      # Episode 4 - Maraamu (after swap)
    "Gabriel",    # Episode 5 - Maraamu
    "Gina",       # Episode 6 - Maraamu
    # Merge Episode 7 onwards
    "John",       # Episode 7 (first merge boot)
    "Zoe",        # Episode 8
    "Tammy",      # Episode 9
    "Robert",     # Episode 10
    "Sean",       # Episode 11
    "Paschal",    # Episode 12 (purple rock)
    "Kathy",      # Episode 13
    "Neleh",      # Final 2 (Runner-up)
    "Vecepia",    # Final 2 (Winner)
]

# PRE-MERGE voting history (Episodes 1-6 only)
SEASON_VOTING_HISTORY = [
    # Episode 1, Day 3 - Peter voted out (Maraamu tribe)
    {
        "episode": 1,
        "day": 3,
        "tribe": "Maraamu",
        "eliminated": "Peter",
        "votes": {
            "Gabriel": "Peter",
            "Gina": "Peter",
            "John": "Sarah",
            "Neleh": "Peter",
            "Patricia": "Peter",
            "Peter": "Patricia",
            "Sarah": "Peter",
            "Vecepia": "Peter",
        }
    },

    # Episode 2, Day 6 - Patricia voted out (Maraamu tribe)
    {
        "episode": 2,
        "day": 6,
        "tribe": "Maraamu",
        "eliminated": "Patricia",
        "votes": {
            "Gabriel": "Patricia",
            "Gina": "Patricia",
            "John": "Patricia",
            "Neleh": "Patricia",
            "Patricia": "John",
            "Sarah": "Patricia",
            "Vecepia": "Patricia",
        }
    },

    # Episode 3, Day 9 - Hunter voted out (Rotu tribe)
    {
        "episode": 3,
        "day": 9,
        "tribe": "Rotu",
        "eliminated": "Hunter",
        "votes": {
            "Hunter": "Paschal",
            "Kathy": "Hunter",
            "Paschal": "Hunter",
            "Robert": "Hunter",
            "Sean": "Hunter",
            "Tammy": "Hunter",
            "Zoe": "Hunter",
        }
    },

    # Episode 4, Day 12 - Sarah voted out (Maraamu tribe, after swap)
    # Swap: Neleh & Paschal to Maraamu; Gabriel, Sarah, Vecepia stayed
    {
        "episode": 4,
        "day": 12,
        "tribe": "Maraamu",
        "eliminated": "Sarah",
        "votes": {
            "Gabriel": "Gina",
            "Gina": "Sarah",
            "John": "Sarah",
            "Neleh": "Sarah",
            "Paschal": "Sarah",
            "Sarah": "Neleh",
            "Vecepia": "Sarah",
        }
    },

    # Episode 5, Day 15 - Gabriel voted out (Maraamu tribe)
    {
        "episode": 5,
        "day": 15,
        "tribe": "Maraamu",
        "eliminated": "Gabriel",
        "votes": {
            "Gabriel": "Vecepia",
            "Gina": "Gabriel",
            "John": "Gabriel",
            "Neleh": "Gabriel",
            "Paschal": "Gabriel",
            "Vecepia": "Gabriel",
        }
    },

    # Episode 6, Day 18 - Gina voted out (Maraamu tribe)
    {
        "episode": 6,
        "day": 18,
        "tribe": "Maraamu",
        "eliminated": "Gina",
        "votes": {
            "Gina": "Vecepia",
            "John": "Gina",
            "Neleh": "Gina",
            "Paschal": "Gina",
            "Vecepia": "Gina",
        }
    },
]

if __name__ == "__main__":
    print("Survivor Season 4: Marquesas")
    print("=" * 50)
    print(f"Contestants: {len(SEASON_CONTESTANTS)}")
    print(f"Pre-merge tribal councils: {len(SEASON_VOTING_HISTORY)}")
    print(f"Winner: Vecepia Towery")
    print(f"\nPre-merge boots: {SEASON_CONTESTANTS[:6]}")
