from .base import *
import json

from django.core.exceptions import ImproperlyConfigured

# JSON-based secrets module
with open('secrets_local.json') as f: secrets = json.load(f)

def get_secret(setting, secrets=secrets):
    '''Get the secret variable or return explicit exception.''' 
    try:
        return secrets[setting] 
    except KeyError:
        error_msg = 'Set the {0} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = get_secret('ALLOWED_HOSTS')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += [
        'accounts', # project app
    ]

DATABASES = {
    'default': {
        'ENGINE': get_secret("DB_ENGINE"),
        'NAME': get_secret("DB_NAME"),
        'USER': get_secret("DB_USER"),
        'PASSWORD': get_secret("DB_PASSWORD"),
        'HOST': get_secret("DB_HOST"),
        'PORT': get_secret("DB_PORT"),
    }
}

INSTALLED_APPS += ['debug_toolbar', ]