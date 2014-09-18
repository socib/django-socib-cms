from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from genericadmin.admin import GenericAdminModelAdmin, StackedInlineWithGeneric
import models


class URLLinkAdmin(TranslationAdmin):
    search_fields = ['title', 'url']
    list_display = ('title', 'url')


class GenericLinkInline(StackedInlineWithGeneric):
    model = models.GenericLink
    can_delete = True
    verbose_name_plural = 'links'


class LinkSetAdmin(GenericAdminModelAdmin):
    inlines = (GenericLinkInline, )
    content_type_whitelist = ('news/news', 'pages/page', 'cmsutils/urllink')
    fieldsets = (
        (None, {
            'fields': ('code', 'description')
        }),
    )


admin.site.register(models.URLLink, URLLinkAdmin)
admin.site.register(models.LinkSet, LinkSetAdmin)
