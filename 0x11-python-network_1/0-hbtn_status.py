#!/usr/bin/python3
"""
fetches a link
"""


import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')

        # Displaying the body of the response with tabulation before each line
        lines = body.split('\n')
        for line in lines:
            print(f"\t- {line}")
