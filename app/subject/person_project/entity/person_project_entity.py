from app.db import db
from sqlalchemy.orm import mapper
from ..model.person_project_dto import PersonProjectDTO
from datetime import datetime

class PersonProjectEntity(db.Model):
    
    __tablename__ = 'person_project'
    
    id = db.Column(db.Integer, primary_key=True)
    
    person_id = db.Column(db.String(100), db.ForeignKey("person.institutional_mail"))
    person = db.relationship("PersonEntity", back_populates=("person_project"))

    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    project = db.relationship("ProjectEntity", back_populates=("person_project")) 
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def start_mapper():
        mapper(PersonProjectDTO, PersonProjectEntity)