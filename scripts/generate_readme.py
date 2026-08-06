#!/usr/bin/env python3
"""
generate_readme.py

Scans LeetCode problem folders (####-slug), fetches metadata from LeetCode's
GraphQL API, groups problems by topic, and generates README.md.
Compatible with GitHub Actions.
"""

import json
import os
import re
from collections import defaultdict

import requests

GRAPHQL_URL = "https://leetcode.com/graphql"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com/",
    "Origin": "https://leetcode.com",
}

FOLDER_PATTERN = re.compile(r"^(\d{4})-(.+)$")

QUERY = """
query getQuestionDetail($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    difficulty
    topicTags {
      name
    }
  }
}
"""

EMOJI = {
    "Easy": "🟢 Easy",
    "Medium": "🟡 Medium",
    "Hard": "🔴 Hard",
}


def fetch_metadata(slug):
    payload = {
        "query": QUERY,
        "variables": {"titleSlug": slug},
        "operationName": "getQuestionDetail",
    }
    try:
        r = requests.post(
            GRAPHQL_URL,
            headers=HEADERS,
            data=json.dumps(payload),
            timeout=20,
        )
        r.raise_for_status()
        data = r.json()["data"]["question"]
        if not data:
            return None
        return {
            "difficulty": data["difficulty"],
            "topics": [t["name"] for t in data["topicTags"]],
        }
    except Exception as e:
        print(f"[WARN] Failed for {slug}: {e}")
        return None


def main():
    problems = []
    for name in os.listdir("."):
        if not os.path.isdir(name):
            continue
        m = FOLDER_PATTERN.match(name)
        if not m:
            continue

        number = int(m.group(1))
        slug = m.group(2)

        meta = fetch_metadata(slug)
        if not meta:
            continue

        problems.append({
            "number": number,
            "folder": name,
            "slug": slug,
            "difficulty": meta["difficulty"],
            "topics": meta["topics"] or ["Uncategorized"],
        })

    problems.sort(key=lambda x: x["number"])

    grouped = defaultdict(list)
    for p in problems:
        for topic in p["topics"]:
            grouped[topic].append(p)

    lines = []
    lines.append("# LeetCode Solutions\n")
    lines.append("## Topic Index\n")
    for topic in sorted(grouped):
        anchor = topic.lower().replace(" ", "-")
        lines.append(f"- [{topic}](#{anchor})")
    lines.append("")

    for topic in sorted(grouped):
        anchor = topic.lower().replace(" ", "-")
        lines.append(f"## {topic}\n")
        for p in sorted(grouped[topic], key=lambda x: x["number"]):
            diff = EMOJI.get(p["difficulty"], p["difficulty"])
            title = p["folder"]
            lines.append(
                f"- **{p['number']:04d}** "
                f"[{title}](./{p['folder']}/) — {diff}"
            )
        lines.append("")

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("README.md generated successfully.")


if __name__ == "__main__":
    main()
