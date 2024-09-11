#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        a = ' '.join(str(x) for x in row)
        print(a)
