#!/usr/bin/python3
"""module for a base class"""


class BaseGeometry:
    """Represents base geometry."""
    def area(self):
        raise Exception('area() is not implemented')
