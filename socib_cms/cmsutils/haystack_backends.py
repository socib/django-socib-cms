# coding: utf-8
from django.conf import settings
from django.utils import translation
from haystack import connections
from haystack.backends.elasticsearch_backend import (
    ElasticsearchSearchEngine, ElasticsearchSearchBackend,
    ElasticsearchSearchQuery)
from haystack.constants import DEFAULT_ALIAS


def get_using(language, alias=DEFAULT_ALIAS):
    if language:
        new_using = alias + "_" + language
    else:
        new_using = alias
    using = new_using if new_using in settings.HAYSTACK_CONNECTIONS else alias
    return using


class MultilingualElasticsearchSearchBackend(ElasticsearchSearchBackend):
    def update(self, index, iterable, commit=True, multilingual=True):
        if multilingual:
            initial_language = translation.get_language()
            # retrieve unique backend name
            backends = []
            for language, __ in settings.LANGUAGES:
                using = get_using(language, alias=self.connection_alias)
                # Ensure each backend is called only once
                if using in backends:
                    continue
                else:
                    backends.append(using)
                translation.activate(language)
                backend = connections[using].get_backend()
                backend.update(index, iterable, commit)
            translation.activate(initial_language)
        else:
            print "[%s]" % self.connection_alias
            super(MultilingualElasticsearchSearchBackend, self).update(
                index, iterable, commit)


class MultilingualElasticsearchSearchQuery(ElasticsearchSearchQuery):
    def __init__(self, using=DEFAULT_ALIAS):
        language = translation.get_language()
        using = get_using(language)
        super(MultilingualElasticsearchSearchQuery, self).__init__(using)


class MultilingualElasticsearchSearchEngine(ElasticsearchSearchEngine):
    backend = MultilingualElasticsearchSearchBackend
    query = MultilingualElasticsearchSearchQuery
