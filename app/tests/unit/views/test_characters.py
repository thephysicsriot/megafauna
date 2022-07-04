from flask import url_for
from app.tests.unit import TextMixin
from app.models.character import Character
from flask import json, url_for


class CharacterViewTest(TextMixin):

    def populate_test_data(self):
        char = Character(name='Meilili', race='human').save()

    def test_get(self):
        self.populate_test_data()
        response = self.authorized_request(
            'get',
            url_for('characters.list-characters'),
        )
        response_json = json.loads(response.data)
        assert response_json.get('characters')[0].get('name') == 'Meilili'
