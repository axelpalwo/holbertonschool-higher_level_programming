from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

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
    return jsonify({"error": "User not found"})

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
        'user': {
            'username': username,
            'name': name,
            'age': age,
            'city': city
        }
    }
    return jsonify(response), 201


if __name__ == "__main__": app.run()