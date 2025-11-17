#!/bin/bash
# Quickstart script for vectorizing AutoHotkey documentation

set -e  # Exit on error

echo "=========================================="
echo "AutoHotkey Documentation Vectorization"
echo "=========================================="
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Ask user which approach
echo "Choose your approach:"
echo "  1) Hierarchical structure (RECOMMENDED for vectorization)"
echo "  2) Flat structure (keep current layout)"
echo ""
read -p "Enter choice (1 or 2): " choice

if [ "$choice" = "1" ]; then
    echo ""
    echo "📁 HIERARCHICAL STRUCTURE SELECTED"
    echo "This will organize files into categories for better vectorization"
    echo ""

    # Step 1: Analyze
    echo "[1/4] Analyzing files..."
    python3 scripts/1_analyze_files.py

    if [ $? -ne 0 ]; then
        echo "❌ Analysis failed"
        exit 1
    fi

    echo "✓ Analysis complete. Check analysis_report.json for details."
    echo ""

    # Step 2: Preview reorganization
    echo "[2/4] Preview reorganization..."
    python3 scripts/2_reorganize_files.py
    echo ""

    read -p "Proceed with reorganization? (y/N): " confirm
    if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
        echo "Aborted. Run 'python3 scripts/2_reorganize_files.py --execute' manually when ready."
        exit 0
    fi

    # Step 3: Reorganize
    echo ""
    echo "[3/4] Reorganizing files..."
    python3 scripts/2_reorganize_files.py --execute

    if [ $? -ne 0 ]; then
        echo "❌ Reorganization failed"
        exit 1
    fi

    echo "✓ Files reorganized into docs_reorganized/"
    echo ""

    # Step 4: Vectorize
    echo "[4/4] Vectorizing documentation..."

    if [ -z "$OPENAI_API_KEY" ]; then
        echo "⚠️  OPENAI_API_KEY not set. Creating chunks without embeddings."
        echo "   Set OPENAI_API_KEY and re-run with --embed to add embeddings."
        python3 scripts/3_vectorize_docs.py --input docs_reorganized
    else
        read -p "Create embeddings with OpenAI? (costs ~$0.10) (Y/n): " embed
        if [ "$embed" != "n" ] && [ "$embed" != "N" ]; then
            python3 scripts/3_vectorize_docs.py --input docs_reorganized --embed
        else
            python3 scripts/3_vectorize_docs.py --input docs_reorganized
        fi
    fi

elif [ "$choice" = "2" ]; then
    echo ""
    echo "📄 FLAT STRUCTURE SELECTED"
    echo "Keeping current file layout"
    echo ""

    # Step 1: Analyze
    echo "[1/2] Analyzing files..."
    python3 scripts/1_analyze_files.py

    if [ $? -ne 0 ]; then
        echo "❌ Analysis failed"
        exit 1
    fi

    echo "✓ Analysis complete"
    echo ""

    # Step 2: Vectorize
    echo "[2/2] Vectorizing documentation..."

    if [ -z "$OPENAI_API_KEY" ]; then
        echo "⚠️  OPENAI_API_KEY not set. Creating chunks without embeddings."
        echo "   Set OPENAI_API_KEY and re-run with --embed to add embeddings."
        python3 scripts/3_vectorize_docs.py --input .
    else
        read -p "Create embeddings with OpenAI? (costs ~$0.10) (Y/n): " embed
        if [ "$embed" != "n" ] && [ "$embed" != "N" ]; then
            python3 scripts/3_vectorize_docs.py --input . --embed
        else
            python3 scripts/3_vectorize_docs.py --input .
        fi
    fi

else
    echo "Invalid choice"
    exit 1
fi

echo ""
echo "=========================================="
echo "✓ COMPLETE!"
echo "=========================================="
echo ""
echo "Output:"
echo "  - vectorized_docs.json (chunks with/without embeddings)"
echo "  - analysis_report.json (categorization data)"
if [ "$choice" = "1" ]; then
    echo "  - docs_reorganized/ (organized files)"
fi
echo ""
echo "Next steps:"
echo "  - Query: python3 scripts/4_query_docs.py"
echo "  - Interactive: python3 scripts/4_query_docs.py"
echo "  - Integrate with your RAG system"
echo ""
echo "See scripts/README.md for more details!"
