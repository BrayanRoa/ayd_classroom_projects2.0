from app.ext import ma
from marshmallow import fields
from app.person.person.schema.person_schema import PersonSchema
from marshmallow.exceptions import ValidationError

def validate_email(email):
    if "@ufps.edu.co" not in email:
        raise ValidationError("It is not a valid institutional email")

class PersonGroupSchema(ma.Schema):
    
    institutional_mail=fields.Email(
        validate=validate_email
    )
    group_id=fields.Integer()
    subject_id = fields.String()
    cancelled=fields.Boolean()
    
person_subject_group = PersonGroupSchema()
persons_subject_group = PersonGroupSchema(many=True)

