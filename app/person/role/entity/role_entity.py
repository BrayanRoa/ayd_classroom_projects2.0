from app.db import db
from sqlalchemy.orm import mapper
from datetime import datetime
from ..model.role_dto import RoleDto

class RoleEntity(db.Model):
    
    __tablename__ = 'role'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    state = db.Column(db.Boolean, default=True)
    person = db.relationship('PersonEntity', back_populates='role')
    
        
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return f"id: {self.id}, name:{self.name}"
    
    def start_mapper():
        mapper(RoleDto, RoleEntity)