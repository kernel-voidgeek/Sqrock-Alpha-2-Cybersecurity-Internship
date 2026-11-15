
def generate_vishing_script(target_company, attacker_role, pretext,
                            psychological_triggers):

    script = f"""
====================================================
          VISHING AWARENESS TRAINING
====================================================

Organization : {target_company}
Impersonated Role : {attacker_role}
Scenario : {pretext}

[EXAMPLE CALL]

Caller:
"Hello, I am calling from {attacker_role} at
{target_company}. We noticed an unusual account
activity alert."

Caller pressure tactic:
"The issue needs attention immediately."

[WARNING SIGNS]
1. Unexpected contact claiming authority.
2. Pressure to act immediately.
3. Request for confidential information.
4. Attempt to bypass official verification.

[SAFE RESPONSE]
"I will not share passwords, OTPs or personal
information over an unexpected call. I will
contact the organization using its official
website or verified phone number."

[PSYCHOLOGICAL TRIGGERS]
{psychological_triggers}

[DEFENSIVE LESSON]
Never trust caller identity based only on their
claims. Verify independently using official
communication channels.

====================================================
"""
    return script


scenarios = [
    {
        "company": "Sqrock Training Lab",
        "role": "IT Support",
        "pretext": "Unusual account activity",
        "triggers": "Authority, Fear, Urgency"
    },
    {
        "company": "Example Bank Training Lab",
        "role": "Bank Representative",
        "pretext": "Suspicious banking transaction",
        "triggers": "Authority, Fear, Urgency"
    },
    {
        "company": "Public Services Training Lab",
        "role": "Government Officer",
        "pretext": "Fictional document verification notice",
        "triggers": "Authority, Fear, Scarcity"
    }
]


print("\nGENERATING THREE AWARENESS SCENARIOS...\n")

for scenario in scenarios:

    result = generate_vishing_script(
        scenario["company"],
        scenario["role"],
        scenario["pretext"],
        scenario["triggers"]
    )

    print(result)


print("\nALL THREE TRAINING SCENARIOS GENERATED.")
