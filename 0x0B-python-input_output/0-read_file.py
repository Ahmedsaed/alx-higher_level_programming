#!/usr/bin/python3
"""
read_file function
"""


def read_file(filename=""):
    """read and print the content of a file using it's name"""
    with open(filename, mode='r', encoding="UTF8") as file:
        print(file.read(), end="")
