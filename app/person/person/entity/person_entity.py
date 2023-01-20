from app.db import db
from sqlalchemy.orm import mapper
from app.person.person.model.person_dto import PersonDto

class PersonEntity(db.Model):

    __tablename__ = "person"

    institutional_mail = db.Column(db.String(100), primary_key=True)
    names = db.Column(db.String(30), nullable=False)
    lastnames = db.Column(db.String(30), nullable=False)
    code = db.Column(db.String(7), unique=True, nullable=False)
    img = db.Column(db.String(250), nullable=True)
    document_type_id = db.Column(db.Integer, db.ForeignKey("document_type.id"))
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))

    # many to one
    document_type = db.relationship(
        "DocumentTypeEntity", 
        back_populates="person")
    
    role = db.relationship(
        "RoleEntity", 
        back_populates="person")

    # many to many --> group
    groups = db.relationship(
        "GroupEntity",
        primaryjoin="and_(PersonEntity.institutional_mail == PersonGroupEntity.institutional_mail, PersonGroupEntity.cancelled==False)", 
        secondary="person_group", 
        lazy="joined")
    
    projects = db.relationship("ProjectEntity", secondary="project_person")

    def start_mapper():
        mapper(PersonDto, PersonEntity)