import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from mongoengine import connect


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    # Load config from a .env file:
    load_dotenv()
    MONGODB_URI = os.environ['MONGODB_URI']
    connect(host=MONGODB_URI)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .blueprints import auth
    app.register_blueprint(auth.AuthBlueprint)


    return app