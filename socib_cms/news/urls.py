from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    'socib_cms.news.views',
    url(r'^rss/$',
        views.NewsFeed(),
        name='news_feed'
        ),
    url(r'^(?P<pk>\d+)/more_like_this$',
        views.NewsMoreLikeThisView.as_view(),
        name='news_mlt',
        ),
    url(r'^(?P<slug>[-\w]+)/$',
        views.NewsCategoryDetailView.as_view(),
        name='news_category_detail',
        ),
    url(r'^(?P<slug>[-\w]+)/rss/$',
        views.NewsFeed(),
        name='news_category_feed',
        ),
    url(r'^(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+).html$',
        views.NewsDetailView.as_view(),
        name='news_detail',
        )
)
