
from app.ext import ma
from marshmallow import fields

class ProjectPersonSchema(ma.Schema):
    
    institucional_mail = fields.String(required=True)
    project_id = fields.Integer()
    
project_person_schema = ProjectPersonSchema()
list_project_person_schema = ProjectPersonSchema(many=True)
    