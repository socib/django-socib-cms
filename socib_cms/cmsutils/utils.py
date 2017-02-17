# coding: utf-8
import re
from django.core.urlresolvers import reverse
from django.conf import settings


def reverse_no_i18n(viewname, *args, **kwargs):
    result = reverse(viewname, *args, **kwargs)
    m = re.match(r'(/[^/]*)(/.*$)', result)
    return m.groups()[1]


def change_url_language(url, language):
    if hasattr(settings, 'LANGUAGES'):
        languages = [lang[0] for lang in settings.LANGUAGES]
        m = re.match(r'/([^/]*)(/.*$)', url)
        if m and m.groups()[0] in languages:
            return u"/{lang}{url}".format(
                lang=language,
                url=m.groups()[1])

    return u"/{lang}{url}".format(
        lang=language,
        url=url)
    return url
