# Need to be redefined and tested

from CV.settings import secret
from CV.settings.base import *

ENVIRONMENT_NAME = 'PRODUCTION'
ENVIRONMENT_COLOR = 'red'
DEBUG = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = secret.DJANGO_SECRET_KEY

#########################################################
# LinkedIn Info
#########################################################

LINKEDIN_APPLICATION_RETURN_CALLBACK = 'http://localhost:8000/main'
LINKEDIN_PROFILE_URL = secret.LINKEDIN_PROFILE_URL
LINKEDIN_APPLICATION_KEY = secret.LINKEDIN_APPLICATION_KEY
LINKEDIN_APPLICATION_SECRET = secret.LINKEDIN_APPLICATION_SECRET
