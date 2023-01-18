from app.ext import ma
from marshmallow import fields, validate

class ProjectSchema(ma.Schema):
    
    id = fields.Integer()
    name = fields.String(required=True, validate=validate.Length(min=3, max=50))
    description = fields.String(required=True)
    active = fields.Boolean()
    state = fields.String(required=True)
    group_id = fields.Integer(required=True)
    
project_schema = ProjectSchema()
list_project_schema = ProjectSchema(many=True)