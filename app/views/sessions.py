from flask import jsonify, request
from flask.views import MethodView
from app.views.auth import login_required
from app.models.session import Session


class ListSessionsView(MethodView):

    @login_required
    def get(self):
        sessions = Session.objects().all()
        sessions = [c.to_json() for c in sessions]
        return jsonify(sessions)

    @login_required
    def post(self):
        json = request.get_json()
        session = Session(**json)
        session.save()
        return jsonify(session.to_json())


class GetSessionView(MethodView):

    @login_required
    def get(self, pk):
        session = Session.objects(id=pk).first()
        return jsonify(session.to_json())

    @login_required
    def patch(self, pk):
        json = request.get_json()
        session = Session.objects(id=pk).first()
        session.modify(**json)
        return jsonify(session.to_json())