#!/usr/bin/python3
def roman_to_int(roman_string):
    a_dictionary = {'M': 1000, 'D': 500, 'C': 100,
                     'L': 50, 'X': 10, 'V': 5, 'I': 1}
    if roman_string is None or type(roman_string) != str:
        return 0
    count = 0
    prece = 0
    current = 0
    for a in range(len(roman_string)):
        current = a_dictionary[roman_string[a]]
        if current > prece:
            count += current - 2 * prece
        else:
            count += current
        prece = current
    return count
