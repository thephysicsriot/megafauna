from flask import url_for
from app.tests.unit import TextMixin
from app.models.timeline import Timeline
from flask import json, url_for
from datetime import datetime


class TimelineViewTest(TextMixin):

    def populate_test_data(self):
        self.tline = Timeline(name='Megafauna Test', date_start=datetime(2022,7,23)).save()

    def test_get_timeline_list(self):
        self.populate_test_data()
        response = self.authorized_request(
            'get',
            url_for('timelines.list-timelines'),
        )
        response_json = json.loads(response.data)
        assert isinstance(response_json.get('timelines'), list)
        assert response_json.get('timelines')[0].get('name') == 'Megafauna Test'

    def test_create_timeline(self):
        self.populate_test_data()
        response = self.authorized_request(
            'post',
            url_for('timelines.list-timelines'),
            data=json.dumps({'name': 'New Timeline', 'date_start': '2022-03-02'})
        )
        response_json = json.loads(response.data)
        assert response_json.get('_id')
        assert response_json.get('name') == 'New Timeline'
        assert response_json.get('date_start') == '2022-03-02'

    def test_get_timeline(self):
        self.populate_test_data()
        response = self.authorized_request(
            'get',
            url_for('timelines.get-timeline', pk=str(self.tline._id)),
        )
        response_json = json.loads(response.data)
        assert response_json.get('name') == 'Megafauna Test'

    def test_patch_timeline(self):
        self.populate_test_data()
        assert self.tline.name == 'Megafauna Test'

        response = self.authorized_request(
            'patch',
            url_for('timelines.get-timeline', pk=str(self.tline._id)),
            data=json.dumps({'name': 'Megafauna Foo'})
        )
        response_json = json.loads(response.data)
        self.tline.reload()
        assert response_json.get('name') == 'Megafauna Foo'
        assert self.tline.name == 'Megafauna Foo'

    def test_delete_timeline(self):
        self.populate_test_data()
        response = self.authorized_request(
            'delete',
            url_for('timelines.get-timeline', pk=str(self.tline._id)),
        )
        response_json = json.loads(response.data)
        assert f'Document {self.tline._id} was deleted' in response_json
        assert Timeline.objects(_id=self.tline._id).first() == None