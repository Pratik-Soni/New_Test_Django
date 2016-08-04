'''
Created on 11-Jul-2016

@author: TERAMATRIX\pratik.soni
'''
from django import forms
from models import Article,Comment

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ('title', 'body', 'pub_date','thumbnail')
        #fields = ('title', 'body', 'thumbnail')
        
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('name','body')