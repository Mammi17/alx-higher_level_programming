#!/usr/bin/python3
"""a function that multiplies 2 matrices"""


def transpose(matrix):
    """ transpose a matrix """
    new = []
    for c in matrix[0]:
        new.append([])
    for r in matrix:
        for ind, it in enumerate(r):
            new[ind].append(it)
    return new

def dot_product(r_a, r_b):
    """ multiply dot 2 matrix """
    sum = 0
    for ind, it in enumerate(r_a):
        sum += it * r_b[ind]
    return sum

def mult(m_a, m_b):
    """ multiply a matrix """
    tr = transpose(m_b)
    new = []
    for r in m_a:
        new.append([])
    res = 0
    for ind_a, r_a in enumerate(m_a):
        for ind_b, r_b in enumerate(tr):
            res = dot_product(r_a, r_b)
            new.append(res)
    return new

def matrix_mul(m_a, m_b):
    """ matrix produc """
    a_listerror = "m_a must be a list"
    b_listerror = "m_b must be a list"
    a_list_listerror = "m_a must be a list of lists"
    b_list_listerror = "m_b must be a list of lists"
    a_emptyerror = "m_a can't be empty"
    b_emptyerror = "m_b can't be empty"
    a_interror = "m_a should contain only integers or floats"
    b_interror = "m_b should contain only integers or floats"
    a_recterror = "each row of m_a must be of the same size"
    b_recterror = "each row of m_b must be of the same size"
    cant_multerror = "m_a and m_b can't be multiplied"
    if type(m_a) is not list:
        raise TypeError(a_listerror)
    if type(m_b) is not list:
        raise TypeError(b_listerror)
    for r in m_a:
        if type(r) is not list:
            raise TypeError(a_list_listerror)
    for r in m_b:
        if type(r) is not list:
            raise TypeError(b_list_listerror)
    if m_a == []:
        raise ValueError(a_emptyerror)
    if m_b == []:
        raise ValueError(b_emptyerror)
    for r in m_a:
        if r == []:
            raise ValueError(a_emptyerror)
    for r in m_b:
        if r == []:
            raise ValueError(b_emptyerror)
    longi_a = len(m_a[0])
    longi_b = len(m_b[0])
    for r in m_a:
        for it in r:
            if type(it) is not int and type(it) is not float:
                raise TypeError(a_interror)
    for r in m_b:
        for it in r:
            if type(it) is not int and type(it) is not float:
                raise TypeError(b_interror)
    for r in m_a:
        if len(r) != longi_a:
            raise TypeError(a_recterror)
    for r in m_b:
        if len(r) != longi_b:
            raise TypeError(b_recterror)
    if longi_a != len(m_b):
        raise ValueError(cant_multerror)
    return mult(m_a, m_b)
