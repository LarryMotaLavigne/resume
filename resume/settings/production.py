# Need to be redefined and tested

from resume.settings import secret
from resume.settings.base import *

ENVIRONMENT_NAME = 'PRODUCTION'
ENVIRONMENT_COLOR = 'red'
DEBUG = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECURE_HSTS_SECONDS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_PRELOAD = True

SECRET_KEY = secret.DJANGO_SECRET_KEY

#########################################################
# LinkedIn Info
#########################################################

LINKEDIN_APPLICATION_RETURN_CALLBACK = 'http://larry.motalavigne.fr/main'
LINKEDIN_PROFILE_URL = secret.LINKEDIN_PROFILE_URL
LINKEDIN_APPLICATION_KEY = secret.LINKEDIN_APPLICATION_KEY
LINKEDIN_APPLICATION_SECRET = secret.LINKEDIN_APPLICATION_SECRET
