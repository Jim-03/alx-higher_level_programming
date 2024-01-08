#!/usr/bin/python3
"""module for a base class"""


class BaseGeometry:
    def area(self):
        raise Exception('area() is not implemented')
