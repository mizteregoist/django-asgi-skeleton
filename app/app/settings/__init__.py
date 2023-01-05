import os

if os.environ.get('ENV') == 'prod':
    from .prod import *
elif os.environ.get('ENV') == 'dev':
    from .dev import *
elif os.environ.get('ENV') == 'local':
    from .local import *
