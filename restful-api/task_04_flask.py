from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return 'OK'

@app.route("/users/<username>")
def getUser(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=['POST'])
def addUser():
    data = request.get_json()

    username = data.get('username')
    name = data.get('name')
    age = data.get('age')
    city = data.get('city')

    if not isinstance(username, str) or not username:
        return jsonify({"error":"Username is required"}), 400
    
    users[username] = {
        'username': username,
        'name': name,
        'age': age,
        'city': city
    }

    response = {
        'message': 'User added',
        'user': users[username]
    }
    return jsonify(response), 201


if __name__ == "__main__": app.run()