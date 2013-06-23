from django.conf.urls import patterns

urlpatterns = patterns(
    'appengine_django_blank.views',
    (r'^(?P<message>.*)$', 'index'),
)
