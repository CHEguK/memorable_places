[![Build Status](https://travis-ci.org/CHEguK/memorable_places.svg?branch=master)](https://travis-ci.org/CHEguK/memorable_places)
[![Coverage Status](https://coveralls.io/repos/github/CHEguK/memorable_places/badge.svg?branch=master)](https://coveralls.io/github/CHEguK/memorable_places?branch=master)

# memorable_places
toy_project

# Instruction

## Setting up the environment

Create memorable_plaves/settings_dev.py with following content:
```python
# memorable_plaves/settings_dev.py
from .settings_shared import *

SECRET_KEY = 'dev'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
MAPBOX_TOKEN = ''
```
## Pipenv
```bash
pipenv sync
pipenv shell
```
## or requirements.txt
```bash
pip install -r requirements.txt
```
## Running locally
```bash
export DJANGO_SETTINGS_MODULE=memorable_plaves.settings_dev
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Testing
```python
python manage.py test
```