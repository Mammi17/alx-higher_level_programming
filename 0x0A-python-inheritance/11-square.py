#!/usr/bin/python3
"""Creates a Square class."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle (9-rectangle.py)"""

    def __init__(self, size):
        """Initializes a Square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return str("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Computes the area of a Square instance.
        Overwrites the area()"""

        return self.__size ** 2
