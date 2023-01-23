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
                group_id=project["group_id"],
                state=project["state"],
                number_of_students=project['number_of_students']
            )
        )
        db.session.commit()
        return project
    except ValidationError as error:
        raise ValidationError(error.messages)
    except Exception as error:
        raise Exception(error.args)    
    
    
    
# * TODO: TERMINAR
def registerExcelOfProjects():
    return ""


def findOneProject(id):
    try:
        project = db.session.query(ProjectEntity).filter(ProjectEntity.id == id).first()
        return project_schema.dump(project)
    except NoResultFound:
        raise NoResultFound(f"there is no project with id {id}")
