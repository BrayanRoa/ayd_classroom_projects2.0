from app.db import db
from app.subject.group.schema.group_schema import list_group_schema
from app.subject.group.entity.group_entity import GroupEntity
from sqlalchemy.exc import NoResultFound

def findAll():
    groups = db.session.query(GroupEntity).all()
    if not groups:
        raise NoResultFound('no groups registered yet')
    return list_group_schema.dump(groups)