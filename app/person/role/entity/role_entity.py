from app.db import db
from sqlalchemy.orm import mapper
from ..model.role_dto import RoleDto

class RoleEntity(db.Model):
    
    __tablename__ = 'role'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    person = db.relationship('PersonEntity', back_populates='role')
    
    def __repr__(self) -> str:
        return f"id: {self.id}, name:{self.name}"
    
    def start_mapper():
        mapper(RoleDto, RoleEntity)