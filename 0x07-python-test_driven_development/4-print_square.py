#!/usr/bin/python3
"""Prints a square with # character"""


def print_square(size):
    """
    Args:
        size: the size of the square.
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
