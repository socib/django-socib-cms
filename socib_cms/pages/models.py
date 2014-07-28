from mptt.models import MPTTModel, TreeForeignKey
from mptt.managers import TreeManager
from filer.fields.image import FilerImageField
from filer.fields.folder import FilerFolderField
from django.contrib.auth.models import Group
from django.db import models
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _


class Page(MPTTModel, FlatPage):
    title_menu = models.CharField(_('Short title for menu'), max_length=50)
    order = models.IntegerField(_('order'), default=0)
    introduction = models.CharField(_('Introduction'), max_length=900,
                                    blank=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    related = models.ManyToManyField('self', verbose_name=_('related pages'),
                                     blank=True, null=True)
    groups = models.ManyToManyField(Group, verbose_name=_('user groups allowed'),
                                    blank=True, null=True)
    is_container = models.BooleanField(_('page is just a container'), default=False)
    hide = models.BooleanField(_('hide this page in lists'), default=False)
    list_children = models.BooleanField(
        _('list children pages inside this page content'),
        default=False)
    picture = FilerImageField(verbose_name=_('picture'), null=True, blank=True,
                              on_delete=models.SET_NULL)
    album = FilerFolderField(verbose_name=_('album'), null=True, blank=True,
                             on_delete=models.SET_NULL)
    css_class = models.CharField(_('CSS class'), max_length=50,
                                 null=True, blank=True)
    old_url = models.CharField(_('Old URL'), max_length=255, null=True, blank=True)
    redirect_link = models.CharField(_('redirect link'), max_length=300,
                                     blank=True, null=True)

    tree = TreeManager()

    class MPTTMeta:
        order_insertion_by = ['order']

    def __unicode__(self):
        return self.title

    @property
    def group_list(self):
        return ', '.join([group.name for group in self.groups.all()])

    @property
    def sector(self):
        if self.is_root_node():
            return self
        else:
            return self.get_ancestors(include_self=True)[1]

    @property
    def section(self):
        if self.is_root_node():
            return self
        else:
            if self.is_leaf_node_or_hidden_children():
                return self.parent
            else:
                return self

    def get_absolute_url(self):
        if self.redirect_link:
            return self.redirect_link
        return self.url

    def is_leaf_node_or_hidden_children(self):
        """
        Returns ``True`` if this model instance is a leaf node (it has no
        children, removing hide children), ``False`` otherwise.
        """
        if not hasattr(self, 'unhidden_children_count'):
            self.unhidden_children_count = self.get_children().filter(hide=False).count()

        return not self.unhidden_children_count
