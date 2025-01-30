#!/usr/bin/python3
"""
Doc
"""
class Square:
    """
    Doc
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size  # Getter devuelve valor size

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
        if self.size == 0:
            print("")
        else:
            for _ in range(self.size):
                print('#' * self.size)
