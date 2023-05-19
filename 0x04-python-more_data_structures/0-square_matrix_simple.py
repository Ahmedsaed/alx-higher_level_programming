#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []

    for i in range(len(matrix)):
        result.append([])
        for j in range(len(matrix[i])):
            result[i].append(matrix[i][j] ** 2)

    return result
