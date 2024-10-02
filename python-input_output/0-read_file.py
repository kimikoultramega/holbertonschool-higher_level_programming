#!/usr/bin/python3
"""
Doc
"""


def read_file(filename=""):
    """
    Doc
    """

    with open(filename, 'r') as file:

        content = file.read()  # Lee el contenido y lo guarda en content

        print(content, end="")
