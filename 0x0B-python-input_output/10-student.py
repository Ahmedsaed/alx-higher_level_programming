#!/usr/bin/python3
"""class student implementation"""


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """initialize instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if type(attrs) is list:
            if all(type(e) is str for e in attrs):
                return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
