from app.db import db
from sqlalchemy.orm import mapper
from ..model.subject_dto import SubjectDto
from datetime import datetime

class SubjectEntity(db.Model):

    __tablename__ = "subject"

    code = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    group = db.relationship('GroupEntity', back_populates='subject')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"code: {self.code}, name:{self.name}"
    
    def start_mapper():
        mapper(SubjectDto, SubjectEntity)
