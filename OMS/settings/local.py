
from .base import * 


ALLOWED_HOSTS = ['*']


DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME' : 'ommcslserver',
        'USER' : 'ommcsl',
        'PASSWORD' : 'MainOne12@',
    }
} 


#SECURE_SSL_REDIRECT = False 
#CSRF_COOKIE_SECURE = True 
#SESSION_COOKIE_SECURE = True 