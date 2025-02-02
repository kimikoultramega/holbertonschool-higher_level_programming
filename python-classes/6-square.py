#!/usr/bin/python3
"""
Doc
"""


class Square:
    """
    Doc
    """
    def __init__(self, size=0, position=(0, 0)):
        self.position = position
        self.size = size

    @property
    def size(self):
        return self.__size  # Getter devuelve valor size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        for tup in value:
            if type(tup) is not int or tup < 0 len(value) != 2:
                raise TypeError("position must be a\
                     tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        if not isinstance(value, int):  # Verificar si value es valido
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Asinar value a size si es valido

    def area(self):
        return self.size * self.size  # Accedemos mediante el getter

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for a in range(self.__position[1]):
            print()
        for b in range(self.__size):
            print(" " * self.position[0] + "#" * self.__size)
