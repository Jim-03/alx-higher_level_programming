#!usr/bin/python3
def magic_string(n):
    magic_string.counter = getattr(magic_string, 'counter', 0) + 1
    return "BestSchool" + ", BestSchool" * (magic_string.counter - 1)
