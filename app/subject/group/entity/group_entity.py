from app.db import db
from sqlalchemy.orm import mapper
from ..model.group_dto import GroupDTO


class GroupEntity(db.Model):
    __tablename__ = "group"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(2), nullable=False)
    number_of_students = db.Column(db.Integer, nullable=False)
    subject_id = db.Column(db.String(8), db.ForeignKey("subject.code"))

    subject = db.relationship("SubjectEntity", back_populates="group")

    persons = db.relationship(
        'PersonEntity', 
        primaryjoin="and_(PersonGroupEntity.cancelled==False, PersonGroupEntity.state=='in_process')",
        secondary='person_group', 
        viewonly=True)
    
    projects = db.relationship('ProjectEntity', back_populates='group')

    task = db.relationship(
        'TaskEntity',
        back_populates='group')
    
    def __repr__(self) -> str:
        return f"id: {self.id}, name: {self.name}, number_of_students: {self.number_of_students}, subject_id: {self.subject_id}"

    def start_mapper():
        mapper(GroupDTO, GroupEntity)