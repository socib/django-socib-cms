from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    'socib_cms.news.views',
    url(r'^(?P<slug>[-\w]+)/$',
        views.NewsCategoryDetailView.as_view(),
        name='news_category_detail',
        ),
    url(r'^(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+).html$',
        views.NewsDetailView.as_view(),
        name='news_detail',
        )
)
