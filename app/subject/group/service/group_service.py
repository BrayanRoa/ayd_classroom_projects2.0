from app.db import db
from app.subject.group.schema.group_schema import list_group_schema, group_schema
from app.subject.group.entity.group_entity import GroupEntity
from sqlalchemy.exc import NoResultFound


def findAll():
    groups = db.session.query(GroupEntity).all()
    if not groups:
        raise NoResultFound("no groups registered yet")
    return list_group_schema.dump(groups)


def findPersonOfSubject(subject, group):
    try:
        persons = (
            db.session.query(GroupEntity)
            .filter(GroupEntity.id == group, GroupEntity.subject_id == subject)
            .one()
        )
        return group_schema.dump(persons)
    except NoResultFound as error:
        raise NoResultFound(error.args)
    
# * TODO: TERMINAR
def create():
    return ""
