import requests
import re


def harvest_emails(url):

    print("=" * 40)
    print("       EMAIL HARVESTER")
    print("=" * 40)

    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status()

        html = response.text

        # Find email addresses using Regex
        emails = set(
            re.findall(
                r'[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}',
                html
            )
        )

        print("\n[+] Emails Found:")

        if emails:
            for email in sorted(emails):
                print(email)
        else:
            print("No email addresses found.")

        print("\nTotal Unique Emails:", len(emails))

        return emails

    except requests.RequestException as error:
        print("Error:", error)
        return set()


harvest_emails("http://127.0.0.1:8000/test_page.html")