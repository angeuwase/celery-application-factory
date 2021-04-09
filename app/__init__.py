from flask import Flask
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from celery import Celery
#from config import config, Config      
from config import Config
import os


# Instantiate Flask Extension Objects
bootstrap = Bootstrap()
mail = Mail()

# Instantiate celery
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL, result_backend=Config.CELERY_BROKER_URL)

def create_app():

    app = Flask(__name__)

    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')

    app.config.from_object(config_type)

    # configure celery
    celery.conf.update(app.config)
    

    # register blueprints
    register_blueprints(app)

    # initialize flask extensions
    initialize_extensions(app)


    return app

def initialize_extensions(app):
    bootstrap.init_app(app)

    mail.init_app(app)

def register_blueprints(app):

    # Import blueprints
    from app.auth import auth_blueprint
    from app.main import main_blueprint



    # Register the blueprints with the flask application instance
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)