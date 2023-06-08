#!/usr/bin/python3
"""function that adds 2 integers."""


def add_integer(a, b=98):
    """Return the addition of two numbers."""
     tpe = [int, float]
    error_a = "a must be an integer"
    error_b = "b must be an integer"
    if (type(a) not in tpe):
        raise TypeError(error_a)
    if (type(b) not in tpe):
        raise TypeError(error_b)
    if (type(a) is float):
        a = int(a)
    if (type(b) is float):
        b = int(b)
    return (a + b)
