from app.db import db
from sqlalchemy.exc import NoResultFound
from sqlalchemy import and_
from ..entity.person_group_entity import PersonGroupEntity
from ..schema.person_groups_schema import list_groups_person_schema


def findAll():
    persons_groups = db.session.query(PersonGroupEntity).all()
    if not persons_groups:
        raise NoResultFound("no persons in groups registered yet")
    return list_groups_person_schema.dump(persons_groups)


def cancelSubject(mail, group):
    try:
        person = (
            db.session.query(PersonGroupEntity)
            .filter(
                and_(
                    PersonGroupEntity.institutional_mail == mail,
                    PersonGroupEntity.group_id == group,
                )
            )
            .one()
        )
        person.cancelled = True
        person.state = "failed"
        db.session.commit()
        return "Subject cancelled"
    except NoResultFound as error:
        raise NoResultFound(error.args)
    except Exception as error:
        raise Exception(error.args)

