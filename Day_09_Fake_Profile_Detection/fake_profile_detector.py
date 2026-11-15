import json

def fake_profile_score(profile):
    score = 0

    age_days = profile.get("account_age_days", 365)
    followers = profile.get("followers", 1)
    following = profile.get("following", 1)

    ratio = following / max(followers, 1)

    if age_days < 30:
        score += 30

    if ratio > 10:
        score += 25

    if profile.get("no_profile_pic"):
        score += 20

    if profile.get("posts", 100) < 5:
        score += 15

    if profile.get("default_bio"):
        score += 10

    return min(score, 100)


profiles = [
    {
        "username": "user_001",
        "account_age_days": 7,
        "followers": 2,
        "following": 900,
        "no_profile_pic": True,
        "posts": 1,
        "default_bio": True
    },
    {
        "username": "user_002",
        "account_age_days": 1200,
        "followers": 4500,
        "following": 320,
        "no_profile_pic": False,
        "posts": 870,
        "default_bio": False
    },
    {
        "username": "user_003",
        "account_age_days": 15,
        "followers": 20,
        "following": 600,
        "no_profile_pic": False,
        "posts": 3,
        "default_bio": True
    },
    {
        "username": "user_004",
        "account_age_days": 400,
        "followers": 100,
        "following": 150,
        "no_profile_pic": True,
        "posts": 25,
        "default_bio": False
    },
    {
        "username": "user_005",
        "account_age_days": 2000,
        "followers": 3000,
        "following": 200,
        "no_profile_pic": False,
        "posts": 500,
        "default_bio": False
    }
]

print("=" * 50)
print("       FAKE PROFILE DETECTION SYSTEM")
print("=" * 50)

results = []

for profile in profiles:
    score = fake_profile_score(profile)

    if score >= 70:
        status = "HIGH RISK"
    elif score >= 40:
        status = "MEDIUM RISK"
    else:
        status = "LOW RISK"

    result = {
        "username": profile["username"],
        "score": score,
        "status": status
    }

    results.append(result)

    print(f"\nProfile: {profile['username']}")
    print(f"Fake Score: {score}/100")
    print(f"Status: {status}")

with open("output.txt", "w") as file:
    file.write("DAY 9 - FAKE PROFILE DETECTION\n\n")
    file.write(json.dumps(results, indent=4))

print("\n[+] Analysis saved to output.txt")
print("[+] SCAN COMPLETED")
