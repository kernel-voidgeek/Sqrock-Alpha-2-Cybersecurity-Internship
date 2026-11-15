import whois
import socket
import requests


def osint_scan(domain):

    print("=" * 45)
    print("       PYTHON OSINT SCANNER")
    print("=" * 45)

    # 1. WHOIS lookup
    print("\n[1] WHOIS INFORMATION")

    try:
        data = whois.whois(domain)

        print("Domain:", domain)
        print("Registrar:", data.registrar)
        print("Creation Date:", data.creation_date)
        print("Expiry Date:", data.expiration_date)

    except Exception as e:
        print("WHOIS lookup failed:", e)

    # 2. DNS lookup
    print("\n[2] DNS INFORMATION")

    try:
        ip = socket.gethostbyname(domain)
        print("Domain:", domain)
        print("IP Address:", ip)

    except socket.gaierror:
        print("DNS lookup failed.")
        return

    # 3. IP Geolocation
    print("\n[3] IP GEOLOCATION")

    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url, timeout=10)
        geo = response.json()

        if geo.get("status") == "success":
            print("Country:", geo.get("country"))
            print("City:", geo.get("city"))
            print("ISP:", geo.get("isp"))
        else:
            print("Geolocation unavailable.")

    except requests.RequestException as e:
        print("Geolocation lookup failed:", e)

    print("\nOSINT SCAN COMPLETED")


osint_scan("example.com")