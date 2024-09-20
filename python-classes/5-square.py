#!/usr/bin/python3
"""
ssss
"""


class Square:

    """
    Plano del cuadrado
    """
    def __init__(self, size=0):
        """
        Inicializa Square con tamaño opcional
        El parámetro size tiene un valor por defecto de 0
        """
        self.size = size

    @property
    def size(self):
        """
        GETTER
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        SETTER
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        sssss
        """
        return self.__size ** 2

    def my_print(self):
        """
        xxx
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
