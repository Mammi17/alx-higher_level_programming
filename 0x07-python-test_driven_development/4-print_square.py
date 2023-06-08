#!/usr/bin/python3
""" print a square"""


def print_square(size):
    """a function that prints a square with the character #."""
    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return None

    for r in range(size):
        print('#' * size)
