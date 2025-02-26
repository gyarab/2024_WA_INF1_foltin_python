from .base import *

ALLOWED_HOSTS = ["kf.svs.gyarab.cz"]

DEBUG = False

STATIC_ROOT = "/var/caddy.root.d/kf.svs.gyarab.cz/static"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db1094',
        'USER': 'db1094',
        'PASSWORD': '', # read from .pgpass
    }
}