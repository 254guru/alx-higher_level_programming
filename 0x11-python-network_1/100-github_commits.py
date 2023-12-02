#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository
"rails" by the user "rails"
You must use the GitHub API
Print all commits by: `<sha>: <author name>` (one by line)
"""
import requests
import sys


if __name__ == "__main__":
    commit_format = "{}: {}"
    api_url = "https://api.github.com/repos/{}/{}/commits"
    formatted_url = api_url.format(argv[2], argv[1])

    response = requests.get(formatted_url)

    if response.status_code == 200:
        count = 0
        for commit in response.json():
            if count < 10:
                sha = commit.get("sha")
                author_name = commit.get("commit").get("author").get("name")
                print(commit_format.format(sha, author_name))
                count += 1
    else:
        print("Failed to fetch commits. Check repository and owner names.")
