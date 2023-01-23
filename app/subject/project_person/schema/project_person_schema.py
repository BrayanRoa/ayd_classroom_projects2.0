from app.ext import ma
from marshmallow import fields, ValidationError


def validate_mail(mail):
    if "@ufps.edu.co" not in mail:
        raise ValidationError("It is not a valid institutional email")


class ProjectPersonSchema(ma.Schema):

    institutional_mail = fields.String(required=True, validate=validate_mail)
    project_id = fields.Integer(required=True)


project_person_schema = ProjectPersonSchema()
list_project_person_schema = ProjectPersonSchema(many=True)
