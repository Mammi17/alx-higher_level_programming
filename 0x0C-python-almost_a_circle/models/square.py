#!/usr/bin/python3
"""a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Create a represention of square."""

    def __init__(self, size, x=0, y=0, id=None):
        """That initialize a new Square.
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """That update of the Square.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes."""
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if argumen is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = argumen
                elif i == 1:
                    self.size = argumen
                elif i == 2:
                    self.x = argumen
                elif i == 3:
                    self.y = argumen
                i += 1

        elif kwargs and len(kwargs) != 0:
            for a, b in kwargs.items():
                if a == "id":
                    if b is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = b
                elif a == "size":
                    self.size = b
                elif a == "x":
                    self.x = b
                elif a == "y":
                    self.y = b

    def to_dictionary(self):
        """That return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """That return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
