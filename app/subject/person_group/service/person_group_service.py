from app.db import db
from sqlalchemy.exc import NoResultFound
from sqlalchemy import and_
from ..entity.person_group_entity import PersonGroupEntity
from ..schema.person_groups_schema import list_person_group_schema, person_group_schema
from ..model.person_group_dto import PersonGroupDTO

PersonGroupEntity.start_mapper()


def findAll():
    persons_groups = db.session.query(PersonGroupEntity).all()
    if not persons_groups:
        raise NoResultFound("no persons in groups registered yet")
    return list_person_group_schema.dump(persons_groups)


def activateSubject(mail, group):
    activate = False
    person = (
        db.session.query(PersonGroupEntity)
        .filter(
            and_(
                PersonGroupEntity.person_id == mail,
                PersonGroupEntity.group_id == group,
            )
        )
        .first()
    )
    if not person:
        return activate

    person.cancelled = False
    person.state = "in_process"
    db.session.commit()
    activate = True
    return activate


def changeStateOfSubject(data):
    try:
        info = person_group_schema.load(data)
        person = (
            db.session.query(PersonGroupEntity)
            .filter(
                and_(
                    PersonGroupEntity.person_id == info['person_id'],
                    PersonGroupEntity.group_id == info['group_id'],
                )
            )
            .one()
        )
        if info['state'] == "cancelled":
            person.cancelled = True
            person.state = info['state']
        elif info['state'] == "approved":
            person.cancelled = False
            person.state = info['state']
        db.session.commit()
        return f"subject successfully {info['state']}"
    except NoResultFound as error:
        raise NoResultFound("check the person's mail or group")
    except Exception as error:
        raise Exception(error.args)


def registered_person(data):
    try:
        validate_data = person_group_schema.load(data)
        db.session.add(
            PersonGroupDTO(
                group_id=validate_data["group_id"],
                person_id=validate_data["person_id"],
                cancelleb=False,
                state="in_process",
            )
        )
        db.session.commit()
        return data
    except Exception as error:
        raise Exception(error.args)
