#!/usr/bin/python3
"""module to read text file"""


def read_file(filename=""):
    """Reads a text file.
    Args:
        filename (str): the name of the file
    """
    with open('filename', encoding="utf-8") as file:
        openFile = file.read()
        print(openFile)
