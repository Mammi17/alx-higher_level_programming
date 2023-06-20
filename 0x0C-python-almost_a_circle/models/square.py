#!/usr/bin/python3
# square.py
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """set the size of the Square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square."""
        if args and len(args) != 0:
            b = 0
            for argu in args:
                if b == 0:
                    if argu is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = argu
                elif b == 1:
                    self.size = argu
                elif b == 2:
                    self.x = argu
                elif b == 3:
                    self.y = argu
                b += 1

        elif kwargs and len(kwargs) != 0:
            for k, c in kwargs.items():
                if k == "id":
                    if c is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = c
                elif k == "size":
                    self.size = c
                elif k == "x":
                    self.x = c
                elif k == "y":
                    self.y = c

    def to_dictionary(self):
        """Return the dictionary of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
