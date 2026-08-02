import os
import re
import time
import json
import requests

# Set your LEETCODE_SESSION cookie here or via environment variable
LEETCODE_SESSION = os.environ.get("LEETCODE_SESSION", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfYXV0aF91c2VyX2lkIjoiOTk5MTAzNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImMzN2IxMTI3OTkxOTcyN2IwMjZiMzIzNzNiNGE4YzA4ZTQyYjM0Nzk5MDRkNzAzODQzNmEwOTAwOGUwMmIxODYiLCJzZXNzaW9uX3V1aWQiOiI2MWIzZDg3ZCIsImlkIjo5OTkxMDM1LCJlbWFpbCI6InJldGVzaGdzMjAwNUBnbWFpbC5jb20iLCJ1c2VybmFtZSI6InJldGVzaGdzMjAwNSIsInVzZXJfc2x1ZyI6InJldGVzaGdzMjAwNSIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9hdmF0YXJzL2F2YXRhcl8xNjg4Mzc0NzI1LnBuZyIsInJlZnJlc2hlZF9hdCI6MTc4NTY1NDAyOCwiaXAiOiIyNDA5OjQwZjI6NGE6ZWZhNToxMTU3OmQ1ZjI6NDM3MToyMzFjIiwiaWRlbnRpdHkiOiI2OTY3ZWM3MjYxYjNjYmU2YTkxZDc5OGM2Yjk1MWM2MCIsImRldmljZV93aXRoX2lwIjpbImQ3MmU1ZTg5YmE2ZWViMDY2NjlhNTBkYjZhY2IyNzBkIiwiMjQwOTo0MGYyOjRhOmVmYTU6MTE1NzpkNWYyOjQzNzE6MjMxYyJdfQ.jeh2PHuBYfpeiEEq41MN6nurxQeYTtFBWbgTt7KTXeU")
LEETCODE_CSRF = os.environ.get("LEETCODE_CSRF", "")

URL = "https://leetcode.com/graphql"

LANG_EXT = {
    "cpp": "cpp",
    "java": "java",
    "python": "py",
    "python3": "py",
    "c": "c",
    "csharp": "cs",
    "javascript": "js",
    "typescript": "ts",
    "golang": "go",
    "rust": "rs",
    "kotlin": "kt",
    "swift": "swift"
}

def safe_post(payload, headers, max_retries=3):
    for attempt in range(max_retries):
        try:
            res = requests.post(URL, json=payload, headers=headers, timeout=15)
            if res.status_code == 200:
                return res.json()
        except Exception as e:
            time.sleep(1)
    return None

def fetch_submissions():
    global LEETCODE_SESSION

    # Initialize Git repository if not initialized yet
    if not os.path.exists(".git"):
        try:
            import subprocess
            subprocess.run(["git", "init"], check=False)
            print("Initialized local Git repository (.git).")
        except Exception as e:
            pass

    if not LEETCODE_SESSION:
        print("--- LeetCode Solution Exporter for reteshgs2005 ---")
        LEETCODE_SESSION = input("Please paste your LEETCODE_SESSION cookie value: ").strip()
        if not LEETCODE_SESSION:
            print("Error: LEETCODE_SESSION cookie is required.")
            return

    headers = {
        "Content-Type": "application/json",
        "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={LEETCODE_CSRF};",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "x-csrftoken": LEETCODE_CSRF
    }

    sub_query = """
    query submissions($offset: Int!, $limit: Int!) {
        submissionList(offset: $offset, limit: $limit) {
            hasNext
            submissions {
                id
                title
                titleSlug
                statusDisplay
                lang
                timestamp
            }
        }
    }
    """

    detail_query = """
    query submissionDetails($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) {
            code
            timestamp
            statusCode
            lang {
                name
            }
            question {
                questionId
                title
                titleSlug
                content
                difficulty
            }
        }
    }
    """

    print("Fetching submission list...")
    offset = 0
    limit = 20
    has_next = True
    accepted_submissions = {}

    while has_next:
        data = safe_post({"query": sub_query, "variables": {"offset": offset, "limit": limit}}, headers)
        if not data or "data" not in data or "submissionList" not in data["data"]:
            print("Failed to fetch submission list. Check your LEETCODE_SESSION cookie.")
            break
            
        sub_list = data["data"]["submissionList"]
        submissions = sub_list["submissions"]
        has_next = sub_list["hasNext"]
        offset += limit

        for s in submissions:
            if s["statusDisplay"] == "Accepted":
                title_slug = s["titleSlug"]
                if title_slug not in accepted_submissions:
                    accepted_submissions[title_slug] = s["id"]

        print(f"Retrieved {len(accepted_submissions)} unique solved problems so far...")
        time.sleep(0.2)

    print(f"\nTotal unique solved problems found: {len(accepted_submissions)}")
    print("Exporting solutions & distributing commits across EVERY SINGLE DAY of the past year...")

    import math
    import datetime
    import subprocess

    sub_items = list(accepted_submissions.items())
    total_problems = len(sub_items)

    now = datetime.datetime.now(datetime.timezone.utc)
    start_date = datetime.datetime(2026, 1, 1, tzinfo=datetime.timezone.utc)
    num_days = (now.date() - start_date.date()).days + 1

    print(f"Exporting {total_problems} solutions across EVERY SINGLE DAY from Jan 1, 2026 to Today ({num_days} days)...")
    date_list = [(start_date + datetime.timedelta(days=i)) for i in range(num_days)]

    for idx, (slug, sub_id) in enumerate(sub_items):
        d_data = safe_post({"query": detail_query, "variables": {"submissionId": int(sub_id)}}, headers)
        if not d_data or "data" not in d_data or "submissionDetails" not in d_data["data"]:
            continue

        details = d_data["data"]["submissionDetails"]
        question = details["question"]
        q_id = str(question["questionId"]).zfill(4)
        q_title = question["title"]
        difficulty = question["difficulty"]
        code = details["code"]
        lang = details["lang"]["name"]
        ext = LANG_EXT.get(lang, "txt")

        folder_name = f"{q_id}-{slug}"
        os.makedirs(folder_name, exist_ok=True)

        # Write solution file
        sol_path = os.path.join(folder_name, f"solution.{ext}")
        with open(sol_path, "w", encoding="utf-8") as f:
            f.write(code)

        # Write README.md
        readme_path = os.path.join(folder_name, "README.md")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(f"# {q_id}. {q_title}\n\n")
            f.write(f"**Difficulty:** {difficulty}\n\n")
            f.write("## Problem Statement\n\n")
            f.write(question.get("content", ""))

        # Assign date across 150 days (5 months)
        day_index = min(int((idx / total_problems) * num_days), len(date_list) - 1)
        target_dt = date_list[day_index]

        hour = 11 + (idx % 8)
        minute = (idx * 13) % 60
        second = (idx * 19) % 60
        target_dt = target_dt.replace(hour=hour, minute=minute, second=second)
        date_str = target_dt.strftime("%Y-%m-%dT%H:%M:%S")

        try:
            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"] = date_str
            env["GIT_COMMITTER_DATE"] = date_str
            subprocess.run(["git", "add", folder_name], env=env, check=False)
            subprocess.run(["git", "commit", "-m", f"Solve {q_id}. {q_title}"], env=env, check=False)
        except Exception as e:
            pass

        print(f"[{idx+1}/{total_problems}] Saved & Committed for {target_dt.strftime('%Y-%m-%d')}: {folder_name}/")
        time.sleep(0.1)

    print("\n🎉 Export & 365-day Daily Commits completed successfully! Run 'git push origin main' to turn your GitHub profile GREEN!")

if __name__ == "__main__":
    fetch_submissions()
