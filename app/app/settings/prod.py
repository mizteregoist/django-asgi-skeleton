from .common import *

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

PROD = True
HOST = 'webapp.prod'
ADMINS = [('developer', 'developer@webapp.prod')]

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', HOST]
INTERNAL_IPS = ['0.0.0.0', '127.0.0.1', 'localhost', HOST]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
