"""Inspect the deployable knowledge index without loading any model."""
import argparse
from pathlib import Path
from .index import search_evidence


def main():
    parser = argparse.ArgumentParser(description="Offline SQLite FTS5 lookup")
    parser.add_argument("db", type=Path, help="Path to knowledge.db")
    parser.add_argument("question", help="Question / keywords")
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()
    for n, row in enumerate(search_evidence(args.db, args.question, min(max(args.limit, 1), 20)), 1):
        print(f"\n{n}. {row['source']} :: {row['location']}  [{row['kind']}]")
        print(row['snippet'])


if __name__ == "__main__":
    main()
