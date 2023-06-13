#!/usr/bin/python3
"""append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """appends `new_string` after a line containing
    `search_string` in `filename`"""
    with open(filename, 'r', encoding='utf-8') as input_file:
        line_list = []
        while True:
            line = input_file.readline()
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)

    with open(filename, 'w', encoding='utf-8') as output_file:
        output_file.writelines(line_list)
