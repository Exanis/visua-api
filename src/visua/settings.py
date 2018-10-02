"""
Visua API settings
Those settings should not be modified as this file load most of its values from environment
Please pass correct values to your env file instead
"""
import environ
from celery.schedules import crontab
import os
import pwd
with open('/tmp/' + str(os.getpid()), 'w') as fp:
    fp.write(pwd.getpwuid(os.getuid()).pw_name)
ENV = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, ['*']),
    DATABASE_URL=(str, None),
    SECRET_KEY=(str, 'change me'),
    RUNNER_KEY=(str, 'change me')
)
ENV.read_env()

# Environment-base parameters
SECRET_KEY = ENV('SECRET_KEY')
DEBUG = ENV('DEBUG')
ALLOWED_HOSTS = ENV('ALLOWED_HOSTS')
DATABASES = {
    'default': ENV.db()
}
RUNNER_KEY = ENV('RUNNER_KEY')

# Celery parameters
CELERY_APP = 'visua'
CELERY_BROKER_URL = 'amqp://localhost'
CELERY_BIN = 'celery'
CELERY_BEAT_SCHEDULE = {
    'refresh-runners': {
        'task': 'pipeline.tasks.refresh_runners_status',
        'schedule': crontab(minute='*')
    }
}

# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'user',
    'pipeline'
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'visua.urls'
WSGI_APPLICATION = 'visua.wsgi.application'
AUTH_USER_MODEL = 'user.User'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 15
}

JWT_AUTH = {
    'JWT_AUTH_COOKIE': 'Token',
    'JWT_GET_USER_SECRET_KEY': lambda u: u.secret_key,
    'JWT_ISSUER': 'Visua',
    'JWT_ALLOW_REFRESH': True
}
