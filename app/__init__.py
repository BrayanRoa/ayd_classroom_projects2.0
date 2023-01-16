from flask import Flask
from .db import db
from .ext import ma, migrate
from app.person.person.controller.person_controller import person
from app.person.role.controller.role_controller import role
from app.person.document_type.controller.document_type_controller import document_type

prefix=f"/api/v1"

def create_app(settings_module):
    app = Flask(__name__)
    
    app.config.from_object(settings_module)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app)
    
    #* BLUEPRINTS
    app.register_blueprint(person, url_prefix=f"{prefix}/person")
    app.register_blueprint(role, url_prefix=f"{prefix}/role")
    app.register_blueprint(document_type, url_prefix=f"{prefix}/document_type")
    return app
    