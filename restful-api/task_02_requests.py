

import requests
import csv

response = requests.get('https://jsonplaceholder.typicode.com/posts')

print(f"Status code: {response.status_code}")

if response.status_code == 200:
    # Convertimos la respuesta en una lista de diccionarios
    posts = response.json()
