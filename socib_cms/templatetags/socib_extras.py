# coding: utf-8
from django import template
# from django.contrib.sites.shortcuts import get_current_site

register = template.Library()


@register.filter
def subtract(value, arg):
    return value - arg


@register.simple_tag(takes_context=True)
def site_name(context):
    return "Test"
    # return get_current_site(context['request']).name
