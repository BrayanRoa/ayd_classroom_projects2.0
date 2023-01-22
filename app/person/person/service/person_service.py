from app.db import db
from app.ext import s3
from marshmallow import ValidationError
from sqlalchemy.exc import NoResultFound
from app.person.person.entity.person_entity import PersonEntity
from app.person.person.schema.person_schema import (
    list_person_schema,
    person_schema,
    person_schema_out,
)
from ..model.person_dto import PersonDto
from app.subject.person_group.service.person_group_service import (
    activateSubject,
)
from app.subject.person_group.service.person_group_service import registered_person
import pandas as pd
import os


PersonEntity.start_mapper()


def findAll():
    persons = db.session.query(PersonEntity).all()
    if not persons:
        raise NoResultFound("no people registered yet")
    return list_person_schema.dump(persons)


def findOneByMail(mail):
    try:
        person = (
            db.session.query(PersonEntity)
            .filter(PersonEntity.institutional_mail == mail)
            .one()
        )
        return person_schema_out.dump(person)
    except NoResultFound:
        raise NoResultFound(f"no exist person with email {mail}")


def findTeachers():
    teachers = db.session.query(PersonEntity).filter(PersonEntity.role_id == 1).all()
    if not teachers:
        raise NoResultFound("no teachers registered yet")
    return list_person_schema.dump(teachers)


def create(data):
    person = None
    try:
        person = person_schema.load(data)
        db.session.add(
            PersonDto(
                institutional_mail=person["institutional_mail"],
                names=person["names"],
                lastnames=person["lastnames"],
                code=person["code"],
                document_type_id=person["document_type_id"],
                role_id=person["role_id"],
                img=person["img"],
            )
        )
        db.session.commit()
        return person
    except ValidationError as error:
        raise ValidationError(error.messages)
    except Exception as error:
        raise Exception(error.args)


def registerInCourse(data):
    try:
        if get_person_of_subject(
            data
        ):  # SOLO ME MUESTRA LOS GRUPOS QUE LA PERSONA TENGA ACTIVOS CANCELLD:FALSE Y STATE: IN PROCESS
            return {"msg": "the person is already registered in the matter"}
        else:
            exist = activateSubject(  # SI YA ESTABA PERO LA HABIA PERDIDO O CANCELADO ENTONCES ACTIVAMOS LA MATERIA
                data["institutional_mail"], data["group_id"]
            )
            if exist:
                return "successfully registered person"
            else:
                return registered_person(data)
    except Exception as error:
        raise Exception(error.args)


def get_person_of_subject(data):
    try:
        exist = (
            db.session.query(PersonEntity)
            .filter(PersonEntity.institutional_mail == data["institutional_mail"])
            .one()
        )
        for info in exist.groups:
            if info.id == data["group_id"] and info.subject_id == data["subject_id"]:
                return True
        return False
    except NoResultFound:
        raise NoResultFound(f"no exist person with email {data['institutional_mail']}")


# * TODO: TERMINAR
def UpdateImage(file):
    print(file)
    s3.upload_file(file.filename, 'ayd-project', file.filename)
    os.remove(file.filename)
    return 'file upload'
