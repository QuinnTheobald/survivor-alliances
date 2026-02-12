"""
Manual Data Entry for Survivor Season 10 (Palau)
Based on: https://survivor.fandom.com/wiki/Survivor:_Palau

Season 10: Palau (2005)
20 contestants, merge at Episode 8
Final 2: Tom Westman (winner), Katie Gallagher

Tribes:
- Koror (Blue): Caryn, Coby, Gregg, Ian, Janu, Jenn, Katie, Tom, Willard
- Ulong (Yellow): Angie, Ashlee, Bobby Jon, Ibrehem, James, Jeff, Jolanda, Kim, Stephenie

Note: Unusual season - Koror won every immunity, Ulong reduced to 1 member
First tribal council eliminated 2 people (Jolanda & Wanda not picked)
"""

# All contestants in elimination order
SEASON_CONTESTANTS = [
    # Not picked in initial schoolyard pick
    "Wanda",      # Not picked, eliminated Day 1
    "Jonathan",   # Not picked, eliminated Day 1
    # Pre-merge eliminations (Ulong decimated)
    "Jolanda",    # Episode 1 - Ulong
    "Ashlee",     # Episode 2 - Ulong
    "Jeff",       # Episode 3 - Ulong
    "Kim",        # Episode 4 - Ulong
    "Willard",    # Episode 5 - Koror (only Koror TC pre-merge)
    "Angie",      # Episode 6 - Ulong
    "James",      # Episode 7 - Ulong
    "Ibrehem",    # Episode 8 - Ulong (last Ulong member)
    # Merge Episode 9 onwards (Stephenie joined Koror)
    "Bobby Jon",  # Episode 9 (first merge boot)
    "Stephenie",  # Episode 10
    "Coby",       # Episode 11
    "Janu",       # Episode 12 (quit)
    "Gregg",      # Episode 13
    "Caryn",      # Episode 14
    "Jenn",       # Episode 15
    "Ian",        # Episode 16 (quit final immunity)
    "Katie",      # Final 2 (Runner-up)
    "Tom",        # Final 2 (Winner)
]

# PRE-MERGE voting history (Episodes 1-7, merge at Episode 8)
# Note: Koror only went to tribal council ONCE pre-merge (Episode 5)
SEASON_VOTING_HISTORY = [
    # Episode 1, Day 3 - Jolanda voted out (Ulong tribe)
    {
        "episode": 1,
        "day": 3,
        "tribe": "Ulong",
        "eliminated": "Jolanda",
        "votes": {
            "Angie": "Jolanda",
            "Ashlee": "Jolanda",
            "Bobby Jon": "Jolanda",
            "Ibrehem": "Jolanda",
            "James": "Jolanda",
            "Jeff": "Jolanda",
            "Jolanda": "Ashlee",
            "Kim": "Jolanda",
            "Stephenie": "Jolanda",
        }
    },

    # Episode 2, Day 6 - Ashlee voted out (Ulong tribe)
    {
        "episode": 2,
        "day": 6,
        "tribe": "Ulong",
        "eliminated": "Ashlee",
        "votes": {
            "Angie": "Ashlee",
            "Ashlee": "James",
            "Bobby Jon": "Ashlee",
            "Ibrehem": "Ashlee",
            "James": "Ashlee",
            "Jeff": "Ashlee",
            "Kim": "Ashlee",
            "Stephenie": "Ashlee",
        }
    },

    # Episode 3, Day 9 - Jeff voted out (Ulong tribe)
    {
        "episode": 3,
        "day": 9,
        "tribe": "Ulong",
        "eliminated": "Jeff",
        "votes": {
            "Angie": "Jeff",
            "Bobby Jon": "Jeff",
            "Ibrehem": "Jeff",
            "James": "Jeff",
            "Jeff": "Kim",
            "Kim": "Jeff",
            "Stephenie": "Jeff",
        }
    },

    # Episode 4, Day 12 - Kim voted out (Ulong tribe)
    {
        "episode": 4,
        "day": 12,
        "tribe": "Ulong",
        "eliminated": "Kim",
        "votes": {
            "Angie": "Kim",
            "Bobby Jon": "Kim",
            "Ibrehem": "Kim",
            "James": "Kim",
            "Kim": "Angie",
            "Stephenie": "Kim",
        }
    },

    # Episode 5, Day 15 - Willard voted out (Koror tribe)
    # ONLY time Koror went to tribal council pre-merge!
    {
        "episode": 5,
        "day": 15,
        "tribe": "Koror",
        "eliminated": "Willard",
        "votes": {
            "Caryn": "Willard",
            "Coby": "Willard",
            "Gregg": "Willard",
            "Ian": "Willard",
            "Janu": "Willard",
            "Jenn": "Willard",
            "Katie": "Willard",
            "Tom": "Willard",
            "Willard": "Coby",
        }
    },

    # Episode 6, Day 18 - Angie voted out (Ulong tribe)
    {
        "episode": 6,
        "day": 18,
        "tribe": "Ulong",
        "eliminated": "Angie",
        "votes": {
            "Angie": "James",
            "Bobby Jon": "Angie",
            "Ibrehem": "Angie",
            "James": "Angie",
            "Stephenie": "Angie",
        }
    },

    # Episode 7, Day 21 - James voted out (Ulong tribe)
    {
        "episode": 7,
        "day": 21,
        "tribe": "Ulong",
        "eliminated": "James",
        "votes": {
            "Bobby Jon": "James",
            "Ibrehem": "James",
            "James": "Ibrehem",
            "Stephenie": "James",
        }
    },

    # Episode 8 would be Ibrehem (last Ulong), but that's at merge
]

if __name__ == "__main__":
    print("Survivor Season 10: Palau")
    print("=" * 50)
    print(f"Contestants: {len(SEASON_CONTESTANTS)}")
    print(f"Pre-merge tribal councils: {len(SEASON_VOTING_HISTORY)}")
    print(f"Winner: Tom Westman")
    print(f"\nNote: Koror dominated, went to tribal only ONCE pre-merge!")
    print(f"Pre-merge boots: {SEASON_CONTESTANTS[2:9]}")  # Skip Wanda & Jonathan
