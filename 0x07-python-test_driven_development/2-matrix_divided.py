#!/usr/bin/python3
"""
This module has matrix_divided implementation
"""


def matrix_divided(matrix, div):
    """divides matrix by scalar integer, rounded to two decimal places"""
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error)
    row_lens = []
    col_count = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(error)
        row_lens.append(len(row))
        for n in row:
            if type(n) not in [int, float]:
                raise TypeError(error)
        col_count += 1

    if len(set(row_lens)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    elif int(div) == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(map(
        lambda row: list(map(
            lambda x: round(x/div, 2), row)), matrix))

    return new_matrix
