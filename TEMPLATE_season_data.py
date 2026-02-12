"""
TEMPLATE for Manual Data Entry
Copy this file to create seasonX_manual_data.py

Instructions:
1. Copy this file: cp TEMPLATE_season_data.py seasonX_manual_data.py
2. Update the season info in the docstring
3. Fill in SEASON_CONTESTANTS list with all contestant names
4. Add voting data for each PRE-MERGE tribal council only
5. Run: python batch_analyze.py && python batch_visualize.py

IMPORTANT: Only include tribal councils BEFORE the merge episode!
"""

# All contestants (in elimination order is helpful but not required)
SEASON_CONTESTANTS = [
    "FirstOut",     # Eliminated Episode 1
    "SecondOut",    # Eliminated Episode 2
    # ... add all contestants
    "RunnerUp",     # Final 2/3
    "Winner",       # Winner
]

# PRE-MERGE voting history ONLY
# Check season_metadata.py for when the merge happens
SEASON_VOTING_HISTORY = [
    # Episode 1 - FirstOut voted out
    {
        "episode": 1,
        "day": 3,
        "eliminated": "FirstOut",
        "votes": {
            "Player1": "FirstOut",
            "Player2": "FirstOut",
            "Player3": "OtherPlayer",
            # ... add all votes from this tribal council
        }
    },

    # Episode 2 - SecondOut voted out
    {
        "episode": 2,
        "day": 6,
        "eliminated": "SecondOut",
        "votes": {
            "Player1": "SecondOut",
            # ... add all votes
        }
    },

    # Continue for all PRE-MERGE tribal councils
    # Stop at merge episode - 1
]

# Tips:
# - Use first names only (or unique nicknames if there are duplicates)
# - Match the names exactly across SEASON_CONTESTANTS and votes
# - Check the wiki for accurate vote counts
# - Include revotes if they happened (use same episode number)
# - Don't forget to update season_metadata.py with finalists/winner!

if __name__ == "__main__":
    print("Survivor Season X: [Name]")
    print("=" * 50)
    print(f"Contestants: {len(SEASON_CONTESTANTS)}")
    print(f"Pre-merge tribal councils: {len(SEASON_VOTING_HISTORY)}")
