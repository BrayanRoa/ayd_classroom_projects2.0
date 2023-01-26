from app.db import db
from ..entity.tasks_entity import TaskEntity
from ..schema.tasks_schema import list_task_schema
from sqlalchemy.exc import NoResultFound


def findAll():
    try:
        task = db.session.query(TaskEntity).all()
        return list_task_schema.dump(task)
    except NoResultFound:
        raise NoResultFound("no homework yet")
    except Exception:
        raise Exception("")


def findByGroupId(id):
    try:
        task = db.session.query(TaskEntity).filter(TaskEntity.group_id == id).all()
        return list_task_schema.dump(task)
    except NoResultFound:
        raise NoResultFound("no homework yet")
    except Exception:
        raise Exception("")


def deleteTask(id):
    try:
        task = db.session.query(TaskEntity).filter(TaskEntity.id == id).one()
        db.session.delete(task)
        db.session.commit()
        return f"task with id {id} successfully removed"
    except NoResultFound:
        raise NoResultFound(f"no exist task with id {id}")
