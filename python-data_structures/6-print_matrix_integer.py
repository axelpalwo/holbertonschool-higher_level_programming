#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) > 0:
        i = 0
        while i < len(matrix):
            v = 0
            while v < len(matrix[i]):
                if v == len(matrix[i]) - 1:
                    print("{:d}".format(matrix[i][v]))
                else:
                    print("{:d}".format(matrix[i][v]), end=' ')
                v += 1
            i += 1
    else:
        print()
