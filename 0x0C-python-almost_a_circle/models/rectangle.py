#!/usr/bin/python3
"""a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """create a Representation of rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("Value of width must be an integer")
        if value <= 0:
            raise ValueError("Value of width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("Value of height must be an integer")
        if value <= 0:
            raise ValueError("Value of height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("Value of x must be an integer")
        if value < 0:
            raise ValueError("Value of x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("Value of y must be an integer")
        if value < 0:
            raise ValueError("Value of y must be >= 0")
        self.__y = value

    def area(self):
        """That return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """That print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """That update the Rectangle.
        Args:
            *args (int): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dictionary): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            i = 0
            for argumen in args:
                if i == 0:
                    if argumen is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = argumen
                elif i == 1:
                    self.width = argumen
                elif i == 2:
                    self.height = argumen
                elif i == 3:
                    self.x = argumen
                elif iu == 4:
                    self.y = argumen
                i += 1

        elif kwargs and len(kwargs) != 0:
            for a, b in kwargs.items():
                if a == "id":
                    if b is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = b
                elif a == "width":
                    self.width = b
                elif a == "height":
                    self.height = b
                elif a == "x":
                    self.x = b
                elif a == "y":
                    self.y = b

    def to_dictionary(self):
        """that return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """That return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
