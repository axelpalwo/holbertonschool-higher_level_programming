#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    i = 0
    while i < len(matrix):
        v = 0
        new_matrix.append([])
        while v < len(matrix[i]):
            new_matrix[i].append(matrix[i][v] * matrix[i][v])
            v += 1
        i += 1
    return new_matrix
