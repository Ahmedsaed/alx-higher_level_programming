#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, cell in enumerate(row):
            print("{:d}{}".format(
                cell,
                " " if (i != len(row) - 1) else ""), end="")
        print()
