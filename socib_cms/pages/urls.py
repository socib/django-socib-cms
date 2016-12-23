from django.conf.urls import url
import views

urlpatterns = [
    # catch all
    url(r'^registration/change_profile$',
        views.ChangeProfileView.as_view(),
        name='pages_change_profile',
        ),
    url(r'^contact/$',
        views.WebContactView.as_view(),
        name='envelope-contact',
        ),
    url(r'^search/$',
        # views.SocibSearchView(searchqueryset=sqs),
        views.SocibSearchView(),
        name='socib_search_view',
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
]
