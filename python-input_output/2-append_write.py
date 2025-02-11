#!/usr/bin/python3
"""
La creativiad, qué es realmente?
"""


def append_write(filename="", text=""):
    """
    Del latín creare, que significa "crear", "hacer algo nuevo" o "producir".
    Aquel que produce es creativo.
    """
    with open(filename, mode='a', encoding="utf-8") as file:
        escribir = file.write(text)
        return escribir
