#!/usr/bin/python3
"""load_from_json_file function"""


def load_from_json_file(filename):
    """loads python object from json string stored in `filename` file"""
    import json

    with open(filename, mode="r", encoding="UTF8") as file:
        return json.load(file)
