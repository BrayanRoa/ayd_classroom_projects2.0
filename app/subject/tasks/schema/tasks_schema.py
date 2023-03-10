from app.ext import ma
from marshmallow import fields, validate
import datetime

class TaskSchema(ma.Schema):

    id = fields.Integer()
    name = fields.String()
    description = fields.String()
    state = fields.Boolean()
    create_at = fields.Date()
    expired_date = fields.Date(
        error_messages={"invalid": "example date: year-month-day"}
    )
    group_id = fields.Integer()
    group = fields.Nested("GroupSchema", only=("id", "name"), many=False)


task_schema = TaskSchema()
list_task_schema = TaskSchema(many=True, exclude=("group", "group_id"))