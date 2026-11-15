
import json
from datetime import datetime

QUESTIONS = [
    {
        "q": "An email asks you to verify your password through a link. What should you do?",
        "opts": [
            "A) Click the link",
            "B) Contact IT through an official channel",
            "C) Reply with your password"
        ],
        "ans": "B",
        "exp": "Never share passwords through email links. Verify independently."
    },
    {
        "q": "You find an unknown USB drive in a parking lot. What should you do?",
        "opts": [
            "A) Plug it into your laptop",
            "B) Give it to security or IT",
            "C) Take it home"
        ],
        "ans": "B",
        "exp": "Unknown USB devices can be used for baiting attacks."
    },
    {
        "q": "Someone calls claiming to be your bank and asks for your OTP.",
        "opts": [
            "A) Share the OTP",
            "B) Ask them to wait",
            "C) Refuse and contact the bank officially"
        ],
        "ans": "C",
        "exp": "Never share OTPs, even with someone claiming to be bank staff."
    },
    {
        "q": "A message says your account will be deleted in 10 minutes unless you click a link.",
        "opts": [
            "A) Click immediately",
            "B) Verify through the official website",
            "C) Forward it to friends"
        ],
        "ans": "B",
        "exp": "Urgency and fear are common social engineering tactics."
    },
    {
        "q": "A stranger requests your company's internal login details.",
        "opts": [
            "A) Share them",
            "B) Verify their identity and refuse unauthorized requests",
            "C) Send a screenshot"
        ],
        "ans": "B",
        "exp": "Confidential credentials must never be shared with unauthorized people."
    },
    {
        "q": "You receive an unexpected invoice attachment from an unknown sender.",
        "opts": [
            "A) Open it immediately",
            "B) Verify the sender and report suspicious email",
            "C) Download it on your work computer"
        ],
        "ans": "B",
        "exp": "Unexpected attachments may contain malicious files."
    },
    {
        "q": "A person follows you into a restricted office without an access card.",
        "opts": [
            "A) Let them enter",
            "B) Politely follow access procedures and notify security",
            "C) Give them your access card"
        ],
        "ans": "B",
        "exp": "Tailgating is a physical social engineering technique."
    },
    {
        "q": "A social media account impersonates your company manager and requests money.",
        "opts": [
            "A) Transfer the money",
            "B) Verify using a known official contact method",
            "C) Share company details"
        ],
        "ans": "B",
        "exp": "Verify unusual financial requests through a separate trusted channel."
    },
    {
        "q": "A pop-up claims your computer is infected and asks you to call a number.",
        "opts": [
            "A) Call the displayed number",
            "B) Install whatever it recommends",
            "C) Close it and contact official IT support"
        ],
        "ans": "C",
        "exp": "Fake technical support alerts often use fear to manipulate users."
    },
    {
        "q": "You accidentally click a suspicious link at work. What should you do?",
        "opts": [
            "A) Hide the incident",
            "B) Report it immediately to IT/security",
            "C) Forward the link to colleagues"
        ],
        "ans": "B",
        "exp": "Prompt reporting helps security teams investigate and reduce damage."
    }
]


def run_quiz():
    score = 0
    results = []

    print("=" * 55)
    print("       SOCIAL ENGINEERING AWARENESS QUIZ")
    print("=" * 55)

    name = input("\nEnter your name: ").strip()

    for i, question in enumerate(QUESTIONS, 1):
        print(f"\nQ{i}. {question['q']}")

        for option in question["opts"]:
            print(option)

        answer = input("Your answer (A/B/C): ").strip().upper()

        while answer not in ["A", "B", "C"]:
            answer = input("Enter A, B or C: ").strip().upper()

        correct = answer == question["ans"]

        if correct:
            print("[+] CORRECT!")
            score += 1
        else:
            print("[-] INCORRECT!")

        print("Explanation:", question["exp"])

        results.append({
            "question_number": i,
            "your_answer": answer,
            "correct_answer": question["ans"],
            "result": "Correct" if correct else "Incorrect",
            "explanation": question["exp"]
        })

    percentage = round((score / len(QUESTIONS)) * 100, 2)

    report = {
        "participant": name,
        "date": str(datetime.now()),
        "total_questions": len(QUESTIONS),
        "correct_answers": score,
        "incorrect_answers": len(QUESTIONS) - score,
        "percentage": percentage,
        "results": results
    }

    with open("score_report.json", "w") as file:
        json.dump(report, file, indent=4)

    with open("output.txt", "w") as file:
        file.write("DAY 11 - SOCIAL ENGINEERING AWARENESS QUIZ\n\n")
        file.write(f"Participant: {name}\n")
        file.write(f"Score: {score}/{len(QUESTIONS)}\n")
        file.write(f"Percentage: {percentage}%\n")
        file.write(f"Correct: {score}\n")
        file.write(f"Incorrect: {len(QUESTIONS)-score}\n")

    print("\n" + "=" * 55)
    print("                 QUIZ COMPLETED")
    print("=" * 55)
    print(f"Participant: {name}")
    print(f"Final Score: {score}/{len(QUESTIONS)}")
    print(f"Percentage: {percentage}%")
    print("[+] Score report saved to score_report.json")
    print("[+] Summary saved to output.txt")


if __name__ == "__main__":
    run_quiz()
