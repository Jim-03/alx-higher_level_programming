#!/usr/bin/python3
"""
Takes in a URL,
Sends a request,
Displays the response of the body.
"""

import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    # Incase of any errors
    try:
        # Handle the request
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as response:
            result = response.read()
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
    print(result.decode('utf-8'))
