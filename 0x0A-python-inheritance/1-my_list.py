#!/usr/bin/python3
"""Creates a class"""


class MyList(list):
    """Class MyList that inherits from list."""

    def print_sorted(self):
        """that prints the list, but sorted"""
        new = self[:]
        new.sort()
        print("{}".format(new))
