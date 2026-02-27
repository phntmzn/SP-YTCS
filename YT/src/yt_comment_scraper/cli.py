import argparse
import sys
from typing import Sequence

from .scraper import fetch_comments, save_comments


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scrape YouTube comments to a JSON file.")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument(
        "-n",
        "--max-comments",
        type=int,
        default=100,
        help="Maximum number of comments to fetch (default: 100)",
    )
    parser.add_argument(
        "-s",
        "--sort",
        choices=("popular", "recent"),
        default="recent",
        help="Sort order for comments (default: recent)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="comments.json",
        help="Output JSON file path (default: comments.json)",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)

    try:
        comments = fetch_comments(args.url, max_comments=args.max_comments, sort=args.sort)
        save_comments(args.output, comments)
    except Exception as exc:
        print(f"Failed to fetch comments: {exc}", file=sys.stderr)
        return 1

    print(f"Saved {len(comments)} comments to {args.output}")
    return 0
