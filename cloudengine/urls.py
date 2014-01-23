from django.conf.urls import patterns, include, url
from django.contrib import admin
from core.views import AccountKeysView
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    
    url(r'^admin/', include(admin.site.urls)),
    (r'', include('core.urls')),
    url(r'^api-auth/', include(
        'rest_framework.urls', namespace='rest_framework')),

    url(r'^socket.io/', 'push.views.socketio_view'),
    url(r'^api/v1/', include('cloudengine.api_v1_urls')),
    url(r'^myaccount/files/', include('files.urls')),
    url(r'^myaccount/keys/$',
        AccountKeysView.as_view(), name='myaccount-keys'),
    url(r'^apps/(?P<app_name>[a-zA-Z0-9]+)/verify_email/$', 
        'users.views.verify_email'),
    url(r'^accounts/', include(
        'registration.backends.simple.urls')),


)
