from mongoengine import Document, StringField, ObjectIdField
from marshmallow import Schema, fields
from bson.objectid import ObjectId


class CharacterSchema(Schema):
    _id = fields.Str()
    name = fields.Str()
    race = fields.Str()
    player_class = fields.Str()
    avatar = fields.Str()


class Character(Document):
    _id = ObjectIdField(default=lambda: ObjectId(), primary_key=True)
    name = StringField()
    race = StringField()
    player_class = StringField()
    avatar = StringField()

    def serialize(self):
        schema = CharacterSchema()
        return schema.dump(self)

    @classmethod
    def serialize_many(cls, qs):
        schema = CharacterSchema(many=True)
        return schema.dump(qs)

