from app.db import db
from ..entity.tasks_entity import TaskEntity
from ..schema.tasks_schema import list_task_schema
from sqlalchemy.exc import NoResultFound 

def findAll():
    try:
        task = db.session.query(TaskEntity).all()
        return list_task_schema.dump(task)
    except NoResultFound:
        raise NoResultFound('no homework yet')
    except Exception:
        raise Exception("")
