#!/usr/bin/python3

from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = "wanako22"
jwt = JWTManager(app)

# Dic de usuarios con contraseña "hasheada"
# Definición de usuario y admin
users = {
    "user1":{"password": generate_password_hash("password1"), "role": "user"}, # Hasheooo
    "admin1":{"password": generate_password_hash("adminpass"), "role": "admin"}
}

# Generamos una instancia para proteger nuestras rutas
auth = HTTPBasicAuth()

# Generamos verificación de credenciales
@auth.verify_password # Este decorador proviene de la instancia auth

def verify_password(username, password):
    if username in users: # Verifica el username en users
        # Verificamos que la contra hasheada coincida con el dato almacenado
        return check_password_hash(users.get(username), password)
    return False

# Ruta pública, sin verificación
@app.route("/")
def hello_world():
    return "Hello, World!"

# Ruta protegida, con autenticación básica
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# Ruta de login para generar JWT
@app.route('/login', methods=['POST'])
def login():

    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users and check_password_hash(users[username]['password'], password):
        # Incluir el rol en el JWT
        access_token = create_access_token(identity={"username": username, "role": users[username]['role']})
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid username or password"}), 401

# Ruta protegida con JWT

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as = current_user), 200

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"msg": "Admin access required"}), 403
    return jsonify({"msg": "Welcome Admin!"})

# Manejadores de errores personalizados para JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(error):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(error):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(error):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(error):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(error):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run(debug=True)
