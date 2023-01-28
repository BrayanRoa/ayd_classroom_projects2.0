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
    document_type = db.relationship("DocumentTypeEntity", back_populates="person")
    role = db.relationship("RoleEntity", back_populates="person")

    # many to many
    person_group = db.relationship("PersonGroupEntity", back_populates="person")

    person_project = db.relationship('PersonProjectEntity', back_populates="person")
     
    def start_mapper():
        mapper(PersonDto, PersonEntity)

    def __repr__(self) -> str:
        return f"mail: {self.institutional_mail}, name: {self.names}, person_group: {self.person_group}"
