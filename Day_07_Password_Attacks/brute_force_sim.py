
import requests

URL = "http://127.0.0.1:5000/login"
USERNAME = "admin"

# Small fictional test wordlist
WORDLIST = [
    "123456",
    "password",
    "qwerty",
    "letmein",
    "lab-demo-2026"
]


def brute_force_sim(url, username, wordlist):

    print("=" * 50)
    print("     LOCAL PASSWORD SECURITY SIMULATOR")
    print("=" * 50)

    for password in wordlist:

        try:
            response = requests.post(
                url,
                data={
                    "username": username,
                    "password": password
                },
                timeout=5
            )

            if response.status_code == 429:
                print("[BLOCKED] Rate limit detected!")
                print("[!] Further attempts stopped.")
                break

            elif response.status_code == 200:
                print("[+] Login successful in local lab.")
                break

            else:
                print(f"[-] Failed attempt: {password}")

        except requests.RequestException as error:
            print("[ERROR]", error)
            break

    print("\nSIMULATION COMPLETED")
    print("Only the local training server was tested.")


if __name__ == "__main__":
    brute_force_sim(URL, USERNAME, WORDLIST)
