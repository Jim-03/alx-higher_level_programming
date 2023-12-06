#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = dict(a_dictionary)
    for k, v in new.items():
        new[k] = v*2
    return new
