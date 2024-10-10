from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(users)

@app.route("/status")
def status():
    return 'OK'

@app.route("/users/<username>")
def getUser(username):
    return jsonify(users[username])

@app.route("/add_user", methods=['POST'])
def addUser():
    data = request.get_json()

    username = data.get('username')
    name = data.get('name')
    age = data.get('age')
    city = data.get('city')

    if username in users:
        return jsonify({'message': 'Username already exists!'}), 400
    
    users[username] = {
        'name': name,
        'age': age,
        'city': city
    }

    response = {
        'message': 'User added successfully!',
        'user': {
            'username': username,
            'name': name,
            'age': age,
            'city': city
        }
    }
    return jsonify(response), 201


if __name__ == "__main__": app.run()