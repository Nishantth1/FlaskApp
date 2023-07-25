from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
mongo_client = MongoClient(app.config["MONGO_URI"])
db = mongo_client.mydatabase  # DataBase with the name 'mydatabase' and the collection as 'users'
users_collection = db.users

# API Endpoints
@app.route('/users', methods=['GET'])
def get_all_users():
    users = users_collection.find()
    data = []
    for user in users:
        data.append({
            'id': str(user['_id']),
            'name': user['name'],
            'email': user['email'],
            'password': user['password']
        })
    return jsonify({'users': data})

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = users_collection.find_one({'_id': ObjectId(id)})
    if user:
        return jsonify({
            'id': str(user['_id']),
            'name': user['name'],
            'email': user['email'],
            'password': user['password']
        })
    else:
        return jsonify({'message': 'User not found'}),404
#         abort(404, description='User not found')

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    if name and email and password:
        user_id = users_collection.insert_one({'name': name, 'email': email, 'password': password}).inserted_id
        return jsonify({'message': 'User created successfully', 'id': str(user_id)}),201
    else:
        return jsonify({'message': 'Name, email, and password are required'}),400

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    if name and email and password:
        result = users_collection.update_one({'_id': ObjectId(id)}, {'$set': {'name': name, 'email': email, 'password': password}})
        if result.modified_count == 1:
            return jsonify({'message': 'User updated successfully'}),200
        else:
            return jsonify({'message': 'User not found'}),404
    else:
        return jsonify({'message': 'Name, email, and password are required'}),400

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    result = users_collection.delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 1:
        return jsonify({'message': 'User deleted successfully'}),200
    else:
        return jsonify({'message': 'User not found'}),404

if __name__ == '__main__':
    app.run(debug=True)
