from app.db import db
from sqlalchemy.exc import NoResultFound
from marshmallow import ValidationError
from sqlalchemy import and_
from ..entity.person_project_entity import PersonProjectEntity
from ..schema.person_project_schema import (
    list_person_project_schema,
    person_project_schema,
)
from app.person.person.service.person_service import findOneByMail
from app.subject.project.service.project_service import findOneProject
from ..model.person_project_dto import PersonProjectDTO

PersonProjectEntity.start_mapper()


def findAll():
    person_project = db.session.query(PersonProjectEntity).all()
    if not person_project:
        raise NoResultFound("no project person registered yet")
    return list_person_project_schema.dump(person_project)


# * HARIA FALTA VALIDAR QUE LA PERSONA ESTE REGISTRADA EN ESA GRUPO Y EN ESA MATERIA
def registerPersonInProject(data):
    person_project = None
    try:
        person_project = person_project_schema.load(data)
        findOneByMail(person_project["institutional_mail"])
        findOneProject(person_project["project_id"])
        existePersonInProject(
            person_project["institutional_mail"], person_project["project_id"]
        )
        db.session.add(
            PersonProjectDTO(
                institutional_mail=person_project["institutional_mail"],
                project_id=person_project["project_id"],
            )
        )
        db.session.commit()
        return "Successfully registered person"
    except Exception as error:
        raise Exception(error.args)


# * retirse del proyecto en caso de ser necesario
# * POR EL MOMENTO VOY A ELIMINAR TOTALMENTE DE LA TABLA A LA PERSONA
def withdrawFromProject(data):
    try:
        person_project = person_project_schema.load(data)
        data = (
            db.session.query(PersonProjectEntity)
            .filter(
                and_(
                    PersonProjectEntity.institutional_mail
                    == person_project["institutional_mail"],
                    PersonProjectEntity.project_id == person_project["project_id"],
                )
            )
            .one()
        )
        db.session.delete(data)
        db.session.commit()
        return "successfully retired person"
    except ValidationError as error:
        raise ValidationError(error.args)
    except NoResultFound:
        raise NoResultFound("person or project not found")


def existePersonInProject(mail, project):
    exist = (
        db.session.query(PersonProjectEntity)
        .filter(
            and_(
                PersonProjectEntity.institutional_mail == mail,
                PersonProjectEntity.project_id == project,
            )
        )
        .first()
    )
    if exist:
        raise Exception("the person is already registered in this project")
