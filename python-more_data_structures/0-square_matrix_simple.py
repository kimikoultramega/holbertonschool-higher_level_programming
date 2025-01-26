#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix2 = [] # Creo una lista vacía

    for row in matrix:
        new_row = [] # Genero otra lista para iterar
        for element in row:
            cuadrado = element * element # Calculo los cuadrados
            new_row.append(cuadrado) # Agrego a mi nueva lista
        matrix2.append(new_row) # Agrego lista de lista
    return matrix2 # Retorno la lista
