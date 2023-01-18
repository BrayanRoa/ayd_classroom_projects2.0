from app.db import db

class PersonGroupEntity(db.Model):
    
    __tablename__ = 'person_group'
    
    institutional_mail = db.Column(db.String(100), db.ForeignKey('person.institutional_mail'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True)
    cancelled = db.Column(db.Boolean, default=False)