from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db.models import TextField
from ckeditor_filer.widgets import CKEditorWidget
from mptt.admin import MPTTModelAdmin
from modeltranslation.admin import TranslationAdmin
import models


class PageForm(FlatpageForm):

    class Meta:
        model = models.Page


class PageAdmin(MPTTModelAdmin, TranslationAdmin, FlatPageAdmin):
    form = PageForm
    formfield_overrides = {TextField: {'widget': CKEditorWidget(config_name='default')}, }
    filter_horizontal = ('related', 'groups',)
    list_display = ('url', 'title', 'order', 'group_list')
    list_filter = ['parent']
    list_editable = ('order',)
    fieldsets = (
        (None, {
            'fields': ('parent', 'url', 'title', 'title_menu', 'order', 'picture',
                       'introduction', 'content', 'sites')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('related', 'enable_comments', 'is_container',
                       'list_children', 'hide', 'css_class',
                       'registration_required', 'groups', 'template_name')
        }),
    )
    actions = ['create_child']

    def create_child(self, request, queryset):
        pages_counter = 0
        for page in queryset:
            new_page = models.Page()
            new_page.parent = page
            new_page.url = page.url + 'new_page/'
            new_page.title = 'Child of ' + page.title
            new_page.save()
            new_page.sites.add(*page.sites.all())
            pages_counter = pages_counter + 1

        if pages_counter == 1:
            message_bit = "1 page was"
        else:
            message_bit = "%s pages were" % pages_counter
        self.message_user(request, "%s successfully created." % message_bit)

    create_child.short_description = "Create child page"

admin.site.unregister(FlatPage)
admin.site.register(models.Page, PageAdmin)
