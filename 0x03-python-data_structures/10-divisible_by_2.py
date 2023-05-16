#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    other_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            other_list.append(True)
        else:
            other_list.append(False)
    return other_list
