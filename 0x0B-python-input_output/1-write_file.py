#!/usr/bin/python3
"""Contains the function "wrtie_file"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
    andreturns the number of characters written"""
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
