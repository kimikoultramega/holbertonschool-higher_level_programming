#!/usr/bin/python3
"""
Wako
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Si copias, moris.
    """
    with open(filename, mode='w', encoding="utf-8") as file:
        # string_json = json.dumps(my_obj)
        # writeee = file.write(string_json)
        json.dump(my_obj, file)
