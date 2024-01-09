#!/usr/bin/python3
"""module for loading json"""
import json


def from_json_string(my_str):
    """return an object in python data structure."""
    return json.loads(my_str)
