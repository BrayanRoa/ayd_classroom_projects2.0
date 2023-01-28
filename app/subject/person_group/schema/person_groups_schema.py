from app.ext import ma
from marshmallow import fields, validate, ValidationError


def validate_mail(email):
    if "@ufps.edu.co" not in email:
        raise ValidationError("It is not a valid institutional email")

class PersonGroupSchema(ma.Schema):

    id = fields.Integer()
    person_id = fields.String()
    group_id = fields.Integer()
    cancelled = fields.Boolean()
    state = fields.String(required=True, validate=validate.OneOf(['in_process', 'approved', 'cancelleb']))
    person = fields.Nested('PersonSchema', only=('names', 'lastnames', 'code', 'institutional_mail'))
    group = fields.Nested('GroupSchema', only=('id', 'name', 'subject'))
    subject_id = fields.String()

person_group_schema = PersonGroupSchema()
list_person_group_schema = PersonGroupSchema(many=True)
