#!/usr/bin/python3
"""
fetches a link
"""

import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)

if response.status_code == 200:
    body = response.text
    lines = body.split('\n')
    for line in lines:
        print(f"\t- {line}")
else:
    print(f"Failed to fetch the URL. Status code: {response.status_code}")
