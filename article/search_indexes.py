'''
Created on 18-Jul-2016

@author: TERAMATRIX\pratik.soni
'''
import datetime
from haystack import indexes
from article.models import Article

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, )