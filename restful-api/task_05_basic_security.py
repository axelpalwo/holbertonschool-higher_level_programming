from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

# Instanciamos la Aplicacion
app = Flask(__name__)

# Clave secreta para los tokens
app.config['JWT_SECRET_KEY'] = 'ULTRA SUPER MEGA SECRET KEY'

# Instanciamos JWT Manager
jwt = JWTManager(app)
auth = HTTPBasicAuth()
# Lista de usuarios
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "admin"
    },
    "user2": {
        "username": "user2",
        "password": generate_password_hash("password"),
        "role": "user"
    }
}

# Login endpoint
@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    # Verificar si el usuario existe y la contraseña es correcta
    if username in users and check_password_hash(users[username]["password"], password):
        # Crear un token con la identidad del usuario y su rol
        access_token = create_access_token(identity={"username": username, "role": users[username]["role"]})
        return jsonify(access_token=access_token), 200
    return jsonify({"message": "Bad username or password"}), 401


#Jwt protected endpoint
@app.route("/jwt-protected")
@jwt_required()
def userprotected():
    return "JWT Auth: Access Granted", 200

# Ruta protegida solo para administradores
@app.route("/admin-only", methods=['GET'])
@jwt_required()
def admin_only():

    current_user = get_jwt_identity()

    if current_user['role'] == 'admin':
        return "Admin Access: Granted", 200
    else:
        return jsonify(error="Admin access required"), 403

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return "Basic Auth: Access Granted", 200
    return "401 Unauthorized", 401

@app.route("/basic-protected", methods=['GET'])
@auth.login_required
def index():
    return auth.current_user()

# Manejador para errores 401 cuando falta el token o es inválido
@jwt.unauthorized_loader
def unauthorized_callback(error):
    return "401 Unauthorized", 401


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run()