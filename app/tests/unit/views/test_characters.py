from flask import url_for
from app.tests.unit import TextMixin
from app.models.character import Character
from flask import json, url_for


class CharacterViewTest(TextMixin):

    def populate_test_data(self):
        self.char = Character(name='Meilili', race='human').save()

    def test_get_character_list(self):
        self.populate_test_data()
        response = self.authorized_request(
            'get',
            url_for('characters.list-characters'),
        )
        response_json = json.loads(response.data)
        assert isinstance(response_json.get('characters'), list)
        assert response_json.get('characters')[0].get('name') == 'Meilili'

    def test_create_character(self):
        self.populate_test_data()
        response = self.authorized_request(
            'post',
            url_for('characters.list-characters'),
            data=json.dumps({'name': 'Criella', 'race': 'tiefling'})
        )
        response_json = json.loads(response.data)
        assert response_json.get('_id')
        assert response_json.get('name') == 'Criella'
        assert response_json.get('race') == 'tiefling'

    def test_get_character(self):
        self.populate_test_data()
        response = self.authorized_request(
            'get',
            url_for('characters.get-character', pk=str(self.char._id)),
        )
        response_json = json.loads(response.data)
        assert response_json.get('name') == 'Meilili'

    def test_patch_character(self):
        self.populate_test_data()
        assert self.char.name == 'Meilili'

        response = self.authorized_request(
            'patch',
            url_for('characters.get-character', pk=str(self.char._id)),
            data=json.dumps({'name': 'Han'})
        )
        response_json = json.loads(response.data)
        self.char.reload()
        assert response_json.get('name') == 'Han'
        assert self.char.name == 'Han'

    def test_delete_character(self):
        self.populate_test_data()
        response = self.authorized_request(
            'delete',
            url_for('characters.get-character', pk=str(self.char._id)),
        )
        response_json = json.loads(response.data)
        assert f'Document {self.char._id} was deleted' in response_json
        assert Character.objects(_id=self.char._id).first() == None