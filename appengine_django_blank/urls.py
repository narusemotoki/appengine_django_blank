from django.conf.urls.defaults import patterns

urlpatterns = patterns(
    'appengine_django_blank.views',
    (r'^(?P<message>.*)$', 'index'),
)
