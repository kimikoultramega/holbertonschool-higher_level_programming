#!/usr/bin/python3

import csv
import json 

def convert_csv_to_json(csv_filename):

    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file: # Asigna el archivo abierto a la variable csv_file para que podamos usarlo dentro del bloque.
            csv_reader = csv.DictReader(csv_file) # Almacenamos los diccionarios generados a partir de csv_file en csv_reader.
            data = list(csv_reader)

        with open('data.json', mode= 'w', encoding='utf-8') as json_file: # Abre o crea un archivo llamado 'data.json'
            json.dump(data, json_file, indent=4)
        
        return True

    except FileNotFoundError:

        return False
    
