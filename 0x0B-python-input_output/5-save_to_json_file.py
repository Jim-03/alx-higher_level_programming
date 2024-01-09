#!/usr/bin/python3
"""Writes an object in json"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation.

    Args:
        my_obj: the object
        filename: the file to be written in
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
