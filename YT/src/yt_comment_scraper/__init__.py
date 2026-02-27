"""Public package interface for yt_comment_scraper."""

from .scraper import fetch_comments, save_comments

__all__ = ["fetch_comments", "save_comments"]
__version__ = "0.1.0"
