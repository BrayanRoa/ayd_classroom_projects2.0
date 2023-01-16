from app.ext import ma
from marshmallow import fields

class DocumentTypeSchema(ma.Schema):
    
    id = fields.Integer()
    name = fields.String(required=True)
    person = fields.Nested('PersonSchema', only=('names', 'lastnames', 'code', 'institutional_mail'))

document_type_schema = DocumentTypeSchema()
list_document_type_schema = DocumentTypeSchema(many=True)