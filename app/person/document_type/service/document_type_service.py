from app.db import db
from sqlalchemy.exc import NoResultFound
from marshmallow import ValidationError
from ..entity.document_type_entity import DocumentTypeEntity
from ..schema.document_type_schema import list_document_type_schema, document_type_schema
from ..model.document_type_dto import DocumentTypeDto

DocumentTypeEntity.start_mapper()

def findAll():
    document_types = db.session.query(DocumentTypeEntity).all()
    if not document_types:
        raise NoResultFound('no document types registered yet')
    return list_document_type_schema.dump(document_types)
    

def create(data):
    document = None
    try:
        document = document_type_schema.load(data)
        db.session.add(DocumentTypeDto(name=document['name']))
        db.session.commit()
        return document
    except ValidationError as error:
        raise ValidationError(error.args)
    except Exception as error:
        raise Exception(error.args)
    

def update(id, data):
    try:
        document_type = db.session.query(DocumentTypeEntity).filter_by(id= id).one()
        document_type.name = data['name']
        db.session.commit()
        return document_type_schema.dump(document_type)
    except NoResultFound:
        raise NoResultFound('Document type with id {id} not found')
    except Exception as error:
        raise Exception(error.args)
        