#!/usr/bin/python3
"""save_to_json_file function"""


def save_to_json_file(my_obj, filename):
    """converts `my_obj` python object into a json string
    and store it in `filename` file"""
    import json

    with open(filename, mode="w", encoding="UTF8") as file:
        json.dump(my_obj, file)
