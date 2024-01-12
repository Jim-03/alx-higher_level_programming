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

    def update(self, *args, **kwargs):
        """Assigns attributes."""
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictioinary representation."""
        square_dict = {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
        }
        return square_dict
