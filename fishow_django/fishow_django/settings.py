"""
Django settings for fishow_django project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from json import load

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2)f3e=c7vska&acn%5m@k&lpd_4zxbe19ab!(0ndp4bxews)rj'

# SECURITY WARNING: don't run with debug turned on in production!


with open(os.path.join(os.path.dirname(__file__), "config.json"), 'r') as json_f:
    config_database = load(json_f)

DEBUG = config_database['debug']

ALLOWED_HOSTS = config_database['allowed_hosts']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'core',


    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook', # new

    'rest_auth',
    'rest_auth.registration',
    'bootstrap4',
    'crispy_forms',
    'webpack_loader',

    'users',
    'blogs',
    'prediction',
    'report', # new
    'django_filters'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST = config_database['cors_origin_whitelist']

ROOT_URLCONF = 'fishow_django.urls'

REST_AUTH_SERIALIZERS = {
    'PASSWORD_RESET_SERIALIZER':
        'users.api.serializers.PasswordResetSerializer',
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'templates', 'allauth')],
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

WSGI_APPLICATION = 'fishow_django.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# with open(os.path.join(os.path.dirname(__file__), "config.json"), 'r') as json_f:
#     config_database = load(json_f)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config_database['database_name'],
        'USER': config_database['user'],
        'PASSWORD': config_database['password'],
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

ACCOUNT_ADAPTER = 'users.views.DefaultAccountAdapterCustom' # new
URL_FRONT = config_database['url_front'] # new
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = config_database['static_root']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'frontend3_1/frontend3/.nuxt/dist/server/'),
    os.path.join(BASE_DIR, 'frontend3_1/frontend3/.nuxt/dist/client/'),
    os.path.join(BASE_DIR, 'frontend3_1/frontend3/static/'),
)
# Custom User Model
AUTH_USER_MODEL = "users.CustomUser"

# django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# django.contrib.sites
SITE_ID = 1

######
# ACCOUNT_EMAIL_VERIFICATION = 'none'
# ACCOUNT_EMAIL_REQUIRED = True
######
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =1

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = "mandatory"

ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5

ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
EMAIL_HOST = "smtp.mail.ru"
EMAIL_PORT = 2525
EMAIL_HOST_USER = "fishow@inbox.ru"
EMAIL_HOST_PASSWORD = "Django2020!"
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
AUTHENTICATION_BACKENDS = (
     'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
#####
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 7
}

#WEBPACK_LOADER = {
#    'DEFAULT': {
#        'BUNDLE_DIR_NAME': 'dist/',
#        'STATS_FILE': os.path.join(BASE_DIR, 'frontend3_1/frontend3/assets', 'webpack-stats.json'),
#    }
#}
