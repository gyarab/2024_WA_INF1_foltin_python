from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse
from django.urls import reverse
import json

# Create your views here.
def articles(request):
    with open('articles.json', encoding="utf-8") as file:
        data = json.load(file) 
    
    html_list = '<ul>'
    id = 0
    for article in data:
        title = article['title']
        url_article = reverse('content:article', args=[id])
        html_list += f'<li><a href="{url_article}">{title}<a></li>'
        id += 1
    html_list += '</ul>'

    return HTTPResponse(html_list)

def article(request, id):
    with open('articles.json', encoding="utf-8") as file:
        data = json.load(file)
    
    article = data[id]
    title = article['title']
    perex = article['perex']
    image = article['image']

    url_articles = reverse('content:articles')
    back = f"<a href='{url_articles}'>Zpet na seznam</a>"
    
    return HTTPResponse(f'<h1>{title}</h1><img src="{image}" alt="Article Image"><p>{perex}</p>'+back)