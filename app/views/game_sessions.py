from flask import jsonify, request
from flask.views import MethodView
from app.views.auth import login_required
from app.models.game_session import GameSession


class ListGameSessionsView(MethodView):

    @login_required
    def get(self):
        game_sessions = GameSession.objects().all()
        game_sessions = GameSession.serialize_many(game_sessions)
        return {'game_sessions': game_sessions}

    @login_required
    def post(self):
        json = request.get_json()
        game_session = GameSession(**json)
        game_session.save()
        return game_session.serialize()


class GetGameSessionView(MethodView):

    @login_required
    def get(self, pk):
        game_session = GameSession.objects(_id=pk).first()
        return game_session.serialize()

    @login_required
    def patch(self, pk):
        json = request.get_json()
        game_session = GameSession.objects(_id=pk).first()
        game_session.modify(**json)
        return game_session.serialize()

    @login_required
    def delete(self, pk):
        game_session = GameSession.objects(_id=pk).first()
        game_session.delete()
        return jsonify(f'Document {pk} was deleted')