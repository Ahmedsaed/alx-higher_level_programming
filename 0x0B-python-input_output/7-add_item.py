#!/usr/bin/python3
"""A script that adds all arguments to a Python list,
and then save them to a file"""

import sys
import json


def main():
    """main function. it creates/overwrites add_item.json
    file with arguments"""
    with open("add_item.json", mode="w") as file:
        json.dump(sys.argv[1:], file)


if __name__ == "__main__":
    main()
