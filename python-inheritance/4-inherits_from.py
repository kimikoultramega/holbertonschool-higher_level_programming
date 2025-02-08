#!/usr/bin/python3
"""
Doc
"""


def inherits_from(obj, a_class):
    tipo = type(obj)
    if tipo is a_class:  # Verificamos la clase
        return False
    return issubclass(tipo, a_class)
