"""
Visua API settings
Those settings should not be modified as this file load most of its values from environment
Please pass correct values to your env file instead
"""
import environ

ENV = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, ['*']),
    DATABASE_URL=(str, 'sqlite:////tmp/virtua.db'),
    SECRET_KEY=(str, 'change me')
)

# Environment-base parameters
SECRET_KEY = ENV('SECRET_KEY')
DEBUG = ENV('DEBUG')
ALLOWED_HOSTS = ENV('ALLOWED_HOSTS')
DATABASES = {
    'default': ENV.db()
}


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
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
