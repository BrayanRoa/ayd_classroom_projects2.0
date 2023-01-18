from flask import Flask
from .db import db
from .ext import ma, migrate
from app.person.person.controller.person_controller import person
from app.person.role.controller.role_controller import role
from app.person.document_type.controller.document_type_controller import document_type
from app.subject.group.controller.group_controller import group
from app.subject.subject.controller.subject_controller import subject
from app.subject.person_group.controller.person_group_controller import persons_groups
from app.subject.project.controller.project_controller import project
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
    app.register_blueprint(group, url_prefix=f"{prefix}/group")
    app.register_blueprint(subject, url_prefix=f"{prefix}/subject")
    app.register_blueprint(persons_groups, url_prefix=f"{prefix}/person_group")
    app.register_blueprint(project, url_prefix=f"{prefix}/project")
    
    return app
    