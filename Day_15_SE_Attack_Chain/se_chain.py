
import os

from modules import osint
from modules import profile
from modules import phish
from modules import template
from modules import ir


MODULES = {
    "1": ("OSINT Scanner", osint.run),
    "2": ("Profile Builder", profile.run),
    "3": ("Phishing URL Scorer", phish.run),
    "4": ("Awareness Email Generator", template.run),
    "5": ("Incident Response", ir.run)
}


def menu():

    os.makedirs("reports", exist_ok=True)

    while True:

        print("\n" + "=" * 50)
        print("          SE ATTACK CHAIN SIMULATOR")
        print("=" * 50)

        print("[1] OSINT Scanner")
        print("[2] Profile Builder")
        print("[3] Phishing URL Scorer")
        print("[4] Awareness Email Generator")
        print("[5] Incident Response")
        print("[0] Exit")

        choice = input("\nSelect module: ").strip()

        if choice == "0":
            print("\n[+] SIMULATOR CLOSED")
            break

        if choice in MODULES:

            name, function = MODULES[choice]

            print(f"\n[+] Launching {name}...")

            try:
                function()
            except Exception as error:
                print("[ERROR]", error)

        else:
            print("[!] Invalid choice.")

        input("\nPress Enter to return to menu...")


if __name__ == "__main__":
    menu()
