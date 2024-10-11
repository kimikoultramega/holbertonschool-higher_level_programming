#!/usr/bin/python3

import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():

    response = requests.get(url)

    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
    # Convertimos la respuesta en una lista de diccionarios
        posts = response.json()

        for post in posts:
            print(f"Title : {post['title']}")
    else:
        print("Error")

def fetch_and_save_posts():

    response = requests.get(url)

    if response.status_code == 200:

        posts = response.json() # Post es una lista de diccionarios

    else:
        print("Error")
    
    post_to_save = [] # Lista vacía
    
    for post in posts: # Bucle

        post_data = {
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
        }

        post_to_save.append(post_data)

    with open('posts.csv', mode='w', newline="") as file:

        # Definimos claves como encabezados
        fieldnames = ["id", "title", "body"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(post_to_save)

        print("Datos guaraddos en posts.csv exitosamente")

fetch_and_print_posts()
fetch_and_save_posts()
