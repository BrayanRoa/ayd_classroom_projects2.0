from app.db import db
from sqlalchemy.orm import mapper
from ..model.person_group_dto import PersonGroupDTO
from datetime import datetime
class PersonGroupEntity(db.Model):
    
    __tablename__ = 'person_group'
    
    institutional_mail = db.Column(db.String(100), db.ForeignKey('person.institutional_mail'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True)
    cancelled = db.Column(db.Boolean, default=False)
    state = db.Column(db.String(30), default='in_process')  
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def start_mapper():
        mapper(PersonGroupDTO, PersonGroupEntity)
# *👀 estados permitidos en esta tabla
# in_process
# approved
# cancel