from app.db import db


class ProjectPersonEntity(db.Model):
    
    __tablename__ = 'project_person'
    
    institucional_mail = db.Column(db.String(100), db.ForeignKey('person.institutional_mail'), primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), primary_key=True)