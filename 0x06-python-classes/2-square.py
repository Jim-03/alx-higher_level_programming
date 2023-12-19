#!/usr/bin/python3
"""module for a square"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """initialize.
        Args:
            size: the length of the square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
