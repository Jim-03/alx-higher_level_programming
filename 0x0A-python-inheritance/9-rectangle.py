#!/usr/bin/python3
"""Module for inheritance"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle."""

    def __init__(self, width, height):
        """ A new Rectangle.
        Args:
            width: the width of the rectangle.
            height: the height of the rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """The area of the rectangle."""
        theArea = self.__width * self.__height
        return theArea

    def __str__(self):
        """returns a representation of the rectangle."""
        a_rectangle = "[" + str(self.__class__.__name__) + "] "
        a_rectangle += str(self.__width) + "/" + str(self.__height)
        return a_rectangle
