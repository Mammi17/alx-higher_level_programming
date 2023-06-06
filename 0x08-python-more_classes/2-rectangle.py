#!/usr/bin/python3

"""This module contains a class Rectangle"""


class Rectangle:
    """This is an class Rectangle with instance attribute heigth and width"""

    def __init__(self, width=0, height=0):
        """Initializes height and width of the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property getter for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """The method area() returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """The method perimeter() return the rectangle perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
