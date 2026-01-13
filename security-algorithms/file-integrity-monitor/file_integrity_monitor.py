"""
File Integrity Monitor

This script calculates and compares SHA-256 hashes to detect unauthorized
file modifications. File integrity monitoring is commonly used to detect
tampering with configuration files or critical system assets.

"""

import hashlib
import os

def calculate_hash(file_path):
    """
    Calculate the SHA-256 hash of a file.
    """
    hasher = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

# Files to monitor for integrity changes
files_to_monitor = ["important_config.txt"]

# Store baseline hashes
baseline_hashes = {}

for file in files_to_monitor:
    if os.path.exists(file):
        baseline_hashes[file] = calculate_hash(file)

print("Baseline file hashes recorded.\n")

# Compare current hashes to baseline
for file, baseline_hash in baseline_hashes.items():
    current_hash = calculate_hash(file)
    if current_hash != baseline_hash:
        print(f"[ALERT] File modification detected: {file}")
    else:
        print(f"[OK] No changes detected for: {file}")
