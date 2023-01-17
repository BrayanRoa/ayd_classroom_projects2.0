from app.db import db
from sqlalchemy.exc import NoResultFound
from app.person.document_type.entity.document_type_entity import DocumentTypeEntity
from app.person.document_type.schema.document_type_schema import list_document_type_schema


def findAll():
    document_types = db.session.query(DocumentTypeEntity).all()
    if not document_types:
        raise NoResultFound('no document types registered yet')
    return list_document_type_schema.dump(document_types)
    
    