#!/usr/bin/python3
""" matrix_divided divides the given matrix"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix."""
    mat0 = "matrix must be a matrix (list of lists) of integers/floats"
    mat1 = "Each row of the matrix must have the same size"
    res = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    for lt in matrix:
        if len(lt) != len(matrix[0]):
            raise TypeError(mat1)
        n = []
        for it in lt:
            if not isinstance(it, (int, float)):
                raise TypeError(mat0)
            else:
                n.append(round(it / div, 2))
        res.append(n)
    return res
