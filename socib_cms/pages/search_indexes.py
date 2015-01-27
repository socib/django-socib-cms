from haystack import indexes
from django.utils import translation
import models


class PageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    pub_date = indexes.DateTimeField(model_attr='updated_on')

    def get_model(self):
        return models.Page

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        if using is not None and using[-3:-2] == '_':
            translation.activate(using[-2:])
        return self.get_model().objects.filter(hide=False)
