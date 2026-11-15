
from datetime import datetime

# FICTIONAL TRAINING DATA ONLY
# These messages are drafts for awareness training.
# They are not sent to anyone.

TARGETS = [
    {
        "name": "Riya Sharma",
        "email": "riya@example.test",
        "company": "Sqrock Training",
        "hook": "a scheduled security-awareness exercise",
        "scenario": "IT account security awareness"
    },
    {
        "name": "Arjun Patel",
        "email": "arjun@example.test",
        "company": "Example Finance",
        "hook": "a fictional invoice review exercise",
        "scenario": "Finance department awareness"
    },
    {
        "name": "Neha Shah",
        "email": "neha@example.test",
        "company": "Example HR",
        "hook": "a simulated employee-policy update",
        "scenario": "HR security awareness"
    }
]


def spear_phish_template(target):

    email = f"""
==================================================
       SECURITY AWARENESS SIMULATION
==================================================

Simulation only — NOT FOR DELIVERY

From (simulated):
[Training IT Security] <training@example.test>

To:
{target['email']}

Subject:
Security Awareness Exercise - {target['company']}

Scenario:
{target['scenario']}

Hello {target['name']},

This is a fictional security-awareness exercise
for {target['company']}.

Context:
This training example refers to {target['hook']}.

Training link:
https://awareness.example.invalid/test

Please do not enter credentials or personal
information. This link is a non-functional
reserved test address.

Regards,
Security Awareness Training Team

--------------------------------------------------
Personalization hook: {target['hook']}
--------------------------------------------------
"""

    return email


def main():

    print("=" * 55)
    print("     SPEAR PHISHING AWARENESS TEMPLATE ENGINE")
    print("=" * 55)

    all_drafts = []

    for target in TARGETS:

        draft = spear_phish_template(target)

        print(draft)
        all_drafts.append(draft)

    with open("drafts.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(all_drafts))

    print("\n[+] THREE TRAINING DRAFTS GENERATED")
    print("[+] Saved to drafts.txt")
    print("[+] No emails were sent.")

    with open("output.txt", "w", encoding="utf-8") as file:
        file.write("Execution completed: " +
                   datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        file.write("\nThree awareness drafts generated successfully.")


if __name__ == "__main__":
    main()
