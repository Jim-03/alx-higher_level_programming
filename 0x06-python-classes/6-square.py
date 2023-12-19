#!/usr/bin/python3
"""module for a square"""


class Square:
    """defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializer
        Args:
            size (int): the length of the square
            postion (int, int): position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """the current position of the square"""
        return (self.__position)

    @position.setter
    def position(self, val):
        if (not isinstance(val, tuple) or
                len(val) != 2 or
                not all(isinstance(num, int) for num in val) or
                not all(num >= 0 for num in val)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = val

    def area(self):
        """finds the area of the square"""
        ans = self.__size * self.__size
        return ans

    def my_print(self):
        """Print the square"""
        for i in range(0, self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
