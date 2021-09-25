from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from config import config_options

def create_app(config_name):
    """This is the app factory
    """
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    #initializing extensions
    db.init_app(app)

    #registering blueprints
    from app.auth import auth
    app.register_blueprint(auth)

    from app.main import main
    app.register_blueprint(main)

    return app