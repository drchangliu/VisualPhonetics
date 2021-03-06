from secret_settings import *

"""
Django settings for VowelCat project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#DEBUG = False

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
    'VowelCat',
    'VowelCatApp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',      
    'django.middleware.locale.LocaleMiddleware',    
    'django.middleware.common.CommonMiddleware', 
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'VowelCat.urls'

WSGI_APPLICATION = 'VowelCat.wsgi.application'

AUTH_USER_MODEL = 'VowelCatApp.MyUser'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

#LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Where to look for the profile object

AUTH_PROFILE_MODULE = "account.UserProfile"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = ''

STATIC_ROOT = 'staticfiles'
MEDIA_ROOT = 'staticfiles/media'

# Template location

TEMPLATE_DIRS = (
   os.path.join(os.path.dirname(BASE_DIR), "VowelCat", "templates"),
)

STATICFILES_DIRS = (
   os.path.join(os.path.dirname(BASE_DIR), "VowelCat", "static"),
)

from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
    ('zh', _('Chinese')),
)

DEPLOY = False

if DEPLOY:
  # Parse database configuration from $DATABASE_URL
  import dj_database_url
  DATABASES['default'] =  dj_database_url.config()

  # Enable Connection Pooling
  DATABASES['default']['ENGINE'] = 'django_postgrespool'

  # Allow all host headers
  ALLOWED_HOSTS = ['*']

  # Simplified static file serving.
  # https://warehouse.python.org/project/whitenoise/
  STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

  # Honor the 'X-Forwarded-Proto' header for request.is_secure()
  SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
