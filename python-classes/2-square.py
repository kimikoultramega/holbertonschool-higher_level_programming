#!/usr/bin/python3
"""

Script
"""


class Square:


    """
    Square
    """

    def __init__(self, size=0):

        """
        Initialize the size
        """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    self.__size = size
