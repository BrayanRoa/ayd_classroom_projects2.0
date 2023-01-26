from app.db import db
import datetime
from sqlalchemy.orm import mapper
from ..model.task_dto import TaskDTO

class TaskEntity(db.Model):

    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    create_at = db.Column(db.Date, default=datetime.datetime.now().date())
    expired_date = db.Column(db.Date)
    state = db.Column(db.Boolean, default=False) #* TRUE --> TAREA ELIMINADA
    
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))
    group = db.relationship("GroupEntity", back_populates="task")

    
    def start_mapper():
        mapper(TaskDTO, TaskEntity)