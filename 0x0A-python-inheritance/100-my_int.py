#!/usr/bin/python3
"""Contains the class MyInt"""


class MyInt(int):
    """a class MyInt that inherits from int"""
    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, autre):
        """what was == is now !="""
        return int(self) == autre
