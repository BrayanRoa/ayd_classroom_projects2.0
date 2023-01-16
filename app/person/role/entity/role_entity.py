from app.db import db

class RoleEntity(db.Model):
    
    __tablename__ = 'role'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    person = db.relationship('PersonEntity', back_populates='person')
    
    def __repr__(self) -> str:
        return f"id: {self.id}, name:{self.name}"