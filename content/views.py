from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse
from django.http import HttpResponseRedirect as HTTPResponseRedirect
from django.urls import reverse

import json
from .models import Article, Category, Author, Comment
from .forms import CommentForm

# Create your views here.
def homepage(request):
    categories = Category.objects.all()
    authors = Author.objects.all()
    articles = Article.objects.all()
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
        cookiename=f'voted_{article.id}'
        if cookiename in request.COOKIES:
            return HTTPResponseRedirect(reverse('content:article', args=[id]))
        
        vote = int(request.GET['vote'])
        if vote <= 5 and vote >= 1:
            article.vote_sum += vote
            article.vote_count += 1
            article.save()

            response = HTTPResponseRedirect(reverse('content:article', args=[id]))
            response.set_cookie(cookiename, '1')
            return response
        
    
    return render(request, 'content/article.html', {
            'categories': categories, 
            'authors': authors, 
            'article': article,
            'form': form
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
