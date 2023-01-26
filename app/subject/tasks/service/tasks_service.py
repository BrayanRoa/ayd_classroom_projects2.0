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
        task = db.session.query(TaskEntity).filter(TaskEntity.group_id == id).all()
        return list_task_schema.dump(task)
    except NoResultFound:
        raise NoResultFound(f"Task with id {id} not found")
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
