from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse
from django.urls import reverse
import json

# Create your views here.
def articles(request):
    with open('articles.json', encoding="utf-8") as file:
        data = json.load(file) 
    
    return render(request, 'content/articles.html', {'data': data})

def article(request, id):
    with open('articles.json', encoding="utf-8") as file:
        data = json.load(file)
     
    article = data[id]
    return render(request, 'content/article.html', {'article': article})
    
