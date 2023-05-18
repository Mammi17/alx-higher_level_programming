#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict1 = a_dictionary.copy()
    if (value in a_dictionary.values()):
        for a, va in dict1.items():
            if (va == value):
                del dict1[key]
        a_dictionary = dict1
        return dict1
    else:
        return a_dictionary
