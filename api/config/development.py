# Flask settings
import os
from app import constants

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.abspath(constants.CM_DB_NAME_DEV)

from app import secrets
DEBUG = True
FLASK_SECRET_KEY = 'paPTvnNME5NBHHuIOlFqG6zS77vHadbo'
SQLALCHEMY_DATABASE_URI = secrets.SQLALCHEMY_DATABASE_URI_DEVELOPMENT
SQLALCHEMY_BINDS = {
    'db_cm': 'sqlite:///' + db_path
}
SECRET_KEY = 'paPTvnNME5NBHHuIOlFqG6zS77vHadbo'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
ERROR_404_HELP = False
RESTPLUS_JSON = {
    'separators': (',', ':')
}
CELERY_BROKER_URL = 'amqp://admin:mypass@rabbit:5672/'
#CELERY_BROKER_URL = 'amqp://localhost//'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
UPLOAD_FOLDER = 'uploaded_file'

user = secrets.dev_user
host = secrets.dev_host
password = secrets.dev_password
port = secrets.dev_port
database = secrets.dev_database

MAIL_USERNAME = secrets.MAIL_USERNAME
MAIL_PASSWORD = secrets.MAIL_PASSWORD
MAIL_DEFAULT_SENDER = secrets.MAIL_USERNAME
MAIL_SERVER = secrets.MAIL_SERVER
MAIL_PORT = secrets.MAIL_PORT
