#!/usr/bin/python3

"""a base model class."""
import json
import csv
import turtle


class Base:
    """create a Base model in package models.

    Private Class Attributes:
        __nb_object: Number of instantiated Bases."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base.
        Args:
            id : The identity of the new Base."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return a resentation of the JSON serialization of a list of dicts.
        Args:
            list_dictionaries: it's a list of dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """That write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dict = [l.to_dictionary() for l in list_objs]
                jsonfile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """That return the deserialization ofJSON to a JSON string.
        Args:
            json_string (string): A JSON str representation of a list of dicts.
        Returns: If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string. """
        if json_string is None or json_string == "[]":
            return []
        else
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """That return a class instantied from a dictionary of attributes.
        Args:
            cls: a atribute 
            **dictionary (dictionary): Key/value pairs of attributes to initialize."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                n = cls(1, 1)
            else:
                n = cls(1)
            n.update(**dictionary)
            return n

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        args:
            cls: a attribute
        Returns:If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes."""
        filename = str(cls.__name__) + "for .json"
        try:
            with open(filename, "r") as jsonfile:
                list_dict = Base.from_json_string(jsonfile.read())
                return [cls.create(**dictio) for dictio in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances."""
        filename = cls.__name__ + "in .csv"
        with open(filename, "w", newligne="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldname = ["id", "width", "height", "x", "y"]
                else:
                    fieldname = ["id", "size", "x", "y"]
                ecriture = csv.DictWriter(csvfile, fieldname=fieldname)
                for objects in list_objs:
                    ecriture.writerow(objects.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes."""
        filename = cls.__name__ + "in .csv"
        try:
            with open(filename, "r", newligne="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldname = ["id", "width", "height", "x", "y"]
                else:
                    fieldname = ["id", "size", "x", "y"]
                list_dict = csv.DictReader(csvfile, fieldname=fieldname)
                list_dict = [dict([a, int(b)] for a, b in dictio.items())
                              for dictio in list_dict]
                return [cls.create(**dictio) for dictio in list_dict]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args: list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw."""
        turtl = turtle.Turtle()
        turtl.screen.bgcolor("#b7312c")
        turtl.pensize(3)
        turtl.shape("turtle")
        turtl.color("#ffffff")
        for rectangl in list_rectangles:
            turtl.showturtle()
            turtl.up()
            turtl.goto(rect.x, rect.y)
            turtl.down()
            for a in range(2):
                turtl.forward(rect.width)
                turtl.left(90)
                turtl.forward(rect.height)
                turtl.left(90)
            turtl.hideturtle()

        turtl.color("#b5e3d8")
        for squar in list_squares:
            turtl.showturtle()
            turtl.up()
            turtl.goto(sq.x, sq.y)
            turtl.down()
            for a in range(2):
                turtl.forward(sq.width)
                turtl.left(90)
                turtl.forward(sq.height)
                turtl.left(90)
            turtl.hideturtle()

        turtle.exitonclick()
