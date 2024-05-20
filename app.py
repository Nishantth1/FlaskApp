from flask import Flask, jsonify
from flask_restful import Api, Resource
from resources.user import UserResource

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"

api = Api(app)

# Define the root resource
class RootResource(Resource):
    def get(self):
        return jsonify({"message": "Welcome to the API"})

# Add resources to the API
api.add_resource(RootResource, '/')
api.add_resource(UserResource, '/users', '/users/<string:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
