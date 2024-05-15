#!/usr/bin/python3
"""Takes in a url
sends a request to the url
displays body response
prints error codes equal to or above 400.
"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: ", r.status_code)
    else:
        print(r.text)
