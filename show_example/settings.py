"""
You should not have to touch this I hope :)




Django settings for show_example project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '785ki%ipwfub5kefd+v@ki-^t!nyhpco^xb*uo1-oi5p1hgh+s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'show_example',
)

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
MEDIA_ROOT = PROJECT_PATH + '/media/'
TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/',
)



MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware'
)

ROOT_URLCONF = 'show_example.urls'

WSGI_APPLICATION = 'show_example.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

MYSQL = False
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
if MYSQL:
    DATABASES = {
         'default': {
             'ENGINE'   : 'django.db.backends.mysql',
             'NAME' : 'playground',
             'USER' : os.getenv('USER'), #Added Windows support  
         'PASSWORD' : 'password',
         'HOST' : 'localhost',
         'PORT' : '3306',
         }
    }
else:
    DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
         }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
