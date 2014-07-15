from django.conf.urls import patterns, include

urlpatterns = patterns(
    (r'^news/', include('socib_cms.news.urls')),
    (r'^', include('socib_cms.pages.urls')),
)
