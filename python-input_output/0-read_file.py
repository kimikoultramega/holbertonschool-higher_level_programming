#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, mode='r') as file:
        #  Dentro de este bloque leo el contenido
        contenido = file.read()
        print(contenido)
