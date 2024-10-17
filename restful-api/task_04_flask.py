#!/usr/bin/python3

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")  # Ruta dinámica
def get_user(username):  # El valor de username se pasa como parametro
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")

    # Validar que el nombre de usuario sea una cadena no vacía
    if not isinstance(username, str) or username == "":
        return jsonify({"error": "Username is required"}), 400

    # Validar que el nombre sea una cadena no vacía
    name = data.get("name")
    if not isinstance(name, str) or name == "":
        return jsonify({"error": "Name is required and must be a string"}), 400

    # Validar que la edad sea un entero
    age = data.get("age")
    if not isinstance(age, int):
        return jsonify({"error": "Age must be an integer"}), 400

    # Validar que la ciudad sea una cadena no vacía
    city = data.get("city")
    if not isinstance(city, str) or city == "":
        return jsonify({"error": "City is required and must be a string"}), 400

    # Verificar si el usuario ya existe
    # if username in users:
    #     return jsonify({"error": "Username already exists"}), 409  # Código 409 para conflicto

    # Agregar el nuevo usuario al diccionario
    users[username] = {
        "username": username,
        "name": name,
        "age": age,
        "city": city
    }

    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run()
