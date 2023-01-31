from app.db import db
from sqlalchemy.exc import NoResultFound
from marshmallow import ValidationError
from ..entity.tasks_entity import TaskEntity
from ..schema.tasks_schema import list_task_schema, task_schema
from ..model.task_dto import TaskDTO
from ...group.service.group_service import findPersonOfGroup as findGroupById


TaskEntity.start_mapper()


def findAll():
    try:
        task = db.session.query(TaskEntity).all()
        return list_task_schema.dump(task)
    except NoResultFound:
        raise NoResultFound("no homework yet")
    except Exception as error:
        raise Exception(error.args)


def findByGroupId(id):
    try:
        task = db.session.query(TaskEntity).filter_by(group_id=id).all()
        if len(task) == 0:
            raise NoResultFound(f"Task with id {id} not found")
        return list_task_schema.dump(task)
    except Exception as error:
        raise Exception(error.args)


def deleteTask(id):
    try:
        task = db.session.query(TaskEntity).filter(TaskEntity.id == id).one()
        task.state = True
        db.session.commit()
        return f"task with id {id} successfully removed"
    except NoResultFound:
        raise NoResultFound(f"no exist task with id {id}")


def createTask(data):
    task = None
    try:
        task = task_schema.load(data)
        findGroupById(task["group_id"])
        db.session.add(
            TaskDTO(
                name=task["name"],
                description=task["description"],
                state=False,
                group_id=task["group_id"],
                expired_date=task["expired_date"],
            )
        )
        db.session.commit()
        return task
    except ValidationError as error:
        raise ValidationError(error.messages)


def update(id, data):
    try:
        task = db.session.query(TaskEntity).filter_by(id=id).one()
        if "name" in data:
            task.name = data.get("name")
        if "description" in data:
            task.description = data.get("description")
        if "expired_date" in data:
            task.expired_date = data.get("expired_date")
        if "group_id" in data:
            task.group_id = data.get("group_id")
        db.session.commit()
        return f"task with id {id} updated successfully"
    except ValidationError as error:
        raise ValidationError(error.args)
    except Exception as error:
        raise Exception(error.args)
