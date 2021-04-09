# Flask application environment variables (keep them like this)
FLASK_APP = app.py
FLASK_ENV = development
CONFIG_TYPE = config.DevelopmentConfig


# environment variables to specify:
SECRET_KEY = 
MAIL_USERNAME = 
MAIL_PASSWORD =
MAIL_DEFAULT_SENDER = 

# Celery
CELERY_BROKER_URL = redis://localhost:6379
CELERY_RESULT_BACKEND = redis://localhost:6379