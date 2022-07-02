from flask import Blueprint
from app.views.timelines import ListTimelinesView, GetTimelineView


TimelinesBlueprint = Blueprint('timelines', __name__, url_prefix='/timelines')

TimelinesBlueprint.add_url_rule('/', view_func=ListTimelinesView.as_view('list-timelines'))
TimelinesBlueprint.add_url_rule('/<pk>', view_func=GetTimelineView.as_view('get-timeline'))
