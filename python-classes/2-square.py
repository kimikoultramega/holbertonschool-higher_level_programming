#!/usr/bin/python3
"""
Script
"""


class Square:
    """
    Square class
    """
    def __init__(self, size=0):

        """
        Initialize the size
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
