# coding: utf-8
from datetime import datetime, time
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from haystack.query import SearchQuerySet
from socib_cms.pages.views import BasePageView
from socib_cms.pages.models import Page
from socib_cms.cmsutils.views import JSONResponseMixin
import models


class NewsCategoryDetailView(DetailView, BasePageView):

    template_name = "news/category.html"
    model = models.NewsCategory
    context_object_name = 'category'

    def get_page(self):
        try:
            url = reverse('news_category_detail',
                          args=[self.object.slug])
            page = Page.objects.get(url=url)
        except ObjectDoesNotExist:
            page = Page()
            page.title = self.object.name
        return page

    def get_page_parent(self):
        try:
            url = reverse('news_category_detail',
                          args=[self.object.slug])
            page = Page.objects.get(url=url).parent
        except ObjectDoesNotExist:
            try:
                url = reverse('news_list')
                page = Page.objects.get(url=url)
            except ObjectDoesNotExist:
                page = Page()
                page.title = self.object.name
        return page

    def get_news(self):
        page = self.request.GET.get('page', 1)
        news_list = self.object.news_set.published()
        # Paginate results
        paginator = Paginator(news_list, 5)  # Show 5 news per page
        try:
            news_paginated = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            news_paginated = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            news_paginated = paginator.page(paginator.num_pages)
        return news_paginated

    def get_context_data(self, **kwargs):
        context = super(NewsCategoryDetailView, self).get_context_data(**kwargs)
        context['page'] = self.get_page()
        context['news_list'] = self.get_news()
        context['category_page_parent'] = self.get_page_parent()
        return context


class NewsListView(ListView, BasePageView):

    template_name = "news/list.html"
    model = models.News
    paginate_by = 5

    def get_page(self):
        try:
            url = reverse('news_list')
            page = Page.objects.get(url=url)
        except ObjectDoesNotExist:
            page = Page()
            page.title = _('News')
        return page

    def get_queryset(self):
        qs = super(NewsListView, self).get_queryset()
        qs = qs.published()
        qs = qs.filter(category__hide_cat_menu=False)
        return qs

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['page'] = self.get_page()
        return context


class NewsDetailView(DetailView, BasePageView):

    template_name = "news/news.html"
    model = models.News
    context_object_name = 'news'

    # TODO: Modify get_object to search by category + slug.
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.redirect_link:
            return redirect(obj.redirect_link)
        return super(NewsDetailView, self).dispatch(request, *args, **kwargs)

    def get_page(self):
        try:
            url = reverse('news_category_detail',
                          args=[self.object.category.slug])
            page = Page.objects.get(url=url)
        except ObjectDoesNotExist:
            try:
                url = reverse('news_list')
                page = Page.objects.get(url=url)
            except ObjectDoesNotExist:
                page = Page()
                page.title = self.object.category.name
        return page

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['page'] = self.get_page()
        return context


class NewsFeed(Feed):
    title = "News"
    link = "/news/"
    description = "description"

    def get_object(self, *args, **kwargs):
        if 'slug' in kwargs:
            self.category = get_object_or_404(models.NewsCategory, slug=kwargs['slug'])
        else:
            self.category = None

    def items(self):
        if self.category:
            return self.category.news_set.latest(10)
        return models.News.objects.latest(10)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summary

    def item_link(self, item):
        return item.get_absolute_url()

    def item_pubdate(self, item):
        return datetime.combine(item.publish_date, time())


class NewsMoreLikeThisView(JSONResponseMixin, DetailView):

    model = models.News
    context_object_name = 'news'

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        sqs = SearchQuerySet().models(models.News).more_like_this(obj)
        news_list = []
        for result in sqs[:5]:
            try:
                news = {
                    'score': result.score,
                    'title': result.object.title,
                    'url': result.object.get_absolute_url(),
                    'summary': result.object.summary,
                    'publish_date': result.object.publish_date.isoformat()
                }
                news_list.append(news)
            except:
                pass
        return self.render_to_response(news_list)

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)
