#!/usr/bin/python3
"""Defines inheritance from list."""


class MyList(list):
    def print_sorted(self):
        """Prints list in ascending order."""
        print(sorted(self))
