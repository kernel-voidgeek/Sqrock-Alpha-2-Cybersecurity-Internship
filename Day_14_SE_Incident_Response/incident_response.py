
import datetime
import json


def ir_response(incident):

    print("=" * 55)
    print("       SOCIAL ENGINEERING INCIDENT RESPONSE")
    print("=" * 55)

    print("\n[+] INCIDENT RESPONSE TRIGGERED")
    print("Time     :", datetime.datetime.now())
    print("Type     :", incident["type"])
    print("Severity :", incident["severity"])
    print("User     :", incident["user"])

    actions = []

    # High severity containment
    if incident["severity"] in ("HIGH", "CRITICAL"):

        actions += [
            "SIMULATE: Lock user account",
            "SIMULATE: Revoke active sessions",
            "Notify SOC team",
            "Preserve email logs"
        ]

    # Phishing-specific response
    if incident["type"].lower() == "phishing":

        actions += [
            "SIMULATE: Quarantine suspicious email",
            "SIMULATE: Block sender domain",
            "Scan attachments in sandbox"
        ]

    print("\n[ACTIONS TAKEN]")

    for action in actions:
        print("[+] " + action)

    # Generate incident report
    report = {
        "incident": incident,
        "actions": actions,
        "timestamp": str(datetime.datetime.now()),
        "status": "SIMULATED RESPONSE COMPLETED"
    }

    with open("ir_report.json", "w") as file:
        json.dump(report, file, indent=4)

    # Generate terminal summary
    with open("output.txt", "w") as file:
        file.write("DAY 14 - INCIDENT RESPONSE SUMMARY\n\n")
        file.write(f"Incident Type: {incident['type']}\n")
        file.write(f"Severity: {incident['severity']}\n")
        file.write(f"Affected User: {incident['user']}\n")
        file.write("\nActions:\n")

        for action in actions:
            file.write("- " + action + "\n")

        file.write("\nStatus: SIMULATED RESPONSE COMPLETED\n")

    print("\n" + "=" * 55)
    print("[+] JSON report saved: ir_report.json")
    print("[+] Summary saved: output.txt")
    print("[+] INCIDENT RESPONSE COMPLETED")


# Fictional training incident
sample_incident = {
    "type": "phishing",
    "severity": "HIGH",
    "user": "riya@example.test"
}

if __name__ == "__main__":
    ir_response(sample_incident)
