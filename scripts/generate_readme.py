```python
#!/usr/bin/env python3

"""
LeetCode README Generator

Account:
    reteshgs2005

Generates:
    - Total LeetCode progress
    - Easy / Medium / Hard progress
    - Progress percentages
    - Topic-wise solved count from repository
    - Problem lists grouped by topic
"""

import json
import os
import re
from collections import defaultdict

import requests


# =========================================================
# Configuration
# =========================================================

USERNAME = "reteshgs2005"

GRAPHQL = "https://leetcode.com/graphql"

PATTERN = re.compile(r"^(\d{4})-(.+)$")

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json",
    "Origin": "https://leetcode.com",
    "Referer": "https://leetcode.com/",
}


# =========================================================
# GraphQL Queries
# =========================================================

USER_STATS_QUERY = """
query userProblemsSolved($username: String!) {
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

        profile {
            ranking
            reputation
        }
    }
}
"""


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


# =========================================================
# GraphQL helper
# =========================================================

def graphql_request(query, variables, operation_name):

    payload = {
        "query": query,
        "variables": variables,
        "operationName": operation_name,
    }

    response = requests.post(
        GRAPHQL,
        headers=HEADERS,
        json=payload,
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    if "errors" in data:
        raise RuntimeError(data["errors"])

    return data["data"]


# =========================================================
# Fetch LeetCode account statistics
# =========================================================

def fetch_user_stats():

    data = graphql_request(
        USER_STATS_QUERY,
        {"username": USERNAME},
        "userProblemsSolved",
    )

    user = data.get("matchedUser")

    if not user:
        raise RuntimeError(
            f"LeetCode user '{USERNAME}' was not found."
        )

    # ---------------------------------------------
    # Total available questions
    # ---------------------------------------------

    total_questions = {}

    for item in data["allQuestionsCount"]:
        total_questions[item["difficulty"]] = item["count"]

    # ---------------------------------------------
    # User solved questions
    # ---------------------------------------------

    solved_questions = {}

    for item in user["submitStatsGlobal"]["acSubmissionNum"]:
        solved_questions[item["difficulty"]] = item["count"]

    return {
        "total": total_questions.get("All", 0),
        "easy_total": total_questions.get("Easy", 0),
        "medium_total": total_questions.get("Medium", 0),
        "hard_total": total_questions.get("Hard", 0),

        "solved": solved_questions.get("All", 0),
        "easy_solved": solved_questions.get("Easy", 0),
        "medium_solved": solved_questions.get("Medium", 0),
        "hard_solved": solved_questions.get("Hard", 0),

        "ranking": user.get("profile", {}).get("ranking"),
        "reputation": user.get("profile", {}).get("reputation"),
    }


# =========================================================
# Fetch individual problem information
# =========================================================

def fetch_problem(slug):

    try:

        data = graphql_request(
            QUESTION_QUERY,
            {"titleSlug": slug},
            "getQuestion",
        )

        question = data.get("question")

        if not question:
            return None

        return {
            "title": question["title"],
            "difficulty": question["difficulty"],
            "topics": [
                topic["name"]
                for topic in question["topicTags"]
            ] or ["Other"],
        }

    except Exception as error:

        print(
            f"Skipping {slug}: {error}"
        )

        return None


# =========================================================
# Percentage helper
# =========================================================

def percentage(solved, total):

    if total == 0:
        return 0

    return (solved / total) * 100


# =========================================================
# Progress bar
# =========================================================

def progress_bar(solved, total, length=20):

    if total == 0:
        return "░" * length

    ratio = solved / total

    filled = round(ratio * length)

    filled = min(filled, length)

    return (
        "█" * filled
        + "░" * (length - filled)
    )


# =========================================================
# Main
# =========================================================

def main():

    print(
        f"Fetching LeetCode statistics for "
        f"{USERNAME}..."
    )

    # -----------------------------------------------------
    # Account statistics
    # -----------------------------------------------------

    stats = fetch_user_stats()

    print(
        f"LeetCode solved: "
        f"{stats['solved']}/{stats['total']}"
    )

    # -----------------------------------------------------
    # Repository problems
    # -----------------------------------------------------

    problems = []

    for entry in os.listdir("."):

        if not os.path.isdir(entry):
            continue

        match = PATTERN.match(entry)

        if not match:
            continue

        number = int(match.group(1))
        slug = match.group(2)

        print(
            f"Fetching problem "
            f"{number:04d}: {slug}"
        )

        metadata = fetch_problem(slug)

        if metadata is None:
            continue

        problems.append(
            {
                "number": number,
                "folder": entry,
                **metadata,
            }
        )

    # -----------------------------------------------------
    # Sort problems
    # -----------------------------------------------------

    problems.sort(
        key=lambda problem: problem["number"]
    )

    # -----------------------------------------------------
    # Group repository problems by topic
    # -----------------------------------------------------

    grouped = defaultdict(list)

    for problem in problems:

        for topic in problem["topics"]:
            grouped[topic].append(problem)

    # -----------------------------------------------------
    # Topic counts
    # -----------------------------------------------------

    topic_counts = {
        topic: len(items)
        for topic, items in grouped.items()
    }

    # =====================================================
    # README
    # =====================================================

    out = []

    # -----------------------------------------------------
    # Header
    # -----------------------------------------------------

    out.append("# LeetCode Solutions\n")

    out.append(
        f"Solutions and progress for "
        f"**[{USERNAME}](https://leetcode.com/u/{USERNAME}/)**.\n"
    )

    # -----------------------------------------------------
    # Overall progress
    # -----------------------------------------------------

    total_solved = stats["solved"]
    total_questions = stats["total"]

    overall_percentage = percentage(
        total_solved,
        total_questions,
    )

    out.append("## 📊 LeetCode Progress\n")

    out.append(
        f"### {total_solved} / {total_questions} "
        f"problems solved\n"
    )

    out.append(
        f"`{progress_bar(total_solved, total_questions)}` "
        f"**{overall_percentage:.2f}%**\n"
    )

    # -----------------------------------------------------
    # Difficulty table
    # -----------------------------------------------------

    out.append("| Difficulty | Solved | Total | Progress |")
    out.append("|------------|-------:|------:|---------:|")

    difficulties = [
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

    for name, solved, total in difficulties:

        pct = percentage(solved, total)

        out.append(
            f"| {name} | "
            f"{solved} | "
            f"{total} | "
            f"{pct:.2f}% |"
        )

    out.append("")

    # -----------------------------------------------------
    # Repository statistics
    # -----------------------------------------------------

    out.append("## 💻 Repository\n")

    out.append(
        f"**{len(problems)} solutions** "
        f"uploaded to this repository.\n"
    )

    repo_difficulty = defaultdict(int)

    for problem in problems:
        repo_difficulty[
            problem["difficulty"]
        ] += 1

    out.append("| Difficulty | Solutions |")
    out.append("|------------|----------:|")

    out.append(
        f"| 🟢 Easy | "
        f"{repo_difficulty['Easy']} |"
    )

    out.append(
        f"| 🟡 Medium | "
        f"{repo_difficulty['Medium']} |"
    )

    out.append(
        f"| 🔴 Hard | "
        f"{repo_difficulty['Hard']} |"
    )

    out.append("")

    # -----------------------------------------------------
    # Topics
    # -----------------------------------------------------

    out.append("## 🧠 Topics\n")

    out.append(
        "| Topic | Problems Solved |"
    )

    out.append(
        "|-------|----------------:|"
    )

    for topic in sorted(
        topic_counts,
        key=lambda x: (-topic_counts[x], x),
    ):

        out.append(
            f"| {topic} | "
            f"{topic_counts[topic]} |"
        )

    out.append("")

    # -----------------------------------------------------
    # Topic navigation
    # -----------------------------------------------------

    out.append("## 📚 Solutions by Topic\n")

    for topic in sorted(grouped):

        anchor = (
            topic.lower()
            .replace(" ", "-")
            .replace("&", "")
        )

        out.append(
            f"- [{topic}](#{anchor})"
        )

    out.append("\n---\n")

    # -----------------------------------------------------
    # Problems by topic
    # -----------------------------------------------------

    for topic in sorted(grouped):

        out.append(
            f"## {topic}\n"
        )

        out.append(
            "| Problem | Difficulty |"
        )

        out.append(
            "|---------|------------|"
        )

        for problem in sorted(
            grouped[topic],
            key=lambda x: x["number"],
        ):

            out.append(
                f"| "
                f"[{problem['number']:04d} "
                f"{problem['title']}]"
                f"(./{problem['folder']}/) "
                f"| "
                f"{problem['difficulty']} |"
            )

        out.append("")

    # -----------------------------------------------------
    # Footer
    # -----------------------------------------------------

    out.append("---\n")

    out.append(
        f"*README automatically generated from "
        f"LeetCode profile `{USERNAME}`.*"
    )

    # -----------------------------------------------------
    # Write README
    # -----------------------------------------------------

    with open(
        "README.md",
        "w",
        encoding="utf-8",
    ) as file:

        file.write(
            "\n".join(out)
        )

    print(
        "\nREADME.md generated successfully!"
    )


if __name__ == "__main__":
    main()
```
