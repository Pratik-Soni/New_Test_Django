'''
Created on 20-Jul-2016

@author: TERAMATRIX\pratik.soni
'''
from django.conf.urls import patterns, url


urlpatterns = [
               url(r'^show/(?P<notification_id>\d+)/$','notification.views.show_notification'),
               url(r'^delete/(?P<notification_id>\d+)/$','notification.views.delete_notification'),               
               
               ]