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
        if not isinstance(size, int):
            raise TypeError('Width must be an integer')
        if size <= 0:
            raise ValueError('height must be > 0')
        self.__width = size

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, size):
        if not isinstance(size, int):
            raise TypeError('height must be an integer')
        if size <= 0:
            raise ValueError('height must be > 0')
        self.__height = size

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, size):
        if not isinstance(size, int):
            raise TypeError('x must be an integer')
        if size < 0:
            raise ValueError('x must be >= 0')
        self.__x = size

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, size):
        if not isinstance(size, int):
            raise TypeError('y must be an integer')
        if size < 0:
            raise ValueError('y must be >= 0')
        self.__y = size

    def area(self):
        return self.width * self.height

    def display(self):
        """prints out the rectangle using #."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        return "[Rectangle) ({}) {}/{} - {}/{}".\
                format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute."""
        if args:
            attr = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representation of the rectangle."""
        rectangular_dict = {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
        }
        return rectangular_dict
