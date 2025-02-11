#!/usr/bin/python3

def write_file(filename="", text=""):
    with open(filename, mode='w', encoding="utf-8") as file:
        #  Dentro del bloque utilizamos write.
        escribir = file.write(text)
        #  Aquí escribirmos text dentro de nuestro archivo
        return escribir
