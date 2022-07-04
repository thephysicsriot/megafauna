from flask import jsonify, request
from flask.views import MethodView
from app.views.auth import login_required
from app.models.character import Character


class ListCharactersView(MethodView):

    @login_required
    def get(self):
        characters = Character.objects().all()
        characters = Character.serialize_many(characters)
        return {'characters': characters}

    @login_required
    def post(self):
        json = request.get_json()
        character = Character(**json)
        character.save()
        return Character.serialize(character)


class GetCharacterView(MethodView):

    @login_required
    def get(self, pk):
        character = Character.objects(_id=pk).first()
        return Character.serialize(character)

    @login_required
    def patch(self, pk):
        json = request.get_json()
        character = Character.objects(_id=pk).first()
        character.modify(**json)
        return Character.serialize(character)

    @login_required
    def delete(self, pk):
        character = Character.objects(_id=pk).first()
        character.delete()
        return jsonify(f'Document {pk} was deleted')
