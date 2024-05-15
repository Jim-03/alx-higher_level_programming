#!/usr/bin/python3
""" Module takes in a url,
sends a request
and displays id from the header.
"""
import sys
import urllib.request


url = sys.argv[1]  # The url argument
req = urllib.request.Request(url)  # Request Handler
# Make the request with resource closing at the end
with urllib.request.urlopen(req) as response:
    x_id = response.getheader('X-Request-Id')  # The reponse id
print(x_id)  # Print the id
