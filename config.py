class Config:
    """This are the configurations for the entire app in every environment
    """

class DevConfig(Config):
    """This are the configurations for the development environment

    Args:
        Config ([type]): [description]
    """
    DEBUG=True

config_options = {
    'development':DevConfig
}