#!/usr/bin/python3
"""
Hay que colocar texto
"""

class Square:
    """
    Otro poco de texto
    """
    def __init__(self, size=0):
        """
        Más texto
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

 def area(self):

    return self.__size ** 2
