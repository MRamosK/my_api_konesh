import json

class Config:
    """
    Configuration class for the Flask application.
    """
    with open('config.json') as config_file:
        config = json.load(config_file)
    
    SQLALCHEMY_DATABASE_URI = config['DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
