from app import create_app
from app.config import configs
from mongoengine import connect, disconnect
from unittest import TestCase
from app.models.user import User

class TextMixin(TestCase):

    def setUp(self):
        app = create_app()
        self.app = app
        app.config.from_object(configs.get('testing'))

        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

        disconnect()
        connect('test', host=app.config.get('MONGODB_URI'))

    def tearDown(self):
        disconnect()
        self.app_context.pop()


    def authorized_request(self, method, url, data=None, params=None, content_type="application/json",):
        user = User(name='kristen', email='kristen@email.com')
        user.save()
        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = str(user.id)
        req = getattr(self.client, method)
        headers = {"Content-Type": content_type}
        options = {"data": data, "headers": headers, "content_type": content_type}
        if params:
            options["query_string"] = params
        res = req(url, **options)
        return res