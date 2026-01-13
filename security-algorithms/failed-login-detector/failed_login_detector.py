"""
Failed Login Detector

This script analyzes an authentication log file to identify IP addresses
that exceed a defined number of failed login attempts. This logic is commonly
used in intrusion detection and SOC monitoring environments.
"""

from collections import defaultdict

# Threshold for flagging suspicious behavior
FAILED_LOGIN_THRESHOLD = 5

# Dictionary to track failed login attempts per IP address
failed_attempts = defaultdict(int)

# Path to the log file
LOG_FILE = "sample_auth_log.txt"

try:
    with open(LOG_FILE, "r") as file:
        for line in file:
            # Expected log format: IP_ADDRESS STATUS
            # Example: 192.168.1.10 FAIL
            parts = line.strip().split()

            if len(parts) != 2:
                continue

            ip_address, status = parts

            # Count failed login attempts
            if status.upper() == "FAIL":
                failed_attempts[ip_address] += 1

except FileNotFoundError:
    print("Log file not found. Please check the file path.")
    exit(1)

# Output suspicious IPs
print("\nSuspicious IP addresses detected:")
for ip, count in failed_attempts.items():
    if count >= FAILED_LOGIN_THRESHOLD:
        print(f"{ip} → {count} failed login attempts")
