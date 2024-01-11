#!/usr/bin/python3
"""Defines a rectangle from base."""
from  models.base import Base


class Rectangle(Base):
    """Rectangle inheriting from base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, size):
        if isinstance(size, int) and size > 0:
            self.__width = size

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, size):
        if isinstance(size, int) and size > 0:
            self.__height = size

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, size):
        if isinstance(size, int) and size > 0:
            self.__x = size

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, size):
        if isinstance(size, int) and size > 0:
            self.__y = size
