from haystack import indexes
from .models import Bingzheng, Bingjixibie, Zhibingjili, Lifang


class BingzhengIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Bingzheng

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class BingjixibieIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Bingjixibie

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class ZhibingjiliIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Zhibingjili

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class LifangIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Lifang

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
