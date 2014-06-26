from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = patterns('',
    url(r'^uploader/$', 'uploader.views.list', name='list'),
    (r'^$', RedirectView.as_view(url='/uploader/')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
urlpatterns = patterns('',
    (r'^uploader/', include('hellohost.uploader.urls')),
    (r'^$', RedirectView.as_view(url='/uploader/list/')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''