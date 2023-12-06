#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    ans = 0
    for i in new:
        ans += i
    return ans
