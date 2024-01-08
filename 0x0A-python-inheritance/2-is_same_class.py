#!/usr/bin/python3
"""defines boolean result on an object"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the specified class.

    Args:
        obj: the object
        a_class: the class
    """
    return type(obj) is a_class
