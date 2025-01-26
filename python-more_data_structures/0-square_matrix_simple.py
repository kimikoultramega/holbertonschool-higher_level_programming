#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix2 = []

    for row in matrix:
        new_row = []
        for element in row:
            cuadrado = element * element
            new_row.append(cuadrado)
        matrix2.append(new_row)
    return matrix2
