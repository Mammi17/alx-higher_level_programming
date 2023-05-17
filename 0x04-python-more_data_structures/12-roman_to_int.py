#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return dec = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                     "D": 500, "M": 1000}
        decs = [dec.get(a) for a in roman_string]
        result = 0
        for b in range(len(decs)):
            result += decs[b]
            if decs[b - 1] < decs[b] and b != 0:
                result += (decs[b] - decs[b - 1] - decs[b - 1]
        return result
