from app.db import db
from sqlalchemy.orm import mapper
from ..model.person_group_dto import PersonGroupDTO

class PersonGroupEntity(db.Model):
    
    __tablename__ = 'person_group'
    
    institutional_mail = db.Column(db.String(100), db.ForeignKey('person.institutional_mail'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True)
    cancelled = db.Column(db.Boolean, default=False)
    state = db.Column(db.String(30), default='in process')  
    
    
    def start_mapper():
        mapper(PersonGroupDTO, PersonGroupEntity)
# *👀 estados permitidos en esta tabla
# in process
# approved
# failed