#!/usr/bin/python3
""" Takes in a url,
sends post request
and displays the body.
"""
import urllib.request
import urllib.parse
import sys


value ={'email': sys.argv[2]}  # Variable for post request
# Encode the value in a standard format
data = urllib.parse.urlencode(value)
data = data.encode('ascii')  # Data in bytes
# Handle a request
req = urllib.request.Request(sys.argv[1])  # Parameter contains url from command line
# Connect and disconnect after making a request
with urllib.request.openurl(req) as response:
    # Read the body
    result = response.read()
print(result.decode('utf-8'))