
from flask import Flask, request
from datetime import datetime, timedelta

app = Flask(__name__)

# Fictional credentials for this local training lab
USERNAME = "admin"
PASSWORD = "lab-demo-2026"

MAX_ATTEMPTS = 3
LOCKOUT_SECONDS = 60

# Store failed attempts and lockout expiry by client IP
failed_attempts = {}
locked_until = {}


@app.route("/")
def home():
    return "Day 7 Local Login Security Lab"


@app.route("/login", methods=["POST"])
def login():

    ip = request.remote_addr
    now = datetime.now()

    # Check whether this IP is temporarily locked
    if ip in locked_until:
        if now < locked_until[ip]:
            remaining = int((locked_until[ip] - now).total_seconds())
            return f"Rate limited. Try again in {remaining}s.", 429
        else:
            locked_until.pop(ip, None)
            failed_attempts[ip] = 0

    username = request.form.get("username", "")
    password = request.form.get("password", "")

    # Check the fictional lab credentials
    if username == USERNAME and password == PASSWORD:
        failed_attempts[ip] = 0
        return "Welcome! Login successful.", 200

    # Record failed login
    failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    print(
        f"[ALERT] Failed login from {ip} "
        f"Attempt: {failed_attempts[ip]}"
    )

    # Apply temporary lockout
    if failed_attempts[ip] >= MAX_ATTEMPTS:
        locked_until[ip] = now + timedelta(
            seconds=LOCKOUT_SECONDS
        )

        return "Too many failed attempts. Access temporarily blocked.", 429

    return "Invalid username or password.", 401


if __name__ == "__main__":
    print("DAY 7 - LOCAL LOGIN SECURITY LAB")
    print("Server running at http://127.0.0.1:5000")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
