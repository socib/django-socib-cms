from django.conf.urls import url
from django.conf import settings
import views

urlpatterns = [
    url(r'^prepared-json/(?P<path>.*\.json)$',
        views.proxy_to,
        {'target_url': 'file:///data/current/'}),
    # catch all
    url(r'^services/(?P<path>.*)$',
        views.proxy_to,
        {'target_url': settings.SOCIB_DATADISCOVERY})
]
