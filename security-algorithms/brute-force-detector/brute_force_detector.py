"""
Brute Force Login Detection Script
---------------------------------
This script analyzes authentication logs to detect potential
brute-force login attacks based on repeated failed login attempts
from the same IP address within a defined time window.

Author: Jose Varela
"""

from datetime import datetime, timedelta
from collections import defaultdict

# -------------------------------
# Configuration
# -------------------------------

LOG_FILE = "sample_auth_log.txt"

FAILED_ATTEMPT_THRESHOLD = 5          # Number of failed logins allowed
TIME_WINDOW_MINUTES = 10               # Time window for detection


# -------------------------------
# Helper Functions
# -------------------------------

def parse_log_line(line):
    """
    Parses a single log line into components.

    Expected format:
    YYYY-MM-DD HH:MM:SS IP_ADDRESS STATUS

    Example:
    2025-01-15 09:01:12 192.168.1.10 FAIL
    """
    try:
        timestamp_str, ip, status = (
            f"{line.split()[0]} {line.split()[1]}",
            line.split()[2],
            line.split()[3]
        )

        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        return timestamp, ip, status

    except (IndexError, ValueError):
        # Skip malformed log entries
        return None


# -------------------------------
# Main Detection Logic
# -------------------------------

def detect_brute_force():
    """
    Reads the log file and detects brute-force login attempts.
    """
    failed_attempts = defaultdict(list)
    alerts = []

    with open(LOG_FILE, "r") as log:
        for line in log:
            parsed = parse_log_line(line.strip())
            if not parsed:
                continue

            timestamp, ip, status = parsed

            # Only track failed login attempts
            if status == "FAIL":
                failed_attempts[ip].append(timestamp)

                # Remove attempts outside the time window
                window_start = timestamp - timedelta(minutes=TIME_WINDOW_MINUTES)
                failed_attempts[ip] = [
                    t for t in failed_attempts[ip] if t >= window_start
                ]

                # Check if threshold is exceeded
                if len(failed_attempts[ip]) >= FAILED_ATTEMPT_THRESHOLD:
                    alerts.append({
                        "ip": ip,
                        "attempts": len(failed_attempts[ip]),
                        "last_attempt": timestamp
                    })

    return alerts


# Output the results

def main():
    alerts = detect_brute_force()

    if not alerts:
        print("No brute-force activity detected.")
    else:
        print("Potential Brute-Force Attack Detected!!! \n")
        for alert in alerts:
            print(f"IP Address: {alert['ip']}")
            print(f"Failed Attempts: {alert['attempts']}")
            print(f"Last Attempt: {alert['last_attempt']}")
            print("-" * 40)


if __name__ == "__main__":
    main()
