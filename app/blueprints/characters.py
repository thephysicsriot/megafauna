from flask import Blueprint
from app.views.characters import ListCharactersView


CharactersBlueprint = Blueprint('characters', __name__, url_prefix='/characters')

CharactersBlueprint.add_url_rule('/', view_func=ListCharactersView.as_view('list-characters'))
