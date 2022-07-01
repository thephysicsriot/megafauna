from flask import Blueprint
from app.views.auth import LoginView, RegisterView

AuthBlueprint = Blueprint('auth', __name__, url_prefix='/auth')

AuthBlueprint.add_url_rule('/login', view_func=LoginView.as_view('login'))
AuthBlueprint.add_url_rule('/register', view_func=RegisterView.as_view('register'))
