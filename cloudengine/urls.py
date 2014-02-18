from django.conf.urls import patterns, include, url
from cloudengine.core.views import AccountKeysView

urlpatterns = patterns(
    '',
    # Examples:
    
    (r'', include('cloudengine.core.urls')),
    url(r'^api-auth/', include(
        'rest_framework.urls', namespace='rest_framework')),

    url(r'^socket.io/', 'cloudengine.push.views.socketio_view'),
    url(r'^api/v1/', include('cloudengine.api_v1_urls')),
    url(r'^files/', include('cloudengine.files.urls')),
    url(r'^keys/$',
        AccountKeysView.as_view(), name='myaccount-keys'),
    url(r'^apps/(?P<app_name>[a-zA-Z0-9]+)/verify_email/$', 
        'cloudengine.users.views.verify_email'),
    url(r'^accounts/', include(
        'registration.backends.simple.urls')),

)
