# Manual Voting Data Entry Guide

## Where to Find Voting Data

1. **Survivor Wiki** - Most reliable for individual votes
   - Visit: https://survivor.fandom.com/wiki/Survivor:[SeasonName]
   - Scroll to "Voting History" table (usually near bottom)
   - Each row shows a tribal council with individual votes

2. **True Dork Times** - Good for summary verification
   - Visit: https://www.truedorktimes.com/survivor/boxscores/s[XX].htm
   - Has aggregate stats to double-check totals

## Data Entry Process (Per Season)

### Season 21: Nicaragua (Merge: Episode 8, so collect Episodes 1-7)

1. Visit https://survivor.fandom.com/wiki/Survivor:_Nicaragua
2. Find the "Voting History" table
3. For each pre-merge tribal council (Episodes 1-7):
   - Note: Episode number, Day, Tribe name, Eliminated player
   - Record every vote: "Voter": "Target"
   - Include special cases (quits use empty votes dict)

### Example Entry Format:

```python
{
    "episode": 1,
    "day": 3,
    "tribe": "Espada",
    "eliminated": "Wendy Jo",
    "votes": {
        "Dan": "Wendy Jo",
        "Holly": "Wendy Jo",
        "Jane": "Wendy Jo",
        "Jill": "Wendy Jo",
        "Jimmy J": "Wendy Jo",
        "Jimmy T": "Wendy Jo",
        "Marty": "Wendy Jo",
        "Tyrone": "Wendy Jo",
        "Yve": "Wendy Jo",
        "Wendy Jo": "Yve"  # Wendy's vote
    }
},
```

## Time Estimate

- ~1.5-2 hours per season
- ~8-10 hours total for seasons 21-25

## Tips

- Use first names only (match metadata finalists exactly)
- Handle duplicates with initials (e.g., "Kim J" vs "Kim P")
- For revotes after ties, use final elimination vote only
- Mark quits/medevacs: `"quit": True, "votes": {}`
