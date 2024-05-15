#!/usr/bin/python3
""" Fetches from a url but using requests library."""

import requests


if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(r))
    print("\t- content:", r.content)
