"""
Django settings for CV project.

"""

import os

from django.conf.global_settings import DATABASES
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy

from B2R import secret

#########################################################
# LinkedIn Info
#########################################################

LINKEDIN_PROFILE_URL = secret.LINKEDIN_PROFILE_URL
LINKEDIN_APPLICATION_KEY = secret.LINKEDIN_APPLICATION_KEY
LINKEDIN_APPLICATION_SECRET = secret.LINKEDIN_APPLICATION_SECRET
URL_WITH_LINKEDIN_AUTH = ['main', 'experiences', 'info', 'passions', 'presentations']
URL_WITHOUT_LINKEDIN_AUTH = ['index']

#########################################################
# Base
#########################################################

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'
INSTALLED_APPS = [
    # Base
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Application
    'core',

    # Debug
    "debug_toolbar",

]

SECRET_KEY = secret.DJANGO_SECRET_KEY

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'core.middleware.LinkedinMiddleware',
]

ROOT_URLCONF = 'CV.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'CV.context_processors.from_settings',  # Admin site color and environment warning
            ],
        },
    },
]

SITE_ID = 1

WSGI_APPLICATION = 'CV.wsgi.application'

#########################################################
#  Environment configuration
#########################################################

if os.getenv('BUILD_ON_TRAVIS', None):
    from B2R.production import *
else:
    from B2R.development import *

#########################################################
# Authentication
#########################################################

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

#########################################################
# Logging
#########################################################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s] %(message)s'
        },
    },
    'loggers': {
        'middleware': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}

#########################################################
# Database
#########################################################

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

#########################################################
# Internationalization
#########################################################

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#########################################################
# Static files
#########################################################

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

#########################################################
# Sentry
#########################################################
# SENTRY_DSN = os.environ.get('SENTRY_DSN')
# if SENTRY_DSN:
#     INSTALLED_APPS += (
#         'raven.contrib.django.raven_compat',
#     )
#     RAVEN_CONFIG = {
#         'dsn': SENTRY_DSN,
#         'release': os.environ.get('HEROKU_SLUG_COMMIT', ''),
#     }
