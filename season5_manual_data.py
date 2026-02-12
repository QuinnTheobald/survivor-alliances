"""
Manual Data Entry for Survivor Season 5 (Thailand)
Based on: https://survivor.fandom.com/wiki/Survivor:_Thailand

Season 5: Thailand (2002)
16 contestants, merge at Episode 7
Final 2: Brian Heidik (winner), Clay Jordan

Tribes:
- Chuay Gahn (Red): Brian, Clay, Ghandia, Helen, Jan, John, Tanya, Ted
- Sook Jai (Yellow): Erin, Jake, Jed, Ken, Penny, Robb, Shii Ann, Stephanie

Note: Tribe fake merge/swap occurred in Episode 4
"""

# All contestants in elimination order
SEASON_CONTESTANTS = [
    # Pre-merge eliminations
    "John",       # Episode 1 - Chuay Gahn
    "Tanya",      # Episode 2 - Chuay Gahn
    "Jed",        # Episode 3 - Sook Jai
    "Stephanie",  # Episode 4 - Sook Jai (fake merge)
    "Robb",       # Episode 5 - Sook Jai
    "Shii Ann",   # Episode 6 - Sook Jai (joined Chuay Gahn)
    # Merge Episode 7 onwards
    "Erin",       # Episode 7 (first merge boot)
    "Ken",        # Episode 8
    "Penny",      # Episode 9
    "Jake",       # Episode 10
    "Ted",        # Episode 11
    "Ghandia",    # Episode 12
    "Jan",        # Episode 13
    "Helen",      # Episode 14
    "Clay",       # Final 2 (Runner-up)
    "Brian",      # Final 2 (Winner)
]

# PRE-MERGE voting history (Episodes 1-6 only)
SEASON_VOTING_HISTORY = [
    # Episode 1, Day 3 - John voted out (Chuay Gahn tribe)
    {
        "episode": 1,
        "day": 3,
        "tribe": "Chuay Gahn",
        "eliminated": "John",
        "votes": {
            "Brian": "John",
            "Clay": "John",
            "Ghandia": "John",
            "Helen": "John",
            "Jan": "John",
            "John": "Clay",
            "Tanya": "John",
            "Ted": "John",
        }
    },

    # Episode 2, Day 6 - Tanya voted out (Chuay Gahn tribe)
    {
        "episode": 2,
        "day": 6,
        "tribe": "Chuay Gahn",
        "eliminated": "Tanya",
        "votes": {
            "Brian": "Tanya",
            "Clay": "Tanya",
            "Ghandia": "Tanya",
            "Helen": "Tanya",
            "Jan": "Tanya",
            "Tanya": "Jan",
            "Ted": "Tanya",
        }
    },

    # Episode 3, Day 9 - Jed voted out (Sook Jai tribe)
    {
        "episode": 3,
        "day": 9,
        "tribe": "Sook Jai",
        "eliminated": "Jed",
        "votes": {
            "Erin": "Jed",
            "Jake": "Jed",
            "Jed": "Stephanie",
            "Ken": "Jed",
            "Penny": "Jed",
            "Robb": "Jed",
            "Shii Ann": "Jed",
            "Stephanie": "Jed",
        }
    },

    # Episode 4, Day 12 - Stephanie voted out (Sook Jai tribe, fake merge)
    {
        "episode": 4,
        "day": 12,
        "tribe": "Sook Jai",
        "eliminated": "Stephanie",
        "votes": {
            "Erin": "Stephanie",
            "Jake": "Stephanie",
            "Ken": "Stephanie",
            "Penny": "Stephanie",
            "Robb": "Shii Ann",
            "Shii Ann": "Robb",
            "Stephanie": "Shii Ann",
        }
    },

    # Episode 5, Day 15 - Robb voted out (Sook Jai tribe)
    {
        "episode": 5,
        "day": 15,
        "tribe": "Sook Jai",
        "eliminated": "Robb",
        "votes": {
            "Erin": "Robb",
            "Jake": "Robb",
            "Ken": "Robb",
            "Penny": "Robb",
            "Robb": "Shii Ann",
            "Shii Ann": "Robb",
        }
    },

    # Episode 6, Day 18 - Shii Ann voted out (Chuay Gahn tribe)
    # Shii Ann joined Chuay Gahn from Sook Jai
    {
        "episode": 6,
        "day": 18,
        "tribe": "Chuay Gahn",
        "eliminated": "Shii Ann",
        "votes": {
            "Brian": "Shii Ann",
            "Clay": "Shii Ann",
            "Ghandia": "Shii Ann",
            "Helen": "Shii Ann",
            "Jan": "Shii Ann",
            "Shii Ann": "Helen",
            "Ted": "Shii Ann",
        }
    },
]

if __name__ == "__main__":
    print("Survivor Season 5: Thailand")
    print("=" * 50)
    print(f"Contestants: {len(SEASON_CONTESTANTS)}")
    print(f"Pre-merge tribal councils: {len(SEASON_VOTING_HISTORY)}")
    print(f"Winner: Brian Heidik")
    print(f"\nPre-merge boots: {SEASON_CONTESTANTS[:6]}")
