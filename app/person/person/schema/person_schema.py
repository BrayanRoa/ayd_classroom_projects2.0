from app.ext import ma
from marshmallow import fields, validate, ValidationError, post_load

def validate_mail(mail):
        if "@ufps.edu.co" not in mail:
            raise ValidationError("It is not a valid institutional email")

class PersonSchema(ma.Schema):
    
    institutional_mail = fields.String(
        required=True, 
        validate=validate_mail,
    )
    
    names = fields.String(required=True, validate=validate.Length(min=3, max=30))
    lastnames = fields.String(required=True, validate=validate.Length(min=3, max=30))
    code = fields.String(required=True, validate=validate.Length(min=7))
    img = fields.String()
    document_type_id = fields.Integer()
    role_id = fields.Integer()
    
    document_type = fields.Nested('DocumentTypeSchema', only=('name',))
    role = fields.Nested('RoleSchema', only=('name',))
    person_group = fields.Nested('PersonGroupSchema', many=True, only=('cancelled', 'state', 'group'))
    
    @post_load
    def lower_names(self, in_data, **kwargs):
        in_data['names'] = in_data['names'].lower().strip()
        in_data['lastnames'] = in_data['lastnames'].lower().strip()
        return in_data
    

person_schema = PersonSchema()
person_schema_out = PersonSchema(exclude=('document_type_id', 'role_id'))
list_person_schema = PersonSchema(many=True, exclude=('document_type_id','role_id', 'person_group'))
# list_person_schema = PersonSchema(many=True, exclude=('document_type_id', 'role_id'))
    
    

    