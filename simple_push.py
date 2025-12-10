#!/usr/bin/env python3
import subprocess
import os

os.environ['GIT_TERMINAL_PROMPT'] = '0'

# Add all changes
result = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
print("Git add completed:", result.returncode)

# Commit changes
result = subprocess.run(['git', 'commit', '-m', 'fix: mensaje de exito corregido - consistencia RealTREM'], 
                       capture_output=True, text=True)
print("Git commit completed:", result.returncode)
if result.stderr:
    print("Commit error:", result.stderr)

# Push to origin
result = subprocess.run(['git', 'push', 'origin', 'main'], 
                       capture_output=True, text=True)
print("Git push completed:", result.returncode)
if result.stderr:
    print("Push error:", result.stderr)
if result.stdout:
    print("Push output:", result.stdout)