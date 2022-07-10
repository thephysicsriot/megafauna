from mongoengine import Document, StringField, DateField, ListField, ObjectIdField
from marshmallow import Schema, fields
from app.models.character import CharacterSchema
from bson.objectid import ObjectId


class TimelineSchema(Schema):
    _id = fields.Str()
    name = fields.Str()
    date_start = fields.Str()
    characters_list = fields.List(fields.Nested(CharacterSchema))


class Timeline(Document):

    _id = ObjectIdField(default=lambda: ObjectId(), primary_key=True)
    name = StringField()
    date_start = DateField()
    character_list = ListField()

    def serialize(self):
        schema = TimelineSchema()
        return schema.dump(self)

    @classmethod
    def serialize_many(cls, qs):
        schema = TimelineSchema(many=True)
        return schema.dump(qs)

