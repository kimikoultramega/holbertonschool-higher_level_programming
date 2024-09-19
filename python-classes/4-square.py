#!/usr/bin/python3
"""
Chuwaka está en el área
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
        Getter para obtener el tamaño de cuadrado
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Setter para establecer el tamaño del cuadrado con validación
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """
        Método público para calcular el área del cuadrado
        """
        return self.__size ** 2