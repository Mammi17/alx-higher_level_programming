#!/usr/bin/python3
"""Find the max integer in a list"""


def max_integer(my_list=[]):
    """Function to find and return the max integer in a list of integers"""
    if len(my_list) == 0:
        return None
    if (not isinstance(my_list, list)):
        raise TypeError

    ind = 0
    while (ind < len(my_list)):
        if (not isinstance(my_list[ind], int)):
            raise TypeError("element not an integer")
        ind += 1
    res = my_list[0]
    a = 1
    while a < len(my_list):
        if my_list[a] > res:
            res = my_list[]
        a += 1
    return res
