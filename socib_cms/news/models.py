from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from taggit.managers import TaggableManager
from datetime import date
from socib_cms.utils import ClonableMixin


class NewsCategory(models.Model):
    name = models.CharField(_('name'), max_length=100)
    slug = models.CharField(_('slug'), max_length=100, unique=True)

    class Meta:
        verbose_name = _('news category')
        verbose_name_plural = _('news categories')

    def __unicode__(self):
        return self.name


class NewsQuerySet(models.query.QuerySet):
    def published(self):
        return self.filter(is_draft=False, publish_date__lte=date.today())


class NewsManager(models.Manager):
    use_for_related_fields = True

    def get_query_set(self):
        return NewsQuerySet(self.model)

    def published(self, *args, **kwargs):
        return self.get_query_set().published(*args, **kwargs)

    def latest10(self, *args, **kwargs):
        return self.get_query_set().published(*args, **kwargs)[:10]


class News(models.Model, ClonableMixin):
    category = models.ForeignKey(NewsCategory, on_delete=models.PROTECT,
                                 verbose_name=_('category'))
    publish_date = models.DateField(_('publishing date'))
    is_draft = models.BooleanField(_('draft'), default=True)
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'), blank=True)
    introduction = models.CharField(_('Introduction'), max_length=900,
                                    blank=True, null=True)
    redirect_link = models.CharField(_('redirect link'), max_length=300,
                                     blank=True, null=True)
    slug = models.CharField(_('slug'), max_length=100)
    related = models.ManyToManyField('self', verbose_name=_('related news'),
                                     blank=True, null=True)
    picture = FilerImageField(verbose_name=_('picture'), null=True, blank=True,
                              on_delete=models.SET_NULL)
    attachment = FilerFileField(verbose_name=_('attachment'), null=True, blank=True,
                                related_name="news_attachment", on_delete=models.SET_NULL)
    css_class = models.CharField(_('CSS class'), max_length=50,
                                 null=True, blank=True)
    tags = TaggableManager(blank=True)
    objects = NewsManager()

    # Audit
    created_on = models.DateTimeField(_('date added'), auto_now_add=True)
    created_by = models.ForeignKey(User, blank=True, null=True,
                                   editable=False, related_name='created-news',
                                   verbose_name=_('created by'))
    updated_on = models.DateTimeField(_('date modified'), auto_now=True)
    updated_by = models.ForeignKey(User, blank=True, null=True,
                                   editable=False, related_name='updated-news',
                                   verbose_name=_('update by'))

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')
        ordering = ('-publish_date',)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        self.updated_by = user
        if not self.id:
            self.created_by = user
        if not self.slug:
            self.slug = slugify(self.title)[0:99]
        return super(News, self).save(*args, **kwargs)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        if self.redirect_link:
            return self.redirect_link
        return reverse('news_detail', args=[self.category.slug, self.slug])
