from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['kf.svs.gyarab.cz']

STATIC_ROOT = '/var/caddy.root.d/kf.svs.gyarab.cz/static'

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'db1094',
            'USER': 'db1094',
            'PASSWORD': '',
        }
    }
    

