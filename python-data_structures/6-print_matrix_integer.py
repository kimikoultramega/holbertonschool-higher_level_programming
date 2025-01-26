#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for fila in matrix:

        formated_num = ["{:d}".format(num) for num in fila]

        new_string = " ".join(formated_num)

        print(new_string)
