#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict1 = a_dictionary.copy()
    for a, va in dict1.items():
        if value == va:
            del a_dictionary[a]
    return a_dictionary
