"""
Django settings for project.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _


def show_toolbar_callback(*args, **kwargs) -> bool:
    """
    When debug enabled
    """
    if os.environ.get('ENV') == 'local' or os.environ.get('ENV') == 'dev':
        return True
    return False


def db_host(*args, **kwargs) -> str:
    """
    Get postgres host
    """
    if os.environ.get('ENV') == 'prod':
        return 'prod-pgsql'
    elif os.environ.get('ENV') == 'dev':
        return 'dev-pgsql'
    return 'host.docker.internal'


def redis_host(*args, **kwargs) -> str:
    """
    Get redis host
    """
    if os.environ.get('ENV') == 'prod':
        return 'prod-redis'
    elif os.environ.get('ENV') == 'dev':
        return 'dev-redis'
    return 'host.docker.internal'


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

APPEND_SLASH = True
PREPEND_WWW = False

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap5',
    'channels',
    'frontend.apps.FrontendConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# Channels
ASGI_APPLICATION = 'app.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [(redis_host(), 6379)],
            "symmetric_encryption_keys": [SECRET_KEY],
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PGSQL_NAME'),
        'USER': os.environ.get('PGSQL_USER'),
        'PASSWORD': os.environ.get('PGSQL_PASS'),
        'HOST': db_host(),
        'PORT': 5432,
    }
}

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

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LANGUAGE_CODE = 'ru-ru'

LANGUAGES = [
    ('ru', _('Russian')),
    ('en', _('English')),
]

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

ACCOUNT_ACTIVATION_DAYS = 2

LOGIN_URL = '/auth/login/'
LOGOUT_URL = '/auth/logout/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# AUTH_USER_MODEL = 'common.User'
FIXTURE_DIRS = [os.path.join(BASE_DIR, 'fixtures')]

ENV = os.environ.get('ENV')
PROD = False
DEV = False
LOCAL = False
