from app.db import db
from sqlalchemy.exc import NoResultFound
from marshmallow import ValidationError
from app.subject.subject.entity.subject_entity import SubjectEntity
from ..schema.subject_schema import list_subject_schema, subject_schema
from ..model.subject_dto import SubjectDto


SubjectEntity.start_mapper()


def findAll():
    subjects = db.session.query(SubjectEntity).all()
    if not subjects:
        raise NoResultFound("no subject registered yet")
    return list_subject_schema.dump(subjects)


def findOneByCode(code):
    try:
        subject = (
            db.session.query(SubjectEntity).filter(SubjectEntity.code == code).one()
        )
        return subject_schema.dump(subject)
    except NoResultFound as error:
        raise NoResultFound(error.args)


def create(data):
    subject = None
    try:
        subject = subject_schema.load(data)
        db.session.add(SubjectDto(code=subject["code"], name=subject["name"]))
        db.session.commit()
        return subject
    except ValidationError as error:
        raise ValidationError(error.args)
    except Exception as error:
        raise Exception(error.args)
