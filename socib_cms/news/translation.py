# coding: utf-8
from modeltranslation.translator import translator, TranslationOptions
import models


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'introduction', 'content',)


class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(models.News, NewsTranslationOptions)
translator.register(models.NewsCategory, NewsCategoryTranslationOptions)
