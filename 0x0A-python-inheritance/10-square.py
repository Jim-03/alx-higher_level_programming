#!/usr/bin/python3
"""the module for a square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """
        Initializes a new square.

        Args:
            size: the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

        def area(self):
            return self._Rectangle__width * self._Rectangle__height
