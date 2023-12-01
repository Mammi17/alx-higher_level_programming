#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """peak of list_of_integers or None"""

    size = len(list_of_integers)
    m = size
    m_1 = size // 2

    if size == 0:
        return None

    while True:
        m = m // 2
        if (m_1 < size - 1 and
                list_of_integers[m_1] < list_of_integers[m_1 + 1]):
            if m // 2 == 0:
                m = 2
            m_1 = m_1 + m // 2
        elif m > 0 and list_of_integers[m_1] < list_of_integers[m_1 - 1]:
            if m // 2 == 0:
                m = 2
            m_1 = m_1 - m // 2
        else:
            return list_of_integers[m_1]
