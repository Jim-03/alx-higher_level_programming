#!/usr/bin/python3
""" Takes in a url,
sends post request
and displays the body.
"""


import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    value = {'email': sys.argv[2]}  # Variable for post request
    # Encode the value in a standard format
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')  # Data in bytes
    # Handle a request
    # Parameter contains url from command line
    req = urllib.request.Request(sys.argv[1], data=data, method='POST')
    # Connect and disconnect after making a request
    with urllib.request.urlopen(req) as response:
        # Read the body
        result = response.read()
    print(result.decode('utf-8'))
