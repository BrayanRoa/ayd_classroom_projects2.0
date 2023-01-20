from app.ext import ma
from marshmallow import fields, validate, ValidationError


def validate_mail(email):
    if "@ufps.edu.co" not in email:
        raise ValidationError("It is not a valid institutional email")

class PersonGroupSchema(ma.Schema):

    cancelled = fields.Boolean()
    institutional_mail = fields.String(required=True, validate=validate_mail)
    group_id = fields.Integer()
    state = fields.String(required=True, validate=validate.OneOf(['in process', 'approved', 'failed']))
    subject_id = fields.String()

person_group_schema = PersonGroupSchema()
list_person_group_schema = PersonGroupSchema(many=True)
