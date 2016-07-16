from __future__ import unicode_literals

from django.db import models
import datetime
from django.utils.timezone import *
from time import time

# Create your models here.

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s"%(str(time()).replace('.','_'), filename)

class Article(models.Model):
    title = models.TextField(max_length=500)
    body = models.TextField()
    pub_date = models.DateTimeField('date pubished', blank=True)
    likes = models.IntegerField(default=0)
    thumbnail = models.FileField(upload_to=get_upload_file_name, blank=True)
    
    def __unicode__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date pubished', blank=True)
    article = models.ForeignKey(Article)

