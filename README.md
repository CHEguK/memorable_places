[![Build Status](https://travis-ci.org/CHEguK/memorable_places.svg?branch=master)](https://travis-ci.org/CHEguK/memorable_places)
[![Coverage Status](https://coveralls.io/repos/github/CHEguK/memorable_places/badge.svg?branch=master)](https://coveralls.io/github/CHEguK/memorable_places?branch=master)

# memorable_places
toy_project

# Instruction

## Setting up the environment

Create memorable_places/settings_dev.py with following content:
```python
# memorable_plaves/settings_dev.py
import sys
from .settings_shared import *

SECRET_KEY = 'dev'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Token from https://www.mapbox.com/ for displaying the map in /memories/create.html
MAPBOX_TOKEN = ''

# Facebook APP secret key
SOCIAL_AUTH_FACEBOOK_KEY = ''     # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = ''  # App Secret
```
## Pipenv
```bash
pipenv sync
pipenv shell
```
## Running locally
```bash
export DJANGO_SETTINGS_MODULE='memorable_places.settings_dev'
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Testing
Typing
```bash
mypy accounts/ memories/ memorable_places/
```
Django tests
```bash
python manage.py test
```
Codestyle
```bash
pycodestyle
pylint accounts/ memories/ memorable_places/
```
Running all tests
```bash
./runtests.sh
```