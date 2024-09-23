#!/usr/bin/python3code
"""
Documentación
"""


class Rectangle:
    """
    Documentación
    """
    def __init__(self, width=0, height=0):
        """
        Documentación
        """
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """
        Documentación
        """
        return self.__height
     
    @property
    def width(self):
        """
        Documentación
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        Documentación
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        return self.__width = value

    @height.setter
    def height(self, value):
        """
        Documentación
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        return self.__height = value
