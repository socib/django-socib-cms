from django.conf.urls import include, url

urlpatterns = [
    url(r'^filebrowser_filer/', include('ckeditor_filebrowser_filer.urls')),
    url(r'^password/', include('password_reset.urls')),
    url(r'^news/', include('socib_cms.news.urls')),
    url(r'^', include('socib_cms.cmsutils.urls')),
    url(r'^', include('socib_cms.pages.urls')),
]
