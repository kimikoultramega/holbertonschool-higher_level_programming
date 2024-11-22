#!/usr/bin/python3
import json

def  serialize_and_save_to_file(data, filename):
    """Serializa un dic y lo guarda en un archivo JSON."""
    with open(filename, 'w') as file: #Abrimos el archivo en modo de escritura
        json.dump(data, file) #Serializamos los datos y los escribimos en el string

def load_and_deserialize(filename):
    """Carga y deserializa datos desde un archivo JSON."""
    with open(filename, 'r') as file:
        return json.load(file)
