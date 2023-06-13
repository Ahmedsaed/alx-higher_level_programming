#!/usr/bin/python3
"""pascal_triangle function"""


def pascal_triangle(n):
    """return a list of lists where each list represents a
    row in pascal triangle"""
    if n <= 0:
        return []

    pascal = []
    for i in range(1, n+1):
        if i == 1:
            pascal.append([1])
        elif i == 2:
            pascal.append([1, 1])
        else:
            row = [0] * i
            row[0] = 1
            row[i - 1] = 1
            for j in range(1, i - 1):
                row[j] = pascal[-1][j - 1] + pascal[-1][j]
            pascal.append(row)

    return pascal
