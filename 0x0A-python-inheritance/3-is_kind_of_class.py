#!/usr/bin/python3
"""Module to check if is an instance"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: the object
        a_class: the class
    """
    if isinstance(obj, a_class):
        return True
    return False
