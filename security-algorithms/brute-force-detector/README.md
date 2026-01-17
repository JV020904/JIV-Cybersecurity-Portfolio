# Brute-Force Login Detection (Time Window Analysis)

## Overview

This project simulates SIEM-style brute-force detection logic by analyzing
authentication logs for repeated failed login attempts from the same IP address
within a defined time window.

The goal is to identify potential brute-force attacks using realistic
security monitoring techniques.


## How It Works

1. Reads authentication log entries from a file
2. Parses timestamps, IP addresses, and login status
3. Tracks failed login attempts per IP address
4. Applies a sliding time window to remove outdated attempts
5. Triggers alerts when a threshold is exceeded


## Detection Rules

- **Threshold:** 5 failed login attempts
- **Time Window:** 10 minutes
- **Condition:** Same IP exceeding threshold within the time window



