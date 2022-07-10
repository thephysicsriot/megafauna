from mongoengine import Document, StringField, DateField, ListField, ObjectIdField
from marshmallow import Schema, fields
from bson.objectid import ObjectId


class GameSessionSchema(Schema):
    _id = fields.Str()
    name = fields.Str()
    date_and_time = fields.Str()
    player_class = fields.Str()
    avatar = fields.Str()


class GameSession(Document):
    _id = ObjectIdField(default=lambda: ObjectId(), primary_key=True)
    name = StringField()
    date_and_time = DateField()
    location = StringField()
    attendees = ListField()

    def serialize(self):
        schema = GameSessionSchema()
        return schema.dump(self)

    @classmethod
    def serialize_many(cls, qs):
        schema = GameSessionSchema(many=True)
        return schema.dump(qs)

