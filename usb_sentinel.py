import os
import time
import json
from datetime import datetime

LOG_FILE = "usb_activity.log"
KNOWN_DRIVES = set()

def get_usb_drives():
    drives = set()

    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        drive = f"{letter}:\\"
        if os.path.exists(drive):
            drives.add(drive)

    return drives

def calculate_risk(connected_count):
    if connected_count >= 5:
        return "HIGH"
    elif connected_count >= 3:
        return "MEDIUM"
    return "LOW"

def log_event(event, drive):
    record = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "event": event,
        "drive": drive
    }

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(json.dumps(record) + "\n")

def display_event(event, drive, risk):
    print("\n" + "=" * 45)
    print("           USB SENTINEL")
    print("=" * 45)
    print(f"Event       : {event}")
    print(f"Drive       : {drive}")
    print(f"Time        : {datetime.now().strftime('%H:%M:%S')}")
    print(f"Risk Level  : {risk}")
    print("=" * 45)

def monitor_usb():
    global KNOWN_DRIVES

    KNOWN_DRIVES = get_usb_drives()

    print("=" * 45)
    print("        USB SENTINEL - ACTIVE")
    print("=" * 45)
    print("Monitoring connected drives...")
    print("Press Ctrl+C to stop.\n")

    while True:
        current_drives = get_usb_drives()

        connected = current_drives - KNOWN_DRIVES
        disconnected = KNOWN_DRIVES - current_drives

        for drive in connected:
            risk = calculate_risk(len(current_drives))
            log_event("CONNECTED", drive)
            display_event("USB CONNECTED", drive, risk)

        for drive in disconnected:
            log_event("DISCONNECTED", drive)
            display_event("USB DISCONNECTED", drive, "LOW")

        KNOWN_DRIVES = current_drives
        time.sleep(2)

if __name__ == "__main__":
    monitor_usb()
