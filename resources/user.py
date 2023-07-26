from flask_restful import Resource, reqparse
from bson.objectid import ObjectId
from .mongodb import get_db

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help='Cannot have blank name')
parser.add_argument('email', type=str, required=True, help='Blank Email')
parser.add_argument('password', type=str, required=True, help='Password blank.')

class UserResource(Resource):
    def get_list(self):
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

    def get(self, user_id=None):
        db = get_db()
        if user_id:
            user = db.users.find_one({'_id': ObjectId(user_id)})
            if user:
                user['_id'] = str(user['_id'])
                return user
            return {'message': 'User not found'}, 404
        else:
            users = db.users.find()
            user_list = []
            for user in users:
                user['_id'] = str(user['_id'])
                user_list.append(user)
            return {'users': user_list}

    def post(self):
        args = parser.parse_args()
        db = get_db()
        user_id = db.users.insert_one(args).inserted_id
        return {'message': 'User created successfully', 'id': str(user_id)}, 201

    def put(self, user_id):
        args = parser.parse_args()
        db = get_db()
        result = db.users.update_one({'_id': ObjectId(user_id)}, {'$set': args})
        if result.modified_count == 1:
            return {'message': 'User updated successfully'}, 200
        return {'message': 'User not found'}, 404

    def delete(self, user_id):
        db = get_db()
        result = db.users.delete_one({'_id': ObjectId(user_id)})
        if result.deleted_count == 1:
            return {'message': 'User deleted successfully'}, 200
        return {'message': 'User not found'}, 404
