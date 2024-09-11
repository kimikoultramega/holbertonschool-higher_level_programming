#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for integer in row:
            if integer is row[-1]:
                print("{}".format(integer))
            else:
                print("{}".format(integer), end= " ")