from django.conf.urls import patterns, url
from django.conf import settings
import views

urlpatterns = patterns(
    'socib_cms.cmsutils.views',
    url(r'^prepared-json/(?P<path>.*\.json)$',
        views.proxy_to,
        {'target_url': 'file:///data/current/'}),
    # catch all
    url(r'^(?P<path>.*)$',
        views.proxy_to,
        {'target_url': settings.SOCIB_DATADISCOVERY}),
)
