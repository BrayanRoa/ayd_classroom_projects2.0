from app.db import db

class ProjectEntity(db.Model):
    
    __tablename__ = 'project'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    active = db.Column(db.Boolean, default=True)
    state = db.Column(db.String(50))
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))
    
    group = db.relationship('GroupEntity', back_populates='projects')
    
    