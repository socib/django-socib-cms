from mptt.models import MPTTModel, TreeForeignKey
from mptt.managers import TreeManager
from filer.fields.image import FilerImageField
from filer.fields.folder import FilerFolderField
from django.contrib.auth.models import Group
from django.db import models
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _


class Page(MPTTModel, FlatPage):

    PICTURE_LOCATION_CHOICES = (
        ('header', _('Header')),
        ('extra', _('Inside extra content')),
        ('background', _('As background image')),
        ('none', _('Do not show')),
    )

    title_menu = models.CharField(_('Short title for menu'), max_length=50)
    order = models.IntegerField(_('order'), default=0)
    introduction = models.CharField(_('Introduction'), max_length=900,
                                    blank=True, null=True,
                                    help_text=_('This text will be used in lists. If empty, the system will use the first 20 words of content'))
    extra_content = models.TextField(_('extra content'), blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children',
                            verbose_name=_('parent'))
    related = models.ManyToManyField('self', verbose_name=_('related pages'),
                                     blank=True, null=True)
    groups = models.ManyToManyField(Group, verbose_name=_('user groups allowed'),
                                    blank=True, null=True)
    is_container = models.BooleanField(_('page is just a container'), default=False)
    hide = models.BooleanField(_('hide this page in lists'), default=False)
    list_children = models.BooleanField(
        _('list children pages inside this page content'),
        default=False)
    include_children = models.BooleanField(
        _('children pages content is shown in sections of this page'),
        default=False)
    picture = FilerImageField(verbose_name=_('picture'), null=True, blank=True,
                              on_delete=models.SET_NULL)
    picture_description = models.CharField(_('picture description'), max_length=900,
                                           blank=True, null=True)
    picture_location = models.CharField(_('picture location'), max_length=10,
                                        choices=PICTURE_LOCATION_CHOICES,
                                        default='extra')
    album = FilerFolderField(verbose_name=_('album'), null=True, blank=True,
                             on_delete=models.SET_NULL)
    js_code = models.TextField(_('javascript code'), blank=True)
    css_class = models.CharField(_('CSS class'), max_length=50,
                                 null=True, blank=True)
    css_container_style = models.CharField(_('CSS styles'), max_length=300,
                                           null=True, blank=True)
    old_url = models.CharField(_('Old URL'), max_length=255, null=True, blank=True)
    redirect_link = models.CharField(_('redirect link'), max_length=300,
                                     blank=True, null=True)
    show_section_menu = models.BooleanField(_('show section menu'), default=True)
    content_template_name = models.CharField(
        _('content template name'), max_length=70, blank=True,
        help_text=_(
            "Example: 'pages/content/intro.html'. If this isn't provided, "
            "the system will use 'pages/content/default.html'."
        ),
    )
    content_columns = models.IntegerField(_('content columns'), default=12)
    extra_content_columns = models.IntegerField(_('extra content columns'), default=4)
    float_extra_content = models.BooleanField(_('float extra content'), default=True)

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

    @property
    def get_content_template(self):
        if self.content_template_name:
            return self.content_template_name
        else:
            return 'pages/content/default.html'

    def get_absolute_url(self):
        if self.redirect_link:
            return self.redirect_link
        return self.url

    def is_leaf_node_or_hidden_children(self):
        """
        Returns ``True`` if this model instance is a leaf node (it has no
        children, removing hide children), ``False`` otherwise.
        """
        if self.include_children and not self.list_children:
            return True
        if not hasattr(self, 'unhidden_children_count'):
            self.unhidden_children_count = self.get_children().filter(hide=False).count()

        return not self.unhidden_children_count
