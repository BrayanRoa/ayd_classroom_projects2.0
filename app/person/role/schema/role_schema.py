from app.ext import ma
from marshmallow import fields

class RoleSchema(ma.Schema):
    
    id = fields.Integer()
    name = fields.String(required=True)
    person = fields.Nested('PersonSchema', only=('names', 'lastnames', 'code', 'institutional_mail'))

    
role_schema = RoleSchema()
list_role_schema = RoleSchema(many=True)
