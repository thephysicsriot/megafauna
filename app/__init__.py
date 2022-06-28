import os
from flask import Flask, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    # Load config from a .env file:
    load_dotenv()
    MONGODB_URI = os.environ['MONGODB_URI']

    client = MongoClient(MONGODB_URI)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/user')
    # just testing db connection
    def user():
        dev_db = client['dev']
        users = dev_db.users
        user = users.find_one()
        return jsonify(user.get('name'))

    return app