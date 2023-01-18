from app.ext import ma
from marshmallow import fields


class PersonGroupSchema(ma.Schema):

    cancelled = fields.Boolean()
    institutional_mail = fields.String()
    group_id = fields.Integer()


group_person_schema = PersonGroupSchema()
list_groups_person_schema = PersonGroupSchema(many=True)
