from flask import Blueprint
from app.views.game_sessions import ListGameSessionsView, GetGameSessionView


GameSessionsBlueprint = Blueprint('game_sessions', __name__, url_prefix='/game_sessions')

GameSessionsBlueprint.add_url_rule('/', view_func=ListGameSessionsView.as_view('list-game-sessions'))
GameSessionsBlueprint.add_url_rule('/<pk>', view_func=GetGameSessionView.as_view('get-game-session'))
