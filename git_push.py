#!/usr/bin/env python3
import subprocess
import os

# Disable git terminal prompts
os.environ['GIT_TERMINAL_PROMPT'] = '0'

def run_git_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        print(f"Command: {command}")
        print(f"Return code: {result.returncode}")
        print(f"Output: {result.stdout}")
        print(f"Error: {result.stderr}")
        print("-" * 50)
        return result.returncode == 0
    except Exception as e:
        print(f"Error running {command}: {e}")
        return False

# Commands to run
commands = [
    "git add .",
    'git commit -m "fix: mensaje de éxito corregido - consistencia RealTREM"',
    "git push origin main"
]

for cmd in commands:
    if not run_git_command(cmd):
        print(f"Failed to execute: {cmd}")
        break