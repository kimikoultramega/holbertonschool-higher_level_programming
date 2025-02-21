import requests
import csv

def fetch_and_print_posts():

#  Se envía una solicitud HTTP GET a la URL
response = requests.get("https://jsonplaceholder.typicode.com/posts")

print(f"{response.status_code}")

if response.status_code == 200:
    posts = response.json()
    for post in posts:
        print(post["title"])

fetch_and_print_posts()

def fetch_and_save_posts():

    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        #  Convertimos en lista de diccionarios
        posts = response.json()

        with open("posts.csv", mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader
            for post in posts:
                writer.writerow({'id': post['id'], 'title': post['title'], 'body': post['body']})
fetch_and_save_posts
