#!/usr/bin/python3
import sys
import urllib.request
""" Module takes in a url, sends arequest and displays data from the header."""


url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    x_id = response.getheader('X-Request-Id')
print(x_id)
