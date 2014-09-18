# coding: utf-8
from modeltranslation.translator import translator, TranslationOptions
from models import URLLink


class URLLinkTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

translator.register(URLLink, URLLinkTranslationOptions)
