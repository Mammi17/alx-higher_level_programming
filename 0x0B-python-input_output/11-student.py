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
        if attrs is None:
            return self.__dict__
        new = {}
        for b in attrs:
            try:
                new[b] = self.__dict__[b]
            except:
                pass
        return new

    def reload_from_json(self, json):
        """that replaces all attributes of the Student instance"""
        for c in json:
            try:
                setattr(self, c, json[c])
            except:
                pass
