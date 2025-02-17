#!/usr/bin/python3
"""
Doc
"""
import csv
import json


def convert_csv_to_json(csv_filename: str):
    """
    Doc
    """
    data = []
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for i in csv_reader:
                data.append(i)
    except FileNotFoundError:
        return False

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)

    return True
