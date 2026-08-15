#!/usr/bin/env python3
"""Search GitHub repositories via the official REST Search API.

Usage:
    python github_search.py "<query>" [--language <lang>] [--min-stars <n>] [--limit <n>]

Examples:
    python github_search.py "music player" --limit 5
    python github_search.py "music player" --language python --min-stars 100
    python github_search.py "音乐播放器" --limit 5

Notes:
    - Unauthenticated search is rate-limited to 10 requests/min; set the GITHUB_TOKEN
      environment variable for 30 requests/min.
    - Results are sorted by stars by default.
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.github.com/search/repositories"


def main():
    parser = argparse.ArgumentParser(description="Search GitHub repositories via the official REST Search API.")
    parser.add_argument("query", help="Search keywords, e.g. 'music player' or Chinese keywords")
    parser.add_argument("--language", help="Filter by primary language, e.g. python")
    parser.add_argument("--min-stars", type=int, help="Only repositories with at least this many stars")
    parser.add_argument("--limit", type=int, default=5, help="Number of results to return (default 5)")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN", "")

    # Build query with qualifiers
    q = args.query.strip()
    if args.language:
        q += f" language:{args.language}"
    if args.min_stars is not None:
        q += f" stars:>={args.min_stars}"

    params = urllib.parse.urlencode({
        "q": q,
        "sort": "stars",
        "order": "desc",
        "per_page": max(1, min(args.limit, 100)),
    })
    url = f"{API}?{params}"

    headers = {
        "User-Agent": "dont-skill-github-search",
        "Accept": "application/vnd.github+json",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"[ERROR] GitHub API error {e.code}: {e.reason}", file=sys.stderr)
        if e.code == 403:
            print("[ERROR] Rate limited. Set GITHUB_TOKEN for 30 requests/min.", file=sys.stderr)
        if e.code == 422:
            print("[ERROR] Invalid search query.", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"[ERROR] Network error: {e.reason}", file=sys.stderr)
        sys.exit(1)

    items = data.get("items", [])
    total = data.get("total_count", 0)
    print(f"total_count: {total} | showing top {len(items)} (sorted by stars)")

    for item in items:
        desc = (item.get("description") or "").strip()
        if len(desc) > 90:
            desc = desc[:90] + "..."
        print("-" * 70)
        print(f"name       : {item.get('full_name')}")
        print(f"stars      : {item.get('stargazers_count')}")
        print(f"language   : {item.get('language') or 'N/A'}")
        print(f"license    : {item.get('license', {}).get('spdx_id') or 'N/A'}")
        print(f"archived   : {'yes' if item.get('archived') else 'no'}")
        print(f"open_issues: {item.get('open_issues_count', 0)}")
        print(f"url        : {item.get('html_url')}")
        print(f"updated    : {item.get('pushed_at', '')[:10]}")
        print(f"description: {desc}")


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    main()
