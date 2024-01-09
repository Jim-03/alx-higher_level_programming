#!/usr/bin/python3
import json
"""module for json"""


def to_json_string(my_obj):
    """returns the JSON representation of an object (string).

    Args:
        my_obj: the object (string)
    """
    return json.dumps(my_obj)
