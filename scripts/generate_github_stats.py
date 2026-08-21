#!/usr/bin/env python3
"""Generate a compact, self-hosted GitHub activity SVG for this profile."""

from __future__ import annotations

import argparse
import html
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import UTC, datetime, timedelta
from pathlib import Path

API_URL = "https://api.github.com/graphql"

QUERY = """
query ProfileStats($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
      totalRepositoriesWithContributedCommits
    }
  }
}
"""


def fetch_stats(login: str, token: str) -> dict[str, int]:
    now = datetime.now(UTC)
    payload = json.dumps({"query": QUERY, "variables": {"login": login, "from": (now - timedelta(days=365)).isoformat(), "to": now.isoformat()}}).encode()
    request = urllib.request.Request(API_URL, data=payload, headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "User-Agent": "profile-stats-generator"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.load(response)
    except urllib.error.URLError as error:
        raise RuntimeError(f"GitHub API request failed: {error}") from error

    if result.get("errors"):
        raise RuntimeError(f"GitHub GraphQL error: {result['errors']}")
    user = result.get("data", {}).get("user")
    if not user:
        raise RuntimeError(f"GitHub user '{login}' was not found")
    activity = user["contributionsCollection"]
    return {"Commits": activity["totalCommitContributions"], "Pull requests": activity["totalPullRequestContributions"], "Issues": activity["totalIssueContributions"], "Contributed to": activity["totalRepositoriesWithContributedCommits"]}


def render_svg(login: str, stats: dict[str, int]) -> str:
    items = list(stats.items())
    width, column_width = 800, 150
    left = (width - column_width * len(items)) // 2
    nodes = []
    for index, (label, value) in enumerate(items):
        x = left + index * column_width + column_width // 2
        divider = "" if index == 0 else f'<line x1="{x - 75}" y1="68" x2="{x - 75}" y2="136" class="divider" />'
        nodes.append(f'''{divider}
      <text x="{x}" y="98" class="value" text-anchor="middle">{value:,}</text>
      <text x="{x}" y="122" class="label" text-anchor="middle">{html.escape(label)}</text>''')
    escaped_login = html.escape(login)
    summary = ", ".join(f"{label} {value}" for label, value in items)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="168" viewBox="0 0 {width} 168" role="img" aria-labelledby="title desc">
  <title id="title">GitHub activity for {escaped_login}</title>
  <desc id="desc">GitHub contributions for the last 12 months: {summary}.</desc>
  <style>
    .title {{ font: 600 18px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #24292f; }}
    .period, .label {{ font: 400 13px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #57606a; }}
    .value {{ font: 600 27px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #24292f; }}
    .divider {{ stroke: #d0d7de; stroke-width: 1; }}
  </style>
  <rect x="0.5" y="0.5" width="799" height="167" rx="8" fill="#ffffff" stroke="#d0d7de" />
  <rect x="28" y="23" width="3" height="16" rx="1.5" fill="#0969da" />
  <text x="40" y="36" class="title">GitHub Activity</text>
  <text x="772" y="36" class="period" text-anchor="end">Last 12 months</text>
  <line x1="28" y1="52" x2="772" y2="52" class="divider" />
  <g>{"".join(nodes)}
  </g>
</svg>
'''


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--username", required=True, help="GitHub login to query")
    parser.add_argument("--output", type=Path, required=True, help="SVG output path")
    args = parser.parse_args()
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN is required to generate GitHub statistics.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_svg(args.username, fetch_stats(args.username, token)), encoding="utf-8")


if __name__ == "__main__":
    main()
