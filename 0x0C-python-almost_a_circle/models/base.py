#!/usr/bin/python3
"""Defines a base model class"""
import json
import csv
import turtle


class Base:
    """define the base model.
    Attributes:
        __nb_objects (int): The number of instantiated Bases."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list of objects to a file"""
        fil = cls.__name__ + ".json"
        with open(fil, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_dic = cls(1, 1)
            else:
                new_dic = cls(1)
            new_dic.update(**dictionary)
            return new_dic

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`."""
        fil = str(cls.__name__) + ".json"
        try:
            with open(fil, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """class base
        Write the CSV serialization of a list of objects to a file"""
        fil = cls.__name__ + ".csv"
        with open(fil, "w", nline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldname = ["id", "width", "height", "x", "y"]
                else:
                    fieldname = ["id", "size", "x", "y"]
                writ = csv.DictWriter(csvfile, fieldname=fieldname)
                for obj in list_objs:
                    writ.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`"""
        fil = cls.__name__ + ".csv"
        try:
            with open(fil, "r", nline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldname = ["id", "width", "height", "x", "y"]
                else:
                    fieldname = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldname=fieldname)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """that opens a window and draws all the Rectangles and Squares"""
        tur = turtle.Turtle()
        tur.screen.bgcolor("#b7312c")
        tur.pensize(3)
        tur.shape("turtle")

        tur.color("#ffffff")
        for rec in list_rectangles:
            tur.showturtle()
            tur.up()
            tur.goto(rec.x, rec.y)
            tur.down()
            for a in range(2):
                tur.forward(rec.width)
                tur.left(90)
                tur.forward(rec.height)
                tur.left(90)
            tur.hideturtle()

        tur.color("#b5e3d8")
        for carre in list_squares:
            tur.showturtle()
            tur.up()
            tur.goto(carre.x, carre.y)
            tur.down()
            for a in range(2):
                tur.forward(carre.width)
                tur.left(90)
                tur.forward(carre.height)
                tur.left(90)
            tur.hideturtle()

        turtle.exitonclick()
