from app.db import db
from sqlalchemy.exc import NoResultFound
from app.person.person.entity.person_entity import PersonEntity
from app.person.person.schema.person_schema import list_person_schema

def get_all():
    persons = db.session.query(PersonEntity).all()
    if not persons:
        raise NoResultFound('no people registered yet')
    return list_person_schema.dump(persons)
    