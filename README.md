# Flask User CRUD API with MongoDB

This is a simple Flask application that provides REST API endpoints for CRUD operations on a User resource. The application uses MongoDB as the database to store user information.

## Prerequisites

- Python 3
- Flask
- PyMongo
- MongoDB Server

## Installation

1. Clone the repository:
```
git clone <link>
```

2.Install the required dependencies:
```
pip install Flask pymongo
```
Start MongoDB server on localhost:27017.

## Usage
1.Run the Flask application:
```bash
python app.py
```
## API Endpoints

### GET /users

Returns a list of all users.

### GET /users/<id>

Returns the user with the specified ID.

### POST /users

Creates a new user with the specified data.

### PUT /users/<id>

Updates the user with the specified ID with the new data.

### DELETE /users/<id>

Deletes the user with the specified ID.

## Testing with Postman
1.Install Postman if you haven't already.

2.Open Postman and create a new HTTP request for each of the API endpoints mentioned above.

3.Send requests to the endpoints to test the CRUD operations on the User resource.

4.Verify that the responses are correct and the database is being updated correctly.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
