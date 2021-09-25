import os

class Config:
    """This are the configurations for the entire app in every environment
    """

class DevConfig(Config):
    """This are the configurations for the development environment

    Args:
        Config ([type]): [description]
    """
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kenmbira:1234@localhost/blogspot'

config_options = {
    'development':DevConfig
}