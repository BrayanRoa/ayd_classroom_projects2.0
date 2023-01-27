from app.db import db
import datetime
from sqlalchemy.orm import mapper
from ..model.task_dto import TaskDTO
from datetime import datetime

class TaskEntity(db.Model):

    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    expired_date = db.Column(db.Date)
    state = db.Column(db.Boolean, default=False) #* TRUE --> TAREA ELIMINADA
    
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))
    group = db.relationship("GroupEntity", back_populates="task")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def start_mapper():
        mapper(TaskDTO, TaskEntity)