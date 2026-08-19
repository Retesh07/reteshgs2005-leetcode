#!/usr/bin/env python3

import os
import re
from collections import defaultdict

import requests


# ============================================================
# CONFIGURATION
# ============================================================

USERNAME = "reteshgs2005"

LEETCODE_PROFILE = (
    f"https://leetcode.com/u/{USERNAME}/"
)

LEETCODE_CARD = (
    f"https://leetcard.jacoblin.cool/{USERNAME}"
    "?theme=dark"
    "&font=Baloo_2"
    "&border=0"
    "&radius=12"
    "&animation=true"
    "&cache=3600"
)

GRAPHQL_URL = "https://leetcode.com/graphql"

FOLDER_PATTERN = re.compile(
    r"^(\d{4})-(.+)$"
)

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json",
    "Origin": "https://leetcode.com",
    "Referer": "https://leetcode.com/",
}


# ============================================================
# LEETCODE QUERY
# ============================================================

QUESTION_QUERY = """
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


# ============================================================
# GRAPHQL REQUEST
# ============================================================

def graphql_request(query, variables, operation_name):
    payload = {
        "query": query,
        "variables": variables,
        "operationName": operation_name,
    }

    response = requests.post(
        GRAPHQL_URL,
        headers=HEADERS,
        json=payload,
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    if "errors" in data:
        raise RuntimeError(data["errors"])

    return data["data"]


# ============================================================
# FETCH PROBLEM DATA
# ============================================================

def fetch_problem(slug):
    try:
        data = graphql_request(
            QUESTION_QUERY,
            {"titleSlug": slug},
            "getQuestion",
        )

        question = data.get("question")

        if not question:
            print(f"⚠️ Problem not found: {slug}")
            return None

        topics = [
            tag["name"]
            for tag in question.get("topicTags", [])
        ]

        if not topics:
            topics = ["Other"]

        return {
            "title": question["title"],
            "difficulty": question["difficulty"],
            "topics": topics,
        }

    except Exception as error:
        print(
            f"❌ Failed to fetch {slug}: {error}"
        )
        return None


# ============================================================
# SCAN REPOSITORY
# ============================================================

def scan_repository():
    problems = []

    print()
    print("=" * 60)
    print("Scanning repository")
    print("=" * 60)

    for folder in os.listdir("."):

        if not os.path.isdir(folder):
            continue

        match = FOLDER_PATTERN.match(folder)

        if not match:
            continue

        number = int(match.group(1))
        slug = match.group(2)

        print(
            f"Fetching {number:04d} - {slug}"
        )

        metadata = fetch_problem(slug)

        if metadata is None:
            continue

        problems.append({
            "number": number,
            "folder": folder,
            "slug": slug,
            **metadata,
        })

    problems.sort(
        key=lambda problem: problem["number"]
    )

    return problems


# ============================================================
# GENERATE README
# ============================================================

def generate_readme(problems):

    topics = defaultdict(list)

    difficulty_counts = {
        "Easy": 0,
        "Medium": 0,
        "Hard": 0,
    }

    # --------------------------------------------------------
    # Organize problems
    # --------------------------------------------------------

    for problem in problems:

        difficulty = problem["difficulty"]

        if difficulty in difficulty_counts:
            difficulty_counts[difficulty] += 1

        for topic in problem["topics"]:
            topics[topic].append(problem)

    # --------------------------------------------------------
    # README
    # --------------------------------------------------------

    lines = []

    # ========================================================
    # HEADER
    # ========================================================

    lines.append(
        "# LeetCode Solutions"
    )

    lines.append("")

    lines.append(
        f"Solutions and progress for "
        f"[**{USERNAME}**]({LEETCODE_PROFILE})."
    )

    lines.append("")

    # ========================================================
    # DYNAMIC LEETCODE CARD
    # ========================================================

    lines.append(
        "<p align=\"center\">"
    )

    lines.append(
        f"  <a href=\"{LEETCODE_PROFILE}\">"
    )

    lines.append(
        f"    <img "
        f"src=\"{LEETCODE_CARD}\" "
        f"alt=\"LeetCode Stats\" "
        f"width=\"500\" />"
    )

    lines.append(
        "  </a>"
    )

    lines.append(
        "</p>"
    )

    lines.append("")

    # ========================================================
    # REPOSITORY STATS
    # ========================================================

    lines.append(
        "## 📚 Repository Statistics"
    )

    lines.append("")

    lines.append(
        f"**{len(problems)} solutions** "
        f"are currently stored in this repository."
    )

    lines.append("")

    lines.append(
        "| Difficulty | Solutions |"
    )

    lines.append(
        "|------------|----------:|"
    )

    lines.append(
        f"| 🟢 Easy | "
        f"{difficulty_counts['Easy']} |"
    )

    lines.append(
        f"| 🟡 Medium | "
        f"{difficulty_counts['Medium']} |"
    )

    lines.append(
        f"| 🔴 Hard | "
        f"{difficulty_counts['Hard']} |"
    )

    lines.append("")

    # ========================================================
    # TOPICS
    # ========================================================

    lines.append(
        "## 🧠 Topics"
    )

    lines.append("")

    lines.append(
        "| Topic | Problems |"
    )

    lines.append(
        "|-------|---------:|"
    )

    sorted_topics = sorted(
        topics.keys(),
        key=lambda topic: (
            -len(topics[topic]),
            topic.lower(),
        ),
    )

    for topic in sorted_topics:

        lines.append(
            f"| {topic} | "
            f"{len(topics[topic])} |"
        )

    lines.append("")

    # ========================================================
    # TOPIC NAVIGATION
    # ========================================================

    lines.append(
        "## 🔎 Browse by Topic"
    )

    lines.append("")

    for topic in sorted(topics):

        anchor = (
            topic.lower()
            .replace(" ", "-")
            .replace("&", "")
            .replace("/", "")
        )

        lines.append(
            f"- [{topic}](#{anchor})"
        )

    lines.append("")

    lines.append("---")

    lines.append("")

    # ========================================================
    # PROBLEMS BY TOPIC
    # ========================================================

    for topic in sorted(
        topics,
        key=lambda x: x.lower(),
    ):

        lines.append(
            f"## {topic}"
        )

        lines.append("")

        lines.append(
            "| Problem | Difficulty |"
        )

        lines.append(
            "|---------|------------|"
        )

        topic_problems = sorted(
            topics[topic],
            key=lambda problem: problem["number"],
        )

        for problem in topic_problems:

            lines.append(
                f"| "
                f"[{problem['number']:04d} "
                f"{problem['title']}]"
                f"(./{problem['folder']}/) "
                f"| {problem['difficulty']} |"
            )

        lines.append("")

    # ========================================================
    # FOOTER
    # ========================================================

    lines.append("---")

    lines.append("")

    lines.append(
        "<p align=\"center\">"
    )

    lines.append(
        "  <i>Keep solving. Keep learning. 🚀</i>"
    )

    lines.append(
        "</p>"
    )

    lines.append("")

    return "\n".join(lines)


# ============================================================
# MAIN
# ============================================================

def main():

    print()
    print("=" * 60)
    print("🚀 LeetCode README Generator")
    print("=" * 60)

    print(
        f"Username: {USERNAME}"
    )

    print(
        f"Profile: {LEETCODE_PROFILE}"
    )

    problems = scan_repository()

    print()
    print(
        f"Found {len(problems)} problems "
        f"in repository."
    )

    readme = generate_readme(
        problems
    )

    with open(
        "README.md",
        "w",
        encoding="utf-8",
    ) as file:
        file.write(readme)

    print()
    print("=" * 60)
    print("✅ README.md generated successfully")
    print("=" * 60)


if __name__ == "__main__":
    main()
