#!/usr/bin/python3
"""Module to find the peak of a list."""


def find_peak(list_of_integers):
    """ Finds the peak of a list."""
    if not list_of_integers:  # if list is null
        return None

    # Take the first and last digits
    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2  # Find the midpoint
        # If the midpoint is less than preceeding value
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1  # Set the starting point to be the preceeding value
        else:
            right = mid  # If not the midpoint is the new last digit
    return list_of_integers[left]  # Return the peak
