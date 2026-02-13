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
    },
    11: {
        "name": "Guatemala",
        "year": 2005,
        "location": "Guatemala",
        "url": "https://survivor.fandom.com/wiki/Survivor:_Guatemala",
        "merge_episode": 7,
        "episodes": 14,
        "contestants": 18,
        "finalists": ["Danni", "Stephenie"],
        "winner": "Danni",
        "tribe_merge_name": "Xhakúm"
    },
    12: {
        "name": "Panama - Exile Island",
        "year": 2006,
        "location": "Pearl Islands, Panama",
        "url": "https://survivor.fandom.com/wiki/Survivor:_Panama",
        "merge_episode": 8,
        "episodes": 14,
        "contestants": 16,
        "finalists": ["Aras", "Danielle"],
        "winner": "Aras",
        "tribe_merge_name": "Gitanos"
    },
    13: {
        "name": "Cook Islands",
        "year": 2006,
        "location": "Cook Islands",
        "url": "https://survivor.fandom.com/wiki/Survivor:_Cook_Islands",
        "merge_episode": 11,
        "episodes": 14,
        "contestants": 20,
        "finalists": ["Yul", "Ozzy", "Becky"],  # Final 3
        "winner": "Yul",
        "tribe_merge_name": "Aitutonga"
    },
    14: {
        "name": "Fiji",
        "year": 2007,
        "location": "Fiji",
        "url": "https://survivor.fandom.com/wiki/Survivor:_Fiji",
        "merge_episode": 9,
        "episodes": 14,
        "contestants": 19,
        "finalists": ["Earl", "Cassandra", "Dreamz"],  # Final 3
        "winner": "Earl",
        "tribe_merge_name": "Bula Bula"
    },
    15: {
        "name": "China",
        "year": 2007,
        "location": "Jiangxi Province, China",
        "url": "https://survivor.fandom.com/wiki/Survivor:_China",
        "merge_episode": 8,
        "episodes": 14,
        "contestants": 16,
        "finalists": ["Todd", "Courtney", "Amanda"],  # Final 3
        "winner": "Todd",
        "tribe_merge_name": "Hae Da Fung"
    },
    16: {
        "name": "Micronesia - Fans vs Favorites",
        "year": 2008,
        "location": "Micronesia",
        "url": "https://survivor.fandom.com/wiki/Survivor:_Micronesia",
        "merge_episode": 8,
        "episodes": 14,
        "contestants": 20,
        "finalists": ["Parvati", "Amanda"],  # Final 2 (unusual for this era)
        "winner": "Parvati",
        "tribe_merge_name": "Dabu"
    },
    17: {
        "name": "Gabon",
        "year": 2008,
        "location": "Gabon",
        "url": "https://survivor.fandom.com/wiki/Survivor:_Gabon",
        "merge_episode": 8,
        "episodes": 14,
        "contestants": 18,
        "finalists": ["Bob", "Susie", "Sugar"],  # Final 3
        "winner": "Bob",
        "tribe_merge_name": "Nobag"
    },
    18: {
        "name": "Tocantins",
        "year": 2009,
        "location": "Tocantins, Brazil",
        "url": "https://survivor.fandom.com/wiki/Survivor:_Tocantins",
        "merge_episode": 9,
        "episodes": 14,
        "contestants": 16,
        "finalists": ["JT", "Stephen"],  # Final 2
        "winner": "JT",
        "tribe_merge_name": "Forza"
    },
    19: {
        "name": "Samoa",
        "year": 2009,
        "location": "Samoa",
        "url": "https://survivor.fandom.com/wiki/Survivor:_Samoa",
        "merge_episode": 8,
        "episodes": 14,
        "contestants": 20,
        "finalists": ["Natalie", "Russell", "Mick"],  # Final 3
        "winner": "Natalie",
        "tribe_merge_name": "Aiga"
    },
    20: {
        "name": "Heroes vs Villains",
        "year": 2010,
        "location": "Samoa",
        "url": "https://survivor.fandom.com/wiki/Survivor:_Heroes_vs._Villains",
        "merge_episode": 10,
        "episodes": 14,
        "contestants": 20,
        "finalists": ["Sandra", "Parvati", "Russell"],  # Final 3
        "winner": "Sandra",
        "tribe_merge_name": "Yin Yang"
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
