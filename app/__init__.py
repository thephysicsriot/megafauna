import os
from flask import Flask, jsonify, session, g
from dotenv import load_dotenv
from mongoengine import connect


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    # Load config from a .env file:
    load_dotenv()
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    MONGODB_URI = os.environ['MONGODB_URI']
    connect(host=MONGODB_URI)

    if int(os.environ['DEBUG']):
        app.debug = True

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .blueprints import auth
    from .blueprints import characters
    from .blueprints import timelines
    app.register_blueprint(auth.AuthBlueprint)
    app.register_blueprint(characters.CharactersBlueprint)
    app.register_blueprint(timelines.TimelinesBlueprint)

    @app.before_request
    def load_user():
        if session.get('user_id'):
            g.user_id = session.get('user_id')
        else:
            g.user_id = None

    return app