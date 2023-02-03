from app.db import db
from sqlalchemy.exc import NoResultFound
from marshmallow import ValidationError
import pandas as pd
from ...group.service.group_service import findGroup
from ..entity.project_entity import ProjectEntity
from ..schema.project_schema import (
    project_schema,
    list_project_without_persons_schema,
)
from ..model.project_dto import ProjectDTO

ProjectEntity.start_mapper()


def findAll():
    projects = db.session.query(ProjectEntity).all()
    if not projects:
        raise NoResultFound("no projects registered in groups yet")
    return list_project_without_persons_schema.dump(projects)


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
                number_of_students=project["number_of_students"],
            )
        )
        db.session.commit()
        return project
    except ValidationError as error:
        raise ValidationError(error.messages)
    except Exception as error:
        raise Exception(error.args)


# ? 👀 SI ES FINISHED DEBERIA CAMBIAR EL ESTADO A FALSE??
def changeStateProject(id, state):
    try:
        status = ["in_process", "finished"]
        if state in status:
            project = (
                db.session.query(ProjectEntity).filter(ProjectEntity.id == id).one()
            )
            project.state = state
            db.session.commit()
            return f"project: '{project.name}' {state}"
        else:
            raise Exception(f"status {state} is not valid")
    except NoResultFound:
        raise Exception(f"project with id {id} not found")

#* OJO ME FALTA VALIDAR QUE EXISTA EL GRUPO EN EL QUE VOY A REGISTRAR LOS PROYECTOS
def registerExcelOfProjects(file):
    try:
        data = pd.read_excel(file)
        msg = []
        for i, row in data.iterrows():
            if not existProject(row["name"].lower()):
                create(row.to_dict())
            else:
                msg.append(row["name"].lower())
        if len(msg) != 0:
            return f"there are already projects with these names in the database: {msg}"
        return "list of successfully registered projects"     
    except Exception as e:
        raise Exception(e.args)


def findOneProject(id):
    try:
        project = db.session.query(ProjectEntity).filter(ProjectEntity.id == id).one()
        return project_schema.dump(project)
    except NoResultFound:
        raise NoResultFound(f"project with id {id} not found")


def updateProject(id, data):
    try:
        project_schema.load(data)
        project = db.session.query(ProjectEntity).filter_by(id=id).one()

        if "name" in data:
            project.name = data.get("name")
        if "description" in data:
            project.description = data.get("description")
        if "number_of_students" in data:
            project.number_of_students = data.get("number_of_students")

        db.session.commit()
        return f"project updated successfully"
    # except ValidationError as error:
    #     raise ValidationError(error.args)
    except NoResultFound:
        raise NoResultFound(f"project with id {id} not found")


def existProject(name):
    try:
        db.session.query(ProjectEntity).filter(ProjectEntity.name == name).one()
        return True
    except NoResultFound:
        return False