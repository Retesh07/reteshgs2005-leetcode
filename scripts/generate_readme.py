
#!/usr/bin/env python3
"""
Production README generator for a LeetCode repository.

Features
- Scans folders matching ^\d{4}-.*
- Fetches title, difficulty and topic tags from LeetCode GraphQL
- Groups problems by topic
- Sorts topics alphabetically
- Sorts problems numerically
- Generates a clean README.md
- Uses only requests
"""

import json
import os
import re
from collections import defaultdict

import requests

GRAPHQL = "https://leetcode.com/graphql"
PATTERN = re.compile(r"^(\d{4})-(.+)$")

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json",
    "Origin": "https://leetcode.com",
    "Referer": "https://leetcode.com/",
}

QUERY = """
query getQuestion($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    title
    difficulty
    topicTags {
      name
    }
  }
}
"""

def fetch(slug):
    payload = {
        "query": QUERY,
        "variables": {"titleSlug": slug},
        "operationName": "getQuestion"
    }
    try:
        r = requests.post(
            GRAPHQL,
            headers=HEADERS,
            data=json.dumps(payload),
            timeout=20
        )
        r.raise_for_status()
        q = r.json()["data"]["question"]
        if not q:
            return None
        return {
            "title": q["title"],
            "difficulty": q["difficulty"],
            "topics": [x["name"] for x in q["topicTags"]] or ["Other"]
        }
    except Exception as e:
        print(f"Skipping {slug}: {e}")
        return None

def main():
    problems = []

    for entry in os.listdir("."):
        if not os.path.isdir(entry):
            continue

        m = PATTERN.match(entry)
        if not m:
            continue

        number = int(m.group(1))
        slug = m.group(2)

        meta = fetch(slug)
        if meta is None:
            continue

        problems.append({
            "number": number,
            "folder": entry,
            **meta
        })

    problems.sort(key=lambda x: x["number"])

    grouped = defaultdict(list)

    for p in problems:
        for topic in p["topics"]:
            grouped[topic].append(p)

    out = []
    out.append("# LeetCode Solutions\n")
    out.append("## LeetCode Topics\n")

    for topic in sorted(grouped):
        anchor = topic.lower().replace(" ", "-")
        out.append(f"- [{topic}](#{anchor})")

    out.append("\n---\n")

    for topic in sorted(grouped):
        out.append(f"## {topic}\n")
        out.append("| Problem Name | Difficulty |")
        out.append("|--------------|------------|")

        for p in sorted(grouped[topic], key=lambda x: x["number"]):
            out.append(
                f"| [{p['number']:04d} {p['title']}](./{p['folder']}/) | {p['difficulty']} |"
            )

        out.append("")

    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(out))

    print("README.md generated successfully.")

if __name__ == "__main__":
    main()
