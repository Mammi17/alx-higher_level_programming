#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    count = 0
    result = 0
    for a, b in my_list:
        count += a * b
        result += b
    return (count / result)
