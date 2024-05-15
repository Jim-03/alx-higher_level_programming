#!/usr/bin/python3
""" Takes in a url,
sends a request
displays the header id.
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers["X-Request-Id"])
