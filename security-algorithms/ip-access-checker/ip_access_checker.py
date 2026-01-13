"""
IP Access Checker

This script simulates basic allow-list access control logic.
It demonstrates how IP-based filtering can be used to restrict
access to trusted sources.
"""

# Define allowed IP addresses
ALLOWED_IPS = {
    "192.168.1.10",
    "10.0.0.5"
}

def check_ip_access(ip_address):
    """
    Check whether an IP address is authorized.
    """
    if ip_address in ALLOWED_IPS:
        return "ACCESS GRANTED"
    return "ACCESS DENIED"

# Test IP addresses
test_ips = [
    "192.168.1.10",
    "8.8.8.8"
]

for ip in test_ips:
    print(f"{ip}: {check_ip_access(ip)}")
