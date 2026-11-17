#!/usr/bin/env python3
"""Refresh the "Recently shipped" section of the profile README.

Lists your newest public repositories (newest first) between these two markers in README.md:
    <!-- RECENT-PROJECTS:START -->
    <!-- RECENT-PROJECTS:END -->

Rules:
  * forks, archived repos and this profile repo are skipped
  * repos named in EXCLUDE_REPOS are skipped (comma-separated, case-insensitive)
  * repos with no "About" description are skipped, so a repo only shows up
    once you've written a one-line description for it

Settings come from environment variables: GH_USER, GITHUB_TOKEN, EXCLUDE_REPOS, RECENT_COUNT.
For a local test without the network: python scripts/update_readme.py --from-file sample.json
"""
import json
import os
import re
import sys
import urllib.request
from datetime import datetime

USER = os.environ.get("GH_USER", "Carl090403")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
COUNT = int(os.environ.get("RECENT_COUNT", "5"))
EXCLUDE = {n.strip().lower() for n in os.environ.get("EXCLUDE_REPOS", "").split(",") if n.strip()}
README = os.environ.get("README_PATH", "README.md")

START = "<!-- RECENT-PROJECTS:START -->"
END = "<!-- RECENT-PROJECTS:END -->"


def fetch_repos():
    url = f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner&sort=created&direction=desc"
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "profile-readme-updater"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as resp:
        return json.load(resp)


def build_block(repos):
    picked = []
    for r in sorted(repos, key=lambda r: r["created_at"], reverse=True):
        name = r["name"]
        if r.get("fork") or r.get("archived") or r.get("private"):
            continue
        if name.lower() == USER.lower() or name.lower() in EXCLUDE:
            continue
        if not (r.get("description") or "").strip():
            continue
        picked.append(r)
        if len(picked) == COUNT:
            break

    if not picked:
        return "_New projects coming soon._"

    lines = []
    for r in picked:
        created = datetime.strptime(r["created_at"][:10], "%Y-%m-%d").strftime("%b %Y")
        parts = [f"**[{r['name']}]({r['html_url']})**: {r['description'].strip()}"]
        if r.get("language"):
            parts.append(f"`{r['language']}`")
        if (r.get("homepage") or "").strip():
            parts.append(f"[live]({r['homepage'].strip()})")
        parts.append(created)
        lines.append("- " + " · ".join(parts))
    return "\n".join(lines)


def replace_block(text, block):
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(text):
        sys.exit(f"Markers not found in {README}. Add {START} and {END} where the list should go.")
    return pattern.sub(lambda _: f"{START}\n{block}\n{END}", text, count=1)


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--from-file":
        with open(sys.argv[2], encoding="utf-8") as f:
            repos = json.load(f)
    else:
        repos = fetch_repos()

    with open(README, encoding="utf-8") as f:
        old = f.read()
    new = replace_block(old, build_block(repos))
    if new == old:
        print("README already up to date.")
        return
    with open(README, "w", encoding="utf-8") as f:
        f.write(new)
    print("README updated.")


if __name__ == "__main__":
    main()

