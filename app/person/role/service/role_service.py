from app.db import db
from sqlalchemy.exc import NoResultFound
from marshmallow import ValidationError  
from app.person.role.entity.role_entity import RoleEntity
from ..schema.role_schema import list_role_schema, role_schema
from ..model.role_dto import RoleDto

RoleEntity.start_mapper()

def findAll():
    roles = db.session.query(RoleEntity).all()
    if not roles:
        raise NoResultFound("no roles registered yet")
    return list_role_schema.dump(roles)


def create(data):
    role = None
    try:
        role = role_schema.dump(data) 
        db.session.add(RoleDto(
            name=role['name']
        ))
        db.session.commit()
        return role
    except ValidationError as error:
        raise ValidationError(error.messages)
    except Exception as error:
        raise Exception(error.args)