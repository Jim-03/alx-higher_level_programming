#!/usr/bin/python3
def max_integer(my_list=[]):
    large = my_list[0]
    i = 0
    while i < len(my_list):
        if my_list[i] > large:
            large = my_list[i]
        i += 1
    return large
