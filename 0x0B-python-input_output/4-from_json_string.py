#!/usr/bin/python3
"""from_json_string function"""


def from_json_string(my_str):
    """converts `my_str` json string into a python object"""
    import json
    return json.loads(my_str)
