from flask import Flask
from flask_cors import CORS
from .db import db
from .ext import ma, migrate
from flasgger import Swagger
from app.person.person.controller.person_controller import person
from app.person.role.controller.role_controller import role
from app.person.document_type.controller.document_type_controller import document_type
from app.subject.group.controller.group_controller import group
from app.subject.subject.controller.subject_controller import subject
from app.subject.person_group.controller.person_group_controller import persons_groups
from app.subject.project.controller.project_controller import project
from app.subject.project_person.controller.project_person_controller import project_person
from app.subject.tasks.controller.tasks_controller import task

prefix=f"/api/v1"

def create_app(settings_module):
    app = Flask(__name__)
    
    app.config.from_object(settings_module)
    host = app.config.get('SITE_HOST')
    
    swagger_template = {
        "info": {
            'title': 'Api Python Test',
            'version': '0.1',
            'description': 'This document contains the list of API services '
                           'with Python.',
        },
        "host": host,
        "schemes":["http" , "https"],
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "Authorization: Bearer {token}"
            }   
        },
        "security": [
            {
                "Bearer": []
            }
        ]
    }
    CORS(app, supports_credentials=False)
    Swagger(app, template=swagger_template)
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
    app.register_blueprint(project_person, url_prefix=f"{prefix}/project_person")
    app.register_blueprint(task, url_prefix=f"{prefix}/task")
    
    return app
    