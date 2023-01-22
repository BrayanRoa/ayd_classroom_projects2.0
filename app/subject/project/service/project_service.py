from app.db import db
from sqlalchemy.exc import NoResultFound
from marshmallow import ValidationError
from ..entity.project_entity import ProjectEntity
from ..schema.project_schema import list_project_schema, project_schema
from ..model.project_dto import ProjectDTO

ProjectEntity.start_mapper()


def findAll():
    projects = db.session.query(ProjectEntity).all()
    if not projects:
        raise NoResultFound("no projects registered in groups yet")
    return list_project_schema.dump(projects)


def create(data):
    project = None
    try:
        project = project_schema.load(data)
        db.session.add(
            ProjectDTO(
                name=project["name"],
                description=project["description"],
                active=project["active"],
                group_id=project["group_id"],
                state=project["state"],
            )
        )
        db.session.commit()
        return project
    except ValidationError as error:
        raise ValidationError(error.args)
    except Exception as error:
        raise Exception(error.args)
