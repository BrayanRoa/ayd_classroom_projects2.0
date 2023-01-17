from app.db import db
from sqlalchemy.exc import NoResultFound
from app.subject.subject.entity.subject_entity import SubjectEntity
from ..schema.subject_schema import list_subject_schema


def findAll():
    subjects = db.session.query(SubjectEntity).all()
    if not subjects:
        raise NoResultFound('no subject registered yet')
    return list_subject_schema.dump(subjects)