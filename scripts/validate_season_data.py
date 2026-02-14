#!/usr/bin/env python3
"""
Data Validation Checker for Survivor Season Files

Validates season data files for common errors before running the analysis pipeline.
Checks name consistency, episode ranges, vote integrity, and metadata completeness.

Usage:
    python scripts/validate_season_data.py 21                    # Single season
    python scripts/validate_season_data.py --range 21 30         # Multiple seasons
    python scripts/validate_season_data.py --metadata-only --range 21 30  # Metadata only
"""

import argparse
import importlib
import sys
from pathlib import Path
from collections import Counter

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))
from season_metadata import SEASONS_METADATA


class ValidationError:
    """Represents a validation error."""
    def __init__(self, severity, message):
        self.severity = severity  # 'ERROR' or 'WARNING'
        self.message = message

    def __str__(self):
        icon = "❌" if self.severity == "ERROR" else "⚠️ "
        return f"{icon} {self.message}"


def validate_metadata(season_num):
    """Validate that season has complete metadata."""
    errors = []

    if season_num not in SEASONS_METADATA:
        errors.append(ValidationError("ERROR", f"Season {season_num} not found in SEASONS_METADATA"))
        return errors

    metadata = SEASONS_METADATA[season_num]
    required_fields = ["name", "merge_episode", "finalists", "winner"]

    for field in required_fields:
        if field not in metadata or not metadata[field]:
            errors.append(ValidationError("ERROR", f"Missing required metadata field: {field}"))

    # Check merge_episode is valid
    if "merge_episode" in metadata:
        merge_ep = metadata["merge_episode"]
        if not isinstance(merge_ep, int) or merge_ep < 1:
            errors.append(ValidationError("ERROR", f"Invalid merge_episode: {merge_ep}"))

    # Check finalists is a list
    if "finalists" in metadata and not isinstance(metadata["finalists"], list):
        errors.append(ValidationError("ERROR", "finalists must be a list"))

    # Check winner is in finalists
    if "winner" in metadata and "finalists" in metadata:
        if metadata["winner"] not in metadata["finalists"]:
            errors.append(ValidationError("WARNING", f"Winner '{metadata['winner']}' not in finalists list"))

    return errors


def validate_season_data(season_num):
    """Validate a season's voting data file."""
    errors = []

    # First validate metadata
    metadata_errors = validate_metadata(season_num)
    errors.extend(metadata_errors)

    # If metadata is missing/broken, can't validate data file
    if any(e.severity == "ERROR" for e in metadata_errors):
        return errors

    metadata = SEASONS_METADATA[season_num]

    # Try to import the season data module
    module_name = f"season{season_num}_manual_data"
    try:
        season_module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        errors.append(ValidationError("ERROR", f"Data file {module_name}.py not found"))
        return errors
    except Exception as e:
        errors.append(ValidationError("ERROR", f"Error importing {module_name}.py: {e}"))
        return errors

    # Check required attributes exist
    if not hasattr(season_module, "SEASON_CONTESTANTS"):
        errors.append(ValidationError("ERROR", "Missing SEASON_CONTESTANTS list"))
        return errors

    if not hasattr(season_module, "SEASON_VOTING_HISTORY"):
        errors.append(ValidationError("ERROR", "Missing SEASON_VOTING_HISTORY list"))
        return errors

    contestants = season_module.SEASON_CONTESTANTS
    voting_history = season_module.SEASON_VOTING_HISTORY

    # Check contestants list is populated
    if not contestants:
        errors.append(ValidationError("WARNING", "SEASON_CONTESTANTS list is empty"))

    # Check voting history is populated
    if not voting_history:
        errors.append(ValidationError("WARNING", "SEASON_VOTING_HISTORY list is empty"))
        return errors

    # Validate finalists exist in contestant list
    for finalist in metadata["finalists"]:
        if finalist not in contestants:
            errors.append(ValidationError(
                "ERROR",
                f"Finalist '{finalist}' from metadata not found in SEASON_CONTESTANTS. "
                f"Names must match exactly for highlighting to work!"
            ))

    # Validate winner exists in contestant list
    winner = metadata["winner"]
    if winner not in contestants:
        errors.append(ValidationError(
            "ERROR",
            f"Winner '{winner}' from metadata not found in SEASON_CONTESTANTS"
        ))

    # Validate each tribal council
    merge_episode = metadata["merge_episode"]
    expected_episodes = set(range(1, merge_episode))
    actual_episodes = set()

    for idx, tc in enumerate(voting_history):
        tc_label = f"TC #{idx + 1}"

        # Check required fields
        if "episode" not in tc:
            errors.append(ValidationError("ERROR", f"{tc_label}: Missing 'episode' field"))
            continue

        episode = tc.get("episode")
        actual_episodes.add(episode)

        # Check episode is in valid range
        if episode >= merge_episode:
            errors.append(ValidationError(
                "ERROR",
                f"{tc_label} (Ep {episode}): Episode {episode} is >= merge episode {merge_episode}. "
                f"Only include Episodes 1-{merge_episode - 1}!"
            ))

        if "eliminated" not in tc:
            errors.append(ValidationError("ERROR", f"{tc_label} (Ep {episode}): Missing 'eliminated' field"))

        if "votes" not in tc:
            errors.append(ValidationError("ERROR", f"{tc_label} (Ep {episode}): Missing 'votes' field"))
            continue

        # Check for quit/medevac special cases
        is_quit = tc.get("quit", False)
        is_medevac = tc.get("medevac", False)
        votes = tc["votes"]

        if (is_quit or is_medevac) and votes:
            errors.append(ValidationError(
                "WARNING",
                f"{tc_label} (Ep {episode}): Quit/medevac should have empty votes dict"
            ))

        if not (is_quit or is_medevac) and not votes:
            errors.append(ValidationError(
                "ERROR",
                f"{tc_label} (Ep {episode}): Empty votes dict without quit/medevac flag"
            ))

        # Skip vote validation for quits/medevacs
        if is_quit or is_medevac:
            continue

        eliminated = tc.get("eliminated")

        # Check eliminated player is in contestant list
        if eliminated and eliminated not in contestants and eliminated != "TBD":
            errors.append(ValidationError(
                "ERROR",
                f"{tc_label} (Ep {episode}): Eliminated player '{eliminated}' not in SEASON_CONTESTANTS"
            ))

        # Validate all voters and targets
        for voter, target in votes.items():
            if voter not in contestants and voter != "TBD":
                errors.append(ValidationError(
                    "ERROR",
                    f"{tc_label} (Ep {episode}): Voter '{voter}' not in SEASON_CONTESTANTS"
                ))
            if target not in contestants and target != "TBD":
                errors.append(ValidationError(
                    "ERROR",
                    f"{tc_label} (Ep {episode}): Vote target '{target}' not in SEASON_CONTESTANTS"
                ))

        # Check eliminated player received most votes (if not TBD)
        if eliminated and eliminated != "TBD" and votes:
            vote_counts = Counter(votes.values())
            most_votes_player = vote_counts.most_common(1)[0][0]

            if eliminated != most_votes_player:
                errors.append(ValidationError(
                    "WARNING",
                    f"{tc_label} (Ep {episode}): Eliminated player '{eliminated}' didn't receive "
                    f"most votes ('{most_votes_player}' had {vote_counts[most_votes_player]} votes)"
                ))

    # Check for missing episodes
    missing_episodes = expected_episodes - actual_episodes
    if missing_episodes:
        errors.append(ValidationError(
            "WARNING",
            f"Missing episode(s) in voting data: {sorted(missing_episodes)}. "
            f"Expected Episodes 1-{merge_episode - 1}"
        ))

    # Check for duplicate episodes
    episode_counts = Counter(tc.get("episode") for tc in voting_history)
    duplicates = [ep for ep, count in episode_counts.items() if count > 1]
    if duplicates:
        errors.append(ValidationError(
            "WARNING",
            f"Duplicate episode(s) in voting data: {sorted(duplicates)}"
        ))

    return errors


def main():
    parser = argparse.ArgumentParser(
        description="Validate Survivor season data files"
    )
    parser.add_argument(
        "season",
        type=int,
        nargs="?",
        help="Season number to validate"
    )
    parser.add_argument(
        "--range",
        nargs=2,
        type=int,
        metavar=("START", "END"),
        help="Validate a range of seasons (inclusive)"
    )
    parser.add_argument(
        "--metadata-only",
        action="store_true",
        help="Only validate metadata (skip data file checks)"
    )

    args = parser.parse_args()

    # Determine which seasons to validate
    if args.range:
        start, end = args.range
        seasons = range(start, end + 1)
        print(f"Validating Seasons {start}-{end}...")
        print("=" * 70)
    elif args.season:
        seasons = [args.season]
        print(f"Validating Season {args.season}...")
        print("=" * 70)
    else:
        parser.print_help()
        sys.exit(1)

    # Validate each season
    all_errors = {}
    for season_num in seasons:
        if args.metadata_only:
            errors = validate_metadata(season_num)
        else:
            errors = validate_season_data(season_num)

        all_errors[season_num] = errors

        # Print results for this season
        if not errors:
            print(f"✅ Season {season_num}: All checks passed")
        else:
            print(f"\nSeason {season_num}:")
            for error in errors:
                print(f"  {error}")

    # Summary
    print("\n" + "=" * 70)
    error_count = sum(
        len([e for e in errors if e.severity == "ERROR"])
        for errors in all_errors.values()
    )
    warning_count = sum(
        len([e for e in errors if e.severity == "WARNING"])
        for errors in all_errors.values()
    )
    passed_count = sum(1 for errors in all_errors.values() if not errors)

    print(f"Summary: {passed_count}/{len(seasons)} seasons passed validation")
    if error_count > 0:
        print(f"  ❌ {error_count} error(s) found")
    if warning_count > 0:
        print(f"  ⚠️  {warning_count} warning(s) found")

    # Exit with error code if any errors found
    sys.exit(1 if error_count > 0 else 0)


if __name__ == "__main__":
    main()
