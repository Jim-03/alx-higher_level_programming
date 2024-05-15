#!/usr/bin/python3
import urllib.request
""" Fetches from an internet resource."""


url = 'https://alx-intranet.hbtn.io/status'  # The url
req = urllib.request.Request(url)  # Request
# Make the request and close connection when done
with urllib.request.urlopen(req) as response:
    body = response.read()
# Display the content
print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", body.decode('utf-8'))
