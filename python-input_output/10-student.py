#!/usr/bin/python3
"""
Doc
"""


class Student:
    """
    Doc
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        lista = isinstance(attrs, list)

        if lista and all(isinstance(item, str) for item in attrs):
            dicc = {}
            for key in attrs:
                if key in self.__dict__:
                    dicc[key] = self.__dict__[key]
            return dicc
        else:
            return self.__dict__
