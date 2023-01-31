from app.db import db
from sqlalchemy.orm import mapper
from ..model.project_dto import ProjectDTO
from datetime import datetime


class ProjectEntity(db.Model):

    __tablename__ = "project"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    active = db.Column(db.Boolean, default=True)
    state = db.Column(db.String(50))
    number_of_students = db.Column(db.Integer, default=0)
    full = db.Column(db.Boolean, default=False)

    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))
    group = db.relationship("GroupEntity", back_populates="projects")

    person_project = db.relationship("PersonProjectEntity", back_populates=("project"))

    advance = db.relationship("AdvanceEntity", back_populates="project")
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def start_mapper():
        mapper(ProjectDTO, ProjectEntity)
