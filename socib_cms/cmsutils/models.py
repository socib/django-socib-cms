# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField


class GenericLink(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    linkset = models.ForeignKey('LinkSet')
    order = models.IntegerField(_('order'), default=100)

    def __unicode__(self):
        return str(self.order)

    @property
    def picture(self):
        if hasattr(self.content_object, 'picture'):
            return self.content_object.picture
        return None

    def get_absolute_url(self):
        if hasattr(self.content_object, 'get_absolute_url'):
            return self.content_object.get_absolute_url()
        elif hasattr(self.content_object, 'url'):
            return self.content_object.url
        return None

    @property
    def title(self):
        if hasattr(self.content_object, 'title'):
            return self.content_object.title
        return None

    @property
    def description(self):
        if hasattr(self.content_object, 'description'):
            return self.content_object.description
        if hasattr(self.content_object, 'summary'):
            return self.content_object.summary
        if hasattr(self.content_object, 'introduction'):
            return self.content_object.introduction
        return None

    class Meta:
        ordering = ('order',)


class LinkSet(models.Model):
    code = models.CharField(_('code'), max_length=20)
    description = models.CharField(_('description'), max_length=200,
                                   blank=True, null=True)

    def __unicode__(self):
        return self.code


class URLLink(models.Model):
    url = models.URLField(_('URL'))
    title = models.CharField(_('title'), max_length=200)
    description = models.CharField(_('description'), max_length=900,
                                   blank=True, null=True)
    picture = FilerImageField(verbose_name=_('picture'), null=True, blank=True,
                              on_delete=models.SET_NULL)
    css_class = models.CharField(_('CSS class'), max_length=50,
                                 null=True, blank=True)
    # Audit
    created_on = models.DateTimeField(_('date added'), auto_now_add=True)
    created_by = models.ForeignKey(User, blank=True, null=True,
                                   editable=False, related_name='created-urllink',
                                   verbose_name=_('created by'))
    updated_on = models.DateTimeField(_('date modified'), auto_now=True)
    updated_by = models.ForeignKey(User, blank=True, null=True,
                                   editable=False, related_name='updated-urllink',
                                   verbose_name=_('update by'))

    class Meta:
        verbose_name = _('URL link')
        verbose_name_plural = _('URL links')

    def __unicode__(self):
        return "%s: %s" % (self.title, self.url)

    def save(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        self.updated_by = user
        if not self.id:
            self.created_by = user
        return super(URLLink, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return self.url
