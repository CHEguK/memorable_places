''' memorable_places/settings_prod.py '''
import sys

from .settings_shared import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('NAME_DB'),
        'HOST': os.getenv('HOST_DB'),
        'PORT': os.getenv('PORT_DB'),
        'USER': os.getenv('USER_DB'),
        'PASSWORD': os.getenv('PASSWORD_DB'),

    }
}

if 'test' in sys.argv:
    # Configuration for test database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


SOCIAL_AUTH_FACEBOOK_KEY = os.getenv('SOCIAL_AUTH_FACEBOOK_KEY')        # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv('SOCIAL_AUTH_FACEBOOK_SECRET')  # App Secret


MAPBOX_TOKEN = os.getenv('MAPBOX_TOKEN')
