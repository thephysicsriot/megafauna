from flask import Blueprint, request
from app.views.auth import RegisterView

AuthBlueprint = Blueprint('auth', __name__, url_prefix='/auth')

AuthBlueprint.add_url_rule('/register', view_func=RegisterView.as_view('register'))
