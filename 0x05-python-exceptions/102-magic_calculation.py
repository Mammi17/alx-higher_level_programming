#!/usr/bin/python3

def magic_calculation(a, b):
    count = 0
    for e in range(1, 3):
        try:
            if e > a:
                raise Exception('Too far')
            else:
                count += a ** b / e
        except:
            count = b + a
            break
    return (count)
