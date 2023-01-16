from app.person.role.entity.role_entity import RoleEntity
from app.db import db
from sqlalchemy.exc import NoResultFound
from app.person.role.schema.role_schema import list_role_schema

def get_all():
    roles = db.session.query(RoleEntity).all()
    if not roles:
        raise NoResultFound('no roles registered yet')
    return list_role_schema.dump(roles)