#!/usr/bin/python3
"""
This module has text_indentation implementation
"""


def text_indentation(text):
    """prints a text with 2 new lines after each
    of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = 0
    for i in text:
        if flag == 0 and i == ' ':
            continue
        elif flag == 0 and i != ' ':
            flag = 1

        if flag == 1 and i in ['.', '?', ':']:
            print(i)
            print()
            flag = 0
        elif flag == 1:
            print(i, end="")
