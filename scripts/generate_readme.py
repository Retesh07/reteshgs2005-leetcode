#!/usr/bin/env python3

import os
import re
from collections import defaultdict

import requests


USERNAME = "reteshgs2005"

GRAPHQL_URL = "https://leetcode.com/graphql"

FOLDER_PATTERN = re.compile(r"^(\d{4})-(.+)$")

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json",
    "Origin": "https://leetcode.com",
    "Referer": "https://leetcode.com/",
}


USER_STATS_QUERY = """
query userStats($username: String!) {
    allQuestionsCount {
        difficulty
        count
    }

    matchedUser(username: $username) {
        username

        submitStatsGlobal {
            acSubmissionNum {
                difficulty
                count
            }
        }
    }
}
"""


QUESTION_QUERY = """
query questionData($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
        title
        difficulty
        topicTags {
            name
        }
    }
}
"""


def graphql(query, variables, operation_name):
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


def get_user_stats():
    print(f"Fetching LeetCode stats for {USERNAME}...")

    data = graphql(
        USER_STATS_QUERY,
        {"username": USERNAME},
        "userStats",
    )

    user = data.get("matchedUser")

    if not user:
        raise RuntimeError(
            f"LeetCode user '{USERNAME}' was not found."
        )

    totals = {
        item["difficulty"]: item["count"]
        for item in data["allQuestionsCount"]
    }

    solved = {
        item["difficulty"]: item["count"]
        for item in user["submitStatsGlobal"]["acSubmissionNum"]
    }

    return {
        "total": totals.get("All", 0),
        "easy_total": totals.get("Easy", 0),
        "medium_total": totals.get("Medium", 0),
        "hard_total": totals.get("Hard", 0),
        "solved": solved.get("All", 0),
        "easy_solved": solved.get("Easy", 0),
        "medium_solved": solved.get("Medium", 0),
        "hard_solved": solved.get("Hard", 0),
    }


def get_problem(slug):
    try:
        data = graphql(
            QUESTION_QUERY,
            {"titleSlug": slug},
            "questionData",
        )

        question = data.get("question")

        if not question:
            print(f"Problem not found: {slug}")
            return None

        return {
            "title": question["title"],
            "difficulty": question["difficulty"],
            "topics": [
                tag["name"]
                for tag in question["topicTags"]
            ] or ["Other"],
        }

    except Exception as error:
        print(f"Failed to fetch {slug}: {error}")
        return None


def percent(solved, total):
    if total == 0:
        return 0

    return solved / total * 100


def progress_bar(solved, total, size=20):
    if total == 0:
        return "░" * size

    filled = int((solved / total) * size)
    filled = min(filled, size)

    return "█" * filled + "░" * (size - filled)


def scan_repository():
    problems = []

    for folder in os.listdir("."):
        if not os.path.isdir(folder):
            continue

        match = FOLDER_PATTERN.match(folder)

        if not match:
            continue

        number = int(match.group(1))
        slug = match.group(2)

        print(f"Fetching problem {number:04d} - {slug}")

        data = get_problem(slug)

        if data is None:
            continue

        problems.append({
            "number": number,
            "folder": folder,
            "slug": slug,
            **data,
        })

    problems.sort(key=lambda x: x["number"])

    return problems


def generate_readme(stats, problems):
    topics = defaultdict(list)

    for problem in problems:
        for topic in problem["topics"]:
            topics[topic].append(problem)

    lines = []

    lines.append("# LeetCode Solutions")
    lines.append("")
    lines.append(
        f"Solutions by "
        f"[{USERNAME}](https://leetcode.com/u/{USERNAME}/)"
    )
    lines.append("")

    # =====================================================
    # LeetCode Account Progress
    # =====================================================

    lines.append("## 📊 LeetCode Progress")
    lines.append("")

    overall = percent(
        stats["solved"],
        stats["total"],
    )

    lines.append(
        f"### {stats['solved']} / {stats['total']} Problems Solved"
    )
    lines.append("")

    lines.append(
        f"`{progress_bar(stats['solved'], stats['total'])}` "
        f"**{overall:.2f}%**"
    )

    lines.append("")

    lines.append("| Difficulty | Solved | Total | Progress |")
    lines.append("|------------|-------:|------:|---------:|")

    difficulty_data = [
        (
            "🟢 Easy",
            stats["easy_solved"],
            stats["easy_total"],
        ),
        (
            "🟡 Medium",
            stats["medium_solved"],
            stats["medium_total"],
        ),
        (
            "🔴 Hard",
            stats["hard_solved"],
            stats["hard_total"],
        ),
    ]

    for name, solved, total in difficulty_data:
        lines.append(
            f"| {name} | {solved} | {total} | "
            f"{percent(solved, total):.2f}% |"
        )

    lines.append("")

    # =====================================================
    # Repository Stats
    # =====================================================

    lines.append("## 💻 Repository")
    lines.append("")

    lines.append(
        f"**{len(problems)} solutions** are currently "
        f"stored in this repository."
    )

    lines.append("")

    repo_difficulty = defaultdict(int)

    for problem in problems:
        repo_difficulty[problem["difficulty"]] += 1

    lines.append("| Difficulty | Solutions |")
    lines.append("|------------|----------:|")
    lines.append(
        f"| 🟢 Easy | {repo_difficulty['Easy']} |"
    )
    lines.append(
        f"| 🟡 Medium | {repo_difficulty['Medium']} |"
    )
    lines.append(
        f"| 🔴 Hard | {repo_difficulty['Hard']} |"
    )

    lines.append("")

    # =====================================================
    # Topics
    # =====================================================

    lines.append("## 🧠 Topics")
    lines.append("")

    lines.append("| Topic | Problems |")
    lines.append("|-------|---------:|")

    topic_order = sorted(
        topics,
        key=lambda topic: (-len(topics[topic]), topic),
    )

    for topic in topic_order:
        lines.append(
            f"| {topic} | {len(topics[topic])} |"
        )

    lines.append("")

    # =====================================================
    # Solutions
    # =====================================================

    lines.append("## 📝 Solutions")
    lines.append("")

    for topic in sorted(topics):

        lines.append(f"### {topic}")
        lines.append("")

        lines.append("| Problem | Difficulty |")
        lines.append("|---------|------------|")

        topic_problems = sorted(
            topics[topic],
            key=lambda x: x["number"],
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

    # =====================================================
    # Footer
    # =====================================================

    lines.append("---")
    lines.append("")
    lines.append(
        "*README automatically generated from LeetCode.*"
    )

    return "\n".join(lines) + "\n"


def main():
    print("=" * 60)
    print("LeetCode README Generator")
    print("=" * 60)

    stats = get_user_stats()

    print(
        f"Account solved: "
        f"{stats['solved']} / {stats['total']}"
    )

    problems = scan_repository()

    print(
        f"Repository solutions: {len(problems)}"
    )

    readme = generate_readme(
        stats,
        problems,
    )

    with open(
        "README.md",
        "w",
        encoding="utf-8",
    ) as file:
        file.write(readme)

    print("=" * 60)
    print("README.md generated successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
