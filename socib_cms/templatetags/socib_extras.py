# coding: utf-8
from django import template
from django.contrib.sites.shortcuts import get_current_site
from django.template.defaultfilters import stringfilter
from socib_cms.news.models import NewsCategory

register = template.Library()


@register.filter
def subtract(value, arg):
    return value - arg


@register.simple_tag(takes_context=True)
def site_name(context):
    return get_current_site(context['request']).name


def chlocale(url, locale):
    """
    Override localeurl.chlocale, to manage external urls
    """
    if url and url[0] != '/':
        return url
    else:
        # return localeurl_chlocale(url, locale)
        return url

chlocale = stringfilter(chlocale)
register.filter('chlocale', chlocale)

@register.assignment_tag
def visible_categories():
    return NewsCategory.objects.filter(hide_cat_menu=False)
