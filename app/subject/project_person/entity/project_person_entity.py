from app.db import db
from sqlalchemy.orm import mapper
from ..model.project_person_dto import ProjectPersonDTO
from datetime import datetime

class ProjectPersonEntity(db.Model):
    
    __tablename__ = 'project_person'
    
    institutional_mail = db.Column(db.String(100), db.ForeignKey('person.institutional_mail'), primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    
    def start_mapper():
        mapper(ProjectPersonDTO, ProjectPersonEntity)