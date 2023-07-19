#!/usr/bin/python3
"""write_file function"""


def write_file(filename="", text=""):
    """write `text` contents into `filename` file and
    overwrites the file if it exists"""
    with open(filename, mode="w", encoding="utf=8") as file:
        return file.write(text)
