#!/usr/bin/python3
"""module to check if the object is an instance of a class that inherited (directly or indirectly) from the specified class """


def inherits_from(obj, a_class):
    """
    Args:
        obj: the object
        a_class: the class
    Return:
        True: if the object is an instance of a class that inherited
        False: if the object isn't an instance of a class that inherited
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
