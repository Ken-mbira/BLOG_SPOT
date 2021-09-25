from flask import Flask

from config import config_options

def create_app(config_name):
    """This is the app factory
    """
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    #registering blueprints
    from app.auth import auth
    app.register_blueprint(auth)

    return app