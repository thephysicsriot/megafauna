from app import create_app
from app.config import configs
from mongoengine import connect, disconnect
from unittest import TestCase

class TextMixin(TestCase):

    def setUp(self):
        app = create_app()
        app.config.from_object(configs.get('testing'))

        disconnect()
        connect('test', host=app.config.get('MONGODB_URI'))


    def tearDown(self):
        disconnect()
