"""
Analyze Season 1 voting data using manual data entry
This demonstrates the analysis logic without requiring web scraping
"""

from season1_manual_data import SEASON_1_VOTING_HISTORY, FINAL_TRIBAL_COUNCIL, SEASON_1_CONTESTANTS
from collections import defaultdict
import json

def calculate_vote_alignments(voting_history, pre_merge_only=False):
    """Calculate how many times each pair of players voted together.

    Args:
        voting_history: List of tribal council dictionaries
        pre_merge_only: If True, only analyze pre-merge votes
    """
    alignment_counts = defaultdict(int)

    for tribal_council in voting_history:
        # Skip merge and post-merge votes if pre_merge_only is True
        if pre_merge_only and tribal_council.get('merge', False):
            break
        if pre_merge_only and tribal_council.get('episode', 999) >= 7:
            continue
        votes = tribal_council['votes']
        voters = list(votes.keys())
        
        # For each pair of voters
        for i, voter1 in enumerate(voters):
            for voter2 in voters[i+1:]:
                # Check if they voted for the same person
                if votes[voter1] == votes[voter2]:
                    # Create sorted tuple as key (order doesn't matter)
                    pair = tuple(sorted([voter1, voter2]))
                    alignment_counts[pair] += 1
    
    return alignment_counts

def analyze_alliances(alignment_counts, min_votes=2):
    """Filter and analyze strong voting alliances."""
    strong_alliances = {k: v for k, v in alignment_counts.items() if v >= min_votes}
    return strong_alliances

def main():
    print("Survivor Season 1: Borneo - Voting Analysis (PRE-MERGE ONLY)")
    print("=" * 60)

    # Calculate alignments (PRE-MERGE ONLY)
    print("\n1. Calculating vote alignments (Episodes 1-6, before merge)...")
    alignments = calculate_vote_alignments(SEASON_1_VOTING_HISTORY, pre_merge_only=True)

    # Count pre-merge tribal councils
    pre_merge_tcs = sum(1 for tc in SEASON_1_VOTING_HISTORY if tc.get('episode', 999) < 7)
    print(f"   Total player pairs: {len(alignments)}")
    
    # Filter for strong alliances (2+ votes together)
    print("\n2. Identifying strong alliances (2+ votes together)...")
    strong_alliances = analyze_alliances(alignments, min_votes=2)
    print(f"   Strong alliance pairs: {len(strong_alliances)}")
    
    # Sort by vote count
    sorted_alliances = sorted(strong_alliances.items(), key=lambda x: x[1], reverse=True)
    
    print("\n3. Top 10 Strongest Voting Pairs:")
    print("-" * 60)
    for i, (pair, count) in enumerate(sorted_alliances[:10], 1):
        player1, player2 = pair
        print(f"   {i:2d}. {player1:12s} <-> {player2:12s}: {count:2d} votes together")
    
    # Finalists analysis
    finalists = FINAL_TRIBAL_COUNCIL['finalists']
    print(f"\n4. Finalists: {', '.join(finalists)}")
    print("-" * 60)
    
    # Find alliances involving finalists
    finalist_alliances = {}
    for finalist in finalists:
        finalist_pairs = []
        for (p1, p2), count in sorted_alliances:
            if finalist in (p1, p2):
                other = p2 if p1 == finalist else p1
                finalist_pairs.append((other, count))
        finalist_alliances[finalist] = sorted(finalist_pairs, key=lambda x: x[1], reverse=True)
    
    for finalist in finalists:
        print(f"\n   {finalist}'s strongest alliances:")
        for other, count in finalist_alliances[finalist][:5]:
            print(f"      - {other:12s}: {count:2d} votes together")
    
    # Save results
    print("\n5. Saving results...")
    
    # Convert to list for JSON serialization
    results = {
        "season": 1,
        "season_name": "Borneo",
        "analysis_type": "pre_merge_only",
        "total_tribal_councils": pre_merge_tcs,
        "total_tribal_councils_all_season": len(SEASON_1_VOTING_HISTORY),
        "contestants": SEASON_1_CONTESTANTS,
        "finalists": finalists,
        "winner": FINAL_TRIBAL_COUNCIL['winner'],
        "all_alignments": [
            {
                "player1": pair[0],
                "player2": pair[1],
                "votes_together": count
            }
            for pair, count in sorted(alignments.items(), key=lambda x: x[1], reverse=True)
        ],
        "strong_alliances": [
            {
                "player1": pair[0],
                "player2": pair[1],
                "votes_together": count
            }
            for pair, count in sorted_alliances
        ]
    }
    
    with open('season1_analysis_results.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print("   ✓ Saved to season1_analysis_results.json")
    
    # Summary statistics
    print("\n6. Summary Statistics:")
    print("-" * 60)
    print(f"   Total contestants: {len(SEASON_1_CONTESTANTS)}")
    print(f"   PRE-MERGE tribal councils analyzed: {pre_merge_tcs}")
    print(f"   Total tribal councils (all season): {len(SEASON_1_VOTING_HISTORY)}")
    print(f"   Total player pairs analyzed: {len(alignments)}")
    print(f"   Strong alliances (2+ votes): {len(strong_alliances)}")
    if sorted_alliances:
        print(f"   Strongest alliance: {sorted_alliances[0][0][0]} & {sorted_alliances[0][0][1]} ({sorted_alliances[0][1]} votes)")
    
    print("\n" + "=" * 60)
    print("Analysis complete!")
    print("\nNext step: Create network visualization with:")
    print("  - Nodes = players")
    print("  - Edges = pairs with 2+ votes together")
    print("  - Edge thickness = vote count")
    print("  - Highlighted finalists")

if __name__ == "__main__":
    main()
