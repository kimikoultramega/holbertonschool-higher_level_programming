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
        return jsonify(user), 200
    else:
        return jsonify({"error": "User  not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")

    if not isinstance(username, str) or username.strip() == "":
        return jsonify({"error": "Username is required"}), 400

    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({"message": "User  added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run()