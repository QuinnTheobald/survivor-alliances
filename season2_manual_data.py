"""
Manual Data Entry for Survivor Season 2 (The Australian Outback)
Based on: https://survivor.fandom.com/wiki/Survivor:_The_Australian_Outback

Season 2: The Australian Outback (2001)
16 contestants, merge at Episode 7
Final 2: Tina Wesson (winner), Colby Donaldson

Tribes:
- Kucha (Yellow): Alicia, Elisabeth, Jeff, Kimmi, Michael, Nick, Rodger, Debb
- Ogakor (Blue): Amber, Colby, Jerri, Keith, Kel, Maralyn, Mitchell, Tina
"""

# All contestants in elimination order
SEASON_CONTESTANTS = [
    # Pre-merge eliminations
    "Debb",       # Episode 1 - Kucha
    "Kel",        # Episode 2 - Ogakor
    "Maralyn",    # Episode 3 - Ogakor
    "Mitchell",   # Episode 4 - Ogakor
    "Kimmi",      # Episode 5 - Kucha
    "Jeff",       # Episode 6 - Kucha
    # Merge Episode 7 onwards
    "Alicia",     # Episode 7 (first merge boot)
    "Jerri",      # Episode 8
    "Nick",       # Episode 9
    "Amber",      # Episode 10
    "Rodger",     # Episode 11
    "Elisabeth",  # Episode 12
    "Keith",      # Episode 13
    "Tina",       # Final 2 (Winner)
    "Colby",      # Final 2 (Runner-up)
]

# PRE-MERGE voting history (Episodes 1-6 only, before Episode 7 merge)
SEASON_VOTING_HISTORY = [
    # Episode 1, Day 3 - Debb voted out (Kucha tribe)
    {
        "episode": 1,
        "day": 3,
        "tribe": "Kucha",
        "eliminated": "Debb",
        "votes": {
            "Alicia": "Debb",
            "Debb": "Jeff",
            "Elisabeth": "Debb",
            "Jeff": "Debb",
            "Kimmi": "Debb",
            "Michael": "Debb",
            "Nick": "Debb",
            "Rodger": "Debb",
        }
    },

    # Episode 2, Day 6 - Kel voted out (Ogakor tribe)
    {
        "episode": 2,
        "day": 6,
        "tribe": "Ogakor",
        "eliminated": "Kel",
        "votes": {
            "Amber": "Kel",
            "Colby": "Kel",
            "Jerri": "Kel",
            "Keith": "Kel",
            "Kel": "Tina",
            "Maralyn": "Kel",
            "Mitchell": "Jerri",
            "Tina": "Kel",
        }
    },

    # Episode 3, Day 9 - Maralyn voted out (Ogakor tribe)
    {
        "episode": 3,
        "day": 9,
        "tribe": "Ogakor",
        "eliminated": "Maralyn",
        "votes": {
            "Amber": "Maralyn",
            "Colby": "Maralyn",
            "Jerri": "Maralyn",
            "Keith": "Maralyn",
            "Maralyn": "Jerri",
            "Mitchell": "Maralyn",
            "Tina": "Maralyn",
        }
    },

    # Episode 4, Day 12 - Mitchell voted out (Ogakor tribe)
    {
        "episode": 4,
        "day": 12,
        "tribe": "Ogakor",
        "eliminated": "Mitchell",
        "votes": {
            "Amber": "Mitchell",
            "Colby": "Mitchell",
            "Jerri": "Mitchell",
            "Keith": "Mitchell",
            "Mitchell": "Keith",
            "Tina": "Mitchell",
        }
    },

    # Episode 5, Day 15 - Kimmi voted out (Kucha tribe)
    {
        "episode": 5,
        "day": 15,
        "tribe": "Kucha",
        "eliminated": "Kimmi",
        "votes": {
            "Alicia": "Kimmi",
            "Elisabeth": "Jeff",
            "Jeff": "Kimmi",
            "Kimmi": "Alicia",
            "Michael": "Kimmi",
            "Nick": "Kimmi",
            "Rodger": "Kimmi",
        }
    },

    # Episode 6, Day 18 - Jeff voted out (Kucha tribe)
    {
        "episode": 6,
        "day": 18,
        "tribe": "Kucha",
        "eliminated": "Jeff",
        "votes": {
            "Alicia": "Jeff",
            "Elisabeth": "Jeff",
            "Jeff": "Alicia",
            "Michael": "Jeff",
            "Nick": "Jeff",
            "Rodger": "Jeff",
        }
    },
]

if __name__ == "__main__":
    print("Survivor Season 2: The Australian Outback")
    print("=" * 50)
    print(f"Contestants: {len(SEASON_CONTESTANTS)}")
    print(f"Pre-merge tribal councils: {len(SEASON_VOTING_HISTORY)}")
    print(f"Winner: Tina Wesson")
    print(f"\nPre-merge boots: {SEASON_CONTESTANTS[:6]}")
