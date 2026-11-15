import re
from urllib.parse import urlparse

KEYWORDS = [
    "login",
    "verify",
    "secure",
    "update",
    "account",
    "bank",
    "paypal"
]


def phish_score(url):

    p = urlparse(url)
    score = 0

    # Check HTTPS
    if not url.startswith("https"):
        score += 30

    # Check suspicious keywords in domain
    for kw in KEYWORDS:
        if kw in p.netloc.lower():
            score += 20

    # Check excessive subdomains
    if p.netloc.count(".") > 3:
        score += 25

    # Check IP address in domain
    if re.search(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
        p.netloc
    ):
        score += 40

    return min(score, 100)


# Ten test URLs
urls = [
    "https://github.com",
    "https://www.wikipedia.org",
    "http://example.com",
    "https://paypal-login.evil.com/verify",
    "http://secure-account-update.example.com",
    "https://192.168.1.10/login",
    "http://192.168.1.10",
    "https://login.verify.secure.account.bank.paypal.example.com",
    "http://support.microsoft.com",
    "https://accounts.google.com"
]

print("=" * 55)
print("          PYTHON PHISHING URL DETECTOR")
print("=" * 55)

for url in urls:

    score = phish_score(url)

    if score >= 70:
        status = "HIGH RISK"
    elif score >= 40:
        status = "MEDIUM RISK"
    else:
        status = "LOW RISK"

    print(f"\nURL: {url}")
    print(f"Risk Score: {score}/100")
    print(f"Status: {status}")

print("\nSCAN COMPLETED")