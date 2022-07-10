from flask import jsonify, request
from flask.views import MethodView
from app.views.auth import login_required
from app.models.timeline import Timeline


class ListTimelinesView(MethodView):

    @login_required
    def get(self):
        timelines = Timeline.objects().all()
        timelines = Timeline.serialize_many(timelines)
        return {'timelines': timelines}

    @login_required
    def post(self):
        json = request.get_json()
        timeline = Timeline(**json)
        timeline.save()
        return timeline.serialize()


class GetTimelineView(MethodView):

    @login_required
    def get(self, pk):
        timeline = Timeline.objects(_id=pk).first()
        return timeline.serialize()

    @login_required
    def patch(self, pk):
        json = request.get_json()
        timeline = Timeline.objects(_id=pk).first()
        timeline.modify(**json)
        return timeline.serialize()

    @login_required
    def delete(self, pk):
        timeline = Timeline.objects(_id=pk).first()
        timeline.delete()
        return jsonify(f'Document {pk} was deleted')