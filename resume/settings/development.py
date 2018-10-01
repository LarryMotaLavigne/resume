from resume.settings import secret
from resume.settings.base import *

ENVIRONMENT_NAME = 'DEVELOPMENT'
ENVIRONMENT_COLOR = 'grey'
DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'resume',
        'USER': 'resume_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
INTERNAL_IPS = ['127.0.0.1']  # django-debug-toolbar need

SECRET_KEY = "development_key"

#########################################################
# LinkedIn Info
#########################################################

LINKEDIN_APPLICATION_RETURN_CALLBACK = 'http://localhost:8000/main'
LINKEDIN_PROFILE_URL = secret.LINKEDIN_PROFILE_URL
LINKEDIN_APPLICATION_KEY = secret.LINKEDIN_APPLICATION_KEY
LINKEDIN_APPLICATION_SECRET = secret.LINKEDIN_APPLICATION_SECRET

INSTALLED_APPS += (
        'debug_toolbar',
    )


MIDDLEWARE += {
    'debug_toolbar.middleware.DebugToolbarMiddleware',
}
