from flask import jsonify, request
from flask.views import MethodView
from app.views.auth import login_required
from app.models.timeline import Timeline


class ListTimelinesView(MethodView):

    @login_required
    def get(self):
        timelines = Timeline.objects().all()
        timelines = [c.to_json() for c in timelines]
        return jsonify(timelines)

    @login_required
    def post(self):
        json = request.get_json()
        timeline = Timeline(**json)
        timeline.save()
        return jsonify(timeline.to_json())


class GetTimelineView(MethodView):

    @login_required
    def get(self, pk):
        timeline = Timeline.objects(id=pk).first()
        return jsonify(timeline.to_json())

    @login_required
    def patch(self, pk):
        json = request.get_json()
        timeline = Timeline.objects(id=pk).first()
        timeline.modify(**json)
        return jsonify(timeline.to_json())