from mongoengine import Document, StringField, DateField, ListField

class GameSession(Document):
    name = StringField()
    date_and_time = DateField()
    location = StringField()
    attendees = ListField()