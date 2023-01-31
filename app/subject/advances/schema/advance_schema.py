from app.ext import ma
from marshmallow import fields

class AdvanceSchema(ma.Schema):
    
    id = fields.Integer()
    name = fields.String(required=True)
    description = fields.String(required=True)
    link = fields.String()
    state = fields.Boolean()
    delivery_date = fields.Date(
        required=True,
        error_messages={"invalid": "example date: year-month-day"}
    )
    
    project_id = fields.Integer(required=True)
    project = fields.Nested("ProjectSchema", only=('name',))
    
advance_schema = AdvanceSchema()
list_advance_schema = AdvanceSchema(many=True)
    