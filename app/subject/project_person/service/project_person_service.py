from app.db import db
from sqlalchemy.exc import NoResultFound
from ..entity.project_person_entity import ProjectPersonEntity
from ..schema.project_person_schema import list_project_person_schema

def findAll():
    project_person = db.session.query(ProjectPersonEntity).all()
    if not project_person:
        raise NoResultFound('no project person registered yet')
    return list_project_person_schema.dump(project_person)