MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)

INSTALLED_APPS = (
    'appengine_django_blank'
)

ROOT_URLCONF = 'appengine_django_blank.urls'

import os
ROOT_PATH = os.path.dirname(__file__)
TEMPLATE_DIRS = (
    ROOT_PATH + '/templates',
)

CACHE_BACKEND = 'memcached:///'
