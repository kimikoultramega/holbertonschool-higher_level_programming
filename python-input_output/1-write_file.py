#!/usr/bin/python3
"""
Porque es mejor ser alguien, que no ser nadie. En la masa, nadie es nada.
"""


def write_file(filename="", text=""):
    """
    Abriendo, escribiendo, cerrando, retornando. Camino zen.
    """
    with open(filename, mode='w', encoding="utf-8") as file:
        #  Dentro del bloque utilizamos write.
        escribir = file.write(text)
        #  Aquí escribirmos text dentro de nuestro archivo
        return escribir
