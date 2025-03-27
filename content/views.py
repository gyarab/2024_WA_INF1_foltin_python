from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse
from django.http import HttpResponseRedirect as HTTPResponseRedirect
from django.urls import reverse
from django.db.models import F

import json
from .models import Article, Category, Author, Comment
from .forms import CommentForm

# Create your views here.
def homepage(request):
    categories = Category.objects.order_by('name').exclude(id=1).all()
    authors = Author.objects.all()
    articles = list(Article.objects.filter(vote_count__gte=1).select_related("author").prefetch_related("categories").all())
    return render(request, 'content/homepage.html', {'categories': categories, 'authors': authors, 'articles': articles})

def article(request, id):
    categories = Category.objects.all()
    authors = Author.objects.all()
    article = Article.objects.get(id=id)

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment = Comment()
            comment.name = data['name']
            comment.text = data['text']
            comment.article = article
            comment.ip = request.META.get('REMOTE_ADDR')
            comment.user_agent = request.META.get('HTTP_USER_AGENT')
            comment.save()
            return HTTPResponseRedirect(reverse('content:article', args=[id]))
    
    if request.method == 'GET' and 'vote' in request.GET:
        cookie_name=f'voted_{article.id}'
        if cookie_name in request.COOKIES:
            return HTTPResponseRedirect(reverse('content:article', args=[id]))
        
        vote = int(request.GET['vote'])
        if vote <= 5 and vote >= 1:
            Article.objects.filter(id=id).update(
                vote_sum=F('vote_sum') + vote,
                vote_count=F('vote_count') + 1
            )

            response = HTTPResponseRedirect(reverse('content:article', args=[id]))
            #response.set_cookie(cookie_name, '1')
            return response
            
        
    voted = request.COOKIES.get(f'voted_{id}')
    
    return render(request, 'content/article.html', {
            'categories': categories, 
            'authors': authors, 
            'article': article,
            'form': form,
            'voted': voted,
            })

def category(request, id):
    categories = Category.objects.all()
    authors = Author.objects.all()
    category = Category.objects.get(id=id)

    articles = category.articles.all()
    return render(request, 'content/category.html', {'categories': categories, 'authors': authors, 'category':category, 'articles': articles})

def author(request, id):
    categories = Category.objects.all()
    authors = Author.objects.all()
    author = Author.objects.get(id=id)
    
    articles = author.articles.all()
    
    return render(request, 'content/author.html', {'categories': categories, 'authors': authors, 'author': author, 'articles': articles})
    
def info(request):
    meta = {k: str(v) for k, v in request.META.items()}
    return HTTPResponse(json.dumps(meta, indent=4), content_type='application/json')
