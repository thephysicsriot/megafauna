from flask import Blueprint
from app.views.sessions import ListSessionsView, GetSessionView


SessionsBlueprint = Blueprint('sessions', __name__, url_prefix='/sessions')

SessionsBlueprint.add_url_rule('/', view_func=ListSessionsView.as_view('list-sessions'))
SessionsBlueprint.add_url_rule('/<pk>', view_func=GetSessionView.as_view('get-session'))
