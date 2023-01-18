from app.db import db
from ..entity.person_group_entity import PersonGroupEntity
from sqlalchemy.exc import NoResultFound
from ..schema.person_groups_schema import list_groups_person_schema

def findAll():
    persons_groups = db.session.query(PersonGroupEntity).all()
    if not persons_groups:
        raise NoResultFound('no persons in groups registered yet')
    return list_groups_person_schema.dump(persons_groups)