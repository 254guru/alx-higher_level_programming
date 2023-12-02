#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
import sys


if len(sys.argv) < 3:
    print("Usage: python script_name.py <username> <token>")
    sys.exit(1)

username = sys.argv[1]
token = sys.argv[2]

url = 'https://api.github.com/user'

response = requests.get(url, auth=(username, token))

if response.status_code == 200:
    user_info = response.json()
    print(f"Your GitHub user ID is: {user_info['id']}")
else:
    print("Failed to fetch user information. Check your credentials.")
