from flask import jsonify
from flask.views import MethodView
from app.views.auth import login_required
from app.models.character import Character

class ListCharactersView(MethodView):

    @login_required
    def get(self):
      characters = Character.objects().all()
      characters = [c.to_json() for c in characters]
      return jsonify(characters)

