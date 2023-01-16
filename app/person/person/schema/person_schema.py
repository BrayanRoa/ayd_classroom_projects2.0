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
    
    document_type_id = fields.Nested('DocumentTypeSchema', only=('name',))
    role = fields.Nested('RoleSchema', only=('name',))
    
    @post_load
    def lower_names(self, in_data, **kwargs):
        in_data['names'] = in_data['names'].lower().strip()
        in_data['lastnames'] = in_data['lastnames'].lower().strip()
        return in_data
    

person_schema = PersonSchema()
list_person_schema = PersonSchema(many=True)
    
    

    