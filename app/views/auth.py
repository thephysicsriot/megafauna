import functools
from flask import jsonify, request, session, g, abort
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

        user = User.objects(email=email).first()

        if user is None:
            return jsonify(status_code=401, text='Incorrect email.'), 401
        if not check_password_hash(user.password, password):
            return jsonify(status_code=401, text='Incorrect password.'), 401

        else:
            session.clear()
            session['user_id'] = str(user.id)
            return jsonify(text='Login successful.'), 200

class RegisterView(MethodView):

    def post(self):
        payload = request.get_json()
        email = payload.get('email')
        password = payload.get('password')

        if not email:
            return jsonify(status_code=400, text='Email is required.'), 400
        if not password:
            return jsonify(status_code=400, text='Password is required.'), 400

        hashed_password = generate_password_hash(password) # going to use bcrypt to hash

        try:
            user = User(email=email, password=hashed_password)
            user.save()
        except NotUniqueError as e:
            return jsonify(status_code=400, text=f'User {email} is already registered.', error=repr(e)), 400
        else:
            return jsonify(status_code=200, text='Register successful.'), 200

