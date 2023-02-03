from app.ext import ma
from marshmallow import fields, validate, post_load

class SubjectSchema(ma.Schema):
    
    code = fields.String(required=True, validate=validate.Length(min=7, max=8))
    name = fields.String(required=True, validate=validate.Length(max=30))
    group = fields.Nested('GroupSchema', only=('id', 'name', 'number_of_students'),  many=True)

    @post_load
    def lower_names(self, in_data, **kwargs):
        in_data['name'] = in_data['name'].lower().strip()
        in_data['code'] = in_data['code'].strip()
        return in_data
        
subject_schema = SubjectSchema()
list_subject_schema = SubjectSchema(many=True)