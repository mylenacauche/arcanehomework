from flask import json
from marshmallow import post_load, Schema, fields


class Property():
    def __init__(self, name, description, type, city, pieces_number, caracteristic, owner):
        self.name = name
        self.description = description
        self.type = type
        self.city = city
        self.pieces_number = pieces_number
        self.caracteristic = caracteristic
        self.owner = owner


class PropertySchema(Schema):
    name = fields.Str(load_from='name')
    description = fields.Str(load_from='description')
    type = fields.Str(load_from='type')
    city = fields.Str(load_from='city')
    pieces_number = fields.Int(load_from='pieces_number')
    caracteristic = fields.Str(load_from='caracteristic')
    owner = fields.Str(load_from='owner')

    @post_load
    def add_property(self, data):
        return Property(**data)

