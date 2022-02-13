from flask import Flask
from .extensions import db
from .routes import short
from config import Config

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    app.register_blueprint(short)
    return app

