
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import json
import os

LOG_FILE = "honeypot_logs.json"


class HoneyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        entry = {
            "timestamp": str(datetime.now()),
            "ip": self.client_address[0],
            "path": self.path,
            "user_agent": self.headers.get("User-Agent", "Unknown")
        }

        # Save each visit locally
        logs = []

        if os.path.exists(LOG_FILE):
            try:
                with open(LOG_FILE, "r") as file:
                    logs = json.load(file)
            except (json.JSONDecodeError, OSError):
                logs = []

        logs.append(entry)

        with open(LOG_FILE, "w") as file:
            json.dump(logs, file, indent=4)

        print("\n[HONEYPOT ALERT]")
        print(json.dumps(entry, indent=4))

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        response = """
        <html>
        <body>
            <h2>Security Awareness Lab</h2>
            <p>Simulated bait link accessed.</p>
            <p>This is a harmless local training exercise.</p>
        </body>
        </html>
        """

        self.wfile.write(response.encode())

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8080), HoneyHandler)

    print("=" * 50)
    print("       DAY 10 - LOCAL HONEYPOT TRACKER")
    print("=" * 50)
    print("Server running at http://127.0.0.1:8080")
    print("Open the local training link in your browser.")
    print("Press CTRL+C to stop the server.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[+] Honeypot server stopped.")
        server.server_close()
