#!/usr/bin/python3
"""to_json_string function"""


def to_json_string(my_obj):
    """converts `my_obj` python object into a json string"""
    import json
    return json.dumps(my_obj)
