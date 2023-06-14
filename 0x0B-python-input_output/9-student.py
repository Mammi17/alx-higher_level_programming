#!/usr/bin/python3
"""that contains the clas "Student" """


class Student:
    """Write a class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that returns a dictionary representation of a Student instance"""
        return self.__dict__
