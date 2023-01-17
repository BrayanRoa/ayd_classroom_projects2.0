from app.ext import ma
from marshmallow import fields, validate

class SubjectSchema(ma.Schema):
    
    code = fields.String(required=True, validate=validate.Length(min=7, max=8))
    name = fields.String(required=True, validate=validate.Length(max=30))
    group = fields.Nested('GroupSchema', only=('id', 'name', 'number_of_students'),  many=True)
    
subject_schema = SubjectSchema()
list_subject_schema = SubjectSchema(many=True)