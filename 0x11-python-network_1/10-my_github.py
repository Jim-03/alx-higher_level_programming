#!/usr/bin/python3
"""Takes in username and password
uses github api to display id.
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(
            f"https://api.github.com/users/{sys.argv[1]}",
            headers={"Authorization": f"token {sys.argv[2]}"}
            )

    print(r.json()["id"])
