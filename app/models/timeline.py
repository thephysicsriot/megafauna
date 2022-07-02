from mongoengine import Document, StringField, DateField, ListField

class Timeline(Document):

    name = StringField()
    date_start = DateField()
    character_list = ListField()
