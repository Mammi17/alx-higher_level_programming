#!/usr/bin/python3
"""Creates a class."""


class BaseGeometry:
    """Class with public instance."""

    def area(self):
        """that raises an Exception with the message
        area() is not implemented"""

        raise Exception('area() is not implemented')
