import os

from CV.settings import BASE_DIR

LINKEDIN_APPLICATION_RETURN_CALLBACK = 'http://localhost:8000/main'

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