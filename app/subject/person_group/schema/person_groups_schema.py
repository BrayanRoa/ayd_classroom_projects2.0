from app.ext import ma
from marshmallow import fields, validate


class PersonGroupSchema(ma.Schema):

    cancelled = fields.Boolean()
    institutional_mail = fields.String()
    group_id = fields.Integer()
    state = fields.String(required=True, validate=validate.OneOf(['in process', 'approved', 'failed']))


group_person_schema = PersonGroupSchema()
list_groups_person_schema = PersonGroupSchema(many=True)
