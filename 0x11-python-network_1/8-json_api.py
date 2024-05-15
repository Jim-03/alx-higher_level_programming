#!/usr/bin/python3
"""Takes in a letter
sends a post request to a url
displays the json data.
"""
import requests
import requests.exceptions
import sys


if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        if r.json():
            print(f"[{r.json()['id']}] {r.json()['name']}")
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
