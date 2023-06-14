#!/usr/bin/python3
"""Pascal's Triangle module"""


def pascal_triangle(n):
    """that returns a list of lists of integers
    representing the Pascal’s triangle of n"""

    if n <= 0:
        return []

    trgle = [[1]]

    for a in range(1, n):
        r = [1]
        for b in range(1, a):
            r.append(trgle[a-1][b-1] + trgle[a-1][b])
        r.append(1)
        trgle.append(r)
    return trgle
