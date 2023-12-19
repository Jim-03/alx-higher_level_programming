#!/usr/bin/python3
"""module for a square"""


class Square:
    """defines a square"""
    def __init__(self, size):
        """
        Args:
            size : the length of the square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """finds the area of the square"""
        area_of_square = self.__size * self.__size
        return area_of_square
