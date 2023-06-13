#!/usr/bin/python3
"""append_write function"""


def append_write(filename="", text=""):
    """append `text` contents into `filename` file"""
    with open(filename, mode="a", encoding="UTF8") as file:
        return file.write(text)
