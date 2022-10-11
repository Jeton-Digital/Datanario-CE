# settings/base.py
import builtins
import sys
import json
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

# JSON-based secrets module
with open('secrets.json') as f: secrets = json.load(f)

def get_secret(setting, secrets=secrets):
    '''Get the secret variable or return explicit exception.''' 
    try:
        return secrets[setting] 
    except KeyError:
        error_msg = 'Set the {0} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)


# BASE directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(BASE_DIR / 'datanario'))

# PROJECT directory
PROJECT_ROOT = BASE_DIR / 'datanario'

# for url prefix purposes only
STATIC_URL = '/assets/'

# for deployment only
STATIC_ROOT = PROJECT_ROOT / 'static_root' 

# for development only
STATICFILES_DIRS = [
    PROJECT_ROOT / 'static',
    PROJECT_ROOT / 'static_boot', # bootstrap files
]

# for development only
MEDIA_ROOT = PROJECT_ROOT / 'media'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_ROOT / 'templates'],
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


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = get_secret('ALLOWED_HOSTS')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts', # project app
    'widget_tweaks', # third-party app
    'crispy_forms', # third-party app
    'crispy_bootstrap5', # third-party app
    'django_feather', # third-party app
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

ROOT_URLCONF = 'config.urls'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret("DB_NAME"),
        'USER': get_secret("DB_USER"),
        'PASSWORD': get_secret("DB_PASSWORD"),
        'HOST': get_secret("DB_HOST"),
        'PORT': get_secret("DB_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redirect to home URL after login
LOGOUT_REDIRECT_URL = "home"
# Login redirect
LOGIN_REDIRECT_URL = "announcement"