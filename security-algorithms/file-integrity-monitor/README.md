# File Integrity Monitoring Algorithm
#By: Jose Varela
#Date: October 4, 2025
## Description
This script detects unauthorized changes to monitored files by comparing
cryptographic hash values. File integrity monitoring is a core security
control in intrusion detection and compliance frameworks.

## How It Works
- Generates a baseline SHA-256 hash for each file
- Recalculates hashes during execution
- Alerts when changes are detected

## Why This Matters
Unauthorized file changes may indicate:
- Malware activity
- Privilege escalation
- Insider threats

## How to Run
```bash
python3 file_integrity_monitor.py
