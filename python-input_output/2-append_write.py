#!/usr/bin/python3
"""
Doc
"""


def append_write(filename="", text=""):
    """
    Doc
    """
    with open(filename, 'a') as f:
        return f.write(text)
