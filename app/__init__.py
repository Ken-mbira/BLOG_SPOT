from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

from config import config_options

def create_app(config_name):
    """This is the app factory
    """
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    #initializing extensions
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    #registering blueprints
    from app.auth import auth
    app.register_blueprint(auth)

    from app.main import main
    app.register_blueprint(main)

    return app