import datetime

from marshmallow import Schema, fields, validate
from src.libs.constants import MAX_FULLNAME_LENGTH, MAX_TITLE_LENGTH, MAX_TEXT_LENGTH



class ContactSchema(Schema):
    name = fields.Str(validate=validate.Length(min=3, max=MAX_FULLNAME_LENGTH), required=True)
    phone = fields.Str(validate=validate.Regexp(r"(\+?\d{12}|\d{10})"))
    email = fields.Email(validate=validate.Email(), required=True)
    birthday = fields.DateTime(format="%Y-%m-%d", validate=lambda x: x < datetime.datetime.now())
    address = fields.Str()


class NoteSchema(Schema):
    title = fields.Str(validate=validate.Length(min=3, max=MAX_TITLE_LENGTH), required=True)
    text = fields.Str(validate=validate.Length(min=1, max=MAX_TEXT_LENGTH))
    tags = fields.Str(required=True)
