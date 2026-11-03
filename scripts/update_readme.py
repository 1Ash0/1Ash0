#!/usr/bin/env python3
"""Refresh the auto-generated sections of README.md from the GitHub API.

Rewrites only the text between marker comments:
  <!-- REPOS:START --> ... <!-- REPOS:END -->
  <!-- COMMITS:START --> ... <!-- COMMITS:END -->
  <!-- UPDATED:START --> ... <!-- UPDATED:END -->

If the API fails, README.md is left untouched.
"""
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone

USER = os.environ.get("GH_USER", "1Ash0")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
README = os.environ.get("README_PATH", "README.md")

# Repos that should never appear (profile repo is always skipped).
EXCLUDE = {r.strip().lower() for r in os.environ.get("EXCLUDE_REPOS", "").split(",") if r.strip()}
EXCLUDE.add(USER.lower())

MAX_REPOS = 5
MAX_COMMITS = 6


def api(path):
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": f"{USER}-profile-readme",
            **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
        },
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.load(resp)


def one_line(text, limit=70):
    text = " ".join((text or "").split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def fmt_date(iso):
    return datetime.fromisoformat(iso.replace("Z", "+00:00")).strftime("%d %b %Y")


def repos_block():
    repos = api(f"/users/{USER}/repos?per_page=100&sort=pushed&type=owner")
    rows = []
    for r in repos:
        if r["fork"] or r["name"].lower() in EXCLUDE:
            continue
        lang = f" · `{r['language']}`" if r.get("language") else ""
        desc = f"<br/><sub>{one_line(r['description'])}</sub>" if r.get("description") else ""
        rows.append(f"- **[{r['name']}]({r['html_url']})**{lang}{desc}")
        if len(rows) == MAX_REPOS:
            break
    return "\n".join(rows) or "_Nothing public yet._"


def commits_block():
    # Built from each recently pushed repo's own commit list, not the public
    # events feed: push events no longer carry their commits reliably.
    repos = api(f"/users/{USER}/repos?per_page=30&sort=pushed&type=owner")
    found = []
    for r in repos[:8]:
        if r["fork"] or r["name"].lower() in EXCLUDE:
            continue
        try:
            commits = api(f"/repos/{USER}/{r['name']}/commits?per_page=5")
        except Exception:
            continue  # an empty or unreadable repo should not blank the feed
        for c in commits:
            # The author= filter misses commits made with a noreply address;
            # match on the linked login instead.
            if (c.get("author") or {}).get("login", "").lower() != USER.lower():
                continue
            found.append((c["commit"]["author"]["date"], r["name"], c))
    found.sort(key=lambda x: x[0], reverse=True)
    rows = []
    for date, name, c in found[:MAX_COMMITS]:
        msg = one_line(c["commit"]["message"].splitlines()[0], 60)
        rows.append(f"- [`{c['sha'][:7]}`]({c['html_url']}) {msg} <sub>· {name} · {fmt_date(date)}</sub>")
    return "\n".join(rows) or "_No recent public commits._"


def replace(text, tag, body, inline=False):
    pattern = re.compile(rf"(<!-- {tag}:START -->)(.*?)(<!-- {tag}:END -->)", re.S)
    if not pattern.search(text):
        sys.exit(f"Marker {tag} not found in {README}")
    middle = body if inline else f"\n{body}\n"
    return pattern.sub(lambda m: f"{m.group(1)}{middle}{m.group(3)}", text)


def main():
    try:
        repos, commits = repos_block(), commits_block()
    except Exception as exc:  # network, rate limit, bad JSON
        sys.exit(f"GitHub API failed, leaving README untouched: {exc}")

    with open(README, encoding="utf-8") as f:
        text = f.read()

    text = replace(text, "REPOS", repos)
    text = replace(text, "COMMITS", commits)
    stamp = datetime.now(timezone.utc).strftime("%d %b %Y, %H:%M UTC")
    text = replace(text, "UPDATED", stamp, inline=True)

    with open(README, "w", encoding="utf-8") as f:
        f.write(text)
    print("README refreshed.")


if __name__ == "__main__":
    main()
