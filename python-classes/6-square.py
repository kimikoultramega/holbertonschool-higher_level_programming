#!/usr/bin/python3
"""
Documentación
"""


class Square:

    """
    Plano del cuadrado
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Inicializa Square con tamaño opcional
        El parámetro size tiene un valor por defecto de 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter size
        """
        return self.__size

    @property
    def position(self):
        """
        Getter position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter position
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
