from flask import url_for
from app.tests.unit import TextMixin
from app.models.game_session import GameSession
from flask import json, url_for
from datetime import datetime


class GameSessionViewTest(TextMixin):

    def populate_test_data(self):
        self.game_sesh = GameSession(name='Foo Cave', date_and_time=datetime(2022,7,24)).save()

    def test_get_game_session_list(self):
        self.populate_test_data()
        response = self.authorized_request(
            'get',
            url_for('game_sessions.list-game-sessions'),
        )
        response_json = json.loads(response.data)
        assert isinstance(response_json.get('game_sessions'), list)
        assert response_json.get('game_sessions')[0].get('name') == 'Foo Cave'

    def test_create_game_session(self):
        self.populate_test_data()
        response = self.authorized_request(
            'post',
            url_for('game_sessions.list-game-sessions'),
            data=json.dumps({'name': 'Bar Cave', 'date_and_time': '2022-08-22'})
        )
        response_json = json.loads(response.data)
        assert response_json.get('_id')
        assert response_json.get('name') == 'Bar Cave'
        assert response_json.get('date_and_time') == '2022-08-22'

    def test_get_game_session(self):
        self.populate_test_data()
        response = self.authorized_request(
            'get',
            url_for('game_sessions.get-game-session', pk=str(self.game_sesh._id)),
        )
        response_json = json.loads(response.data)
        assert response_json.get('name') == 'Foo Cave'

    def test_patch_game_session(self):
        self.populate_test_data()
        assert self.game_sesh.name == 'Foo Cave'

        response = self.authorized_request(
            'patch',
            url_for('game_sessions.get-game-session', pk=str(self.game_sesh._id)),
            data=json.dumps({'name': 'Baz Cave'})
        )
        response_json = json.loads(response.data)
        self.game_sesh.reload()
        assert response_json.get('name') == 'Baz Cave'
        assert self.game_sesh.name == 'Baz Cave'

    def test_delete_game_session(self):
        self.populate_test_data()
        response = self.authorized_request(
            'delete',
            url_for('game_sessions.get-game-session', pk=str(self.game_sesh._id)),
        )
        response_json = json.loads(response.data)
        assert f'Document {self.game_sesh._id} was deleted' in response_json
        assert GameSession.objects(_id=self.game_sesh._id).first() is None