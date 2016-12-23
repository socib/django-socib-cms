from haystack import indexes
from django.utils import translation
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from socib_cms.pages.models import Page
import models


class NewsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    pub_date = indexes.DateTimeField(model_attr='publish_date')
    section_name = indexes.CharField(faceted=True)

    def get_model(self):
        return models.News

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        if using is not None and using[-3:-2] == '_':
            translation.activate(using[-2:])
        return self.get_model().objects.published()

    def prepare_section_name(self, obj):
        section_name = u''
        try:
            url = reverse('news_category_detail',
                          args=[obj.category.slug])
            page = Page.objects.get(url=url)
            section_name = page.sector.title
        except ObjectDoesNotExist:
            section_name = obj.category.name
        return section_name
