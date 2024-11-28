from .base import *

DEBUG = True

ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# CORS settings
CORS_ALLOWED_ORIGINS = environ.get('CORS_ALLOWED_ORIGINS', 'http://localhost:3000').split(',')
CORS_ALLOW_CREDENTIALS = True

# Email backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
