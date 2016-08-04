from django.shortcuts import render, render_to_response
from article.models import Article, Comment
from django.http import HttpResponse, HttpResponseRedirect
from forms import ArticleForm
from django.core.context_processors import csrf
from article.forms import CommentForm
from time import timezone
from datetime import datetime
from django.template import RequestContext
from django.contrib import messages
from django_test import settings


# Create your views here.

def articles(request):
    language = 'en-us'
    session_language = 'en-us'
    
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    
    if 'lang' in request.session:
        session_language = request.session['lang']
        
    args={}
    args.update(csrf(request))
    
    args['articles'] = Article.objects.all()
    args['language'] = language
    args['session_language'] = session_language
    return render_to_response('articles.html',args)


def article(request, article_id=1):
    #return render_to_response('article.html',
    #                         {'article' : Article.objects.get(id=article_id)},
    #                         context_instance = RequestContext(request)
    #                          )

    return render(request, 'article.html',
                  {'article' : Article.objects.get(id=article_id)})


def language(request, language='en-us'):
    response = HttpResponse("setting language to %s"%language)
    response.set_cookie('lang',language)
    request.session['lang'] = language
    return response


def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            a = form.save()
            
            messages.add_message(request,messages.SUCCESS,"Your Article was added")
            return HttpResponseRedirect('/articles/all')
        
    else:
        form = ArticleForm()
        
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('create_article.html',args)


def delete_comment(request, comment_id):
    c = Comment.objects.get(id=comment_id)
    article_id = c.article.id
    c.delete()
    
    messages.add_message(request,
                         settings.DELETE_MESSAGE,
                         "Your Comment was deleted")
    return HttpResponseRedirect("/articles/get/%s" % article_id)    

def like_article(request, article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()
    return HttpResponseRedirect('/articles/get/%s'%article_id)

def add_comment(request, article_id):
    a = Article.objects.get(id=article_id)
    #print "Add Comment ......:",a
    if request.method == "POST":
        f = CommentForm(request.POST)
        #print "Add Comment :",f
        if f.is_valid():
            #print "In is valid ::::"
            c = f.save(commit=False)
            c.pub_date = datetime.now()
            c.article = a
            c.save()
            
            messages.success(request, "Your comment was added")
            return HttpResponseRedirect('/articles/get/%s'%article_id)
        
    else:
        f = CommentForm()
        
    args={}
    args.update(csrf(request))
    args['article'] = a
    args['form'] = f
    return render_to_response('add_comment.html',args)
    
def search_titles(request):
    if request.method == "POST":
        print request.POST['search_text']
        search_text = request.POST['search_text']
    else:
        search_text = ''
        
    articles = Article.objects.filter(title__contains=search_text)
    #print articles
    return render_to_response('ajax_search.html',{'articles' : articles})
        