#!/usr/bin/python3
"""
Doc
"""
import json


def load_from_json_file(filename):
    """
    Doc
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        #  le el contenido del archivo y lo convierte a objeto Python
        obj = json.load(file)
        return obj
