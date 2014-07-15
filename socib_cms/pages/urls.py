from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    'socib_cms.pages.views',
    # catch all
    url(r'^registration/change_profile$',
        views.ChangeProfileView.as_view(),
        name='pages_change_profile',
        ),
    url(r'^contact/$',
        views.WebContactView.as_view(),
        name='envelope-contact',
        ),
    url(r'^(?P<url>.*)$',
        views.GenericPageView.as_view(),
        name='pages_page',
        ),
    url(r'^$',
        views.GenericPageView.as_view(),
        name='pages_home',
        kwargs={'url': ''}
        ),
)
