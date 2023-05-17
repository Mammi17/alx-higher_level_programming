#!/usr/bin/python3
def multiply_by_2(my_dict):
    new = my_dict.copy()
    for a in new.keys():
        new[a] *= 2
    return (new)
