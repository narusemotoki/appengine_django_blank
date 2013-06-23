DEBUG = False

ALLOWED_HOSTS = ['localhost', 'your-app-id.appspot.com']

INSTALLED_APPS = ('appengine_django_blank')

ROOT_URLCONF = 'appengine_django_blank.urls'

SECRET_KEY = 'Change this string'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)

CACHE_BACKEND = 'memcached:///'

import os
ROOT_PATH = os.path.dirname(__file__)
TEMPLATE_DIRS = (ROOT_PATH + '/templates',)
