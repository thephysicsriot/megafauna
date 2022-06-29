from flask import Blueprint, request
from app.views.auth import register

AuthBlueprint = Blueprint('auth', __name__, url_prefix='/auth')

AuthBlueprint.add_url_rule('/register', view_func=register)
