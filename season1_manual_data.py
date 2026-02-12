"""
Manual Data Entry Template for Survivor Season 1 (Borneo)
Use this if web scraping needs adjustment or as verification data

Based on: https://survivor.fandom.com/wiki/Survivor:_Borneo

Season 1: Borneo (2000)
16 contestants, 13 tribal councils
Final 2: Richard Hatch (winner), Kelly Wiglesworth
"""

# All contestants in order of elimination
SEASON_1_CONTESTANTS = [
    "Sonja",      # Eliminated Episode 1
    "B.B.",       # Eliminated Episode 2
    "Stacey",     # Eliminated Episode 3
    "Ramona",     # Eliminated Episode 4
    "Dirk",       # Eliminated Episode 5
    "Joel",       # Eliminated Episode 6
    "Gretchen",   # Eliminated Episode 7
    "Greg",       # Eliminated Episode 8
    "Jenna",      # Eliminated Episode 9
    "Gervase",    # Eliminated Episode 10
    "Colleen",    # Eliminated Episode 11
    "Sean",       # Eliminated Episode 12
    "Sue",        # Eliminated Episode 13
    "Rudy",       # Eliminated Episode 14 (Final 3)
    "Kelly",      # Final 2 (Runner-up)
    "Richard",    # Final 2 (Winner)
]

# Voting history - each entry is a tribal council
# Format: {"voter": "voted_for"}
SEASON_1_VOTING_HISTORY = [
    # Episode 1 - Sonja voted out
    {
        "episode": 1,
        "day": 3,
        "eliminated": "Sonja",
        "votes": {
            "B.B.": "Sonja",
            "Colleen": "Sonja",
            "Dirk": "Rudy",
            "Gervase": "Sonja",
            "Greg": "Sonja",
            "Jenna": "Sonja",
            "Kelly": "Sonja",
            "Richard": "Sonja",
            "Rudy": "Sonja",
            "Sean": "Sonja",
            "Stacey": "Sonja",
            "Sue": "Sonja",
        }
    },
    
    # Episode 2 - B.B. voted out
    {
        "episode": 2,
        "day": 6,
        "eliminated": "B.B.",
        "votes": {
            "B.B.": "Richard",
            "Colleen": "B.B.",
            "Dirk": "B.B.",
            "Gervase": "B.B.",
            "Greg": "B.B.",
            "Jenna": "B.B.",
            "Kelly": "B.B.",
            "Richard": "B.B.",
            "Rudy": "B.B.",
            "Sean": "B.B.",
            "Stacey": "B.B.",
            "Sue": "B.B.",
        }
    },
    
    # Episode 3 - Stacey voted out
    {
        "episode": 3,
        "day": 9,
        "eliminated": "Stacey",
        "votes": {
            "Colleen": "Stacey",
            "Dirk": "Stacey",
            "Gervase": "Stacey",
            "Greg": "Stacey",
            "Jenna": "Stacey",
            "Kelly": "Stacey",
            "Richard": "Stacey",
            "Rudy": "Stacey",
            "Sean": "Stacey",
            "Stacey": "Rudy",
            "Sue": "Stacey",
        }
    },
    
    # Episode 4 - Ramona voted out
    {
        "episode": 4,
        "day": 12,
        "eliminated": "Ramona",
        "votes": {
            "Colleen": "Ramona",
            "Dirk": "Ramona",
            "Gervase": "Ramona",
            "Greg": "Ramona",
            "Jenna": "Dirk",
            "Kelly": "Ramona",
            "Ramona": "Dirk",
            "Richard": "Ramona",
            "Rudy": "Ramona",
            "Sean": "Ramona",
            "Sue": "Ramona",
        }
    },
    
    # Episode 5 - Dirk voted out
    {
        "episode": 5,
        "day": 15,
        "eliminated": "Dirk",
        "votes": {
            "Colleen": "Dirk",
            "Dirk": "Kelly",
            "Gervase": "Dirk",
            "Greg": "Dirk",
            "Jenna": "Kelly",
            "Kelly": "Jenna",
            "Richard": "Dirk",
            "Rudy": "Dirk",
            "Sean": "Dirk",
            "Sue": "Dirk",
        }
    },
    
    # Episode 6 - Joel voted out
    {
        "episode": 6,
        "day": 18,
        "eliminated": "Joel",
        "votes": {
            "Colleen": "Joel",
            "Gervase": "Joel",
            "Greg": "Joel",
            "Jenna": "Gretchen",
            "Joel": "Gretchen",
            "Kelly": "Joel",
            "Richard": "Joel",
            "Rudy": "Joel",
            "Sean": "Joel",
            "Sue": "Joel",
        }
    },
    
    # Episode 7 - Gretchen voted out (MERGE)
    {
        "episode": 7,
        "day": 21,
        "eliminated": "Gretchen",
        "merge": True,
        "votes": {
            "Colleen": "Greg",
            "Gervase": "Colleen",
            "Greg": "Sean",
            "Gretchen": "Richard",
            "Jenna": "Gretchen",
            "Kelly": "Gretchen",
            "Richard": "Gretchen",
            "Rudy": "Gretchen",
            "Sean": "Gretchen",
            "Sue": "Gretchen",
        }
    },
    
    # Episode 8 - Greg voted out
    {
        "episode": 8,
        "day": 24,
        "eliminated": "Greg",
        "votes": {
            "Colleen": "Jenna",
            "Gervase": "Greg",
            "Greg": "Rudy",
            "Jenna": "Greg",
            "Kelly": "Greg",
            "Richard": "Greg",
            "Rudy": "Greg",
            "Sean": "Greg",
            "Sue": "Greg",
        }
    },
    
    # Episode 9 - Jenna voted out
    {
        "episode": 9,
        "day": 27,
        "eliminated": "Jenna",
        "votes": {
            "Colleen": "Sean",
            "Gervase": "Jenna",
            "Jenna": "Gervase",
            "Kelly": "Jenna",
            "Richard": "Jenna",
            "Rudy": "Jenna",
            "Sean": "Jenna",
            "Sue": "Jenna",
        }
    },
    
    # Episode 10 - Gervase voted out
    {
        "episode": 10,
        "day": 30,
        "eliminated": "Gervase",
        "votes": {
            "Colleen": "Sean",
            "Gervase": "Sue",
            "Kelly": "Gervase",
            "Richard": "Gervase",
            "Rudy": "Gervase",
            "Sean": "Gervase",
            "Sue": "Gervase",
        }
    },
    
    # Episode 11 - Colleen voted out
    {
        "episode": 11,
        "day": 33,
        "eliminated": "Colleen",
        "votes": {
            "Colleen": "Richard",
            "Kelly": "Colleen",
            "Richard": "Colleen",
            "Rudy": "Colleen",
            "Sean": "Sue",
            "Sue": "Colleen",
        }
    },
    
    # Episode 12 - Sean voted out
    {
        "episode": 12,
        "day": 36,
        "eliminated": "Sean",
        "votes": {
            "Kelly": "Sean",
            "Richard": "Sean",
            "Rudy": "Sean",
            "Sean": "Sue",
            "Sue": "Sean",
        }
    },
    
    # Episode 13 - Sue voted out
    {
        "episode": 13,
        "day": 37,
        "eliminated": "Sue",
        "votes": {
            "Kelly": "Sue",
            "Richard": "Sue",
            "Rudy": "Sue",
            "Sue": "Richard",
        }
    },
    
    # Episode 14 - Rudy voted out (Final Immunity Challenge)
    {
        "episode": 14,
        "day": 38,
        "eliminated": "Rudy",
        "final_immunity": "Kelly",
        "votes": {
            "Kelly": "Rudy",  # Kelly won immunity and voted out Rudy
        }
    },
]

# Final Tribal Council
FINAL_TRIBAL_COUNCIL = {
    "finalists": ["Richard", "Kelly"],
    "jury": ["Gretchen", "Greg", "Jenna", "Gervase", "Colleen", "Sean", "Sue"],
    "jury_votes": {
        "Gretchen": "Richard",
        "Greg": "Richard",
        "Jenna": "Richard",
        "Gervase": "Richard",
        "Colleen": "Kelly",
        "Sean": "Kelly",
        "Sue": "Richard",
    },
    "winner": "Richard",
    "vote_count": {"Richard": 4, "Kelly": 3}
}

# Known alliances
KNOWN_ALLIANCES = {
    "Tagi Alliance": ["Richard", "Rudy", "Sue", "Kelly"],
    "Pagong Alliance": ["Gretchen", "Greg", "Colleen", "Gervase", "Jenna"],
}

if __name__ == "__main__":
    print("Survivor Season 1: Borneo")
    print("=" * 50)
    print(f"Contestants: {len(SEASON_1_CONTESTANTS)}")
    print(f"Tribal Councils: {len(SEASON_1_VOTING_HISTORY)}")
    print(f"Winner: {FINAL_TRIBAL_COUNCIL['winner']}")
    print(f"\nFinalists: {', '.join(FINAL_TRIBAL_COUNCIL['finalists'])}")
    print(f"\nKnown Alliances:")
    for alliance_name, members in KNOWN_ALLIANCES.items():
        print(f"  {alliance_name}: {', '.join(members)}")
