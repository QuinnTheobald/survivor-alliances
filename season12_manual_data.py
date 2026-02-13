"""
Survivor Season 12: Panama - Exile Island (2006)
18 contestants (4 initial tribes), merge at Episode 8
Final 2: Aras Baskauskas (winner), Danielle DiLorenzo
"""

SEASON_CONTESTANTS = [
    "Tina", "Melinda", "Misty", "Ruth Marie", "Bobby", "Dan", "Sally", "Bruce",
    "Austin", "Nick", "Courtney", "Shane", "Cirie", "Terry", "Danielle", "Aras"
]

SEASON_VOTING_HISTORY = [
    {"episode": 1, "day": 3, "tribe": "Bayoneta", "eliminated": "Tina", "votes": {"Tina": "Bobby", "Bobby": "Tina", "Dan": "Tina", "Austin": "Tina"}},
    {"episode": 2, "day": 6, "tribe": "Viveros", "eliminated": "Melinda", "votes": {"Melinda": "Cirie", "Cirie": "Melinda", "Courtney": "Melinda", "Shane": "Melinda"}},
    {"episode": 3, "day": 9, "tribe": "Bayoneta", "eliminated": "Misty", "votes": {"Misty": "Dan", "Dan": "Misty", "Austin": "Misty", "Sally": "Misty", "Nick": "Misty", "Terry": "Misty"}},
    {"episode": 4, "day": 11, "tribe": "Viveros", "eliminated": "Ruth Marie", "votes": {"Ruth Marie": "Shane", "Shane": "Ruth Marie", "Courtney": "Ruth Marie", "Cirie": "Ruth Marie", "Danielle": "Ruth Marie", "Aras": "Ruth Marie"}},
    {"episode": 5, "day": 13, "tribe": "La Mina", "eliminated": "Bobby", "votes": {"Bobby": "Dan", "Dan": "Bobby", "Austin": "Bobby", "Sally": "Bobby", "Nick": "Bobby", "Terry": "Bobby"}},
    {"episode": 6, "day": 16, "tribe": "Casaya", "eliminated": "Dan", "votes": {"Dan": "Bobby", "Shane": "Dan", "Courtney": "Dan", "Cirie": "Dan", "Danielle": "Dan", "Aras": "Dan", "Bruce": "Dan"}},
    {"episode": 7, "day": 18, "tribe": "La Mina", "eliminated": "Sally", "votes": {"Sally": "Terry", "Austin": "Sally", "Nick": "Sally", "Terry": "Austin"}},
]

if __name__ == "__main__":
    print("Season 12: Panama")
    print(f"Pre-merge TCs: {len(SEASON_VOTING_HISTORY)}")
