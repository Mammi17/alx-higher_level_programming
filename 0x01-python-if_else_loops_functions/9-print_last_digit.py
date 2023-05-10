#!/usr/bin/python3
def print_last_digit(number):
    a = number % 10
    if number < 0:
        a = (number * -1) % 10
        print("{:d}".format(a), end="")
    return a
