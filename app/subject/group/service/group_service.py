from app.db import db
from app.subject.group.schema.group_schema import list_group_schema, group_schema
from app.subject.group.entity.group_entity import GroupEntity
from sqlalchemy.exc import NoResultFound
from marshmallow import ValidationError
from ..model.group_dto import GroupDTO

GroupEntity.start_mapper()


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
    except NoResultFound:
        raise NoResultFound("verify the group and subject code")


def create(data):
    group = None
    try:
        group = group_schema.load(data)
        if findGroup(group["subject_id"], group["name"]):
            return f"the group {group['name']} already exist in subject {group['subject_id']}"
        db.session.add(
            GroupDTO(
                name=group["name"],
                number_of_students=group["number_of_students"],
                subject_id=group["subject_id"],
            )
        )
        db.session.commit()
        return group
    except ValidationError as error:
        raise ValidationError(error.args)
    except Exception as error:
        raise Exception(error.args)


def findGroup(subject, group_name):
    group = (
        db.session.query(GroupEntity)
        .filter(GroupEntity.name == group_name, GroupEntity.subject_id == subject)
        .first()
    )
    if group:
        return True
    return False
