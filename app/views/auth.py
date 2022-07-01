import functools
from flask import request, session, g
from app.models.user import User
from mongoengine import NotUniqueError
from flask.views import MethodView
from werkzeug.security import check_password_hash, generate_password_hash


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if g.user_id is None:
            return 'You are not logged in'

        return view(*args, **kwargs)

    return wrapped_view

class LoginView(MethodView):

    def post(self):
        payload = request.get_json()
        email = payload.get('email')
        password = payload.get('password')
        error = None

        user = User.objects(email=email).first()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = str(user.id)
            return 'You are logged in'

        return 'Incorrect email or password'

class RegisterView(MethodView):

    def post(self):
        payload = request.get_json()
        email = payload.get('email')
        password = payload.get('password')
        error = None

        if not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'

        hashed_password = generate_password_hash(password) # going to use bcrypt to hash

        if error is None:
            try:
                user = User(email=email, password=hashed_password)
                user.save()
            except NotUniqueError:
                error = f"User {email} is already registered."
            else:
                return 'You\'re registered!'
        return error
