#!/usr/bin/python3
for a in range(97, 123):
    if chr(a) == 'e' or chr(a) == 'q':
        continue
    else:
        print("{:s}".format(chr(a)), end="")
