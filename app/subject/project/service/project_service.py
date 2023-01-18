from app.db import db
from sqlalchemy.exc import NoResultFound
from ..entity.project_entity import ProjectEntity
from ..schema.project_schema import list_project_schema

def findAll():
    projects = db.session.query(ProjectEntity).all()
    if not projects:
        raise NoResultFound('no projects registered in groups yet')
    return list_project_schema.dump(projects)
    