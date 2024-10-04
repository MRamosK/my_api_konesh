from flask import Flask
from .routes.cfd_recepcion import main as cfd_recepcion
from app.modules.modules import db

def create_app() -> Flask:
    app = Flask(__name__)
    
    app.config.from_object('config.Config')
    
    
    db.init_app(app)
    
    app.register_blueprint(cfd_recepcion, url_prefix='/api')
    
    return app