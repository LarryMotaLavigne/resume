import os

from B2R import secret
from CV.settings import BASE_DIR

ENVIRONMENT_NAME = 'DEVELOPMENT'
ENVIRONMENT_COLOR = 'grey'
DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
INTERNAL_IPS = ['127.0.0.1']  # django-debug-toolbar need

SECRET_KEY = secret.DJANGO_SECRET_KEY

#########################################################
# LinkedIn Info
#########################################################

LINKEDIN_APPLICATION_RETURN_CALLBACK = 'http://localhost:8000/main'
LINKEDIN_PROFILE_URL = secret.LINKEDIN_PROFILE_URL
LINKEDIN_APPLICATION_KEY = secret.LINKEDIN_APPLICATION_KEY
LINKEDIN_APPLICATION_SECRET = secret.LINKEDIN_APPLICATION_SECRET
