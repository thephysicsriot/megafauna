from flask import Blueprint
from app.views.characters import ListCharactersView, GetCharacterView


CharactersBlueprint = Blueprint('characters', __name__, url_prefix='/characters')

CharactersBlueprint.add_url_rule('/', view_func=ListCharactersView.as_view('list-characters'))
CharactersBlueprint.add_url_rule('/<pk>', view_func=GetCharacterView.as_view('get-character'))
