#!/usr/bin/python3
"""Module to append to a file"""


def append_write(filename="", text=""):
    """Appends a string to a file.

    Args:
        filename: the file
        text: the string
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    return len(text)
