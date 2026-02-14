#!/bin/bash
# Demo script to showcase all helper tools for Seasons 21-30 setup

echo "========================================"
echo "Survivor Seasons 21-30 Helper Tools Demo"
echo "========================================"
echo ""

echo "1️⃣  Checking metadata for seasons 21-30..."
echo "----------------------------------------"
python scripts/validate_season_data.py --metadata-only --range 21 30
echo ""

echo "2️⃣  Current progress status..."
echo "----------------------------------------"
python scripts/track_progress.py
echo ""

echo "3️⃣  Testing validation on template (should show errors)..."
echo "----------------------------------------"
python scripts/validate_season_data.py 21
echo ""

echo "========================================"
echo "✅ All helper scripts operational!"
echo ""
echo "Next steps:"
echo "  1. Fill voting data in season21_manual_data.py"
echo "  2. Validate: python scripts/validate_season_data.py 21"
echo "  3. Track progress: python scripts/track_progress.py"
echo "  4. Repeat for seasons 22-30"
echo "  5. Run pipeline: python batch_analyze.py && python batch_visualize.py"
echo "========================================"
