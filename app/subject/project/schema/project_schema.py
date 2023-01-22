from app.ext import ma
from marshmallow import fields, validate, post_load

class ProjectSchema(ma.Schema):
    
    id = fields.Integer()
    name = fields.String(required=True, validate=validate.Length(min=3, max=50))
    description = fields.String(required=True)
    active = fields.Boolean()
    
    """
    * estados permitidos
    * in process, finished, ???
    """
    state = fields.String(required=True, validate=validate.OneOf(['in process', 'finished']))
    group_id = fields.Integer(required=True)
    
    @post_load
    def lower_names(self, in_data, **kwargs):
        in_data['name'] = in_data['name'].lower().strip()
        in_data['description'] = in_data['description'].lower().strip()
        return in_data
    
project_schema = ProjectSchema()
list_project_schema = ProjectSchema(many=True)