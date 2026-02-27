# yt-comment-scraper

Python package and CLI to fetch comments from a YouTube video and save them to JSON.

## Install

```bash
pip install .
```

For editable local development:

```bash
pip install -e .
```

## Usage

Using the installed CLI:

```bash
yt-comment-scraper "https://www.youtube.com/watch?v=VIDEO_ID" -n 100 -s recent -o comments.json
```

Using the repository script directly:

```bash
python3 scrape_youtube_comments.py "https://www.youtube.com/watch?v=VIDEO_ID" -n 100 -s recent -o comments.json
```

## Arguments

- `url`: YouTube video URL
- `-n, --max-comments`: max comments to fetch (default `100`)
- `-s, --sort`: `recent` or `popular` (default `recent`)
- `-o, --output`: output JSON file path (default `comments.json`)

## Notes

- This tool uses `youtube-comment-downloader`.
- YouTube rate limits and content availability can affect results.
