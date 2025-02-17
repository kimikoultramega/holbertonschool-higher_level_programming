#!/usr/bin/python3
"""
Doc
"""
import json
import sys
import os
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def main():
    """
    Doc
    """
    filename = "add_item.json"

    if os.path.exists(filename):
        data = load_from_json_file(filename)
    else:
        data = []

    for arg in sys.argv[1:]:
        data.append(arg)

    save_to_json_file(data, filename)
