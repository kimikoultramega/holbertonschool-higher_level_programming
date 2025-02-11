#!/usr/bin/python3
"""
Definiciones
"""


import json

def to_json_string(my_obj):
    """
    Documentación que nadie lee
    """
    json_string = json.dumps(my_obj)
    return json_string
