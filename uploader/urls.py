from django.conf.urls import patterns, url

urlpatterns = patterns('hellohost.uploader.views',
    url(r'^list/$', 'list', name='list'),
)