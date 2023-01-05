from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TOOLBAR_CALLBACK": show_toolbar_callback,
    "SHOW_TEMPLATE_CONTEXT": True,
}
