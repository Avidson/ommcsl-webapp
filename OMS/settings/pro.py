
import os
from .base import *

DEBUG = False

ADMIN = (
    ('Chisom', 'marcusjobng@gmail.com'),
    ('Admin', 'info@ommcsl.loan')
)

ALLOWED_HOSTS = ['*']

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
} 

