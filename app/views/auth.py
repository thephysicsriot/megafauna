from flask import request
from app.models.user import User
from mongoengine import NotUniqueError
from flask.views import MethodView


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

        hashed_password = password # going to use bcrypt to hash

        if error is None:
            try:
                user = User(email=email, password=hashed_password)
                user.save()
            except NotUniqueError:
                error = f"User {email} is already registered."
            else:
                return 'You\'re registered!'
        return error
