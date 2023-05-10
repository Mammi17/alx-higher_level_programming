#!/usr/bin/python3
def uppercase(str):
    for b in str:
        if ord(b) >= ord('a') and ord(b) <= 123:
            b = chr(ord(b) - 32)
            print("{:s}".format(b), end="")
