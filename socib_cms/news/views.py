# coding: utf-8
from django.views.generic.detail import DetailView
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from localeurl.models import django_reverse as reverse
from socib_cms.pages.views import BasePageView
from socib_cms.pages.models import Page
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

    def get_news(self):
        page = self.request.GET.get('page', 1)
        news_list = self.object.news_set.published()
        # Paginate results
        paginator = Paginator(news_list, 10)  # Show 10 news per page
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
            page = Page()
            page.title = self.object.category.name
        return page

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['page'] = self.get_page()
        return context
