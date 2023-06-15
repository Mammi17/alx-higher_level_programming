#!/usr/bin/python3
""" A attribute adding module """


def add_attribute(a_class, name, val):
    """ function that adds a new attribute to an object if it’s possible """
    if hasattr(a_class, "__dict__"):
        setattr(a_class, name, val)
    else:
        raise TypeError("can't add new attribute")
