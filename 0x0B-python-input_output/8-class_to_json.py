#!/usr/bin/python3
"""class_to_json function"""


def class_to_json(obj):
    """returns the dictionary description of a
    class with simple data structure"""
    return obj.__dict__
