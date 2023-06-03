#!/usr/bin/python3
"""this module contains the matrix_mul function"""


def matrix_mul(m_a, m_b):
    """multiplies two matrices"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for n in row:
            if type(n) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for n in row:
            if type(n) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    row_lens = []
    for row in m_a:
        row_lens.append(len(row))
    if len(set(row_lens)) != 1:
        raise TypeError("each row of m_a must be of the same size")

    row_lens = []
    for row in m_b:
        row_lens.append(len(row))
    if len(set(row_lens)) != 1:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            new_row.append(0)
        new_matrix.append(new_row)
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                new_matrix[i][j] += m_a[i][k] * m_b[k][j]

    return new_matrix
