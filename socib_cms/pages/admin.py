from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter
from django.db.models import TextField
from ckeditor_filer.widgets import CKEditorWidget
from filer.fields.folder import FilerFolderField, AdminFolderFormField
from mptt.admin import MPTTModelAdmin
from modeltranslation.admin import TranslationAdmin
import models


class PageForm(FlatpageForm):

    class Meta:
        model = models.Page


class PageFilter(SimpleListFilter):
    title = _('parent')
    parameter_name = 'parent'

    def lookups(self, request, model_admin):
        pages = set([page.parent for page in model_admin.model.objects.all()])
        return [(p.id, p.title_menu) for p in pages if p is not None]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(parent__flatpage_ptr__exact=self.value())
        else:
            return queryset


class PageAdmin(MPTTModelAdmin, TranslationAdmin, FlatPageAdmin):
    form = PageForm
    formfield_overrides = {
        TextField: {'widget': CKEditorWidget(config_name='default')},
        FilerFolderField: {'form_class': AdminFolderFormField}}
    search_fields = ['title']
    filter_horizontal = ('related', 'groups',)
    list_display = ('url', 'title', 'order', 'group_list')
    list_filter = [PageFilter]
    list_editable = ('order',)
    fieldsets = (
        (None, {
            'fields': ('parent', 'url', 'title', 'title_menu', 'order', 'picture',
                       'album', 'introduction', 'content', 'sites')
        }),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': ('redirect_link', 'related', 'enable_comments', 'is_container',
                       'list_children', 'hide', 'css_class',
                       'registration_required', 'groups', 'template_name',
                       'old_url')
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
