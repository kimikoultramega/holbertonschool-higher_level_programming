#!/usr/bin/python3
"""
Doc
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Doc
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        write_python_json = json.dump(data, file)

def laod_and_deserialize(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        data = json.load(file)
        return data
