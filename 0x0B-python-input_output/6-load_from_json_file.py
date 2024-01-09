#!/usr/bin/python3
"""module to create an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """creates object from json file."""
    with open(filename) as file:
        return json.load(file)
