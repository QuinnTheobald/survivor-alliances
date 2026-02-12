"""
Manual Data Entry for Survivor Season 9 (Vanuatu)
Based on: https://survivor.fandom.com/wiki/Survivor:_Vanuatu

Season 9: Vanuatu (2004)
18 contestants, merge at Episode 7
Final 2: Chris Daugherty (winner), Twila Tanner

Tribes:
- Lopevi (Men): Brady, Brook, Chad, Chris, John K, John P, Lea, Rory, Travis
- Yasur (Women): Ami, Dolly, Eliza, Julie, LeAnn, Lisa, Mia, Scout, Twila

Note: Tribe swap in Episode 5; men vs women theme
"""

# All contestants in elimination order
SEASON_CONTESTANTS = [
    # Pre-merge eliminations
    "Brook",      # Episode 1 - Lopevi
    "Dolly",      # Episode 2 - Yasur
    "John P",     # Episode 3 - Lopevi
    "Mia",        # Episode 4 - Yasur
    "Travis",     # Episode 5 - Lopevi (after swap)
    "John K",     # Episode 6 - Yasur (after swap)
    # Merge Episode 7 onwards
    "Brady",      # Episode 7 (first merge boot)
    "Lea",        # Episode 8
    "Rory",       # Episode 9
    "LeAnn",      # Episode 10
    "Ami",        # Episode 11
    "Julie",      # Episode 12
    "Eliza",      # Episode 13
    "Scout",      # Episode 14
    "Lisa",       # Episode 15
    "Chad",       # Episode 16
    "Twila",      # Final 2 (Runner-up)
    "Chris",      # Final 2 (Winner)
]

# PRE-MERGE voting history (Episodes 1-6 only)
SEASON_VOTING_HISTORY = [
    # Episode 1, Day 3 - Brook voted out (Lopevi tribe)
    {
        "episode": 1,
        "day": 3,
        "tribe": "Lopevi",
        "eliminated": "Brook",
        "votes": {
            "Brady": "Brook",
            "Brook": "John P",
            "Chad": "Brook",
            "Chris": "Brook",
            "John K": "Brook",
            "John P": "Brook",
            "Lea": "Brook",
            "Rory": "Brook",
            "Travis": "Brook",
        }
    },

    # Episode 2, Day 6 - Dolly voted out (Yasur tribe)
    {
        "episode": 2,
        "day": 6,
        "tribe": "Yasur",
        "eliminated": "Dolly",
        "votes": {
            "Ami": "Dolly",
            "Dolly": "Eliza",
            "Eliza": "Dolly",
            "Julie": "Dolly",
            "LeAnn": "Dolly",
            "Lisa": "Dolly",
            "Mia": "Eliza",
            "Scout": "Dolly",
            "Twila": "Dolly",
        }
    },

    # Episode 3, Day 9 - John P voted out (Lopevi tribe)
    {
        "episode": 3,
        "day": 9,
        "tribe": "Lopevi",
        "eliminated": "John P",
        "votes": {
            "Brady": "John P",
            "Chad": "John P",
            "Chris": "John P",
            "John K": "John P",
            "John P": "Rory",
            "Lea": "John P",
            "Rory": "John P",
            "Travis": "John P",
        }
    },

    # Episode 4, Day 12 - Mia voted out (Yasur tribe)
    {
        "episode": 4,
        "day": 12,
        "tribe": "Yasur",
        "eliminated": "Mia",
        "votes": {
            "Ami": "Mia",
            "Eliza": "Mia",
            "Julie": "Mia",
            "LeAnn": "Mia",
            "Lisa": "Mia",
            "Mia": "Eliza",
            "Scout": "Mia",
            "Twila": "Mia",
        }
    },

    # Episode 5, Day 15 - Travis voted out (Lopevi tribe, after swap)
    # Swap: Rory & Travis to Yasur; Julie & Twila to Lopevi
    {
        "episode": 5,
        "day": 15,
        "tribe": "Lopevi",
        "eliminated": "Travis",
        "votes": {
            "Brady": "Travis",
            "Chad": "Travis",
            "Chris": "Travis",
            "John K": "Travis",
            "Julie": "Travis",
            "Lea": "Travis",
            "Travis": "Julie",
            "Twila": "Travis",
        }
    },

    # Episode 6, Day 18 - John K voted out (Yasur tribe, after swap)
    {
        "episode": 6,
        "day": 18,
        "tribe": "Yasur",
        "eliminated": "John K",
        "votes": {
            "Ami": "John K",
            "Eliza": "John K",
            "John K": "Ami",
            "LeAnn": "John K",
            "Lisa": "John K",
            "Rory": "John K",
            "Scout": "John K",
        }
    },
]

if __name__ == "__main__":
    print("Survivor Season 9: Vanuatu")
    print("=" * 50)
    print(f"Contestants: {len(SEASON_CONTESTANTS)}")
    print(f"Pre-merge tribal councils: {len(SEASON_VOTING_HISTORY)}")
    print(f"Winner: Chris Daugherty")
    print(f"\nPre-merge boots: {SEASON_CONTESTANTS[:6]}")
