#!/usr/bin/python3
"""module to add all arguments to a Python list, and save them to a file."""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file')\
        .load_from_json_file

    try:
        pythonList = load_from_json_file('add_item.json')
    except FileNotFoundError:
        pythonList = []
    pythonList.extend(sys.argv[1:])
    save_to_json_file(pythonList, 'add_item.json')
