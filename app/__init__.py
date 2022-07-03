import os
from flask import Flask, jsonify, session, g
from dotenv import load_dotenv
from mongoengine import connect
from app.config import configs


def configure_app(app):
    load_dotenv()
    config_env = app.env
    app.config.from_object(configs.get(config_env, 'development'))
    connect(host=app.config.get('MONGODB_URI'))

def register_blueprints(app):
    from .blueprints import auth
    from .blueprints import characters
    from .blueprints import game_sessions
    from .blueprints import timelines
    app.register_blueprint(auth.AuthBlueprint)
    app.register_blueprint(characters.CharactersBlueprint)
    app.register_blueprint(game_sessions.GameSessionsBlueprint)
    app.register_blueprint(timelines.TimelinesBlueprint)

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    configure_app(app)
    register_blueprints(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.before_request
    def load_user():
        if session.get('user_id'):
            g.user_id = session.get('user_id')
        else:
            g.user_id = None

    return app