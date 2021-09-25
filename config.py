import os

class Config:
    """This are the configurations for the entire app in every environment
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'

class DevConfig(Config):
    """This are the configurations for the development environment

    Args:
        Config ([type]): [description]
    """
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kenmbira:1234@localhost/blogspot'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

config_options = {
    'development':DevConfig
}