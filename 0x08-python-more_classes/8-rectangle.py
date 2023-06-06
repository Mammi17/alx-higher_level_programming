#!/usr/bin/python3

"""This module contains a class Rectangle"""


class Rectangle:
    """This is an class Rectangle with instance 
    attribute heigth and width"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initializes height and width of the rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        """Property setter for the width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

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
        """The method perimeter() return the perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """Returns a string representation of the rectangle"""

        if self.width == 0 or self.height == 0:
            return ""
        rec = ""
        for a in range(self.height):
            for b in range(self.width):
                rec += str(self.print_symbol)
            if a != self.height - 1:
                rec += "\n"

        return rec

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rec1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rec2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
