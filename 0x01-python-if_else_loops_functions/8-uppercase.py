#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) >= ord('a') and ord(a) <= ord('z'):
            a = chr(ord(a) - 32)
        print("{:s}".format(a), end="")
        print("")
