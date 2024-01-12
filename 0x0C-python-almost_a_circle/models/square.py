#!/usr/bin/python3
"""Defines a square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from rectangle-"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new square."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The string rerpresentation of a square."""
        return "[Square] + ({}) + {}/{} - {}"\
                .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
