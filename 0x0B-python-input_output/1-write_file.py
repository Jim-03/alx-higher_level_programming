#!/usr/bin/python3
"""module to write to a file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8).

    Args:
        filename: the name of the file
        text: the string
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    return len(text)
