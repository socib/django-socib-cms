from django.conf.urls import patterns, include

urlpatterns = patterns(
    '',
    (r'^localeurl/', include('localeurl.urls')),
    (r'^ckeditor_filer/', include('ckeditor_filer.urls')),
    (r'^password/', include('password_reset.urls')),
    (r'^news/', include('socib_cms.news.urls')),
    (r'^', include('socib_cms.cmsutils.urls')),
    (r'^', include('socib_cms.pages.urls')),
)
