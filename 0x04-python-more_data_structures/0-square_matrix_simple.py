#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for a in matrix:
        new.append(list(map(lambda a: a**2, a)))
    return (new)
