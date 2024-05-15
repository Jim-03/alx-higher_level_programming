#!/usr/bin/python3
"""Takes in a url and an email,
sends a post request to the url
displays the body of the response.
"""

import requests
import sys


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(r.text)
