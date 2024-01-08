#!/usr/bin/python3
"""Module for lookup"""


def lookup(obj):
    """returns the list of available attributes and methods of an object.
    Args:
        obj: an object.
    """
    myList = []
    for i in dir(obj):
        myList.append(i)
    return myList
