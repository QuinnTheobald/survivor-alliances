"""
Survivor Season 23: South Pacific (2011)

Pre-merge voting data for alliance analysis.
Merge Episode: 8 (only Episodes 1-7 are included here)

Data Source: https://survivor.fandom.com/wiki/Survivor:South_Pacific
"""

# TODO: Fill contestant list with first names (in elimination order)
# Use first names only, or unique nicknames if there are duplicates
# These names MUST match exactly with names used in voting data below
SEASON_CONTESTANTS = [
    # "FirstEliminated",
    # "SecondEliminated",
    # ... add all contestants in order
]

# Pre-merge tribal councils only (Episodes 1-7)
# Stop BEFORE Episode 8 (merge episode)
SEASON_VOTING_HISTORY = [
    {
        "episode": 1,
        "day": "TBD",  # TODO: Fill from wiki
        "tribe": "TBD",  # TODO: Fill tribe name
        "eliminated": "TBD",  # TODO: Fill eliminated player name
        "votes": {
            # TODO: Fill votes from wiki
            # Format: "Voter": "Target",
        }
    },
    {
        "episode": 2,
        "day": "TBD",  # TODO: Fill from wiki
        "tribe": "TBD",  # TODO: Fill tribe name
        "eliminated": "TBD",  # TODO: Fill eliminated player name
        "votes": {
            # TODO: Fill votes from wiki
            # Format: "Voter": "Target",
        }
    },
    {
        "episode": 3,
        "day": "TBD",  # TODO: Fill from wiki
        "tribe": "TBD",  # TODO: Fill tribe name
        "eliminated": "TBD",  # TODO: Fill eliminated player name
        "votes": {
            # TODO: Fill votes from wiki
            # Format: "Voter": "Target",
        }
    },
    {
        "episode": 4,
        "day": "TBD",  # TODO: Fill from wiki
        "tribe": "TBD",  # TODO: Fill tribe name
        "eliminated": "TBD",  # TODO: Fill eliminated player name
        "votes": {
            # TODO: Fill votes from wiki
            # Format: "Voter": "Target",
        }
    },
    {
        "episode": 5,
        "day": "TBD",  # TODO: Fill from wiki
        "tribe": "TBD",  # TODO: Fill tribe name
        "eliminated": "TBD",  # TODO: Fill eliminated player name
        "votes": {
            # TODO: Fill votes from wiki
            # Format: "Voter": "Target",
        }
    },
    {
        "episode": 6,
        "day": "TBD",  # TODO: Fill from wiki
        "tribe": "TBD",  # TODO: Fill tribe name
        "eliminated": "TBD",  # TODO: Fill eliminated player name
        "votes": {
            # TODO: Fill votes from wiki
            # Format: "Voter": "Target",
        }
    },
    {
        "episode": 7,
        "day": "TBD",  # TODO: Fill from wiki
        "tribe": "TBD",  # TODO: Fill tribe name
        "eliminated": "TBD",  # TODO: Fill eliminated player name
        "votes": {
            # TODO: Fill votes from wiki
            # Format: "Voter": "Target",
        }
    }
]

# Special cases to handle:
# - For quits/medevacs: Add "quit": True or "medevac": True, use "votes": {}
# - For ties/revotes: Include only the final vote that eliminated someone
# - Tribe swaps: Continue including votes with new tribe compositions
