#!/usr/bin/python3
"""
Documentación abstracta, flow criminal 5
"""


def read_file(filename=""):
    """
    Abriendo la caja de pandora, cuidado
    """
    with open(filename, mode='r') as file:
        #  Dentro de este bloque leo el contenido
        contenido = file.read()
        print(contenido, end="")
