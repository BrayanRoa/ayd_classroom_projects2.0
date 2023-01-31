from app.db import db
from datetime import datetime
import json
from sqlalchemy.orm import mapper
from ..model.advance_dto import AdvanceDto

class AdvanceEntity(db.Model):
    
    __tablename__ = 'advance'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(250))
    link = db.Column(db.String(300))
    state = db.Column(db.Boolean, default=False)
    delivery_date = db.Column(db.Date)
    
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"))
    project = db.relationship("ProjectEntity", back_populates="advance")
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def start_mapper():
        mapper(AdvanceDto, AdvanceEntity)
    
    def __repr__(self) -> str:
        return json.dumps({
            "id": self.id,
            "description": self.description,
            "link": self.link,
            "state":self.state,
            "delivery_date":self.delivery_date,
            "project_id":self.project_id,
            "created_at":self.created_at,
            "updated_at":self.updated_at
        })