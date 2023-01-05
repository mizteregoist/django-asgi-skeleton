from .common import *
from .debug import *

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

DEV = True
HOST = 'webapp.dev'
ADMINS = [('developer', 'developer@webapp.dev')]

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', HOST]
INTERNAL_IPS = ['0.0.0.0', '127.0.0.1', 'localhost', HOST]

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'mail')
