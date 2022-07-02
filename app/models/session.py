from mongoengine import Document, StringField, DateField, ListField

class Session(Document):
    name = StringField()
    date_and_time = DateField()
    location = StringField()
    attendees = ListField()