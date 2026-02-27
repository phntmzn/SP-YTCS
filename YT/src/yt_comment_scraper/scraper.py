import json
from itertools import islice
from typing import Any

from youtube_comment_downloader import SORT_BY_POPULAR, SORT_BY_RECENT, YoutubeCommentDownloader


def fetch_comments(url: str, max_comments: int = 100, sort: str = "recent") -> list[dict[str, Any]]:
    sort_map = {"popular": SORT_BY_POPULAR, "recent": SORT_BY_RECENT}
    if sort not in sort_map:
        raise ValueError("sort must be one of: popular, recent")

    downloader = YoutubeCommentDownloader()
    generator = downloader.get_comments_from_url(url, sort_by=sort_map[sort])
    return list(islice(generator, max(0, max_comments)))


def save_comments(path: str, comments: list[dict[str, Any]]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(comments, f, ensure_ascii=False, indent=2)
