#!/usr/bin/python3
"""module for a square"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """initializer
        Args:
            size (int): the length of the square
        """
        self.size = size

    @property
    def size(self):
        """retrieve the size"""
        return self.__size

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError('size must be an integer')
        elif val < 0:
            raise ValueError('size must be >= 0')
        self.__size = val

    def area(self):
        """finds the area of the square"""
        ans = self.__size * self.__size
        return ans

    def my_print(self):
        """Print the square"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
