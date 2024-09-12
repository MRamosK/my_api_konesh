from marshmallow import Schema, fields # type: ignore

class CFDRecepcionSchema(Schema):
    """sour
    Schema for serializing and deserializing User objects.

    Attributes:
        id (fields.Int): User ID.
        username (fields.Str): Username.
        email (fields.Str): Email address.
    """
    id = fields.Int(dump_only=True)
    user_name = fields.Str(required=True)
    email = fields.Str(required=True)
