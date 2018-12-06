from resume.settings import secret
from resume.settings.base import *

ENVIRONMENT_NAME = 'DEVELOPMENT'
ENVIRONMENT_COLOR = 'grey'
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'database',
        'PORT': 5432,
    }
}


SECRET_KEY = "development_key"


#########################################################
# django-debug-toolbar
#########################################################

# We need this URL variabilisation because we can't prevent which internal URL docker will use
from fnmatch import fnmatch


class glob_list(list):
    def __contains__(self, key):
        for elt in self:
            if fnmatch(key, elt):
                return True
        return False


INTERNAL_IPS = glob_list(['127.0.0.1', '172.*.*.*'])

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
