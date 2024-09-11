#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        a = ' '.join('{}' for _ in row).format(*row) #(map(str, row))
        print(a)
