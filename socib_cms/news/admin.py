from django.contrib import admin
from django.db.models import TextField
from modeltranslation.admin import TranslationAdmin
from ckeditor_filer.widgets import CKEditorWidget
from filer.fields.folder import FilerFolderField, AdminFolderFormField
import models


class AuditModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_by', 'updated_by',)
    formfield_overrides = {
        TextField: {'widget': CKEditorWidget(config_name='default')}, }

    def save_model(self, request, obj, form, change):
        obj.save(user=request.user)


class NewsAdmin(AuditModelAdmin, TranslationAdmin):
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = 'publish_date'
    list_display = ('title', 'category', 'publish_date', 'is_draft')
    list_filter = ['category']
    search_fields = ['title']
    actions = ['make_published', 'clone']
    formfield_overrides = {
        FilerFolderField: {'form_class': AdminFolderFormField}}

    def clone(self, request, queryset):
        counter = 0
        for news in queryset:
            n = news.clone()
            n.title = 'Copy of %s' % news.title
            n.save()
            counter = counter + 1
        if counter == 1:
            message_bit = "1 news was"
        else:
            message_bit = "%s news were" % counter
        self.message_user(request, "%s successfully cloned." % message_bit)

    def make_published(self, request, queryset):
        rows_updated = queryset.update(is_draft=False)
        if rows_updated == 1:
            message_bit = "1 news was"
        else:
            message_bit = "%s news were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    clone.short_description = "Clone selected news"
    make_published.short_description = "Mark selected news as published"


class NewsCategoryAdmin(TranslationAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name',)


admin.site.register(models.NewsCategory, NewsCategoryAdmin)
admin.site.register(models.News, NewsAdmin)
