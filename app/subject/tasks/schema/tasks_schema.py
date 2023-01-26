from app.ext import ma
from marshmallow import fields

class TaskSchema(ma.Schema):
    
    id = fields.Integer()
    name = fields.String(required=True)
    description = fields.String(required=True)
    create_at = fields.Date()
    expired_date = fields.Date()
    group_id = fields.Integer()
    group = fields.Nested('GroupSchema', only=('id', 'name'), many=False)
    
task_schema = TaskSchema()
list_task_schema = TaskSchema(many=True, exclude=('group', 'group_id'))