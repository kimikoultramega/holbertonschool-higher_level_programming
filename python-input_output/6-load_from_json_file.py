#!/usr/bin/python3
"""
Doc
"""
import json



def load_from_json_file(filename):
    """
    Doc
    """
    with open(filename, 'r') as file:
        variable = json.load(file)
        return variable