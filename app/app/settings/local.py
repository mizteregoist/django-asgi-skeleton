from .common import *
from .debug import *

LOCAL = True
HOST = 'webapp.local'
ADMINS = [('developer', 'developer@webapp.local')]

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', HOST]
INTERNAL_IPS = ['0.0.0.0', '127.0.0.1', 'localhost', HOST]

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'mail')
