#!/usr/bin/python3
"""
Doc
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Doc
    """
    def __init__(self, size):

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
