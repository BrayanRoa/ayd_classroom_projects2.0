from app.ext import ma
from marshmallow import fields, validate


class GroupSchema(ma.Schema):
    
    id = fields.Integer()
    name = fields.String(required=True)
    number_of_students = fields.Integer(required=True)
    subject_id = fields.String(required=True, validate=validate.Length(min=7, max=8))
    subject = fields.Nested('SubjectSchema', only=('name','code'))
    persons = fields.Nested('PersonSchema', only=('names', 'lastnames', 'code'), many=True)
    task = fields.Nested('TaskSchema', exclude=('group',), many=True)
    
    person_group = fields.Nested('PersonGroupSchema', many=True, only=('cancelled', 'state', 'person'))
    
group_schema = GroupSchema(exclude=('task',))
list_group_schema = GroupSchema(many=True, exclude=('task',))