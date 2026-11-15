
import platform
import socket
import datetime
import os

def usb_payload_sim(output_file="recon_log.txt"):

    print("=" * 50)
    print("       USB DROP ATTACK SIMULATION")
    print("=" * 50)

    # Collect basic local system information
    info = {
        "timestamp": str(datetime.datetime.now()),
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "version": platform.version(),
        "user": os.getenv("USERNAME") or os.getenv("USER"),
        "cwd": os.getcwd()
    }

    # Save information locally
    with open(output_file, "w") as file:
        for key, value in info.items():
            file.write(f"{key}: {value}\n")

    print("\n[+] SYSTEM INFORMATION COLLECTED")

    for key, value in info.items():
        print(f"{key}: {value}")

    print("\n[SIM] Recon data saved to", output_file)
    print("\nSIMULATION COMPLETED")
    print("No data was transmitted.")

usb_payload_sim()
