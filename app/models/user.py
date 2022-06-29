from mongoengine import Document, StringField

class User(Document):
    name = StringField()
    email = StringField(unique=True)
    password = StringField()
