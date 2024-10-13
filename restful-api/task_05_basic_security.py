from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
# Instanciamos las clases
app = Flask(__name__)
auth_basic = HTTPBasicAuth()
auth_token = HTTPTokenAuth(scheme='Bearer')

# Tokens
app.config['SECRET_KEY'] = 'ULTRA SUPER MEGA SECRET KEY'

# Lista de usuarios
users = {
    "axel": generate_password_hash("holacomoestas"),
    "sofia": generate_password_hash("bienyvos")
}

# Verifica contraseñas
@auth_basic.verify_password
def verify_password(username, password):
    if username in users and \
        check_password_hash(users.get(username), password): # Compara contraseñas
        return username

@app.route("/login", methods=['POST'])
@auth_basic.login_required
def login():
    user = auth_basic.current_user()

    token = jwt.encode({
        'username': user
    }, app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'token': token})

@auth_token.verify_token
def verify_token(token):
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return data['username']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    
# Ruta root
@app.route("/")
@auth_token.login_required
def index():
    return "Hello, {}!".format(auth_token.current_user()) # Devuelve username si esta autorizado

if __name__ == '__main__':
    app.run()