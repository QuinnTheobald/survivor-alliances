"""
Metadata for Survivor Seasons 1-10
Contains season names, URLs, merge episodes, and finalists
"""

SEASONS_METADATA = {
    1: {
        "name": "Borneo",
        "year": 2000,
        "location": "Pulau Tiga, Malaysia",
        "url": "https://survivor.fandom.com/wiki/Survivor:_Borneo",
        "merge_episode": 7,
        "episodes": 13,
        "contestants": 16,
        "finalists": ["Richard", "Kelly"],  # First names to match voting data
        "winner": "Richard",
        "tribe_merge_name": "Rattana"
    },
    2: {
        "name": "The Australian Outback",
        "year": 2001,
        "location": "Herbert River, Queensland, Australia",
        "url": "https://survivor.fandom.com/wiki/Survivor:_The_Australian_Outback",
        "merge_episode": 7,
        "episodes": 14,
        "contestants": 16,
        "finalists": ["Tina", "Colby"],  # First names to match voting data
        "winner": "Tina",
        "tribe_merge_name": "Barramundi"
    },
    3: {
        "name": "Africa",
        "year": 2001,
        "location": "Shaba National Reserve, Kenya",
        "url": "https://survivor.fandom.com/wiki/Survivor:_Africa",
        "merge_episode": 7,
        "episodes": 14,
        "contestants": 16,
        "finalists": ["Ethan", "Kim J"],  # First names to match voting data (Kim J to distinguish from Kim P)
        "winner": "Ethan",
        "tribe_merge_name": "Moto Maji"
    },
    4: {
        "name": "Marquesas",
        "year": 2002,
        "location": "Nuku Hiva, Marquesas Islands, French Polynesia",
        "url": "https://survivor.fandom.com/wiki/Survivor:_Marquesas",
        "merge_episode": 7,
        "episodes": 13,
        "contestants": 13,
        "finalists": ["Vecepia", "Neleh"],
        "winner": "Vecepia",
        "tribe_merge_name": "Soliantu"
    },
    5: {
        "name": "Thailand",
        "year": 2002,
        "location": "Ko Tarutao, Thailand",
        "url": "https://survivor.fandom.com/wiki/Survivor:_Thailand",
        "merge_episode": 7,
        "episodes": 14,
        "contestants": 16,
        "finalists": ["Brian", "Clay"],
        "winner": "Brian",
        "tribe_merge_name": "Chuay Jai"
    },
    6: {
        "name": "The Amazon",
        "year": 2003,
        "location": "Rio Negro, Amazonas, Brazil",
        "url": "https://survivor.fandom.com/wiki/Survivor:_The_Amazon",
        "merge_episode": 7,
        "episodes": 13,
        "contestants": 16,
        "finalists": ["Jenna", "Matthew"],
        "winner": "Jenna",
        "tribe_merge_name": "Jacaré"
    },
    7: {
        "name": "Pearl Islands",
        "year": 2003,
        "location": "Pearl Islands, Panama",
        "url": "https://survivor.fandom.com/wiki/Survivor:_Pearl_Islands",
        "merge_episode": 7,
        "episodes": 14,
        "contestants": 16,
        "finalists": ["Sandra", "Lillian"],
        "winner": "Sandra",
        "tribe_merge_name": "Balboa"
    },
    8: {
        "name": "All-Stars",
        "year": 2004,
        "location": "Pearl Islands, Panama",
        "url": "https://survivor.fandom.com/wiki/Survivor:_All-Stars",
        "merge_episode": 7,
        "episodes": 15,
        "contestants": 18,
        "finalists": ["Amber", "Rob M"],  # Rob M to distinguish from Rob C
        "winner": "Amber",
        "tribe_merge_name": "Chaboga Mogo"
    },
    9: {
        "name": "Vanuatu",
        "year": 2004,
        "location": "Vanuatu",
        "url": "https://survivor.fandom.com/wiki/Survivor:_Vanuatu",
        "merge_episode": 7,
        "episodes": 14,
        "contestants": 18,
        "finalists": ["Chris", "Twila"],
        "winner": "Chris",
        "tribe_merge_name": "Alinta"
    },
    10: {
        "name": "Palau",
        "year": 2005,
        "location": "Koror, Palau",
        "url": "https://survivor.fandom.com/wiki/Survivor:_Palau",
        "merge_episode": 8,  # Note: Palau had an unusual structure
        "episodes": 14,
        "contestants": 20,
        "finalists": ["Tom", "Katie"],
        "winner": "Tom",
        "tribe_merge_name": "Koror"  # Unusual: Koror dominated
    }
}

def get_season_info(season_number):
    """Get metadata for a specific season."""
    return SEASONS_METADATA.get(season_number)

def get_all_seasons(start=1, end=10):
    """Get metadata for a range of seasons."""
    return {k: v for k, v in SEASONS_METADATA.items() if start <= k <= end}

if __name__ == "__main__":
    print("Survivor Seasons 1-10 Metadata")
    print("=" * 70)

    for season_num, info in SEASONS_METADATA.items():
        print(f"\nSeason {season_num}: {info['name']} ({info['year']})")
        print(f"  Location: {info['location']}")
        print(f"  Contestants: {info['contestants']}")
        print(f"  Merge: Episode {info['merge_episode']}")
        print(f"  Winner: {info['winner']}")
