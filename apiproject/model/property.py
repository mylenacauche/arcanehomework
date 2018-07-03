from marshmallow import post_load, Schema


class Property():
    def __init__(self, name, description, type, city, pieces_number, caracteristic, owner):
        self.name = name
        self.description = description
        self.type = type
        self.city = city
        self.pieces_number = pieces_number
        self.caracteristic = caracteristic
        self.owner = owner

    def __repr__(self):
        return '<Property(name={self.description!r})>'.format(self=self)


class PropertySchema(Schema):
    @post_load
    def make_income(self, data):
        return Property(**data)

