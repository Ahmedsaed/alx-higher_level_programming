#!/usr/bin/python3
"""A script that adds all arguments to a Python list,
and then save them to a file"""

import sys
import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    """main function. it creates/overwrites add_item.json
    file with arguments"""
    try:
        old = load_from_json_file("add_item.json")
        old.extend(sys.argv[1:])
    except FileNotFoundError:
        old = sys.argv[1:]

    save_to_json_file(old, "add_item.json")


if __name__ == "__main__":
    main()
