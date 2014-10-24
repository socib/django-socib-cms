from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter
from django.template.defaultfilters import slugify
from django.db.models import TextField
from django.contrib.sites.models import Site
from django.forms import Textarea, TextInput
from ckeditor_filer.widgets import CKEditorWidget
from django_ace import AceWidget
from filer.fields.folder import FilerFolderField, AdminFolderFormField
from mptt.admin import MPTTModelAdmin
from modeltranslation.admin import TranslationAdmin
import models


class PageForm(FlatpageForm):

    def __init__(self, *args, **kwargs):
        super(FlatpageForm, self).__init__(*args, **kwargs)
        self.fields['url'].initial = u'/auto-generate-url-from-title/'

    class Meta:
        model = models.Page
        widgets = {
            'js_code': AceWidget(mode='javascript', theme='dawn',
                                 width="800px", height="400px")
        }


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
        (_('Hierarchy'), {
            'fields': ('parent', 'order', 'url')
        }),
        (_('Content'), {
            'fields': ('title', 'title_menu', 'introduction', 'content',
                       'extra_content', )
        }),
        (_('Pictures'), {
            'fields': ('picture', 'picture_description', 'picture_location', 'album', )
        }),
        (_('Layout and design'), {
            'fields': ('template_name', 'content_template_name', 'show_section_menu',
                       'content_columns', 'extra_content_columns', 'float_extra_content',
                       'list_children', 'include_children',
                       'css_class', 'css_container_style', )
        }),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': ('sites', 'redirect_link', 'related', 'enable_comments',
                       'is_container', 'hide', 'registration_required', 'groups',
                       'old_url', 'js_code')
        }),
    )
    actions = ['create_child']

    def save_model(self, request, obj, form, change):
        if obj.url == u'/auto-generate-url-from-title/':
            if obj.parent.id:
                obj.url = "%s%s/" % (obj.parent.url, slugify(obj.title)[0:25])
            else:
                obj.url = "/%s/" % slugify(obj.title)[0:50]
        obj.save()

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['introduction', 'picture_description']:
            kwargs['widget'] = Textarea(
                attrs={'rows': 4, 'cols': 60, 'style': 'width: auto;'})
        if db_field.name == "sites":
            kwargs["initial"] = [Site.objects.get_current()]
        if db_field.name in ["title", "title_menu", "css_container_style"]:
            kwargs['widget'] = TextInput(
                attrs={'style': 'width: 700px;'})
        field = super(PageAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        self.patch_translation_field(db_field, field, **kwargs)
        return field

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

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            '//ajax.googleapis.com/ajax/libs/jqueryui/1.11.1/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.unregister(FlatPage)
admin.site.register(models.Page, PageAdmin)
