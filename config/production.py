DEBUG = False

from main_api import secrets
SECRET_KEY = 'top-secret!'
# Flask settings
FLASK_SECRET_KEY = 'paPTvnNME5NBHHuIOlFqG6zS77vHadbo'

SQLALCHEMY_DATABASE_URI = secrets.SQLALCHEMY_DATABASE_URI_PRODUCTION
#flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
SECRET_KEY = 'paPTvnNME5NBHHuIOlFqG6zS77vHadbo'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
ERROR_404_HELP = False
RESTPLUS_JSON = {
    'separators': (',', ':')
}