from flask import jsonify, request
from flask.views import MethodView
from app.views.auth import login_required
from app.models.character import Character


class ListCharactersView(MethodView):

    @login_required
    def get(self):
        characters = Character.objects().all()
        characters = [c.to_json() for c in characters]
        return jsonify(characters)

    @login_required
    def post(self):
        json = request.get_json()
        character = Character(**json)
        character.save()
        return jsonify(character.to_json())


class GetCharacterView(MethodView):

    @login_required
    def get(self, pk):
        character = Character.objects(id=pk).first()
        return jsonify(character.to_json())

    @login_required
    def patch(self, pk):
        json = request.get_json()
        character = Character.objects(id=pk).first()
        character.modify(**json)
        return jsonify(character.to_json())