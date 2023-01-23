from app.db import db
from sqlalchemy.exc import NoResultFound
from marshmallow import ValidationError
from sqlalchemy import and_
from ..entity.project_person_entity import ProjectPersonEntity
from ..schema.project_person_schema import (
    list_project_person_schema,
    project_person_schema,
)
from app.person.person.service.person_service import findOneByMail
from app.subject.project.service.project_service import findOneProject
from ..model.project_person_dto import ProjectPersonDTO


ProjectPersonEntity.start_mapper()


def findAll():
    project_person = db.session.query(ProjectPersonEntity).all()
    if not project_person:
        raise NoResultFound("no project person registered yet")
    return list_project_person_schema.dump(project_person)


# * HARIA FALTA VALIDAR QUE LA PERSONA ESTE REGISTRADA EN ESA GRUPO Y EN ESA MATERIA
def registerPersonInProject(data):
    project_person = None
    try:
        project_person = project_person_schema.load(data)
        findOneByMail(project_person["institutional_mail"])
        findOneProject(project_person["project_id"])
        db.session.add(
            ProjectPersonDTO(
                institutional_mail=project_person["institutional_mail"],
                project_id=project_person["project_id"],
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
        project_person = project_person_schema.load(data)
        data = (
            db.session.query(ProjectPersonEntity)
            .filter(
                and_(
                    ProjectPersonEntity.institutional_mail
                    == project_person["institutional_mail"],
                    ProjectPersonEntity.project_id == project_person["project_id"],
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
