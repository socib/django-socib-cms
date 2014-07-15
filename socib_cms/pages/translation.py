# coding: utf-8
from modeltranslation.translator import translator, TranslationOptions
from django.contrib.flatpages.models import FlatPage
from models import Page


class FlatPageTranslationOptions(TranslationOptions):
    pass


class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'title_menu', 'introduction', 'content',)

translator.register(FlatPage, FlatPageTranslationOptions)
translator.register(Page, PageTranslationOptions)
