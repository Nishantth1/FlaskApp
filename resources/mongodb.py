from flask import g
from flask import current_app as app
from pymongo import MongoClient

def get_db():
    if 'db' not in g:
        g.db = MongoClient(app.config['MONGO_URI']).mydatabase
    return g.db
