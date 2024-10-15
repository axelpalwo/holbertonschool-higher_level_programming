from flask import Flask, jsonify, abort, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash

# Instanciamos la Aplicacion
app = Flask(__name__)

# Clave secreta para los tokens
app.config['JWT_SECRET_KEY'] = 'ULTRA SUPER MEGA SECRET KEY'

# Instanciamos JWT Manager
jwt = JWTManager(app)

# Lista de usuarios
users = {
    "axel": {
        "username": "axel",
        "password": generate_password_hash("holacomoestas"),
        "role": "admin"
    },
    "sofia": {
        "username": "sofia",
        "password": generate_password_hash("bienyvos"),
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
    if username not in users or not check_password_hash(users[username]["password"], password):
        return jsonify({"msg": "Bad username or password"}), 401

    # Crear un token con la identidad del usuario y su rol
    access_token = create_access_token(identity={"username": username, "role": users[username]["role"]})
    return jsonify(access_token=access_token)

# Ruta protegida solo para administradores
@app.route("/admin-only", methods=['GET'])
@jwt_required()
def admin_only():

    current_user = get_jwt_identity()

    if current_user['role'] != 'admin':
        abort(403)

    return jsonify({"message": "Admin Access: Granted"}), 200

@app.route("/", methods=['GET'])
@jwt_required()
def index():
    # Obtener identidad del usuario desde el token JWT
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run()