'''
Created on 13-Jul-2016

@author: TERAMATRIX\pratik.soni
'''

from tastypie.resources import ModelResource
from tastypie.constants import ALL
from models import Article


class ArticleResource(ModelResource):
    class Meta:
        queryset = Article.objects.all()
        resource_name = 'article'
        filtering = { 'title' : ALL }
        
        