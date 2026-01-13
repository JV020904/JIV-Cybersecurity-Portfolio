# Failed Login Detection Algorithm
#By: Jose Varela
#Date: August 11, 2025

## Description
This Python script analyzes authentication logs to identify IP addresses
that exceed a defined threshold of failed login attempts. This type of
analysis is commonly used in SOC environments to detect brute-force attacks
and unauthorized access attempts.

## How It Works
- Reads login data from a log file
- Counts failed login attempts per IP address
- Flags IPs that exceed a defined threshold

## Why This Matters
Repeated failed login attempts are a common indicator of:
- Brute-force attacks
- Credential stuffing
- Unauthorized access attempts

Automating this detection reduces response time and improves security posture.

## How to Run
```bash
python3 failed_login_detector.py
