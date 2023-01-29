from app.ext import ma
from marshmallow import fields, ValidationError, post_load


def validate_mail(mail):
    if "@ufps.edu.co" not in mail:
        raise ValidationError("It is not a valid institutional email")


class PersonProjectSchema(ma.Schema):

    person_id = fields.String(required=True, validate=validate_mail)
    project_id = fields.Integer(required=True)
    person = fields.Nested('PersonSchema', only=('names', 'lastnames', 'code', 'institutional_mail'))

    @post_load
    def lower_names(self, in_data, **kwargs):
        in_data['person_id'] = in_data['person_id'].lower().strip()
        return in_data
    
person_project_schema = PersonProjectSchema()
list_person_project_schema = PersonProjectSchema(many=True)