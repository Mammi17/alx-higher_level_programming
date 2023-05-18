#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return dec = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                     "D": 500, "M": 1000}
        dics = [dec.get(a) for a in roman_string]
        result = 0
        for b in range(len(dics)):
            result += dics[b]
            if dics[b - 1] < dics[b] and b != 0:
                result += (dics[b] - dics[b - 1] - dics[b - 1]
        return result
