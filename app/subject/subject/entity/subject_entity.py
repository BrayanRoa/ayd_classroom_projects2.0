from app.db import db
from sqlalchemy.orm import mapper
from ..model.subject_dto import SubjectDto

class SubjectEntity(db.Model):

    __tablename__ = "subject"

    code = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    group = db.relationship('GroupEntity', back_populates='subject')
    
    def __repr__(self) -> str:
        return f"code: {self.code}, name:{self.name}"
    
    def start_mapper():
        mapper(SubjectDto, SubjectEntity)
