
import re
from collections import Counter
from datetime import datetime

LOG_FILE = "sample_logs.txt"
OUTPUT_FILE = "output.txt"
ALERT_FILE = "alert_report.txt"

def analyze_logs(logs):

    alerts = []

    # Detect failed login attempts
    failures = re.findall(
        r'FAILED_LOGIN user=(\w+) ip=([\d.]+)',
        logs
    )

    # Detect email forwarding rules
    rules = re.findall(
        r'EMAIL_RULE_CREATED user=(\w+) rule=(\S+)',
        logs
    )

    # Count failed attempts per user
    fail_counts = Counter(
        (user, ip) for user, ip in failures
    )

    print("\nFAILED LOGIN ANALYSIS")

    for (user, ip), count in fail_counts.items():

        print(f"User: {user}")
        print(f"IP: {ip}")
        print(f"Failed attempts: {count}")

        if count >= 3:
            alert = (
                f"[HIGH ALERT] Possible brute-force activity: "
                f"{user} from {ip} ({count} failures)"
            )
            alerts.append(alert)
            print(alert)

    # Detect suspicious email rules
    print("\nEMAIL RULE ANALYSIS")

    for user, rule in rules:

        alert = (
            f"[HIGH ALERT] Suspicious email rule created "
            f"by {user}: {rule}"
        )

        alerts.append(alert)
        print(alert)

    return alerts


def main():

    print("=" * 55)
    print("       SIEM LOG ANALYSIS SYSTEM")
    print("=" * 55)

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            logs = file.read()

    except FileNotFoundError:
        print("[ERROR] sample_logs.txt not found!")
        return

    alerts = analyze_logs(logs)

    report = []
    report.append("DAY 13 - SIEM LOG ANALYSIS REPORT")
    report.append(f"Analysis time: {datetime.now()}")
    report.append("")

    report.append("Total log entries: " +
                  str(len(logs.strip().splitlines())))

    report.append("Total failed login events: " +
                  str(logs.count("FAILED_LOGIN")))

    report.append("Total suspicious email rules: " +
                  str(logs.count("EMAIL_RULE_CREATED")))

    report.append("")
    report.append("SECURITY ALERTS")

    if alerts:
        report.extend(alerts)
    else:
        report.append("No alerts detected.")

    report_text = "\n".join(report)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(report_text)

    with open(ALERT_FILE, "w", encoding="utf-8") as file:
        file.write(report_text)

    print("\n" + "=" * 55)
    print("ANALYSIS COMPLETED")
    print(f"Total alerts: {len(alerts)}")
    print("[+] Saved to output.txt")
    print("[+] Saved to alert_report.txt")


if __name__ == "__main__":
    main()
