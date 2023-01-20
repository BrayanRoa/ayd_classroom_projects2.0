from app.db import db
from sqlalchemy.exc import NoResultFound
from app.person.person.entity.person_entity import PersonEntity
from app.person.person.schema.person_schema import (
    list_person_schema,
    person_schema,
    person_schema_out,
)
from app.person.person.model.person_dto import PersonDto
from marshmallow import ValidationError

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
