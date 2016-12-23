from django.conf.urls import include, url

urlpatterns = [
    url(r'^ckeditor_filer/', include('ckeditor_filer.urls')),
    url(r'^password/', include('password_reset.urls')),
    url(r'^news/', include('socib_cms.news.urls')),
    url(r'^', include('socib_cms.cmsutils.urls')),
    url(r'^', include('socib_cms.pages.urls')),
]
