from .base import *

DEBUG = False
ALLOWED_HOSTS = ['ip-address', 'www.yourwebsite.com']

DATABASES = {
    'default': env.db()
}
