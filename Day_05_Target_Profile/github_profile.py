
import requests
import json


BASE_URL = "https://api.github.com"


def github_profile(username):

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "Sqrock-OSINT-Lab"
    }

    print("\n[*] Collecting public GitHub information...")

    try:
        # Fetch public profile
        profile_response = requests.get(
            f"{BASE_URL}/users/{username}",
            headers=headers,
            timeout=10
        )

        profile_response.raise_for_status()
        user = profile_response.json()

        # Fetch public repositories
        repo_response = requests.get(
            f"{BASE_URL}/users/{username}/repos",
            headers=headers,
            params={"per_page": 10, "sort": "updated"},
            timeout=10
        )

        repo_response.raise_for_status()
        repos = repo_response.json()

        # Count programming languages
        languages = {}

        for repo in repos:
            language = repo.get("language")

            if language:
                languages[language] = (
                    languages.get(language, 0) + 1
                )

        # Build public profile
        result = {
            "username": user.get("login"),
            "name": user.get("name"),
            "company": user.get("company"),
            "location": user.get("location"),
            "bio": user.get("bio"),
            "public_repos": user.get("public_repos"),
            "top_languages_in_recent_repos": languages
        }

        # Save JSON report
        with open("profile.json", "w", encoding="utf-8") as file:
            json.dump(result, file, indent=4)

        print("\n[+] PROFILE GENERATED")
        print(json.dumps(result, indent=4))
        print("\n[+] Saved to profile.json")

    except requests.exceptions.HTTPError as error:
        print("GitHub API error:", error)

    except requests.exceptions.RequestException as error:
        print("Network error:", error)


# Use your own GitHub username or an authorized
# public organization account for this lab.
username = input("Enter github username: ").strip()

if username:
    github_profile(username)
else:
    print("Please enter a valid username.")
