#!/usr/bin/python3

"""Defines a Square module."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        [print("") for a in range(0, self.__position[1])]
        for a in range(0, self.__size):
            [print(" ", end="") for b in range(0, self.__position[0])]
            [print("#", end="") for l in range(0, self.__size)]
            print("")

    def __str__(self):
        if self.__size != 0:
            [print("") for a in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for b in range(0, self.__position[0])]
            [print("#", end="") for l in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
