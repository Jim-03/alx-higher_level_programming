#!/usr/bin/python3
def no_c(my_string):
    i = 0
    while i < len(my_string):
        if my_string[i].lower() == 'c':
            my_string = my_string[:i] + my_string[i + 1:]
        else:
            i += 1
    return my_string
