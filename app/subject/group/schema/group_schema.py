from app.ext import ma
from marshmallow import fields, validate


class GroupSchema(ma.Schema):
    
    id = fields.Integer()
    name = fields.String(required=True)
    number_of_students = fields.Integer(required=True)
    subject_id = fields.String(required=True, validate=validate.Length(min=7, max=8))
    subject = fields.Nested('SubjectSchema', only=('name',))
    
group_schema = GroupSchema()
list_group_schema = GroupSchema(many=True)
    