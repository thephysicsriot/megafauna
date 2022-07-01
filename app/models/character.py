from mongoengine import Document, StringField

class Character(Document):
    name = StringField()
    race = StringField()
    player_class = StringField()
    avatar = StringField()

