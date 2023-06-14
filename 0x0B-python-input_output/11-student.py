#!/usr/bin/python3
"""that contains the clas "Student" """


class Student:
    """a class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a Student instance"""
        new = dict()
        if attrs and all(isinstance(a, str) for a in attrs):
            for a in attrs:
                if a in self.__dict__:
                    new.update({a: self.__dict__[a]})
            return new
        return self.__dict__

    def reload_from_json(self, json):
        """that replaces all attributes of the Student instance"""
        for a in json:
            self.__dict__.update({a: json[a]})
