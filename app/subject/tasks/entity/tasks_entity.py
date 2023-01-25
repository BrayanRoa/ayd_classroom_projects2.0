from app.db import db
import datetime


class TaskEntity(db.Model):

    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    create_at = db.Column(db.Date, default=datetime.datetime.now().date())
    expired_date = db.Column(db.Date)
    
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))
    group = db.relationship("GroupEntity", back_populates="task")
