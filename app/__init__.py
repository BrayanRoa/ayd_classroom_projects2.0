from flask import Flask
from .db import db
from .ext import ma, migrate

prefix=f"/api/v1"

def create_app(settings_module):
    app = Flask(__name__)
    
    app.config.from_object(settings_module)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app)
    
    #* BLUEPRINTS
    # app.register_blueprint(nombre, url_prefix=f"{prefix}/person")
    return app
    