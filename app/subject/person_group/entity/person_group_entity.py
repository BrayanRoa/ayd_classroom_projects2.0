from app.db import db
from sqlalchemy.orm import mapper
from ..model.person_group_dto import PersonGroupDTO
from datetime import datetime


class PersonGroupEntity(db.Model):

    __tablename__ = "person_group"

    id = db.Column(db.Integer, primary_key=True)

    person_id = db.Column(db.String(100), db.ForeignKey("person.institutional_mail"))
    person = db.relationship("PersonEntity", back_populates=("person_group"))

    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))
    group = db.relationship("GroupEntity", back_populates=("person_group"))

    cancelled = db.Column(db.Boolean, default=False)
    state = db.Column(db.String(30), default="in_process")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def start_mapper():
        mapper(PersonGroupDTO, PersonGroupEntity)

    def __repr__(self) -> str:
        return f"person_id: {self.person_id}, group_id: {self.group_id}, cancelled: {self.cancelled}, state: {self.state}, group: {self.group}"


# *👀 estados permitidos en esta tabla
# in_process
# approved
# cancel
